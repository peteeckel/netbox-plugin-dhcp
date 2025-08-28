from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import PDPool


__all__ = ("PDPoolSerializer",)


class PDPoolSerializer(NetBoxModelSerializer):
    class Meta:
        model = PDPool

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
        view_name="plugins-api:netbox_dhcp-api:pdpool-detail"
    )
