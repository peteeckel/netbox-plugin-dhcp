from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from ..models import ClientClass


__all__ = ("ClientClassFilterSet",)


class ClientClassFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = ClientClass

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
