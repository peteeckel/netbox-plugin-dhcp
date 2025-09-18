import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import HostReservation

from .mixins import NetBoxDHCPTableMixin

__all__ = ("HostReservationTable",)


class HostReservationTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = HostReservation

        fields = (
            "description",
            "duid",
            "circuit_id",
            "client_id",
            "flex_id",
            "client_class_definitions",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "hostname",
            "user_context",
            "comment",
        )

        default_columns = (
            "name",
            "hostname",
            "ipv4_address",
            "ipv6_addresses",
            "comment",
        )

    hw_address = tables.Column(
        verbose_name=_("Hardware Address"),
        linkify=True,
    )

    ipv4_address = tables.Column(
        verbose_name=_("IPv4 Address"),
        linkify=True,
    )
    ipv6_addresses = tables.ManyToManyColumn(
        verbose_name=_("IPv6 Addresses"),
        linkify_item=True,
    )
    ipv6_prefixes = tables.ManyToManyColumn(
        verbose_name=_("IPv6 Prefixes"),
        linkify_item=True,
    )
    exlcuded_ipv6_prefixes = tables.ManyToManyColumn(
        verbose_name=_("Excluded IPv6 Prefixes"),
        linkify_item=True,
    )
