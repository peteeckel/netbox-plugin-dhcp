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

from netbox_dhcp.models import DHCPCluster


__all__ = (
    "DHCPClusterForm",
    "DHCPClusterFilterForm",
    "DHCPClusterImportForm",
    "DHCPClusterBulkEditForm",
)


class DHCPClusterForm(NetBoxModelForm):
    class Meta:
        model = DHCPCluster

        fields = (
            "name",
            "description",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("DHCP Cluster"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class DHCPClusterFilterForm(NetBoxModelFilterSetForm):
    model = DHCPCluster

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("DHCP Cluster"),
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

    tag = TagFilterField(DHCPCluster)


class DHCPClusterImportForm(NetBoxModelImportForm):
    class Meta:
        model = DHCPCluster

        fields = (
            "name",
            "description",
            "tags",
        )


class DHCPClusterBulkEditForm(NetBoxModelBulkEditForm):
    model = DHCPCluster

    fieldsets = (
        FieldSet(
            "description",
            name=_("DHCP Cluster"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
