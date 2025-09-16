from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import (
    TagFilterField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVChoiceField,
    CSVModelChoiceField,
)
from utilities.forms.rendering import FieldSet, TabbedGroups
from utilities.forms import add_blank_choice

from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox_dhcp.models import DHCPServer, DHCPCluster
from netbox_dhcp.choices import DHCPServerStatusChoices

from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
)


__all__ = (
    "DHCPServerForm",
    "DHCPServerFilterForm",
    "DHCPServerImportForm",
    "DHCPServerBulkEditForm",
)


class DHCPServerForm(NetBoxModelForm):
    class Meta:
        model = DHCPServer

        fields = (
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "status",
            "dhcp_cluster",
            name=_("DHCP Server"),
        ),
        FieldSet(
            TabbedGroups(
                FieldSet("device", name=_("Physical")),
                FieldSet("virtual_machine", name=_("Virtual")),
            ),
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    status = forms.ChoiceField(
        choices=DHCPServerStatusChoices,
        required=False,
        label=_("Status"),
    )
    dhcp_cluster = DynamicModelChoiceField(
        queryset=DHCPCluster.objects.all(),
        required=False,
        quick_add=True,
        label=_("DHCP Cluster"),
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label=_("Device"),
        selector=True,
    )
    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label=_("Virtual Machine"),
        selector=True,
    )

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)

        if self.cleaned_data["virtual_machine"] and self.cleaned_data["device"]:
            error_text = _(
                "Cannot assign a device and a virtual machine to a DHCP server."
            )
            raise forms.ValidationError(
                {
                    "device": error_text,
                    "virtual_machine": error_text,
                }
            )


class DHCPServerFilterForm(NetBoxDHCPFilterFormMixin, NetBoxModelFilterSetForm):
    model = DHCPServer

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
            "dhcp_cluster",
            name=_("DHCP Server"),
        ),
        FieldSet(
            "device",
            name=_("DCIM"),
        ),
        FieldSet(
            "virtual_machine",
            name=_("Virtualization"),
        ),
    )

    status = forms.MultipleChoiceField(
        choices=DHCPServerStatusChoices,
        required=False,
        label=_("Status"),
    )
    dhcp_cluster_id = DynamicModelMultipleChoiceField(
        queryset=DHCPCluster.objects.all(),
        required=False,
        label=_("DHCP Cluster"),
    )

    device_id = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label=_("Device"),
    )
    virtual_machine_id = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label=_("Virtual Machine"),
    )

    tag = TagFilterField(DHCPServer)


class DHCPServerImportForm(NetBoxModelImportForm):
    class Meta:
        model = DHCPServer

        fields = (
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
            "tags",
        )

    status = CSVChoiceField(
        choices=DHCPServerStatusChoices,
        required=False,
        label=_("Status"),
    )
    dhcp_cluster = CSVModelChoiceField(
        queryset=DHCPCluster.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("DHCP cluster %(value)s not found"),
        },
        label=_("DHCP Cluster"),
    )

    device = CSVModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Device %(value)s not found"),
        },
        label=_("Device"),
    )
    virtual_machine = CSVModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Virtual machine %(value)s not found"),
        },
        label=_("Virtual Machine"),
    )


class DHCPServerBulkEditForm(NetBoxDHCPBulkEditFormMixin, NetBoxModelBulkEditForm):
    model = DHCPServer

    fieldsets = (
        FieldSet(
            "description",
            "status",
            "dhcp_cluster",
            name=_("DHCP Server"),
        ),
    )

    nullable_fields = (
        "description",
        "dhcp_cluster",
    )

    status = forms.ChoiceField(
        choices=add_blank_choice(DHCPServerStatusChoices),
        required=False,
        label=_("Status"),
    )
    dhcp_cluster = DynamicModelChoiceField(
        queryset=DHCPCluster.objects.all(),
        required=False,
        label=_("DHCP Cluster"),
    )
