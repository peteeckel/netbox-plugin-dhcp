import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import PDPool

from .mixins import NetBoxDHCPTableMixin

__all__ = ("PDPoolTable",)


class PDPoolTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = PDPool

        fields = (
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
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
            "prefix",
            "delegated_length",
            "tags",
        )

    prefix = tables.Column(
        verbose_name=_("IPv6 Prefix"),
        linkify=True,
    )
    excluded_prefix = tables.Column(
        verbose_name=_("Excluded IPv6 Prefix"),
        linkify=True,
    )
