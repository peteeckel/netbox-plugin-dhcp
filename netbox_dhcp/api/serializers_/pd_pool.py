from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import PrefixSerializer

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
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "user_context",
            "comment",
            "tags",
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

    prefix = PrefixSerializer(
        nested=True,
        read_only=False,
        required=True,
    )
    excluded_prefix = PrefixSerializer(
        nested=True,
        read_only=False,
        required=False,
    )
