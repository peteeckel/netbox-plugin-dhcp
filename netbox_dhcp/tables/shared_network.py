# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import SharedNetwork

from .mixins import NetBoxDHCPTableMixin

__all__ = ("SharedNetworkTable",)


class SharedNetworkTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "user_context",
            "comment",
        )

        default_columns = ("name",)
