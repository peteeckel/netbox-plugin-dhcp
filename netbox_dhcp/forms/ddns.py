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

from netbox_dhcp.models import DDNS


__all__ = (
    "DDNSForm",
    "DDNSFilterForm",
    "DDNSImportForm",
    "DDNSBulkEditForm",
)


class DDNSForm(NetBoxModelForm):
    class Meta:
        model = DDNS

        fields = (
            "name",
            "description",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Dynamic DNS"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class DDNSFilterForm(NetBoxModelFilterSetForm):
    model = DDNS

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Dynamic DNS"),
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

    tag = TagFilterField(DDNS)


class DDNSImportForm(NetBoxModelImportForm):
    class Meta:
        model = DDNS

        fields = (
            "name",
            "description",
            "tags",
        )


class DDNSBulkEditForm(NetBoxModelBulkEditForm):
    model = DDNS

    fieldsets = (
        FieldSet(
            "description",
            name=_("Dynamic DNS"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
