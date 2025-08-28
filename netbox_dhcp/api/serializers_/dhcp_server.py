from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

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
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:dhcpserver-detail"
    )
