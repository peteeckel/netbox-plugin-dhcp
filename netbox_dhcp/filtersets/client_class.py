import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet

from ..models import ClientClass
from .mixins import (
    BOOTPFilterMixin,
    LifetimeFilterMixin,
)


__all__ = ("ClientClassFilterSet",)


class ClientClassFilterSet(
    BOOTPFilterMixin,
    LifetimeFilterMixin,
    NetBoxModelFilterSet,
):
    class Meta:
        model = ClientClass

        fields = (
            "id",
            "name",
            "description",
            "test",
            "template_test",
            "only_in_additional_list",
            *BOOTPFilterMixin.FILTER_FIELDS,
            *LifetimeFilterMixin.FILTER_FIELDS,
            "comment",
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
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
            | Q(comment__icontains=value)
        )
        return queryset.filter(qs_filter)
