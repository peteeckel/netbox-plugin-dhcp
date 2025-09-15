import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, TagColumn

from netbox_dhcp.models import Pool


__all__ = ("PoolTable",)


class PoolTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Pool

        fields = (
            "description",
            "ip_range",
            "client_class",
            "require_client_classes",
            "user_context",
            "comment",
            "tags",
        )

        default_columns = (
            "name",
            "ip_range",
            "tags",
        )

    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )
    ip_range = tables.Column(
        verbose_name=_("IP Range"),
        linkify=True,
    )
    client_class = tables.Column(
        verbose_name=_("Client Class"),
        linkify=True,
    )
    require_client_classes = tables.ManyToManyColumn(
        verbose_name=_("Require Client Classes"),
        linkify_item=True,
    )

    tags = TagColumn(
        url_name="plugins:netbox_dhcp:pdpool_list",
    )
