# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import SharedNetwork

from .mixins import NetBoxDHCPTableMixin

__all__ = ("SharedNetworkTable",)


class SharedNetworkTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = SharedNetwork

        fields = ("description",)

        default_columns = ("name",)
