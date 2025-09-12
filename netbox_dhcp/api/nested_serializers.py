from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer

from netbox_dhcp.models import DHCPCluster


__all__ = ("NestedDHCPClusterSerializer",)


class NestedDHCPClusterSerializer(WritableNestedSerializer):
    class Meta:
        model = DHCPCluster

        fields = (
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
