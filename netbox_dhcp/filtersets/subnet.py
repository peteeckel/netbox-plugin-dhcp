import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Subnet

from .mixins import (
    ClientClassFilterMixin,
    DDNSUpdateFilterMixin,
    ChildSubnetFilterMixin,
    ChildPoolFilterMixin,
    ChildPDPoolFilterMixin,
    ChildHostReservationFilterMixin,
)

__all__ = ("SubnetFilterSet",)


class SubnetFilterSet(
    ClientClassFilterMixin,
    DDNSUpdateFilterMixin,
    ChildSubnetFilterMixin,
    ChildPoolFilterMixin,
    ChildPDPoolFilterMixin,
    ChildHostReservationFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = Subnet

        fields = (
            "id",
            "name",
            "description",
            "family",
            "subnet_id",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "renew_timer",
            "rebind_timer",
            "match_client_id",
            "authoritative",
            "reservations_global",
            "reservations_out_of_pool",
            "reservations_in_subnet",
            "calculate_tee_times",
            "t1_percent",
            "t2_percent",
            "cache_threshold",
            "cache_max_age",
            "adaptive_lease_time_threshold",
            "store_extended_info",
            "allocator",
            "pd_allocator",
            "relay",
            "interface_id",
            "rapid_commit",
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
    prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="prefix",
        label=_("Prefix"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(boot_file_name__icontains=value)
            | Q(comment__icontains=value)
        )
        return queryset.filter(qs_filter)
