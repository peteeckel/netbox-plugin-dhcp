import strawberry_django
from strawberry_django import FilterLookup

from netbox.graphql.filters import BaseModelFilter

from netbox_dhcp.models import ClientClass

from .mixins import (
    DHCPServerGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
)


@strawberry_django.filter_type(ClientClass, lookups=True)
class NetBoxDHCPClientClassFilter(
    DHCPServerGraphQLFilterMixin,
    BOOTPGraphQLFilterMixin,
    LifetimeGraphQLFilterMixin,
    BaseModelFilter,
):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()
    weight: FilterLookup[int] | None = strawberry_django.filter_field()
    test: FilterLookup[str] | None = strawberry_django.filter_field()
    template_test: FilterLookup[str] | None = strawberry_django.filter_field()
    only_in_additional_list: FilterLookup[bool] | None = (
        strawberry_django.filter_field()
    )
