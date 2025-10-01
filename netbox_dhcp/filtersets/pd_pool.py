import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import PDPool

from .mixins import (
    ClientClassFilterMixin,
)

__all__ = ("PDPoolFilterSet",)


class PDPoolFilterSet(
    ClientClassFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = PDPool

        fields = (
            "id",
            "name",
            "description",
            "delegated_length",
            "comment",
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    family = django_filters.ChoiceFilter(
        choices=IPAddressFamilyChoices,
        field_name="prefix__prefix__family",
        label=_("Address Family"),
    )
    prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="prefix",
        label=_("IPv6 Prefix"),
    )
    excluded_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="excluded_prefix",
        label=_("Excluded IPv6 Prefix"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
