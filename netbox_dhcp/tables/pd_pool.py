import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import PDPool

from .mixins import (
    ClientClassTableMixin,
    EvaluateClientClassTableMixin,
    NetBoxDHCPTableMixin,
)

__all__ = (
    "PDPoolTable",
    "RelatedPDPoolTable",
)


class PDPoolTable(
    ClientClassTableMixin,
    EvaluateClientClassTableMixin,
    NetBoxDHCPTableMixin,
    NetBoxTable,
):
    class Meta(NetBoxTable.Meta):
        model = PDPool

        fields = (
            "name",
            "description",
            "prefix",
            "delegated_length",
            "excluded_prefix",
            "client_classes",
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


class RelatedPDPoolTable(PDPoolTable):
    class Meta(PDPoolTable.Meta):
        fields = (
            "name",
            "description",
            "excluded_prefix",
        )

        default_columns = (
            "name",
            "description",
            "excluded_prefix",
        )

    actions = None
