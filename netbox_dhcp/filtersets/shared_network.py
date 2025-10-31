import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import SharedNetwork

from .mixins import (
    PrefixFilterMixin,
    ClientClassFilterMixin,
    EvaluateClientClassFilterMixin,
    BOOTPFilterMixin,
    DDNSUpdateFilterMixin,
    LifetimeFilterMixin,
    LeaseFilterMixin,
    NetworkFilterMixin,
    ChildSubnetFilterMixin,
    ParentDHCPServerFilterMixin,
)

__all__ = ("SharedNetworkFilterSet",)


class SharedNetworkFilterSet(
    PrefixFilterMixin,
    ClientClassFilterMixin,
    EvaluateClientClassFilterMixin,
    BOOTPFilterMixin,
    LifetimeFilterMixin,
    LeaseFilterMixin,
    DDNSUpdateFilterMixin,
    ChildSubnetFilterMixin,
    ParentDHCPServerFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = SharedNetwork

        fields = (
            "id",
            "name",
            "description",
            *PrefixFilterMixin.FILTER_FIELDS,
            *BOOTPFilterMixin.FILTER_FIELDS,
            *LifetimeFilterMixin.FILTER_FIELDS,
            *LeaseFilterMixin.FILTER_FIELDS,
            *DDNSUpdateFilterMixin.FILTER_FIELDS,
            *NetworkFilterMixin.FILTER_FIELDS,
            *ChildSubnetFilterMixin.FILTER_FIELDS,
            *ParentDHCPServerFilterMixin.FILTER_FIELDS,
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    family = django_filters.ChoiceFilter(
        choices=IPAddressFamilyChoices,
        field_name="prefix__prefix",
        lookup_expr="family",
        label=_("Address Family"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(boot_file_name__icontains=value)
        )
        return queryset.filter(qs_filter)
