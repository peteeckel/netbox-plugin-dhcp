from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import IPRangeSerializer

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassSerializerMixin,
    EvaluateClientClassSerializerMixin,
)

from .subnet import SubnetSerializer

__all__ = ("PoolSerializer",)


class PoolSerializer(
    ClientClassSerializerMixin,
    EvaluateClientClassSerializerMixin,
    NetBoxModelSerializer,
):
    class Meta:
        model = Pool

        fields = (
            "id",
            "url",
            "display",
            "display_url",
            "name",
            "description",
            "subnet",
            "ip_range",
            "client_classes",
            "evaluate_additional_classes",
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
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
        view_name="plugins-api:netbox_dhcp-api:pool-detail"
    )

    subnet = SubnetSerializer(
        nested=True,
        read_only=False,
        required=True,
    )
    ip_range = IPRangeSerializer(
        nested=True,
        read_only=False,
        required=False,
    )

    def create(self, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pool = super().create(validated_data)

        if client_classes is not None:
            pool.client_classes.set(client_classes)
        if evaluate_additional_classes is not None:
            pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pool

    def update(self, instance, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pool = super().update(instance, validated_data)

        if client_classes is not None:
            pool.client_classes.set(client_classes)
        if evaluate_additional_classes is not None:
            pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pool
