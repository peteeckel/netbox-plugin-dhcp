from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import DHCPCluster

from .dhcp_server import DHCPServerSerializer


__all__ = ("DHCPClusterSerializer",)


class DHCPClusterSerializer(NetBoxModelSerializer):
    class Meta:
        model = DHCPCluster

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "status",
            "dhcp_servers",
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
        view_name="plugins-api:netbox_dhcp-api:dhcpcluster-detail"
    )

    dhcp_servers = DHCPServerSerializer(
        many=True,
        nested=True,
        read_only=True,
        required=False,
        allow_null=True,
        help_text=_("DHCP servers assigned to the cluster"),
    )
