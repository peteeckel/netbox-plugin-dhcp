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

from netbox_dhcp.models import Subnet
from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
)


__all__ = (
    "SubnetForm",
    "SubnetFilterForm",
    "SubnetImportForm",
    "SubnetBulkEditForm",
)


class SubnetForm(
    ClientClassFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Subnet"),
        ),
        FieldSet(
            "client_class_definitions",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class",
            "required_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "user_context",
            "comment",
            "evaluate_additional_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class SubnetFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    NetBoxModelFilterSetForm,
):
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
        FieldSet(
            "network_client_class_id",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class_id",
            "required_client_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "comment",
            "evaluate_additional_class_id",
            name=_("Assignment"),
        ),
    )

    tag = TagFilterField(Subnet)


class SubnetImportForm(ClientClassImportFormMixin, NetBoxModelImportForm):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "evaluate_additional_classes",
            "tags",
        )


class SubnetBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Subnet

    fieldsets = (
        FieldSet(
            "description",
            name=_("Subnet"),
        ),
    )

    nullable_fields = ("description",)
