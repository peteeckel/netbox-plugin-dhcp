from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from netbox_dhcp.choices import DHCPClusterStatusChoices


__all__ = (
    "DHCPCluster",
    "DHCPClusterIndex",
)


class DHCPCluster(NetBoxModel):
    class Meta:
        verbose_name = _("DHCP Cluster")
        verbose_name_plural = _("DHCP Clusters")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "status",
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
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=50,
        choices=DHCPClusterStatusChoices,
        default=DHCPClusterStatusChoices.STATUS_ACTIVE,
        blank=True,
    )

    def get_status_color(self):
        return DHCPClusterStatusChoices.colors.get(self.status)


@register_search
class DHCPClusterIndex(SearchIndex):
    model = DHCPCluster

    fields = (
        ("name", 100),
        ("description", 200),
    )
