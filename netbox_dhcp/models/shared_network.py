# from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import NetBoxDHCPMixin

__all__ = (
    "SharedNetwork",
    "SharedNetworkIndex",
)


class SharedNetwork(NetBoxDHCPMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Shared Network")
        verbose_name_plural = _("Shared Networks")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
    )


@register_search
class SharedNetworkIndex(SearchIndex):
    model = SharedNetwork

    fields = (
        ("name", 100),
        ("description", 200),
    )
