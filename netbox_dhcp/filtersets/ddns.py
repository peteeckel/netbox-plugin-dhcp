from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import DDNS


__all__ = ("DDNSFilterSet",)


class DDNSFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DDNS

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
