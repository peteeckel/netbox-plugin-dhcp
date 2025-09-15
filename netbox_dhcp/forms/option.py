from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField
from utilities.forms.rendering import FieldSet

from netbox_dhcp.models import Option


__all__ = (
    "OptionForm",
    "OptionFilterForm",
    "OptionImportForm",
    "OptionBulkEditForm",
)


class OptionForm(NetBoxModelForm):
    class Meta:
        model = Option

        fields = (
            "name",
            "description",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Option"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class OptionFilterForm(NetBoxModelFilterSetForm):
    model = Option

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Option"),
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

    tag = TagFilterField(Option)


class OptionImportForm(NetBoxModelImportForm):
    class Meta:
        model = Option

        fields = (
            "name",
            "description",
            "tags",
        )


class OptionBulkEditForm(NetBoxModelBulkEditForm):
    model = Option

    fieldsets = (
        FieldSet(
            "description",
            name=_("Option"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
