from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import IPRangeSerializer

from netbox_dhcp.models import Pool
from ..nested_serializers import NestedClientClassSerializer

from .mixins import (
    ClientClassSerializerMixin,
)

__all__ = ("PoolSerializer",)


class PoolSerializer(
    ClientClassSerializerMixin,
    NetBoxModelSerializer,
):
    class Meta:
        model = Pool

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "ip_range",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
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

    def create(self, validated_data):
        client_class_definitions = validated_data.pop("client_class_definitions", None)
        required_client_classes = validated_data.pop("required_client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pool = super().create(validated_data)

        if client_class_definitions is not None:
            pool.client_class_definitions.set(client_class_definitions)
        if required_client_classes is not None:
            pool.required_client_classes.set(required_client_classes)
        if evaluate_additional_classes is not None:
            pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pool

    def update(self, instance, validated_data):
        client_class_definitions = validated_data.pop("client_class_definitions", None)
        required_client_classes = validated_data.pop("required_client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pool = super().update(instance, validated_data)

        if client_class_definitions is not None:
            pool.client_class_definitions.set(client_class_definitions)
        if required_client_classes is not None:
            pool.required_client_classes.set(required_client_classes)
        if evaluate_additional_classes is not None:
            pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pool
