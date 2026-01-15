import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from utilities.filtersets import register_filterset

from netbox_dhcp.models import DHCPCluster
from netbox_dhcp.choices import DHCPClusterStatusChoices


__all__ = ("DHCPClusterFilterSet",)


@register_filterset
class DHCPClusterFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DHCPCluster

        fields = (
            "id",
            "name",
            "description",
            "status",
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=DHCPClusterStatusChoices,
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
