# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import DDNS

from .mixins import NetBoxDHCPTableMixin

__all__ = ("DDNSTable",)


class DDNSTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = DDNS

        fields = ("description",)

        default_columns = ("name",)
