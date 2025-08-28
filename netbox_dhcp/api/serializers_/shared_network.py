from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import SharedNetwork


__all__ = ("SharedNetworkSerializer",)


class SharedNetworkSerializer(NetBoxModelSerializer):
    class Meta:
        model = SharedNetwork

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
        view_name="plugins-api:netbox_dhcp-api:sharednetwork-detail"
    )
