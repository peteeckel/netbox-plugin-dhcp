import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

from netbox_dhcp.models import SharedNetwork

from .mixins import (
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
    NetworkGraphQLFilterMixin,
    LeaseGraphQLFilterMixin,
    ParentDHCPServerGraphQLFilterMixin,
    ChildSubnetGraphQLFilterMixin,
)


@strawberry_django.filter_type(SharedNetwork, lookups=True)
class NetBoxDHCPSharedNetworkFilter(
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    DDNSUpdateGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
    NetworkGraphQLFilterMixin,
    LeaseGraphQLFilterMixin,
    ParentDHCPServerGraphQLFilterMixin,
    ChildSubnetGraphQLFilterMixin,
    NetBoxModelFilterMixin,
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
