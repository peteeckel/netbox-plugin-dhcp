import django_filters
from django.utils.translation import gettext as _

from netbox_dhcp.models import ClientClass
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
)

__all__ = (
    "ClientClassAssignmentFilterMixin",
    "ClientClassDefinitionFilterMixin",
    "ClientClassFilterMixin",
    "DDNSUpdateFilterMixin",
)


class ClientClassAssignmentFilterMixin:
    assign_client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="assign_client_classes__name",
        to_field_name="name",
        label=_("Assign Client Class"),
    )
    assign_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="assign_client_classes",
        label=_("Assign Client Class ID"),
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


class ClientClassFilterMixin(ClientClassDefinitionFilterMixin):
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
    required_client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="required_client_classes__name",
        to_field_name="name",
        label=_("Require Client Class"),
    )
    required_client_class_id = django_filters.ModelMultipleChoiceFilter(
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


class DDNSUpdateFilterMixin:
    ddns_replace_client_name = django_filters.MultipleChoiceFilter(
        choices=DDNSReplaceClientNameChoices,
        label=_("Replace Client Name"),
    )
    ddns_conflict_resolution_mode = django_filters.MultipleChoiceFilter(
        choices=DDNSConflictResolutionModeChoices,
        label=_("Conflict Resolution Mode"),
    )
