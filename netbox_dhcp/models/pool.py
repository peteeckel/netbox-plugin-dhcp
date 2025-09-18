from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import IPRange

from .mixins import (
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    DDNSUpdateModelMixin,
)

__all__ = (
    "Pool",
    "PoolIndex",
)


class Pool(
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    DDNSUpdateModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("Address Pool")
        verbose_name_plural = _("Address Pools")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "client_class_definitions",
        "client_class",
        "required_client_classes",
        "evaluate_additional_classes",
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

    pool_id = models.PositiveIntegerField(
        verbose_name=_("Pool ID"),
        blank=True,
        null=True,
    )
    ip_range = models.ForeignKey(
        verbose_name=_("IP Range"),
        to=IPRange,
        related_name="netbox_dhcp_pool",
        on_delete=models.PROTECT,
    )


@register_search
class PoolIndex(SearchIndex):
    model = Pool

    fields = (
        ("name", 100),
        ("description", 200),
        ("comment", 200),
    )
