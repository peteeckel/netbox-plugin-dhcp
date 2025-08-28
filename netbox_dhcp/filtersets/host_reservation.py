from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dhcp.models import HostReservation


__all__ = ("HostReservationFilterSet",)


class HostReservationFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = HostReservation

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
