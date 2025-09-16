import django_filters
from django.utils.translation import gettext as _

from netbox_dhcp.models import ClientClass

__all__ = (
    "NetworkClientClassesMixin",
    "ClientClassMixin",
)


class NetworkClientClassesMixin:
    network_client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_classes__name",
        to_field_name="name",
        label=_("Network Client Class"),
    )
    network_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_classes",
        label=_("Network Client Class ID"),
    )


class ClientClassMixin:
    client_class = django_filters.ModelMultipleChoiceFilter(
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
        field_name="require_client_classes__name",
        to_field_name="name",
        label=_("Required Client Class"),
    )
    require_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="require_client_classes",
        label=_("Required Client Class ID"),
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
