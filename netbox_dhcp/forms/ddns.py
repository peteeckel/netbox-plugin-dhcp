# from django import forms
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

from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
)


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
            "tags",
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


class DDNSFilterForm(NetBoxDHCPFilterFormMixin, NetBoxModelFilterSetForm):
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

    tag = TagFilterField(DDNS)


class DDNSImportForm(NetBoxModelImportForm):
    class Meta:
        model = DDNS

        fields = (
            "name",
            "description",
            "tags",
        )


class DDNSBulkEditForm(NetBoxDHCPBulkEditFormMixin, NetBoxModelBulkEditForm):
    model = DDNS

    fieldsets = (
        FieldSet(
            "description",
            name=_("Dynamic DNS"),
        ),
    )

    nullable_fields = ("description",)
