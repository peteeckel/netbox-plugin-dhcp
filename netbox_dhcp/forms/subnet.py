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

from netbox_dhcp.models import Subnet


__all__ = (
    "SubnetForm",
    "SubnetFilterForm",
    "SubnetImportForm",
    "SubnetBulkEditForm",
)


class SubnetForm(NetBoxModelForm):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Subnet"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class SubnetFilterForm(NetBoxModelFilterSetForm):
    model = Subnet

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Subnet"),
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

    tag = TagFilterField(Subnet)


class SubnetImportForm(NetBoxModelImportForm):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "tags",
        )


class SubnetBulkEditForm(NetBoxModelBulkEditForm):
    model = Subnet

    fieldsets = (
        FieldSet(
            "description",
            name=_("Subnet"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
