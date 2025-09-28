import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, ChoiceFieldColumn

from netbox_dhcp.models import Option

from .mixins import NetBoxDHCPTableMixin

__all__ = (
    "OptionTable",
    "ChildOptionTable",
)


class OptionTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Option

        fields = (
            "name",
            "family",
            "space",
            "assigned_object",
            "assigned_object_type",
            "code",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
        )

        default_columns = (
            "name",
            "family",
            "space",
            "code",
            "data",
            "assigned_object",
            "assigned_object_type",
        )

    family = tables.Column(
        accessor="definition__family",
        verbose_name=_("Address Family"),
    )
    space = tables.Column(
        accessor="definition__space",
        verbose_name=_("Space"),
    )
    name = tables.Column(
        accessor="definition__name",
        verbose_name=_("Name"),
        linkify=True,
    )
    family = tables.Column(
        accessor="definition__family",
        verbose_name=_("Address Family"),
    )
    code = tables.Column(
        accessor="definition__code",
        verbose_name=_("Code"),
    )
    assigned_object = tables.Column(
        verbose_name=_("Assigned Object"),
        linkify=True,
    )
    assigned_object_type = tables.Column(
        verbose_name=_("Assigned Object Type"),
        accessor="assigned_object_type__name",
    )


class ChildOptionTable(OptionTable):
    class Meta(OptionTable.Meta):
        default_columns = (
            "space",
            "name",
            "code",
            "data",
        )
