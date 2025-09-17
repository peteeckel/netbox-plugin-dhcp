# from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import NetBoxDHCPModelMixin

__all__ = (
    "Subnet",
    "SubnetIndex",
)


class Subnet(NetBoxDHCPModelMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Subnet")
        verbose_name_plural = _("Subnets")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
    )


@register_search
class SubnetIndex(SearchIndex):
    model = Subnet

    fields = (
        ("name", 100),
        ("description", 200),
    )
