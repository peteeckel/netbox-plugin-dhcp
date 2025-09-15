from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


__all__ = (
    "Subnet",
    "SubnetIndex",
)


class Subnet(NetBoxModel):
    class Meta:
        verbose_name = _("Subnet")
        verbose_name_plural = _("Subnets")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
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


@register_search
class SubnetIndex(SearchIndex):
    model = Subnet

    fields = (
        ("name", 100),
        ("description", 200),
    )
