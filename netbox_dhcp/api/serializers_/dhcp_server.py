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
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
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
