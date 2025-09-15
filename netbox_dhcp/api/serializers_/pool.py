from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import IPRangeSerializer

from netbox_dhcp.models import Pool
from ..nested_serializers import NestedClientClassSerializer


__all__ = ("PoolSerializer",)


class PoolSerializer(NetBoxModelSerializer):
    class Meta:
        model = Pool

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "ip_range",
            "client_class",
            "require_client_classes",
            "user_context",
            "comment",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "ip_range",
            "comment",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:pool-detail"
    )

    ip_range = IPRangeSerializer(
        nested=True,
        read_only=False,
        required=False,
    )
    client_class = NestedClientClassSerializer(
        nested=True,
        read_only=False,
        required=False,
    )
    require_client_classes = NestedClientClassSerializer(
        nested=True,
        many=True,
        read_only=False,
        required=False,
    )

    def create(self, validated_data):
        require_client_classes = validated_data.pop("require_client_classes", None)

        pool = super().create(validated_data)

        if require_client_classes is not None:
            pool.require_client_classes.set(require_client_classes)

        return pool

    def update(self, instance, validated_data):
        require_client_classes = validated_data.pop("require_client_classes", None)

        pool = super().update(instance, validated_data)

        if require_client_classes is not None:
            pool.require_client_classes.set(require_client_classes)

        return pool
