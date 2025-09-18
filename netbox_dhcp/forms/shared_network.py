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

from netbox_dhcp.models import SharedNetwork
from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
)


__all__ = (
    "SharedNetworkForm",
    "SharedNetworkFilterForm",
    "SharedNetworkImportForm",
    "SharedNetworkBulkEditForm",
)


class SharedNetworkForm(
    ClientClassFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Shared Network"),
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


class SharedNetworkFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    NetBoxModelFilterSetForm,
):
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
        FieldSet(
            "client_class_definition_id",
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

    tag = TagFilterField(SharedNetwork)


class SharedNetworkImportForm(
    ClientClassImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "evaluate_additional_classes",
            "tags",
        )


class SharedNetworkBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = SharedNetwork

    fieldsets = (
        FieldSet(
            "description",
            name=_("Shared Network"),
        ),
    )

    nullable_fields = ("description",)
