from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from dcim.api.serializers import DeviceSerializer
from virtualization.api.serializers import VirtualMachineSerializer

from ..nested_serializers import NestedDHCPClusterSerializer
from .mixins import (
    ChildSubnetSerializerMixin,
    ChildSharedNetworkSerializerMixin,
    ChildHostReservationSerializerMixin,
    ChildClientClassSerializerMixin,
)

from netbox_dhcp.models import DHCPServer


__all__ = ("DHCPServerSerializer",)


class DHCPServerSerializer(
    ChildSubnetSerializerMixin,
    ChildSharedNetworkSerializerMixin,
    ChildHostReservationSerializerMixin,
    ChildClientClassSerializerMixin,
    NetBoxModelSerializer,
):
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
            "virtual_machine",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            "child_subnets",
            "child_shared_networks",
            "child_host_reservations",
            "child_client_classes",
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

    dhcp_cluster = NestedDHCPClusterSerializer(
        many=False,
        read_only=False,
        required=False,
        default=None,
        help_text=_("DHCP cluster the server is assigned to"),
    )
    device = DeviceSerializer(
        nested=True,
        many=False,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Device"),
    )
    virtual_machine = VirtualMachineSerializer(
        nested=True,
        many=False,
        read_only=False,
        required=False,
        default=None,
        help_text=_("Virtual Machine"),
    )

    def create(self, validated_data):
        child_subnets = validated_data.pop("child_subnets", None)
        child_shared_networks = validated_data.pop("child_shared_networks", None)
        child_host_reservations = validated_data.pop("child_host_reservations", None)
        child_client_classes = validated_data.pop("child_client_classes", None)

        dhcp_server = super().create(validated_data)

        if child_subnets is not None:
            dhcp_server.child_subnets.set(child_subnets)
        if child_shared_networks is not None:
            dhcp_server.child_shared_networks.set(child_shared_networks)
        if child_host_reservations is not None:
            dhcp_server.child_host_reservations.set(child_host_reservations)
        if child_client_classes is not None:
            dhcp_server.child_client_classes.set(child_client_classes)

        return dhcp_server

    def update(self, instance, validated_data):
        child_subnets = validated_data.pop("child_subnets", None)
        child_shared_networks = validated_data.pop("child_shared_networks", None)
        child_host_reservations = validated_data.pop("child_host_reservations", None)
        child_client_classes = validated_data.pop("child_client_classes", None)

        dhcp_server = super().update(instance, validated_data)

        if child_subnets is not None:
            dhcp_server.child_subnets.set(child_subnets)
        if child_shared_networks is not None:
            dhcp_server.child_shared_networks.set(child_shared_networks)
        if child_host_reservations is not None:
            dhcp_server.child_host_reservations.set(child_host_reservations)
        if child_client_classes is not None:
            dhcp_server.child_client_classes.set(child_client_classes)

        return dhcp_server
