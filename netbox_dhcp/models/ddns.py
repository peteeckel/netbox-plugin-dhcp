from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import (
    NetBoxDHCPMixin,
)

__all__ = (
    "DDNS",
    "DDNSIndex",
)


class DDNS(NetBoxDHCPMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Dynamic DNS Server")
        verbose_name_plural = _("Dynamic DNS Servers")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
    )


@register_search
class DDNSIndex(SearchIndex):
    model = DDNS

    fields = (
        ("name", 100),
        ("description", 200),
    )
