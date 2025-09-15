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
from ipam.models import Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import PDPool, ClientClass


__all__ = (
    "PDPoolForm",
    "PDPoolFilterForm",
    "PDPoolImportForm",
    "PDPoolBulkEditForm",
)


class PDPoolForm(NetBoxModelForm):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
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
            "prefix",
            "delegated_length",
            "excluded_prefix",
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

    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={
            "family": IPAddressFamilyChoices.FAMILY_6,
        },
        required=True,
        selector=True,
        label=_("IPv6 Prefix"),
    )
    excluded_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={
            "family": IPAddressFamilyChoices.FAMILY_6,
        },
        required=False,
        selector=True,
        label=_("Excluded IPv6 Prefix"),
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


class PDPoolFilterForm(NetBoxModelFilterSetForm):
    model = PDPool

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class",
            "require_client_classes",
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
    prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={
            "family": IPAddressFamilyChoices.FAMILY_6,
        },
        required=False,
        label=_("IPv6 Prefix"),
    )
    delegated_length = forms.IntegerField(
        required=False,
        label=_("Delegated Length"),
    )
    excluded_prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={
            "family": IPAddressFamilyChoices.FAMILY_6,
        },
        required=False,
        label=_("Excluded IPv6 Prefix"),
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

    tag = TagFilterField(PDPool)


class PDPoolImportForm(NetBoxModelImportForm):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "excluded_prefix",
            "require_client_classes",
            "user_context",
            "comment",
            "tags",
        )

    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        required=False,
        to_field_name="prefix",
        error_messages={
            "invalid_choice": _("IPv6 prefix %(value)s not found"),
        },
        label=_("IPv6 Prefix"),
    )
    excluded_prefix = CSVModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        required=False,
        to_field_name="prefix",
        error_messages={
            "invalid_choice": _("IPv6 prefix %(value)s not found"),
        },
        label=_("Excluded IPv6 Prefix"),
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


class PDPoolBulkEditForm(NetBoxModelBulkEditForm):
    model = PDPool

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "delegated_length",
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
    delegated_length = forms.CharField(
        required=False,
        label=_("Delegated Length"),
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
