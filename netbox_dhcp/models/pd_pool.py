from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import Prefix

from netbox_dhcp.mixins import PoolModelFields, CommonModelFields

__all__ = (
    "PDPool",
    "PDPoolIndex",
)


class PDPool(PoolModelFields, CommonModelFields, NetBoxModel):
    class Meta:
        verbose_name = _("Prefix Delegation Pool")
        verbose_name_plural = _("Prefix Delegation Pools")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "delegated_length",
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
    prefix = models.ForeignKey(
        verbose_name=_("IPv6 Prefix"),
        to=Prefix,
        related_name="netbox_dhcp_pd_pool",
        on_delete=models.PROTECT,
    )
    delegated_length = models.IntegerField(
        verbose_name=_("Delegated Length"),
        validators=[MinValueValidator(0), MaxValueValidator(128)],
    )
    excluded_prefix = models.ForeignKey(
        verbose_name=_("Excluded IPv6 Prefix"),
        to=Prefix,
        related_name="netbox_dhcp_pd_excluded_pool",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


@register_search
class PDPoolIndex(SearchIndex):
    model = PDPool

    fields = (
        ("name", 100),
        ("description", 200),
        ("comment", 200),
    )
