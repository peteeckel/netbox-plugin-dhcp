import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPRange
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassFilterMixin,
    EvaluateClientClassFilterMixin,
    DDNSUpdateFilterMixin,
    ParentSubnetFilterMixin,
)

__all__ = ("PoolFilterSet",)


class PoolFilterSet(
    ClientClassFilterMixin,
    EvaluateClientClassFilterMixin,
    DDNSUpdateFilterMixin,
    ParentSubnetFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = Pool

        fields = (
            "id",
            "name",
            "description",
            *DDNSUpdateFilterMixin.FILTER_FIELDS,
            "comment",
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    pool_id = django_filters.NumberFilter(
        label=_("Pool ID"),
    )
    family = django_filters.ChoiceFilter(
        label=_("Address Family"),
        choices=IPAddressFamilyChoices,
        field_name="ip_range__start_address",
        lookup_expr="family",
    )
    ip_range_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPRange.objects.all(),
        field_name="ip_range",
        label=_("IP Range ID"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(comment__icontains=value)
        return queryset.filter(qs_filter)
