from typing import Annotated, List, Union, TYPE_CHECKING

import strawberry
import strawberry_django

from netbox.graphql.types import NetBoxObjectType

if TYPE_CHECKING:
    from ipam.graphql.types import IPAddressType, PrefixType
    from dcim.graphql.types import MACAddressType, DeviceType
    from virtualization.graphql.types import VirtualMachineType

from netbox_dhcp.models import (
    ClientClass,
    DHCPCluster,
    DHCPServer,
    HostReservation,
    OptionDefinition,
    Option,
)
from .filters import (
    NetBoxDHCPClientClassFilter,
    NetBoxDHCPClusterFilter,
    NetBoxDHCPServerFilter,
    NetBoxDHCPHostReservationFilter,
    NetBoxDHCPOptionDefinitionFilter,
    NetBoxDHCPOptionFilter,
)


@strawberry.type
class BOOTPGraphQLTypeMixin:
    next_server: str | None
    server_hostname: str | None
    boot_file_name: str | None


@strawberry.type
class DDNSUpdateGraphQLTypeMixin:
    ddns_send_updates: bool | None
    ddns_override_no_update: bool | None
    ddns_override_client_update: bool | None
    ddns_replace_client_name: str | None
    ddns_generated_prefix: str | None
    ddns_qualifying_suffix: str | None
    ddns_update_on_renew: bool | None
    ddns_conflict_resolution_mode: str | None
    ddns_ttl_percent: float | None
    ddns_ttl: int | None
    ddns_ttl_min: int | None
    ddns_ttl_max: int | None
    hostname_char_set: str | None
    hostname_char_replacement: str | None


@strawberry.type
class OfferLifetimeGraphQLTypeMixin:
    offer_lifetime: int | None


@strawberry.type
class LifetimeGraphQLTypeMixin(OfferLifetimeGraphQLTypeMixin):
    valid_lifetime: int | None
    min_valid_lifetime: int | None
    max_valid_lifetime: int | None
    preferred_lifetime: int | None
    min_preferred_lifetime: int | None
    max_preferred_lifetime: int | None


@strawberry.type
class LeaseGraphQLTypeMixin:
    renew_timer: int | None
    rebind_timer: int | None
    match_client_id: bool | None
    authoritative: bool | None
    reservations_global: bool | None
    reservations_out_of_pool: bool | None
    reservations_in_subnet: bool | None
    calculate_tee_times: bool | None
    t1_percent: float | None
    t2_percent: float | None
    cache_threshold: float | None
    cache_max_age: int | None
    adaptive_lease_time_threshold: float | None
    store_extended_info: bool | None
    allocator: str | None
    pd_allocator: str | None


@strawberry_django.type(ClientClass, fields="__all__", filters=NetBoxDHCPClientClassFilter)
class NetBoxDHCPClientClassType(
    BOOTPGraphQLTypeMixin,
    LifetimeGraphQLTypeMixin,
    NetBoxObjectType,
):
    name: str
    description: str | None
    test: str | None
    template_test: str | None
    only_if_required: bool | None
    only_in_additional_list: bool | None


@strawberry_django.type(DHCPCluster, fields="__all__", filters=NetBoxDHCPClusterFilter)
class NetBoxDHCPDHCPClusterType(NetBoxObjectType):
    name: str
    description: str | None
    status: str
    dhcp_servers: List[Annotated["NetBoxDHCPDHCPServerType", strawberry.lazy("netbox_dhcp.graphql.types")]]


@strawberry_django.type(DHCPServer, fields="__all__", filters=NetBoxDHCPServerFilter)
class NetBoxDHCPDHCPServerType(
    BOOTPGraphQLTypeMixin,
    DDNSUpdateGraphQLTypeMixin,
    NetBoxObjectType,
):
    name: str
    description: str | None
    status: str
    server_id: str | None
#   host_reservation_identifiers:
    echo_client_id: bool | None
    relay_supplied_options: List[int] | None
    dhcp_cluster: Annotated["NetBoxDHCPDHCPClusterType", strawberry.lazy("netbox_dhcp.graphql.types")] | None
    device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None
    virtual_machine: Annotated["VirtualMachineType", strawberry.lazy("virtualization.graphql.types")] | None
    decline_probation_period: float | None


@strawberry_django.type(HostReservation, fields="__all__", filters=NetBoxDHCPHostReservationFilter)
class NetBoxDHCPHostReservationType(
    BOOTPGraphQLTypeMixin,
    NetBoxObjectType,
):
    name: str
    description: str | None
    duid: str | None
    hw_address: Annotated["MACAddressType", strawberry.lazy("dcim.graphql.types")] | None
    flex_id: str | None
    circuit_id: str | None
    client_id: str | None
    hostname: str | None
    ipv4_address: Annotated["IPAddressType", strawberry.lazy("ipam.graphql.types")] | None
    ipv6_addresses: List[Annotated["IPAddressType", strawberry.lazy("ipam.graphql.types")]] | None
    ipv6_prefixes: List[Annotated["PrefixType", strawberry.lazy("ipam.graphql.types")]] | None
    excluded_ipv6_prefixes: List[Annotated["PrefixType", strawberry.lazy("ipam.graphql.types")]] | None
    assign_client_classes: List[Annotated["NetBoxDHCPClientClassType", strawberry.lazy("netbox_dhcp.graphql.types")]] | None


@strawberry_django.type(OptionDefinition, fields="__all__", filters=NetBoxDHCPOptionDefinitionFilter)
class NetBoxDHCPOptionDefinitionType(NetBoxObjectType):
    name: str
    description: str | None
    code: int
    space: str
    encapsulate: str | None
    family: int
    type: str
    record_types: List[str] | None


@strawberry_django.type(Option, exclude=['assigned_object_type', 'assigned_object_id'], filters=NetBoxDHCPOptionFilter)
class NetBoxDHCPOptionType(NetBoxObjectType):
    definition: Annotated["NetBoxDHCPOptionDefinitionType", strawberry.lazy("netbox_dhcp.graphql.types")]
    data: str | None
    description: str | None
    csv_format: bool | None
    always_send: bool | None
    never_send: bool | None
    assigned_object: Annotated[
        Union[
            Annotated["NetBoxDHCPDHCPServerType", strawberry.lazy('netbox_dhcp.graphql.types')],
#           Annotated["NetBoxDHCPSubnetType", strawberry.lazy('netbox_dhcp.graphql.types')].
#           Annotated["NetBoxDHCPSharedNetworkType", strawberry.lazy('netbox_dhcp.graphql.types')],
#           Annotated["NetBoxDHCPPoolType", strawberry.lazy('netbox_dhcp.graphql.types')],
#           Annotated["NetBoxDHCPPDPoolType", strawberry.lazy('netbox_dhcp.graphql.types')],
            Annotated["NetBoxDHCPHostReservationType", strawberry.lazy('netbox_dhcp.graphql.types')],
            Annotated["NetBoxDHCPClientClassType", strawberry.lazy('netbox_dhcp.graphql.types')],
        ], strawberry.union("OptionAssignmentType")
    ] | None
