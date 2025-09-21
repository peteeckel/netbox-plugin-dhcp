from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import Prefix

from .mixins import (
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    LifetimeModelMixin,
    DDNSUpdateModelMixin,
    LeaseModelMixin,
    NetworkModelMixin,
    ChildSubnetModelMixin,
)

__all__ = (
    "SharedNetwork",
    "SharedNetworkIndex",
)


class SharedNetwork(
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    LifetimeModelMixin,
    DDNSUpdateModelMixin,
    LeaseModelMixin,
    NetworkModelMixin,
    NetBoxModel,
    ChildSubnetModelMixin,
):
    class Meta:
        verbose_name = _("Shared Network")
        verbose_name_plural = _("Shared Networks")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "client_class_definitions",
        "client_class",
        "required_client_classes",
        "evaluate_additional_classes",
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

    prefix = models.ForeignKey(
        verbose_name=_("Prefix"),
        to=Prefix,
        related_name="netbox_dhcp_shared_networks",
        on_delete=models.PROTECT,
        null=False,
    )


@register_search
class SharedNetworkIndex(SearchIndex):
    model = SharedNetwork

    fields = (
        ("name", 100),
        ("description", 200),
        ("next_server", 300),
        ("server_hostname", 300),
        ("boot_file_name", 300),
        ("comment", 200),
    )
