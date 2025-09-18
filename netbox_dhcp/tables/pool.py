import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import Pool

from .mixins import NetBoxDHCPTableMixin

__all__ = ("PoolTable",)


class PoolTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Pool

        fields = (
            "description",
            "ip_range",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "user_context",
            "comment",
            "evaluate_additional_classes",
            "tags",
        )

        default_columns = (
            "name",
            "ip_range",
            "tags",
        )

    ip_range = tables.Column(
        verbose_name=_("IP Range"),
        linkify=True,
    )
    client_class_definitions = tables.Column(
        verbose_name=_("Client Class Definitions"),
        linkify=True,
    )
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
