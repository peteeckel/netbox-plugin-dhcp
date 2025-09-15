import django_filters
from django.utils.translation import gettext as _

from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPRange

from netbox_dhcp.models import Pool, ClientClass


__all__ = ("PoolFilterSet",)


class PoolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Pool

        fields = (
            "id",
            "name",
            "description",
            "comment",
        )

    ip_range_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPRange.objects.all(),
        field_name="ip_range",
        label=_("IP Range"),
    )
    client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class__name",
        to_field_name="name",
        label=_("Client Class"),
    )
    client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="client_class",
        label=_("Client Class ID"),
    )
    require_client_class = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="require_client_classes__name",
        to_field_name="name",
        label=_("Required Client Class"),
    )
    require_client_class_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ClientClass.objects.all(),
        field_name="require_client_classes",
        label=_("Required Client Class ID"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(comment__icontains=value)
        return queryset.filter(qs_filter)
