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
    CSVModelMultipleChoiceField,
    JSONField,
)
from utilities.forms.rendering import FieldSet
from ipam.models import IPRange

from netbox_dhcp.models import Pool, ClientClass


__all__ = (
    "PoolForm",
    "PoolFilterForm",
    "PoolImportForm",
    "PoolBulkEditForm",
)


class PoolForm(NetBoxModelForm):
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
    client_class = DynamicModelChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Class"),
    )
    require_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Require Client Classes"),
    )


class PoolFilterForm(NetBoxModelFilterSetForm):
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

    name = forms.CharField(
        required=False,
        label=_("Name"),
    )
    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
    ip_range_id = DynamicModelMultipleChoiceField(
        queryset=IPRange.objects.all(),
        required=False,
        label=_("IP Range"),
    )
    client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Class"),
    )
    require_client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Require Client Class"),
    )

    comment = forms.CharField(
        required=False,
        label=_("Comment"),
    )

    tag = TagFilterField(Pool)


class PoolImportForm(NetBoxModelImportForm):
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
    client_class = CSVModelChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Client Classes"),
    )
    require_client_classes = CSVModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Require Client Classes"),
    )


class PoolBulkEditForm(NetBoxModelBulkEditForm):
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

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
    client_class = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        selector=True,
        label=_("Client Class"),
    )
    require_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        selector=True,
        label=_("Require Client Classes"),
    )

    user_context = JSONField(
        required=False,
        label=_("User Context"),
    )
    comment = forms.CharField(
        required=False,
        label=_("Comment"),
    )
