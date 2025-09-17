from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import IPRange

from .mixins import (
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    ContextCommentModelMixin,
)

__all__ = (
    "Pool",
    "PoolIndex",
)


class Pool(
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    ContextCommentModelMixin,
    NetBoxModel,
):
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
