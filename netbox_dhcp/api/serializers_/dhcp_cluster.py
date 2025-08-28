from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import DHCPCluster


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
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:dhcpcluster-detail"
    )
