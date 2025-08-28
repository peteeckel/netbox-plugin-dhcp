from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import HostReservation


__all__ = ("HostReservationSerializer",)


class HostReservationSerializer(NetBoxModelSerializer):
    class Meta:
        model = HostReservation

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
        view_name="plugins-api:netbox_dhcp-api:hostreservation-detail"
    )
