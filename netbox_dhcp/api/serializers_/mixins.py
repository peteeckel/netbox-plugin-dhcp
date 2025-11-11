from django.utils.translation import gettext as _

from netbox.api.serializers import NetBoxModelSerializer

from ..nested_serializers import (
    NestedClientClassSerializer,
)


__all__ = (
    "ClientClassSerializerMixin",
    "EvaluateClientClassSerializerMixin",
)


class ClientClassSerializerMixin(NetBoxModelSerializer):
    client_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client Classes"),
    )


class EvaluateClientClassSerializerMixin(NetBoxModelSerializer):
    evaluate_additional_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client classes to evaluate after matching"),
    )
