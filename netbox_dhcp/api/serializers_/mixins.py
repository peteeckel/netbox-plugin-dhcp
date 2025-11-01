from django.utils.translation import gettext as _

from ..nested_serializers import (
    NestedClientClassSerializer,
    NestedSubnetSerializer,
    NestedSharedNetworkSerializer,
    NestedPoolSerializer,
    NestedPDPoolSerializer,
    NestedHostReservationSerializer,
)


__all__ = (
    "ClientClassSerializerMixin",
    "EvaluateClientClassSerializerMixin",
    "ChildHostReservationSerializerMixin",
)


class ClientClassSerializerMixin:
    client_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client Classes"),
    )


class EvaluateClientClassSerializerMixin:
    evaluate_additional_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client classes to evaluate after matching"),
    )


class ChildHostReservationSerializerMixin:
    child_host_reservations = NestedHostReservationSerializer(
        many=True,
        read_only=False,
        required=False,
    )
