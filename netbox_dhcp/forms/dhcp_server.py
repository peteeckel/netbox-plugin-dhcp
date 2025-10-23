from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField

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
from utilities.forms import add_blank_choice, BOOLEAN_WITH_BLANK_CHOICES

from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox_dhcp.models import DHCPServer, DHCPCluster
from netbox_dhcp.choices import (
    DHCPServerStatusChoices,
    DHCPServerIDTypeChoices,
    HostReservationIdentifierChoices,
)

from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    ChildSubnetFormMixin,
    ChildSubnetFilterFormMixin,
    ChildSubnetImportFormMixin,
    ChildSubnetBulkEditFormMixin,
    ChildSharedNetworkFormMixin,
    ChildSharedNetworkFilterFormMixin,
    ChildSharedNetworkImportFormMixin,
    ChildSharedNetworkBulkEditFormMixin,
    ChildHostReservationFormMixin,
    ChildHostReservationFilterFormMixin,
    ChildHostReservationImportFormMixin,
    ChildHostReservationBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
)


__all__ = (
    "DHCPServerForm",
    "DHCPServerFilterForm",
    "DHCPServerImportForm",
    "DHCPServerBulkEditForm",
)


class DHCPServerForm(
    ClientClassFormMixin,
    ChildSubnetFormMixin,
    ChildSharedNetworkFormMixin,
    ChildHostReservationFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = DHCPServer

        fields = (
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            *ClientClassFormMixin.FIELDS,
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
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
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            name=_("Configuration"),
        ),
        ClientClassFormMixin.FIELDSET,
        FieldSet(
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
            name=_("Child Objects"),
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
    echo_client_id = forms.NullBooleanField(
        label=_("Echo Client ID"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
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


class DHCPServerFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    ChildSubnetFilterFormMixin,
    ChildSharedNetworkFilterFormMixin,
    ChildHostReservationFilterFormMixin,
    NetBoxModelFilterSetForm,
):
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
            "device_id",
            name=_("Physical"),
        ),
        FieldSet(
            "virtual_machine_id",
            name=_("Virtual"),
        ),
        FieldSet(
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            name=_("Configuration"),
        ),
        ClientClassFilterFormMixin.FIELDSET,
        FieldSet(
            "child_subnet_id",
            "child_shared_network_id",
            "child_host_reservation_id",
            name=_("Child Objects"),
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

    server_id = forms.MultipleChoiceField(
        choices=DHCPServerIDTypeChoices,
        required=False,
        label=_("Server ID"),
    )
    host_reservation_identifiers = forms.MultipleChoiceField(
        choices=HostReservationIdentifierChoices,
        required=False,
        label=_("Host Reservation Identifier"),
    )

    tag = TagFilterField(DHCPServer)


class DHCPServerImportForm(
    ClientClassImportFormMixin,
    ChildSubnetImportFormMixin,
    ChildSharedNetworkImportFormMixin,
    ChildHostReservationImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = DHCPServer

        fields = (
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
            *ClientClassImportFormMixin.FIELDS,
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


class DHCPServerBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    ChildSubnetBulkEditFormMixin,
    ChildSharedNetworkBulkEditFormMixin,
    ChildHostReservationBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = DHCPServer

    fieldsets = (
        FieldSet(
            "description",
            "status",
            "dhcp_cluster",
            name=_("DHCP Server"),
        ),
        FieldSet(
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            name=_("Configuration"),
        ),
        ClientClassBulkEditFormMixin.FIELDSET,
        FieldSet(
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
            name=_("Child Objects"),
        ),
    )

    nullable_fields = (
        "description",
        "dhcp_cluster",
        "server_id",
        "host_reservation_identifiers",
        "echo_client_id",
        "relay_supplied_options",
        "child_subnets",
        "child_shared_networks",
        "child_host_reservations",
        *ClientClassBulkEditFormMixin.NULLABLE_FIELDS,
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

    server_id = forms.ChoiceField(
        choices=DHCPServerIDTypeChoices,
        required=False,
        label=_("Server ID"),
    )
    host_reservation_identifiers = forms.MultipleChoiceField(
        choices=HostReservationIdentifierChoices,
        required=False,
        label=_("Host Reservation Identifier"),
    )
    echo_client_id = forms.NullBooleanField(
        label=_("Echo Client ID"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    relay_supplied_options = SimpleArrayField(
        label=_("Relay Supplied Options"),
        base_field=forms.IntegerField(
            min_value=1,
            max_value=255,
        ),
        required=False,
    )
