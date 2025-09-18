import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import TagColumn

__all__ = (
    "NetBoxDHCPTableMixin",
    "ClientClassDefinitionTableMixin",
    "ClientClassTableMixin",
)


class NetBoxDHCPTableMixin:
    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )
    tags = TagColumn(
        url_name="plugins:netbox_dhcp:subnet_list",
    )


class ClientClassDefinitionTableMixin:
    client_class_definitions = tables.Column(
        verbose_name=_("Client Class Definitions"),
        linkify=True,
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
