import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import Device, Interface
from virtualization.models import VirtualMachine, VMInterface
from utilities.filters import MultiValueCharFilter

from netbox_dhcp.models import DHCPServer, DHCPCluster, ClientClass
from netbox_dhcp.choices import (
    DHCPServerStatusChoices,
    DHCPServerIDTypeChoices,
    HostReservationIdentifierChoices,
)
from .mixins import (
    BOOTPFilterMixin,
    LifetimeFilterMixin,
    LeaseFilterMixin,
    DDNSUpdateFilterMixin,
    ChildSubnetFilterMixin,
    ChildSharedNetworkFilterMixin,
    ChildHostReservationFilterMixin,
)

__all__ = ("DHCPServerFilterSet",)


class DHCPServerFilterSet(
    BOOTPFilterMixin,
    LifetimeFilterMixin,
    LeaseFilterMixin,
    DDNSUpdateFilterMixin,
    ChildSubnetFilterMixin,
    ChildSharedNetworkFilterMixin,
    ChildHostReservationFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = DHCPServer

        fields = (
            "id",
            "name",
            "description",
            "server_id",
            "host_reservation_identifiers",
            "echo_client_id",
            "relay_supplied_options",
            "status",
            "dhcp_cluster",
            "device",
            "device_interfaces",
            "virtual_machine",
            "virtual_machine_interfaces",
            "decline_probation_period",
            *BOOTPFilterMixin.FILTER_FIELDS,
            *LifetimeFilterMixin.FILTER_FIELDS,
            *LeaseFilterMixin.FILTER_FIELDS,
            *DDNSUpdateFilterMixin.FILTER_FIELDS,
            *ChildSubnetFilterMixin.FILTER_FIELDS,
            *ChildSharedNetworkFilterMixin.FILTER_FIELDS,
            *ChildHostReservationFilterMixin.FILTER_FIELDS,
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=DHCPServerStatusChoices,
    )
    server_id = django_filters.MultipleChoiceFilter(
        choices=DHCPServerIDTypeChoices,
    )

    dhcp_cluster_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPCluster.objects.all(),
        label=_("DHCP Cluster ID"),
    )
    dhcp_cluster = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPCluster.objects.all(),
        field_name="dhcp_cluster__name",
        to_field_name="name",
        label=_("DHCP Cluster"),
    )

    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name="device",
        label=_("Device ID"),
    )
    device = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name="device__name",
        to_field_name="name",
        label=_("Device"),
    )
    device_interface_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Interface.objects.all(),
        field_name="device_interfaces",
        label=_("Device Interface ID"),
    )
    device_interface = django_filters.ModelMultipleChoiceFilter(
        queryset=Interface.objects.all(),
        field_name="device_interfaces__name",
        to_field_name="name",
        label=_("Device Interface"),
    )
    virtual_machine_id = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        field_name="virtual_machine",
        label=_("Virtual Machine ID"),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        field_name="virtual_machine__name",
        to_field_name="name",
        label=_("Virtual Machine"),
    )
    virtual_machine_interface_id = django_filters.ModelMultipleChoiceFilter(
        queryset=VMInterface.objects.all(),
        field_name="virtual_machine_interfaces",
        label=_("Virtual Machine Interface ID"),
    )
    virtual_machine_interface = django_filters.ModelMultipleChoiceFilter(
        queryset=VMInterface.objects.all(),
        field_name="virtual_machine_interfaces__name",
        to_field_name="name",
        label=_("Virtual Machine Interface"),
    )
    host_reservation_identifiers = django_filters.MultipleChoiceFilter(
        choices=HostReservationIdentifierChoices,
        method="filter_host_reservation_identifiers",
        label=_("Host Reservation Identifiers"),
    )
    relay_supplied_options = MultiValueCharFilter(
        method="filter_relay_supplied_options",
        label=_("Relay Supplied Options"),
    )
    decline_probation_period = django_filters.NumberFilter(
        label=_("Decline Probation Period"),
    )

    client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class_definition_set",
        label=_("Client Class ID"),
    )
    client_class = django_filters.CharFilter(
        field_name="client_class_definition_set__name",
        distinct=True,
        label=_("Client Class"),
    )

    def filter_host_reservation_identifiers(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(host_reservation_identifiers__overlap=value)

    def filter_relay_supplied_options(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(relay_supplied_options__overlap=value)

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(dhcp_cluster__name__icontains=value)
            | Q(device__name__icontains=value)
            | Q(virtual_machine__name__icontains=value)
        )
        return queryset.filter(qs_filter)
