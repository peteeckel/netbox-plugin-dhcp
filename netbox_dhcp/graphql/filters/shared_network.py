import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

from netbox_dhcp.models import SharedNetwork

from .mixins import (
    DHCPServerGraphQLFilterMixin,
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    EvaluateClientClassGraphQLFilterMixin,
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
    DHCPServerGraphQLFilterMixin,
    PrefixGraphQLFilterMixin,
    ClientClassGraphQLFilterMixin,
    EvaluateClientClassGraphQLFilterMixin,
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
    weight: FilterLookup[int] | None = strawberry_django.filter_field()
