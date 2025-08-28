from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import DDNS


__all__ = ("DDNSSerializer",)


class DDNSSerializer(NetBoxModelSerializer):
    class Meta:
        model = DDNS

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
        view_name="plugins-api:netbox_dhcp-api:ddns-detail"
    )
