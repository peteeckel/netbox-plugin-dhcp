from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import IPRange

from netbox_dhcp.mixins import CommonModelFields, PoolModelFields


__all__ = (
    "Pool",
    "PoolIndex",
)


class Pool(CommonModelFields, PoolModelFields, NetBoxModel):
    class Meta:
        verbose_name = _("Address Pool")
        verbose_name_plural = _("Address Pools")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "client_class",
        "require_client_classes",
        "comment",
    )

    def __str__(self):
        return str(self.name)

    name = models.CharField(
        verbose_name=_("Name"),
        unique=True,
        max_length=255,
        db_collation="natural_sort",
    )
    description = models.CharField(
        verbose_name=_("Description"),
        blank=True,
        max_length=200,
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
