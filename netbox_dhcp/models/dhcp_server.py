from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox_dhcp.choices import DHCPServerStatusChoices

from .mixins import (
    NetBoxDHCPModelMixin,
)

__all__ = (
    "DHCPServer",
    "DHCPServerIndex",
)


class DHCPServer(NetBoxDHCPModelMixin, NetBoxModel):
    class Meta:
        verbose_name = _("DHCP Server")
        verbose_name_plural = _("DHCP Servers")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "status",
        "dhcp_cluster",
    )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=50,
        choices=DHCPServerStatusChoices,
        default=DHCPServerStatusChoices.STATUS_ACTIVE,
        blank=True,
    )

    dhcp_cluster = models.ForeignKey(
        to="DHCPCluster",
        verbose_name=_("DHCP Cluster"),
        on_delete=models.SET_NULL,
        related_name="dhcp_servers",
        blank=True,
        null=True,
    )
    device = models.ForeignKey(
        to=Device,
        verbose_name=_("Device"),
        on_delete=models.SET_NULL,
        related_name="netbox_dhcp_dhcp_servers",
        blank=True,
        null=True,
    )
    virtual_machine = models.ForeignKey(
        to=VirtualMachine,
        verbose_name=_("Virtual Machine"),
        on_delete=models.SET_NULL,
        related_name="netbox_dhcp_dhcp_servers",
        blank=True,
        null=True,
    )

    def get_status_color(self):
        return DHCPServerStatusChoices.colors.get(self.status)


@register_search
class DHCPServerIndex(SearchIndex):
    model = DHCPServer

    fields = (
        ("name", 100),
        ("description", 200),
    )
