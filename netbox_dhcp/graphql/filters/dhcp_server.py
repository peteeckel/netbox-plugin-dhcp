from typing import Annotated, TYPE_CHECKING

import strawberry
import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

if TYPE_CHECKING:
    from netbox.graphql.filter_lookups import IntegerArrayLookup
    from dcim.graphql.filters import DeviceFilter
    from virtualization.graphql.filters import VirtualMachineFilter
    from .enums import (
        NetBoxDHCPServerStatusEnum,
        NetBoxDHCPServerIDTypeEnum,
    )
    from .dhcp_cluster import NetBoxDHCPClusterFilter

from netbox_dhcp.models import DHCPServer

from .mixins import (
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
)

__all__ = ("NetBoxDHCPServerFilter",)


@strawberry_django.filter_type(DHCPServer, lookups=True)
class NetBoxDHCPServerFilter(
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    NetBoxModelFilterMixin
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
    server_id: Annotated["NetBoxDHCPServerIDTypeEnum", strawberry.lazy("netbox_dhcp.graphql.enums")] | None = strawberry_django.filter_field()
    status: Annotated["NetBoxDHCPServerStatusEnum", strawberry.lazy("netbox_dhcp.graphql.enums")] | None = strawberry_django.filter_field()
#   host_reservation_identifiers: Array Lookup with Enum elements
    echo_client_id:  FilterLookup[bool] | None = strawberry_django.filter_field()
    relay_supplied_options: Annotated["IntegerArrayLookup", strawberry.lazy('netbox.graphql.filter_lookups')] | None = strawberry_django.filter_field()
    dhcp_cluster: Annotated["NetBoxDHCPClusterFilter", strawberry.lazy("netbox_dhcp.graphql.filters")] | None = strawberry_django.filter_field()
    device: Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")] | None
    virtual_machine: Annotated["VirtualMachineFilter", strawberry.lazy("virtualization.graphql.filters")] | None
    decline_probation_period: FilterLookup[float] | None = strawberry_django.filter_field()
