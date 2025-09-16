import django_filters
from django.utils.translation import gettext as _

from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPRange

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassMixin,
)

__all__ = ("PoolFilterSet",)


class PoolFilterSet(
    ClientClassMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = Pool

        fields = (
            "id",
            "name",
            "description",
            "comment",
        )

    ip_range_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPRange.objects.all(),
        field_name="ip_range",
        label=_("IP Range"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(comment__icontains=value)
        return queryset.filter(qs_filter)
