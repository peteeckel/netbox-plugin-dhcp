# import django_tables2 as tables
# from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from netbox_dhcp.models import Option

from .mixins import NetBoxDHCPTableMixin

__all__ = ("OptionTable",)


class OptionTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Option

        fields = (
            "name",
            "description",
        )

        default_columns = ("name",)
