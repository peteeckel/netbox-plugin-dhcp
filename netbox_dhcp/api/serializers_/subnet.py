from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import Subnet


__all__ = ("SubnetSerializer",)


class SubnetSerializer(NetBoxModelSerializer):
    class Meta:
        model = Subnet

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
        view_name="plugins-api:netbox_dhcp-api:subnet-detail"
    )
