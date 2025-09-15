import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, TagColumn

from netbox_dhcp.models import PDPool


__all__ = ("PDPoolTable",)


class PDPoolTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = PDPool

        fields = (
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "client_class",
            "require_client_classes",
            "user_context",
            "comment",
            "tags",
        )

        default_columns = (
            "name",
            "prefix",
            "delegated_length",
            "tags",
        )

    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )
    prefix = tables.Column(
        verbose_name=_("IPv6 Prefix"),
        linkify=True,
    )
    excluded_prefix = tables.Column(
        verbose_name=_("Excluded IPv6 Prefix"),
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
