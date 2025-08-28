from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import ClientClass


__all__ = ("ClientClassSerializer",)


class ClientClassSerializer(NetBoxModelSerializer):
    class Meta:
        model = ClientClass

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
        view_name="plugins-api:netbox_dhcp-api:clientclass-detail"
    )
