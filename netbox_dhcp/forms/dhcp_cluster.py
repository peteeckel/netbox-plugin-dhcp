from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField, CSVChoiceField
from utilities.forms.rendering import FieldSet
from utilities.forms import add_blank_choice

from netbox_dhcp.models import DHCPCluster
from netbox_dhcp.choices import DHCPClusterStatusChoices


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
            "status",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "status",
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
            "status",
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
    status = forms.MultipleChoiceField(
        choices=DHCPClusterStatusChoices,
        required=False,
        label=_("Status"),
    )

    tag = TagFilterField(DHCPCluster)


class DHCPClusterImportForm(NetBoxModelImportForm):
    class Meta:
        model = DHCPCluster

        fields = (
            "name",
            "description",
            "status",
            "tags",
        )

    status = CSVChoiceField(
        choices=DHCPClusterStatusChoices,
        required=False,
        label=_("Status"),
    )


class DHCPClusterBulkEditForm(NetBoxModelBulkEditForm):
    model = DHCPCluster

    fieldsets = (
        FieldSet(
            "description",
            "status",
            name=_("DHCP Cluster"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
    status = forms.ChoiceField(
        choices=add_blank_choice(DHCPClusterStatusChoices),
        required=False,
        label=_("Status"),
    )
