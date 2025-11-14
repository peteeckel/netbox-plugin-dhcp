import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import MultiValueCharFilter
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import OptionDefinition
from netbox_dhcp.choices import OptionSpaceChoices, OptionTypeChoices


__all__ = ("OptionDefinitionFilterSet",)


class OptionDefinitionFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = OptionDefinition

        fields = (
            "id",
            "name",
            "code",
            "description",
            "encapsulate",
            "array",
            "standard",
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    code = django_filters.NumberFilter(
        label=_("Code"),
    )
    encapsulate = django_filters.CharFilter(
        label=_("Encapsulate"),
    )
    family = django_filters.ChoiceFilter(
        label=_("Address Family"),
        choices=IPAddressFamilyChoices,
    )
    space = django_filters.MultipleChoiceFilter(
        label=_("Space"),
        choices=OptionSpaceChoices,
    )
    type = django_filters.MultipleChoiceFilter(
        label=_("Type"),
        choices=OptionTypeChoices,
    )
    record_types = MultiValueCharFilter(
        method="filter_record_types",
        label=_("Record Types"),
    )

    def filter_record_types(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(record_types__overlap=value)

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = Q(Q(name__icontains=value) | Q(space__icontains=value))
        try:
            value = int(value)
            qs_filter |= Q(code=value)
        except ValueError:
            pass

        return queryset.filter(qs_filter)
