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

from netbox_dhcp.models import ClientClass


__all__ = (
    "ClientClassForm",
    "ClientClassFilterForm",
    "ClientClassImportForm",
    "ClientClassBulkEditForm",
)


class ClientClassForm(NetBoxModelForm):
    class Meta:
        model = ClientClass

        fields = (
            "name",
            "description",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Client Class"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class ClientClassFilterForm(NetBoxModelFilterSetForm):
    model = ClientClass

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Client Class"),
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

    tag = TagFilterField(ClientClass)


class ClientClassImportForm(NetBoxModelImportForm):
    class Meta:
        model = ClientClass

        fields = (
            "name",
            "description",
            "tags",
        )


class ClientClassBulkEditForm(NetBoxModelBulkEditForm):
    model = ClientClass

    fieldsets = (
        FieldSet(
            "description",
            name=_("Client Class"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
