import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, ChoiceFieldColumn

from netbox_dhcp.models import DHCPServer

from .mixins import NetBoxDHCPTableMixin

__all__ = ("DHCPServerTable",)


class DHCPServerTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = DHCPServer

        fields = (
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
            "server_id",
            "echo_client_id",
            "tags",
        )

        default_columns = (
            "name",
            "status",
            "dhcp_cluster",
        )

    status = ChoiceFieldColumn(
        verbose_name=_("Status"),
    )
    dhcp_cluster = tables.Column(
        verbose_name=_("DHCP Cluster"),
        linkify=True,
    )

    device = tables.Column(
        verbose_name=_("Device"),
        linkify=True,
    )
    virtual_machine = tables.Column(
        verbose_name=_("Virtual Machine"),
        linkify=True,
    )
    server_id = ChoiceFieldColumn(
        verbose_name=_("Server ID"),
    )
