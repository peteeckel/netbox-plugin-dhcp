from typing import Annotated, TYPE_CHECKING

import strawberry
from strawberry.scalars import ID
import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    ParentSubnetGraphQLFilterMixin,
)

if TYPE_CHECKING:
    from ipam.graphql.filters import IPRangeFilter


@strawberry_django.filter_type(Pool, lookups=True)
class NetBoxDHCPPoolFilter(
    ClientClassGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    ParentSubnetGraphQLFilterMixin,
    NetBoxModelFilterMixin,
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
    pool_id: FilterLookup[int] | None = strawberry_django.filter_field()
    ip_range: (
        Annotated["IPRangeFilter", strawberry.lazy("ipam.graphql.filters")] | None
    ) = strawberry_django.filter_field()
    ip_range_id: ID | None = strawberry_django.filter_field()
