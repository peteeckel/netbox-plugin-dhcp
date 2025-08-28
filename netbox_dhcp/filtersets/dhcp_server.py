from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import DHCPServer


__all__ = ("DHCPServerFilterSet",)


class DHCPServerFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DHCPServer

        fields = (
            "id",
            "name",
            "description",
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
