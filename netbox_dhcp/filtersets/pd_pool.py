import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import Prefix

from netbox_dhcp.models import PDPool

from .mixins import (
    PrefixFilterMixin,
    ClientClassFilterMixin,
    ParentSubnetFilterMixin,
)

__all__ = ("PDPoolFilterSet",)


class PDPoolFilterSet(
    PrefixFilterMixin,
    ClientClassFilterMixin,
    ParentSubnetFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = PDPool

        fields = (
            "id",
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
    delegated_length = django_filters.NumberFilter(
        label=_("Delegated Length"),
    )
    excluded_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="excluded_prefix",
        label=_("Excluded Prefix"),
    )
    excluded_prefix = django_filters.CharFilter(
        field_name="excluded_prefix__prefix",
        label=_("Excluded Prefix"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
