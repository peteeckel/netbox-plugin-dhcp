from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import (
    TagFilterField,
    CSVChoiceField,
    CSVMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet
from utilities.forms import add_blank_choice, BOOLEAN_WITH_BLANK_CHOICES
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import OptionDefinition
from netbox_dhcp.choices import OptionTypeChoices, OptionSpaceChoices

from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
)


__all__ = (
    "OptionDefinitionForm",
    "OptionDefinitionFilterForm",
    "OptionDefinitionImportForm",
    "OptionDefinitionBulkEditForm",
)


class OptionDefinitionForm(NetBoxModelForm):
    class Meta:
        model = OptionDefinition

        fields = (
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
        )

    fieldsets = (
        FieldSet(
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
            name=_("Option Definition"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    record_types = SimpleArrayField(
        label=_("Record Types"),
        help_text=_(
            "Valid Types: {}".format(
                ", ".join(
                    sorted(
                        type
                        for type in OptionTypeChoices.values()
                        if type
                        not in [
                            OptionTypeChoices.TYPE_EMPTY,
                            OptionTypeChoices.TYPE_RECORD,
                        ]
                    )
                )
            )
        ),
        base_field=forms.ChoiceField(
            choices=OptionTypeChoices,
        ),
        required=False,
    )
    array = forms.NullBooleanField(
        label=_("Array"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )


class OptionDefinitionFilterForm(NetBoxDHCPFilterFormMixin, NetBoxModelFilterSetForm):
    model = OptionDefinition

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
            name=_("Option Definition"),
        ),
    )

    family = forms.ChoiceField(
        label=_("Address Family"),
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
    )
    space = forms.MultipleChoiceField(
        label=_("Space"),
        choices=OptionSpaceChoices,
        required=False,
    )
    code = forms.IntegerField(
        label=_("Code"),
        min_value=1,
        max_value=255,
        required=False,
    )
    type = forms.MultipleChoiceField(
        label=_("Type"),
        choices=OptionTypeChoices,
        required=False,
    )
    record_types = forms.MultipleChoiceField(
        label=_("Record Types"),
        choices=OptionTypeChoices,
        required=False,
    )
    encapsulate = forms.CharField(
        label=_("Encapsulate"),
        required=False,
    )
    array = forms.NullBooleanField(
        label=_("Array"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )

    tag = TagFilterField(OptionDefinition)


class OptionDefinitionImportForm(NetBoxModelImportForm):
    class Meta:
        model = OptionDefinition

        fields = (
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
            "tags",
        )

    family = CSVChoiceField(
        choices=IPAddressFamilyChoices,
        required=False,
        label=_("Address Family"),
    )
    space = CSVChoiceField(
        choices=OptionSpaceChoices,
        required=False,
        label=_("Space"),
    )
    type = CSVChoiceField(
        choices=OptionTypeChoices,
        required=False,
        label=_("Type"),
    )
    record_types = CSVMultipleChoiceField(
        choices=OptionTypeChoices,
        required=False,
        label=_("Recoed Types"),
    )


class OptionDefinitionBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = OptionDefinition

    fieldsets = (
        FieldSet(
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
            name=_("Option Definition"),
        ),
    )

    nullable_fields = ("description",)

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
    code = forms.IntegerField(
        label=_("Code"),
        min_value=1,
        max_value=255,
        required=False,
    )
    type = forms.ChoiceField(
        label=_("Type"),
        choices=add_blank_choice(OptionTypeChoices),
        required=False,
    )
    record_types = SimpleArrayField(
        label=_("Record Types"),
        help_text=_(
            "Valid Types: {}".format(
                ", ".join(
                    sorted(
                        type
                        for type in OptionTypeChoices.values()
                        if type
                        not in [
                            OptionTypeChoices.TYPE_EMPTY,
                            OptionTypeChoices.TYPE_RECORD,
                        ]
                    )
                )
            )
        ),
        base_field=forms.ChoiceField(
            choices=OptionTypeChoices,
        ),
        required=False,
    )
    encapsulate = forms.CharField(
        label=_("Encapsulate"),
        required=False,
    )
    array = forms.NullBooleanField(
        label=_("Array"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
