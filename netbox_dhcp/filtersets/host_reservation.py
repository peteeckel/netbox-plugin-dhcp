import django_filters
from django.utils.translation import gettext as _

from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import MACAddress
from ipam.models import IPAddress, Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import HostReservation

from .mixins import NetworkClientClassesMixin

__all__ = ("HostReservationFilterSet",)


class HostReservationFilterSet(NetworkClientClassesMixin, NetBoxModelFilterSet):
    class Meta:
        model = HostReservation

        fields = (
            "id",
            "name",
            "description",
            "duid",
            "circuit_id",
            "client_id",
            "flex_id",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "comment",
            "hostname",
        )

    hw_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=MACAddress.objects.all(),
        field_name="hw_address",
        label=_("Hardware Address ID"),
    )

    ipv4_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_4
        ),
        field_name="ipv4_address",
        label=_("IPv4 Address ID"),
    )
    ipv6_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_6
        ),
        field_name="ipv6_addresses",
        label=_("IPv6 Address ID"),
    )
    ipv6_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="ipv6_prefixes",
        label=_("IPv6 Prefix ID"),
    )
    excluded_ipv6_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        field_name="excluded_ipv6_prefixes",
        label=_("Excluded IPv6 Prefix ID"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
