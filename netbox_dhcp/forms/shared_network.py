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

from netbox_dhcp.models import SharedNetwork


__all__ = (
    "SharedNetworkForm",
    "SharedNetworkFilterForm",
    "SharedNetworkImportForm",
    "SharedNetworkBulkEditForm",
)


class SharedNetworkForm(NetBoxModelForm):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Shared Network"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class SharedNetworkFilterForm(NetBoxModelFilterSetForm):
    model = SharedNetwork

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Shared Network"),
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

    tag = TagFilterField(SharedNetwork)


class SharedNetworkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "tags",
        )


class SharedNetworkBulkEditForm(NetBoxModelBulkEditForm):
    model = SharedNetwork

    fieldsets = (
        FieldSet(
            "description",
            name=_("Shared Network"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
