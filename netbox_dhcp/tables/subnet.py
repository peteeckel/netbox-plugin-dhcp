# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import Subnet

from .mixins import NetBoxDHCPTableMixin

__all__ = ("SubnetTable",)


class SubnetTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Subnet

        fields = ("description",)

        default_columns = ("name",)
