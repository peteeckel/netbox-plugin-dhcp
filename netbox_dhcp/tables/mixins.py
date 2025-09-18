import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import TagColumn, NetBoxTable

__all__ = (
    "NetBoxDHCPTableMixin",
    "ClientClassDefinitionTableMixin",
    "ClientClassTableMixin",
)


class NetBoxDHCPTableMixin(NetBoxTable):
    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )
    tags = TagColumn(
        url_name="plugins:netbox_dhcp:subnet_list",
    )


class ClientClassDefinitionTableMixin(NetBoxTable):
    client_class_definitions = tables.ManyToManyColumn(
        verbose_name=_("Client Class Definitions"),
        linkify_item=True,
    )


class ClientClassTableMixin(ClientClassDefinitionTableMixin):
    client_class = tables.Column(
        verbose_name=_("Client Class"),
        linkify=True,
    )
    required_client_classes = tables.ManyToManyColumn(
        verbose_name=_("Required Client Classes"),
        linkify_item=True,
    )
    evaluate_additional_classes = tables.ManyToManyColumn(
        verbose_name=_("Evaluate Additional Classes"),
        linkify_item=True,
    )


class PrefixTableMixin(NetBoxTable):
    prefix = tables.Column(
        verbose_name=_("Prefix"),
        linkify=True,
    )
