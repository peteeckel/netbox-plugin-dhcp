from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import Subnet


__all__ = ("SubnetFilterSet",)


class SubnetFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Subnet

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
