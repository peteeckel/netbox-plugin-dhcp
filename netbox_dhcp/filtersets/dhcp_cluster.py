from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import DHCPCluster


__all__ = ("DHCPClusterFilterSet",)


class DHCPClusterFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DHCPCluster

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
