from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField, CSVModelChoiceField, CSVChoiceField
from utilities.forms.rendering import FieldSet
from utilities.forms import add_blank_choice, BOOLEAN_WITH_BLANK_CHOICES
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Option, OptionDefinition
from netbox_dhcp.choices import OptionSpaceChoices

from .mixins import (
    ClientClassAssignmentFormMixin,
    ClientClassAssignmentImportFormMixin,
    ClientClassAssignmentFilterFormMixin,
    ClientClassAssignmentBulkEditFormMixin,
)


__all__ = (
    "OptionForm",
    "OptionFilterForm",
    "OptionImportForm",
    "OptionBulkEditForm",
)


class OptionForm(ClientClassAssignmentFormMixin, NetBoxModelForm):
    class Meta:
        model = Option

        fields = (
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            name=_("Option"),
        ),
        FieldSet(
            "assign_client_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )


class OptionFilterForm(ClientClassAssignmentFilterFormMixin, NetBoxModelFilterSetForm):
    model = Option

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "space",
            "name",
            "family",
            "code",
            "definition_id",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_class_id",
            name=_("Option"),
        ),
    )

    family = forms.ChoiceField(
        label=_("Address Family"),
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
    )
    space = forms.ChoiceField(
        label=_("Space"),
        choices=add_blank_choice(OptionSpaceChoices),
        required=False,
    )
    name = forms.CharField(
        label=_("Name"),
        required=False,
    )
    data = forms.CharField(
        label=_("Data"),
        help_text=_("Case-insensitive substring match"),
        required=False,
    )
    code = forms.CharField(
        label=_("Code"),
        required=False,
    )
    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )

    tag = TagFilterField(Option)


class OptionImportForm(ClientClassAssignmentImportFormMixin, NetBoxModelImportForm):
    class Meta:
        model = Option

        fields = (
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            "tags",
        )

    space = CSVChoiceField(
        label=_("Space"),
        choices=OptionSpaceChoices,
        required=False,
    )
    definition = CSVModelChoiceField(
        label=_("Option Definitions"),
        queryset=OptionDefinition.objects.all(),
        to_field_name="name",
        required=True,
        error_messages={
            "invalid_choice": _("Option Definition %(value)s not found"),
        },
    )


class OptionBulkEditForm(
    ClientClassAssignmentBulkEditFormMixin, NetBoxModelBulkEditForm
):
    model = Option

    fieldsets = (
        FieldSet(
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            name=_("Option"),
        ),
    )

    nullable_fields = (
        "data",
        "csv_format",
        "always_send",
        "never_send",
        "assign_client_classes",
    )

    definition = forms.ModelChoiceField(
        label=_("Option Definition"),
        queryset=OptionDefinition.objects.all(),
        required=False,
    )
    data = forms.CharField(
        label=_("Data"),
        required=False,
    )
    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
