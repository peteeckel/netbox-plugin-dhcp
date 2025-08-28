import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, TagColumn

from netbox_dhcp.models import DHCPServer


__all__ = ("DHCPServerTable",)


class DHCPServerTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = DHCPServer

        fields = ("description",)

        default_columns = ("name",)

    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )

    tags = TagColumn(
        url_name="plugins:netbox_dhcp:dhcpserver_list",
    )
