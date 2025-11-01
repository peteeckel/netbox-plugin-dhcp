from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from dcim.api.serializers import DeviceSerializer, InterfaceSerializer
from virtualization.api.serializers import (
    VirtualMachineSerializer,
    VMInterfaceSerializer,
)

from .dhcp_cluster import DHCPClusterSerializer
from .client_class import ClientClassSerializer
from ..nested_serializers import (
    NestedSharedNetworkSerializer,
    NestedSubnetSerializer,
    NestedHostReservationSerializer,
)

from netbox_dhcp.models import DHCPServer


__all__ = ("DHCPServerSerializer",)


class DHCPServerSerializer(NetBoxModelSerializer):
    class Meta:
        model = DHCPServer

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "server_id",
            "status",
            "dhcp_cluster",
            "device",
            "device_interfaces",
            "virtual_machine",
            "virtual_machine_interfaces",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            "client_classes",
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "status",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:dhcpserver-detail"
    )

    dhcp_cluster = DHCPClusterSerializer(
        nested=True,
        read_only=False,
        required=False,
        default=None,
        help_text=_("DHCP cluster the server is assigned to"),
    )
    device = DeviceSerializer(
        nested=True,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Device"),
    )
    device_interfaces = InterfaceSerializer(
        nested=True,
        many=True,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Interfaces"),
    )
    virtual_machine = VirtualMachineSerializer(
        nested=True,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Virtual Machine"),
    )
    virtual_machine_interfaces = VMInterfaceSerializer(
        nested=True,
        many=True,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Virtual Interfaces"),
    )

    client_classes = ClientClassSerializer(
        nested=True,
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client Classes"),
    )

    child_shared_networks = NestedSharedNetworkSerializer(
        many=True,
        read_only=True,
        required=False,
    )
    child_subnets = NestedSubnetSerializer(
        many=True,
        read_only=True,
        required=False,
    )
    child_host_reservations = NestedHostReservationSerializer(
        many=True,
        read_only=True,
        required=False,
    )

    def create(self, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        device_interfaces = validated_data.pop("device_interfaces", None)
        virtual_machine_interfaces = validated_data.pop(
            "virtual_machine_interfaces", None
        )

        dhcp_server = super().create(validated_data)

        if client_classes is not None:
            dhcp_server.client_classes.set(client_classes)
        if device_interfaces is not None:
            dhcp_server.device_interfaces.set(device_interfaces)
        if virtual_machine_interfaces is not None:
            dhcp_server.virtual_machine_interfaces.set(virtual_machine_interfaces)

        return dhcp_server

    def update(self, instance, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        device_interfaces = validated_data.pop("device_interfaces", None)
        virtual_machine_interfaces = validated_data.pop(
            "virtual_machine_interfaces", None
        )

        dhcp_server = super().update(instance, validated_data)

        if client_classes is not None:
            dhcp_server.client_classes.set(client_classes)
        if device_interfaces is not None:
            dhcp_server.device_interfaces.set(device_interfaces)
        if virtual_machine_interfaces is not None:
            dhcp_server.virtual_machine_interfaces.set(virtual_machine_interfaces)

        return dhcp_server
