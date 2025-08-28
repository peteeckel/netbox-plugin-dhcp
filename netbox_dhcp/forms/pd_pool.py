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

from netbox_dhcp.models import PDPool


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
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Prefix Delegation Pool"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
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
            name=_("Prefix Delegation Pool"),
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

    tag = TagFilterField(PDPool)


class PDPoolImportForm(NetBoxModelImportForm):
    class Meta:
        model = PDPool

        fields = (
            "name",
            "description",
            "tags",
        )


class PDPoolBulkEditForm(NetBoxModelBulkEditForm):
    model = PDPool

    fieldsets = (
        FieldSet(
            "description",
            name=_("Prefix Delegation Pool"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
