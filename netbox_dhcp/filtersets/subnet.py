from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import Subnet

from .mixins import (
    ClientClassFilterMixin,
)

__all__ = ("SubnetFilterSet",)


class SubnetFilterSet(ClientClassFilterMixin, NetBoxModelFilterSet):
    class Meta:
        model = Subnet

        fields = (
            "id",
            "name",
            "description",
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
            "comment",
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(boot_file_name__icontains=value)
            | Q(comment__icontains=value)
        )
        return queryset.filter(qs_filter)
