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
from ipam.models import Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import PDPool

from .mixins import (
    ClientClassBulkEditFormMixin,
    ClientClassFilterFormMixin,
    ClientClassFormMixin,
    ClientClassImportFormMixin,
    CommonBulkEditFormMixin,
    CommonFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetBoxDHCPFilterFormMixin,
)


__all__ = (
    "PDPoolForm",
    "PDPoolFilterForm",
    "PDPoolImportForm",
    "PDPoolBulkEditForm",
)


class PDPoolForm(ClientClassFormMixin, NetBoxModelForm):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "client_class_definitions",
            "client_class",
            "require_client_classes",
            "evaluate_additional_classes",
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
            "client_class_definitions",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class",
            "require_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "user_context",
            "comment",
            "evaluate_additional_classes",
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


class PDPoolFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    CommonFilterFormMixin,
    NetBoxModelFilterSetForm,
):
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
            "prefix_id",
            "delegated_length",
            "excluded_prefix_id",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class_definition_id",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class_id",
            "required_client_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "comment",
            "evaluate_additional_class_id",
            name=_("Assignment"),
        ),
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

    tag = TagFilterField(PDPool)


class PDPoolImportForm(
    ClientClassImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "client_class_definitions",
            "client_class",
            "require_client_classes",
            "evaluate_additional_classes",
            "user_context",
            "comment",
            "tags",
        )

    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        required=True,
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


class PDPoolBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    CommonBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = PDPool

    fieldsets = (
        FieldSet(
            "description",
            "delegated_length",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "client_class_definitions",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class",
            "require_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "user_context",
            "comment",
            "evaluate_additional_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    nullable_fields = (
        "description",
        "excluded_prefix",
        "client_class",
        "client_class_definitions",
        "require_client_classes",
        "evaluate_additional_classes",
        "user_context",
        "comment",
    )

    delegated_length = forms.CharField(
        required=False,
        label=_("Delegated Length"),
    )
    excluded_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={
            "family": IPAddressFamilyChoices.FAMILY_6,
        },
        required=False,
        label=_("Excluded IPv6 Prefix"),
    )
