import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filters import BaseModelFilter

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
    ChildSubnetGraphQLFilterMixin,
    BaseModelFilter,
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
    weight: FilterLookup[int] | None = strawberry_django.filter_field()
