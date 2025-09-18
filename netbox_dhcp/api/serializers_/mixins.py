from django.utils.translation import gettext as _

from ..nested_serializers import NestedClientClassSerializer


__all__ = (
    "ClientClassAssignmentSerializerMixin",
    "ClientClassDefinitionSerializerMixin",
    "ClientClassSerializerMixin",
)


class ClientClassAssignmentSerializerMixin:
    assign_client_classes = NestedClientClassSerializer(
        many=True,
        nested=True,
        read_only=False,
        required=False,
        help_text=_("Client class to assign"),
    )


class ClientClassDefinitionSerializerMixin:
    client_class_definitions = NestedClientClassSerializer(
        many=True,
        nested=True,
        read_only=False,
        required=False,
        help_text=_("Client class definitions"),
    )


class ClientClassSerializerMixin(ClientClassDefinitionSerializerMixin):
    client_class = NestedClientClassSerializer(
        nested=True,
        read_only=False,
        required=False,
        help_text=_("Client class to be matched"),
    )
    require_client_classes = NestedClientClassSerializer(
        many=True,
        nested=True,
        read_only=False,
        required=False,
        help_text=_("Required client classes to be matched"),
    )
    evaluate_additional_classes = NestedClientClassSerializer(
        many=True,
        nested=True,
        read_only=False,
        required=False,
        help_text=_("Client classes to evaluate after matching"),
    )
