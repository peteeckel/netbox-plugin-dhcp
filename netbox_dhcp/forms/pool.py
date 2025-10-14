from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import (
    TagFilterField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVModelChoiceField,
)
from utilities.forms import add_blank_choice
from utilities.forms.rendering import FieldSet
from ipam.models import IPRange
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassBulkEditFormMixin,
    ClientClassFilterFormMixin,
    ClientClassFormMixin,
    ClientClassImportFormMixin,
    CommonBulkEditFormMixin,
    CommonFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetBoxDHCPFilterFormMixin,
    DDNSUpdateFormMixin,
    DDNSUpdateFilterFormMixin,
    DDNSUpdateImportFormMixin,
    DDNSUpdateBulkEditFormMixin,
)


__all__ = (
    "PoolForm",
    "PoolFilterForm",
    "PoolImportForm",
    "PoolBulkEditForm",
)


class PoolForm(
    ClientClassFormMixin,
    DDNSUpdateFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            *ClientClassFormMixin.FIELDS,
            *DDNSUpdateFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "ip_range",
            name=_("Address Pool"),
        ),
        ClientClassFormMixin.FIELDSET,
        DDNSUpdateFormMixin.FIELDSET,
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    ip_range = DynamicModelChoiceField(
        queryset=IPRange.objects.all(),
        required=True,
        quick_add=True,
        selector=True,
        label=_("IP Range"),
    )


class PoolFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    CommonFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = Pool

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "family",
            "ip_range_id",
            name=_("Address Pool"),
        ),
        ClientClassFilterFormMixin.FIELDSET,
        DDNSUpdateFilterFormMixin.FIELDSET,
        FieldSet(
            "comment",
            name=_("Assignment"),
        ),
    )

    family = forms.ChoiceField(
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
        label=_("Address Family"),
    )
    ip_range_id = DynamicModelMultipleChoiceField(
        queryset=IPRange.objects.all(),
        query_params={
            "family": "$family",
        },
        required=False,
        label=_("IP Range"),
    )

    tag = TagFilterField(Pool)


class PoolImportForm(
    ClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            *ClientClassImportFormMixin.FIELDS,
            *DDNSUpdateImportFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )

    # TODO: Specify IP ranges by (start_address,end_address)
    ip_range = CSVModelChoiceField(
        queryset=IPRange.objects.all(),
        required=True,
        error_messages={
            "invalid_choice": _("IP range %(value)s not found"),
        },
        label=_("IP Range"),
    )


class PoolBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    CommonBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Pool

    fieldsets = (
        FieldSet(
            "description",
            name=_("Address Pool"),
        ),
        ClientClassBulkEditFormMixin.FIELDSET,
        DDNSUpdateBulkEditFormMixin.FIELDSET,
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
    )

    nullable_fields = (
        "description",
        *ClientClassBulkEditFormMixin.NULLABLE_FIELDS,
        *DDNSUpdateBulkEditFormMixin.NULLABLE_FIELDS,
        "user_context",
        "comment",
    )
