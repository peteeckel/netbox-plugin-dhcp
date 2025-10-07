from dataclasses import dataclass

from typing import Annotated, TYPE_CHECKING

import strawberry
import strawberry_django
from strawberry_django import FilterLookup

# from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

if TYPE_CHECKING:
    from netbox_dhcp.graphql.enums import (
        NetBoxDHCPAllocatorTypeEnum,
        NetBoxDHCPPDAllocatorTypeEnum,
    )


__all__ = (
    "BOOTPGraphQLFilterMixin",
    "DDNSUpdateGraphQLFilterMixin",
    "OfferLifetimeGraphQLFilterMixin",
    "LifetimeGraphQLFilterMixin",
    "LeaseGraphQLFilterMixin",
)


@dataclass
class BOOTPGraphQLFilterMixin:
    next_server: FilterLookup[str] | None = strawberry_django.filter_field()
    server_hostname: FilterLookup[str] | None = strawberry_django.filter_field()
    boot_file_name: FilterLookup[str] | None = strawberry_django.filter_field()


@dataclass
class DDNSUpdateGraphQLFilterMixin:
    ddns_send_updates: FilterLookup[bool] | None = strawberry_django.filter_field()
    ddns_override_no_update: FilterLookup[bool] | None = strawberry_django.filter_field()
    ddns_override_client_update: FilterLookup[bool] | None = strawberry_django.filter_field()
    ddns_replace_client_name: FilterLookup[str] | None = strawberry_django.filter_field()
    ddns_generated_prefix: FilterLookup[str] | None = strawberry_django.filter_field()
    ddns_qualifying_suffix: FilterLookup[str] | None = strawberry_django.filter_field()
    ddns_update_on_renew: FilterLookup[bool] | None = strawberry_django.filter_field()
    ddns_conflict_resolution_mode: FilterLookup[str] | None = strawberry_django.filter_field()
    ddns_ttl_percent: FilterLookup[float] | None = strawberry_django.filter_field()
    ddns_ttl: FilterLookup[int] | None = strawberry_django.filter_field()
    ddns_ttl_min: FilterLookup[int] | None = strawberry_django.filter_field()
    ddns_ttl_max: FilterLookup[int] | None = strawberry_django.filter_field()
    hostname_char_set: FilterLookup[str] | None = strawberry_django.filter_field()
    hostname_char_replacement: FilterLookup[str] | None = strawberry_django.filter_field()


@strawberry.type
class OfferLifetimeGraphQLFilterMixin:
    offer_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()


@strawberry.type
class LifetimeGraphQLFilterMixin(OfferLifetimeGraphQLFilterMixin):
    valid_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()
    min_valid_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()
    max_valid_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()
    preferred_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()
    min_preferred_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()
    max_preferred_lifetime: FilterLookup[int] | None = strawberry_django.filter_field()


@dataclass
class LeaseGraphQLFilterMixin:
    renew_timer: FilterLookup[int] | None = strawberry_django.filter_field()
    rebind_timer: FilterLookup[int] | None = strawberry_django.filter_field()
    match_client_id: FilterLookup[bool] | None = strawberry_django.filter_field()
    authoritative: FilterLookup[bool] | None = strawberry_django.filter_field()
    reservations_global: FilterLookup[bool] | None = strawberry_django.filter_field()
    reservations_out_of_pool: FilterLookup[bool] | None = strawberry_django.filter_field()
    reservations_in_subnet: FilterLookup[bool] | None = strawberry_django.filter_field()
    calculate_tee_times: FilterLookup[bool] | None = strawberry_django.filter_field()
    t1_percent: FilterLookup[float] | None = strawberry_django.filter_field()
    t2_percent: FilterLookup[float] | None = strawberry_django.filter_field()
    cache_threshold: FilterLookup[float] | None = strawberry_django.filter_field()
    cache_max_age: FilterLookup[int] | None = strawberry_django.filter_field()
    adaptive_lease_time_threshold: FilterLookup[float] | None = strawberry_django.filter_field()
    store_extended_info: FilterLookup[bool] | None = strawberry_django.filter_field()
    allocator: Annotated["NetBoxDHCPAllocatorTypeEnum", strawberry.lazy("netbox_dhcp.graphql.enums")] | None = strawberry_django.filter_field()
    pd_allocator: Annotated["NetBoxDHCPPDAllocatorTypeEnum", strawberry.lazy("netbox_dhcp.graphql.enums")] | None = strawberry_django.filter_field()
