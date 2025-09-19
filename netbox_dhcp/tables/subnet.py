# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import Subnet

from .mixins import (
    NetBoxDHCPTableMixin,
    PrefixTableMixin,
    ClientClassTableMixin,
    DDNSUpdateTableMixin,
    LeaseTableMixin,
)

__all__ = ("SubnetTable",)


class SubnetTable(
    NetBoxDHCPTableMixin,
    PrefixTableMixin,
    ClientClassTableMixin,
    DDNSUpdateTableMixin,
    LeaseTableMixin,
    NetBoxTable,
):
    class Meta(NetBoxTable.Meta):
        model = Subnet

        fields = (
            "name",
            "prefix",
            "description",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "renew_timer",
            "rebind_timer",
            "calculate_tee_times",
            "t1_percent",
            "t2_percent",
            "adaptive_lease_time_threshold",
            "match_client_id",
            "reservations_global",
            "reservations_out_of_pool",
            "reservations_in_subnet",
            "cache_threshold",
            "cache_max_age",
            "authoritative",
            "store_extended_info",
            "allocator",
            "pd_allocator",
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
            "user_context",
            "comment",
        )

        default_columns = (
            "name",
            "prefix",
        )
