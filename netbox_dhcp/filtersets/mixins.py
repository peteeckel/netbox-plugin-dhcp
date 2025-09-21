import django_filters
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import ClientClass, Subnet, Pool, PDPool, HostReservation
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
)

__all__ = (
    "ClientClassAssignmentFilterMixin",
    "ClientClassDefinitionFilterMixin",
    "ClientClassFilterMixin",
    "DDNSUpdateFilterMixin",
    "ChildSubnetFilterMixin",
    "ChildPoolFilterMixin",
    "ChildPDPoolFilterMixin",
    "ChildHostReservationFilterMixin",
)


class ClientClassAssignmentFilterMixin(NetBoxModelFilterSet):
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


class ClientClassDefinitionFilterMixin(NetBoxModelFilterSet):
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


class DDNSUpdateFilterMixin(NetBoxModelFilterSet):
    ddns_replace_client_name = django_filters.MultipleChoiceFilter(
        choices=DDNSReplaceClientNameChoices,
        label=_("Replace Client Name"),
    )
    ddns_conflict_resolution_mode = django_filters.MultipleChoiceFilter(
        choices=DDNSConflictResolutionModeChoices,
        label=_("Conflict Resolution Mode"),
    )


class ChildSubnetFilterMixin(NetBoxModelFilterSet):
    child_subnet = django_filters.ModelMultipleChoiceFilter(
        queryset=Subnet.objects.all(),
        field_name="child_subnets__name",
        to_field_name="name",
        label=_("Subnet"),
    )
    child_subnet_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Subnet.objects.all(),
        field_name="child_subnets",
        to_field_name="id",
        label=_("Subnet ID"),
    )


class ChildPoolFilterMixin(NetBoxModelFilterSet):
    child_pool = django_filters.ModelMultipleChoiceFilter(
        queryset=Pool.objects.all(),
        field_name="child_pools__name",
        to_field_name="name",
        label=_("Pool"),
    )
    child_pool_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Pool.objects.all(),
        field_name="child_pools",
        label=_("Pool ID"),
    )


class ChildPDPoolFilterMixin(NetBoxModelFilterSet):
    child_pd_pool = django_filters.ModelMultipleChoiceFilter(
        queryset=PDPool.objects.all(),
        field_name="child_pd_pools__name",
        to_field_name="name",
        label=_("Prefix Delegation Pool"),
    )
    child_pd_pool_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PDPool.objects.all(),
        field_name="child_pd_pools",
        label=_("Prefix Delegation Pool ID"),
    )


class ChildHostReservationFilterMixin(NetBoxModelFilterSet):
    child_host_reservation = django_filters.ModelMultipleChoiceFilter(
        queryset=HostReservation.objects.all(),
        field_name="child_host_reservations__name",
        to_field_name="name",
        label=_("Host Reservation"),
    )
    child_host_reservation_id = django_filters.ModelMultipleChoiceFilter(
        queryset=HostReservation.objects.all(),
        field_name="child_host_reservations",
        label=_("Host Reservation ID"),
    )
