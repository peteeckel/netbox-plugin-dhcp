import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, TagColumn

from netbox_dhcp.models import ClientClass


__all__ = ("ClientClassTable",)


class ClientClassTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = ClientClass

        fields = (
            "description",
            "comment",
            "test",
            "tenplate_test",
            "only_if_required",
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
        )

        default_columns = (
            "name",
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
        )

    name = tables.Column(
        verbose_name=_("Name"),
        linkify=True,
    )
    only_if_required = tables.BooleanColumn(
        verbose_name=_("Only if required"),
    )
    only_in_additional_list = tables.BooleanColumn(
        verbose_name=_("Only in additional list"),
    )

    tags = TagColumn(
        url_name="plugins:netbox_dhcp:clientclass_list",
    )
