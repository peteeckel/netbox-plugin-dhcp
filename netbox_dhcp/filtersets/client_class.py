import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from utilities.filtersets import register_filterset

from ..models import ClientClass
from .mixins import (
    DHCPServerFilterMixin,
    BOOTPFilterMixin,
    LifetimeFilterMixin,
)


__all__ = ("ClientClassFilterSet",)


@register_filterset
class ClientClassFilterSet(
    DHCPServerFilterMixin,
    BOOTPFilterMixin,
    LifetimeFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = ClientClass

        fields = (
            "id",
            "only_in_additional_list",
            *DHCPServerFilterMixin.FILTER_FIELDS,
            *BOOTPFilterMixin.FILTER_FIELDS,
            *LifetimeFilterMixin.FILTER_FIELDS,
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    weight = django_filters.NumberFilter(
        label=_("Weight"),
    )
    test = django_filters.CharFilter(
        label=_("Test"),
    )
    template_test = django_filters.CharFilter(
        label=_("Template Test"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(test__icontains=value)
            | Q(template_test__icontains=value)
            | Q(boot_file_name__icontains=value)
        )
        return queryset.filter(qs_filter)
