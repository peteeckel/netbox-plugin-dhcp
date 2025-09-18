import django_filters
from django.utils.translation import gettext as _

from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPRange

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassFilterMixin,
    DDNSUpdateFilterMixin,
)

__all__ = ("PoolFilterSet",)


class PoolFilterSet(
    ClientClassFilterMixin,
    DDNSUpdateFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = Pool

        fields = (
            "id",
            "name",
            "description",
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
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
