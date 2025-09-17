import django_filters
from django.utils.translation import gettext as _

from netbox_dhcp.models import ClientClass

__all__ = (
    "ClientClassDefinitionFilterMixin",
    "ClientClassFilterMixin",
)


class ClientClassDefinitionFilterMixin:
    client_class_definition = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class_definitions__name",
        to_field_name="name",
        label=_("Client Class Definition"),
    )
    client_class_definition_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class_definitions",
        label=_("Client Class Definition ID"),
    )


class ClientClassFilterMixin:
    client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class__name",
        to_field_name="name",
        label=_("Client Class"),
    )
    client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class",
        label=_("Client Class ID"),
    )
    require_client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="required_client_classes__name",
        to_field_name="name",
        label=_("Require Client Class"),
    )
    require_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="required_client_classes",
        label=_("Require Client Class ID"),
    )
    evaluate_additional_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="evaluate_additional_classes__name",
        to_field_name="name",
        label=_("Evaluate Additional Class"),
    )
    evaluate_additional_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="evaluate_additional_classes",
        label=_("Evaluate Additional Class ID"),
    )
