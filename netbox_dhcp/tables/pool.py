import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassTableMixin,
    EvaluateClientClassTableMixin,
    NetBoxDHCPTableMixin,
)

__all__ = (
    "PoolTable",
    "RelatedPoolTable",
)


class PoolTable(
    ClientClassTableMixin,
    EvaluateClientClassTableMixin,
    NetBoxDHCPTableMixin,
    NetBoxTable,
):
    class Meta(NetBoxTable.Meta):
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            "client_classes",
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


class RelatedPoolTable(PoolTable):
    class Meta(PoolTable.Meta):
        fields = (
            "name",
            "description",
        )

        default_columns = (
            "name",
            "description",
        )

    actions = None
