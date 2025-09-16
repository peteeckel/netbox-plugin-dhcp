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
    "PDPoolForm",
    "PDPoolFilterForm",
    "PDPoolImportForm",
    "PDPoolBulkEditForm",
)


class PDPoolForm(NetworkClientClassesFormMixin, ClientClassFormMixin, NetBoxModelForm):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "client_classes",
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
            "client_classes",
            "client_class",
            "require_client_classes",
            "evaluate_additional_classes",
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


class PDPoolFilterForm(
    NetBoxDHCPFilterFormMixin,
    NetworkClientClassesFilterFormMixin,
    ClientClassFilterFormMixin,
    ContextCommentFilterFormMixin,
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
            "network_client_class_id",
            "client_class_id",
            "require_client_class_id",
            "evaluate_additional_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "comment",
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
    NetworkClientClassesImportFormMixin,
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
            "client_classes",
            "client_class",
            "require_client_classes",
            "evaluate_additional_classes",
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


class PDPoolBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    NetworkClientClassesBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    ContextCommentBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
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
            "client_classes",
            "require_client_classes",
            "evaluate_additional_classes",
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
        "client_classes",
        "require_client_classes",
        "evaluate_additional_classes",
        "user_context",
        "comment",
    )

    delegated_length = forms.CharField(
        required=False,
        label=_("Delegated Length"),
    )
