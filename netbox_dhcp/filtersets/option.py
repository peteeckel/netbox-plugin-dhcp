import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Option, OptionDefinition
from netbox_dhcp.choices import OptionSpaceChoices
from .mixins import ClientClassAssignmentFilterMixin


__all__ = ("OptionFilterSet",)


class OptionFilterSet(ClientClassAssignmentFilterMixin, NetBoxModelFilterSet):
    class Meta:
        model = Option

        fields = (
            "id",
            "data",
            "csv_format",
            "send_option",
        )

    description = django_filters.CharFilter(
        label=_("Description"),
    )
    family = django_filters.ChoiceFilter(
        label=_("Address Family"),
        field_name="definition__family",
        choices=IPAddressFamilyChoices,
    )
    space = django_filters.MultipleChoiceFilter(
        label=_("Space"),
        field_name="definition__space",
        choices=OptionSpaceChoices,
    )
    name = django_filters.CharFilter(
        label=_("Name"),
        field_name="definition__name",
    )
    code = django_filters.NumberFilter(
        label=_("Code"),
        field_name="definition__code",
    )
    data = django_filters.CharFilter(
        label=_("Data"),
    )
    data_ic = django_filters.CharFilter(
        label=_("Data"),
        lookup_expr="icontains",
        field_name="data",
    )
    definition_id = django_filters.ModelMultipleChoiceFilter(
        label=_("Option Definition ID"),
        queryset=OptionDefinition.objects.all(),
    )
    definition = django_filters.CharFilter(
        label=_("Option Definition"),
        field_name="definition__name",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(definition__name__icontains=value) | Q(data__icontains=value)
        return queryset.filter(qs_filter)
