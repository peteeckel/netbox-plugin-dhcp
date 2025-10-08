import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

from netbox_dhcp.models import Subnet

from .mixins import (
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
    NetworkGraphQLFilterMixin,
    LeaseGraphQLFilterMixin,
    ParentSharedNetworkGraphQLFilterMixin,
    ParentSubnetGraphQLFilterMixin,
    ChildSubnetGraphQLFilterMixin,
    ChildPoolGraphQLFilterMixin,
    ChildPDPoolGraphQLFilterMixin,
    ChildHostReservationGraphQLFilterMixin,
)


@strawberry_django.filter_type(Subnet, lookups=True)
class NetBoxDHCPSubnetFilter(
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
    NetworkGraphQLFilterMixin,
    LeaseGraphQLFilterMixin,
    ParentSharedNetworkGraphQLFilterMixin,
    ParentSubnetGraphQLFilterMixin,
    ChildSubnetGraphQLFilterMixin,
    ChildPoolGraphQLFilterMixin,
    ChildPDPoolGraphQLFilterMixin,
    ChildHostReservationGraphQLFilterMixin,
    NetBoxModelFilterMixin,
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
    subnet_id: FilterLookup[int] | None = strawberry_django.filter_field()
