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
    "ClientClassAssignmentSerializerMixin",
    "ClientClassDefinitionSerializerMixin",
    "ClientClassSerializerMixin",
    "ChildSubnetSerializerMixin",
    "ChildSharedNetworkSerializerMixin",
    "ChildPoolSerializerMixin",
    "ChildPDPoolSerializerMixin",
    "ChildHostReservationSerializerMixin",
    "ChildClientClassSerializerMixin",
)


class ClientClassAssignmentSerializerMixin:
    assign_client_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client class to assign"),
    )


class ClientClassDefinitionSerializerMixin:
    client_class_definitions = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Client class definitions"),
    )


class ClientClassSerializerMixin(ClientClassDefinitionSerializerMixin):
    client_class = NestedClientClassSerializer(
        read_only=False,
        required=False,
        help_text=_("Client class to be matched"),
    )
    required_client_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
        help_text=_("Required client classes to be matched"),
    )
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
        read_only=False,
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
        read_only=False,
        required=False,
    )


class ChildHostReservationSerializerMixin:
    child_host_reservations = NestedHostReservationSerializer(
        many=True,
        read_only=False,
        required=False,
    )


class ChildClientClassSerializerMixin:
    child_client_classes = NestedClientClassSerializer(
        many=True,
        read_only=False,
        required=False,
    )
