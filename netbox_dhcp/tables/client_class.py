import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import ClientClass

from .mixins import NetBoxDHCPTableMixin

__all__ = ("ClientClassTable",)


class ClientClassTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = ClientClass

        fields = (
            "name",
            "description",
            "comment",
            "test",
            "tenplate_test",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "tags",
        )

        default_columns = (
            "name",
            "test",
            "template_test",
            "only_in_additional_list",
        )

    only_in_additional_list = tables.BooleanColumn(
        verbose_name=_("Only in additional list"),
    )
