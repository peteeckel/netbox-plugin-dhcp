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
    "ChildSubnetSerializerMixin",
    "ChildSharedNetworkSerializerMixin",
    "ChildPoolSerializerMixin",
    "ChildPDPoolSerializerMixin",
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


class ChildSubnetSerializerMixin:
    child_subnets = NestedSubnetSerializer(
        many=True,
        read_only=False,
        required=False,
    )


class ChildSharedNetworkSerializerMixin:
    child_shared_networks = NestedSharedNetworkSerializer(
        many=True,
        read_only=True,
        required=False,
    )


class ChildPoolSerializerMixin:
    child_pools = NestedPoolSerializer(
        many=True,
        read_only=False,
        required=False,
    )


class ChildPDPoolSerializerMixin:
    child_pd_pools = NestedPDPoolSerializer(
        many=True,
        read_only=True,
        required=False,
    )


class ChildHostReservationSerializerMixin:
    child_host_reservations = NestedHostReservationSerializer(
        many=True,
        read_only=False,
        required=False,
    )
