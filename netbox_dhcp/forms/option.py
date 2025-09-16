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

from netbox_dhcp.models import Option

from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
)


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


class OptionFilterForm(NetBoxDHCPFilterFormMixin, NetBoxModelFilterSetForm):
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

    tag = TagFilterField(Option)


class OptionImportForm(NetBoxModelImportForm):
    class Meta:
        model = Option

        fields = (
            "name",
            "description",
            "tags",
        )


class OptionBulkEditForm(NetBoxDHCPBulkEditFormMixin, NetBoxModelBulkEditForm):
    model = Option

    fieldsets = (
        FieldSet(
            "description",
            name=_("Option"),
        ),
    )

    nullable_fields = ("description",)
