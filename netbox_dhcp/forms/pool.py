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
from utilities.forms.rendering import FieldSet
from ipam.models import IPRange

from netbox_dhcp.models import Pool

from .mixins import (
    NetworkClientClassesFormMixin,
    ClientClassFormMixin,
    NetBoxDHCPFilterFormMixin,
    NetworkClientClassesFilterFormMixin,
    ClientClassFilterFormMixin,
    ContextCommentFilterFormMixin,
    NetworkClientClassesImportFormMixin,
    ClientClassImportFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetworkClientClassesBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    ContextCommentBulkEditFormMixin,
)


__all__ = (
    "PoolForm",
    "PoolFilterForm",
    "PoolImportForm",
    "PoolBulkEditForm",
)


class PoolForm(NetworkClientClassesFormMixin, ClientClassFormMixin, NetBoxModelForm):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            "client_class",
            "require_client_classes",
            "user_context",
            "comment",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "ip_range",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class",
            "require_client_classes",
            name=_("Selection"),
        ),
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
    NetworkClientClassesFilterFormMixin,
    ClientClassFilterFormMixin,
    ContextCommentFilterFormMixin,
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
            "ip_range_id",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class_id",
            "require_client_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "comment",
            name=_("Assignment"),
        ),
    )

    ip_range_id = DynamicModelMultipleChoiceField(
        queryset=IPRange.objects.all(),
        required=False,
        label=_("IP Range"),
    )

    tag = TagFilterField(Pool)


class PoolImportForm(
    NetworkClientClassesImportFormMixin,
    ClientClassImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            "client_class",
            "require_client_classes",
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
        label=_("IP Ramhe"),
    )


class PoolBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    NetworkClientClassesBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    ContextCommentBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Pool

    fieldsets = (
        FieldSet(
            "description",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class",
            "require_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
    )

    nullable_fields = (
        "description",
        "client_class",
        "require_client_classes",
        "user_context",
        "comment",
    )
