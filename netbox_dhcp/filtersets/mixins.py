import django_filters
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import Prefix

from netbox_dhcp.models import (
    ClientClass,
    Subnet,
    Pool,
    PDPool,
    HostReservation,
    SharedNetwork,
    DHCPServer,
)
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
    AllocatorTypeChoices,
    PDAllocatorTypeChoices,
)

__all__ = (
    "BOOTPFilterMixin",
    "OfferLifetimeFilterMixin",
    "LeaseFilterMixin",
    "NetworkFilterMixin",
    "PrefixFilterMixin",
    "ClientClassAssignmentFilterMixin",
    "ClientClassDefinitionFilterMixin",
    "ClientClassFilterMixin",
    "DDNSUpdateFilterMixin",
    "ChildSubnetFilterMixin",
    "ChildSharedNetworkFilterMixin",
    "ChildPoolFilterMixin",
    "ChildPDPoolFilterMixin",
    "ChildHostReservationFilterMixin",
    "ChildClientClassFilterMixin",
    "ParentSubnetFilterMixin",
    "ParentSharedNetworkFilterMixin",
    "ParentDHCPServerFilterMixin",
)


class BOOTPFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "next_server",
        "server_hostname",
        "boot_file_name",
    ]

    next_server = django_filters.CharFilter(
        label=_("Next Server"),
    )
    server_hostname = django_filters.CharFilter(
        label=_("Server Hostname"),
    )
    boot_file_name = django_filters.CharFilter(
        label=_("Boot File Name"),
    )


class OfferLifetimeFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "offer_lifetime",
    ]

    offer_lifetime = django_filters.NumberFilter(
        label=_("Offer Lifetime"),
    )


class LifetimeFilterMixin(OfferLifetimeFilterMixin):
    FILTER_FIELDS = [
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
    ]

    valid_lifetime = django_filters.NumberFilter(
        label=_("Valid Lifetime"),
    )
    min_valid_lifetime = django_filters.NumberFilter(
        label=_("Minimum Valid Lifetime"),
    )
    max_valid_lifetime = django_filters.NumberFilter(
        label=_("Maximum Valid Lifetime"),
    )
    preferred_lifetime = django_filters.NumberFilter(
        label=_("Preferred Lifetime"),
    )
    min_preferred_lifetime = django_filters.NumberFilter(
        label=_("Minimum Preferred Lifetime"),
    )
    max_preferred_lifetime = django_filters.NumberFilter(
        label=_("Maximum Preferred Lifetime"),
    )


class LeaseFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = (
        "renew_timer",
        "rebind_timer",
        "match_client_id",
        "authoritative",
        "reservations_global",
        "reservations_out_of_pool",
        "reservations_in_subnet",
        "calculate_tee_times",
        "t1_percent",
        "t2_percent",
        "cache_threshold",
        "cache_max_age",
        "adaptive_lease_time_threshold",
        "store_extended_info",
        "allocator",
        "pd_allocator",
    )

    renew_timer = django_filters.NumberFilter(
        label=_("Renew Timer"),
    )
    rebind_timer = django_filters.NumberFilter(
        label=_("Rebind Timer"),
    )
    t1_percent = django_filters.NumberFilter(
        label=_("T1"),
    )
    t2_percent = django_filters.NumberFilter(
        label=_("T2"),
    )
    cache_threshold = django_filters.NumberFilter(
        label=_("Cache Threshold"),
    )
    cache_max_age = django_filters.NumberFilter(
        label=_("Cache Maximum Age"),
    )
    adaptive_lease_time_threshold = django_filters.NumberFilter(
        label=_("Adaptive Lease Time Threshold"),
    )
    allocator = django_filters.MultipleChoiceFilter(
        choices=AllocatorTypeChoices,
        label=_("Allocator"),
    )
    pd_allocator = django_filters.MultipleChoiceFilter(
        choices=PDAllocatorTypeChoices,
        label=_("Prefix Delegation Allocator"),
    )


class ClientClassAssignmentFilterMixin(NetBoxModelFilterSet):
    assign_client_class = django_filters.CharFilter(
        field_name="assign_client_classes__name",
        label=_("Assign Client Class"),
    )
    assign_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="assign_client_classes",
        label=_("Assign Client Class ID"),
    )


class ClientClassDefinitionFilterMixin(NetBoxModelFilterSet):
    client_class_definition = django_filters.CharFilter(
        field_name="client_class_definitions__name",
        label=_("Client Class Definition"),
    )
    client_class_definition_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class_definitions",
        label=_("Client Class Definition ID"),
    )


class ClientClassFilterMixin(ClientClassDefinitionFilterMixin):
    client_class = django_filters.CharFilter(
        field_name="client_class__name",
        label=_("Client Class"),
    )
    client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class",
        label=_("Client Class ID"),
    )
    required_client_class = django_filters.CharFilter(
        field_name="required_client_classes__name",
        label=_("Require Client Class"),
    )
    required_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="required_client_classes",
        label=_("Require Client Class ID"),
    )
    evaluate_additional_class = django_filters.CharFilter(
        field_name="evaluate_additional_classes__name",
        label=_("Evaluate Additional Class"),
    )
    evaluate_additional_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="evaluate_additional_classes",
        label=_("Evaluate Additional Class ID"),
    )


class DDNSUpdateFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "hostname_char_set",
        "hostname_char_replacement",
        "ddns_send_updates",
        "ddns_override_no_update",
        "ddns_override_client_update",
        "ddns_replace_client_name",
        "ddns_generated_prefix",
        "ddns_qualifying_suffix",
        "ddns_update_on_renew",
        "ddns_conflict_resolution_mode",
        "ddns_ttl_percent",
        "ddns_ttl",
        "ddns_ttl_min",
        "ddns_ttl_max",
    ]

    hostname_char_set = django_filters.CharFilter(
        label=_("Hostname Character Set"),
    )
    hostname_char_replacement = django_filters.CharFilter(
        label=_("Hostname Replacement Characters"),
    )
    ddns_replace_client_name = django_filters.MultipleChoiceFilter(
        choices=DDNSReplaceClientNameChoices,
        label=_("Replace Client Name"),
    )
    ddns_generated_prefix = django_filters.CharFilter(
        label=_("Generated Prefix"),
    )
    ddns_qualifying_suffix = django_filters.CharFilter(
        label=_("Qualifying Suffix"),
    )
    ddns_conflict_resolution_mode = django_filters.MultipleChoiceFilter(
        choices=DDNSConflictResolutionModeChoices,
        label=_("Conflict Resolution Mode"),
    )
    ddns_ttl_percent = django_filters.NumberFilter(
        label=_("TTL Percent"),
    )
    ddns_ttl = django_filters.NumberFilter(
        label=_("TTL"),
    )
    ddns_ttl_min = django_filters.NumberFilter(
        label=_("Minimum TTL"),
    )
    ddns_ttl_max = django_filters.NumberFilter(
        label=_("Maximum TTL"),
    )


class NetworkFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "relay",
        "interface_id",
        "rapid_commit",
    ]


class PrefixFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "prefix",
    ]

    prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="prefix",
        label=_("Prefix ID"),
    )
    prefix = django_filters.CharFilter(
        field_name="prefix__prefix",
        label=_("Prefix"),
    )


class ChildSubnetFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_subnets",
    ]

    child_subnet = django_filters.CharFilter(
        field_name="child_subnets__name",
        label=_("Subnet"),
    )
    child_subnet_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Subnet.objects.all(),
        field_name="child_subnets",
        label=_("Subnet ID"),
    )


class ChildSharedNetworkFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_shared_networks",
    ]

    child_shared_network = django_filters.CharFilter(
        field_name="child_shared_networks__name",
        label=_("Shared Network"),
    )
    child_shared_network_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SharedNetwork.objects.all(),
        field_name="child_shared_networks",
        label=_("Shared Network ID"),
    )


class ChildPoolFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_pools",
    ]

    child_pool = django_filters.CharFilter(
        field_name="child_pools__name",
        label=_("Pool"),
    )
    child_pool_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Pool.objects.all(),
        field_name="child_pools",
        label=_("Pool ID"),
    )


class ChildPDPoolFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_pd_pools",
    ]

    child_pd_pool = django_filters.CharFilter(
        field_name="child_pd_pools__name",
        label=_("Prefix Delegation Pool"),
    )
    child_pd_pool_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PDPool.objects.all(),
        field_name="child_pd_pools",
        label=_("Prefix Delegation Pool ID"),
    )


class ChildHostReservationFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_host_reservations",
    ]

    child_host_reservation = django_filters.CharFilter(
        field_name="child_host_reservations__name",
        label=_("Host Reservation"),
    )
    child_host_reservation_id = django_filters.ModelMultipleChoiceFilter(
        queryset=HostReservation.objects.all(),
        field_name="child_host_reservations",
        label=_("Host Reservation ID"),
    )


class ChildClientClassFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "child_client_classes",
    ]

    child_client_class = django_filters.CharFilter(
        field_name="child_client_classes__name",
        label=_("Client Class"),
    )
    child_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="child_client_classes",
        label=_("Client Class ID"),
    )


class ParentSubnetFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "parent_subnets",
    ]

    parent_subnet = django_filters.CharFilter(
        field_name="parent_subnets__name",
        label=_("Parent Subnet"),
    )
    parent_subnet_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Subnet.objects.all(),
        field_name="parent_subnets",
        label=_("Parent Subnet ID"),
    )


class ParentSharedNetworkFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "parent_sharednetworks",
    ]

    parent_shared_network = django_filters.CharFilter(
        field_name="parent_sharednetworks__name",
        label=_("Parent Shared Network"),
    )
    parent_shared_network_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SharedNetwork.objects.all(),
        field_name="parent_sharednetworks",
        label=_("Parent Shared Network ID"),
    )


class ParentDHCPServerFilterMixin(NetBoxModelFilterSet):
    FILTER_FIELDS = [
        "parent_dhcpservers",
    ]

    parent_dhcp_server = django_filters.CharFilter(
        field_name="parent_dhcpservers__name",
        label=_("Parent DHCP Server"),
    )
    parent_dhcp_server_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPServer.objects.all(),
        field_name="parent_dhcpservers",
        label=_("Parent DHCP Server ID"),
    )
