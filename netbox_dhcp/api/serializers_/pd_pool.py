from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import PrefixSerializer

from netbox_dhcp.models import PDPool

from .mixins import (
    ClientClassSerializerMixin,
    EvaluateClientClassSerializerMixin,
)

__all__ = ("PDPoolSerializer",)


class PDPoolSerializer(
    ClientClassSerializerMixin,
    EvaluateClientClassSerializerMixin,
    NetBoxModelSerializer,
):
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
            "client_classes",
            "evaluate_additional_classes",
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
            "prefix",
            "comment",
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

    def create(self, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pd_pool = super().create(validated_data)

        if client_classes is not None:
            pd_pool.client_classes.set(client_classes)
        if evaluate_additional_classes is not None:
            pd_pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pd_pool

    def update(self, instance, validated_data):
        client_classes = validated_data.pop("client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        pd_pool = super().update(instance, validated_data)

        if client_classes is not None:
            pd_pool.client_classes.set(client_classes)
        if evaluate_additional_classes is not None:
            pd_pool.evaluate_additional_classes.set(evaluate_additional_classes)

        return pd_pool
