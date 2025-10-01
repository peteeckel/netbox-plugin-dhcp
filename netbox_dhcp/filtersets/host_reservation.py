import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import MACAddress
from ipam.models import IPAddress, Prefix
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import HostReservation, DHCPServer, Subnet

from .mixins import BOOTPFilterMixin, ClientClassAssignmentFilterMixin

__all__ = ("HostReservationFilterSet",)


class HostReservationFilterSet(
    BOOTPFilterMixin,
    ClientClassAssignmentFilterMixin,
    NetBoxModelFilterSet,
):
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
            "comment",
            "hostname",
            *BOOTPFilterMixin.FILTER_FIELDS,
        )

    name = django_filters.CharFilter(
        label=_("Name"),
    )
    description = django_filters.CharFilter(
        label=_("Description"),
    )
    duid = django_filters.CharFilter(
        label=_("DUID"),
    )
    circuit_id = django_filters.CharFilter(
        label=_("Circuit ID"),
    )
    client_id = django_filters.CharFilter(
        label=_("Client ID"),
    )
    flex_id = django_filters.CharFilter(
        label=_("Flex ID"),
    )

    hw_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=MACAddress.objects.all(),
        field_name="hw_address",
        label=_("Hardware Address ID"),
    )
    hw_address = django_filters.CharFilter(
        field_name="hw_address__mac_address",
        label=_("Hardware Address"),
    )
    ipv4_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_4
        ),
        field_name="ipv4_address",
        label=_("IPv4 Address ID"),
    )
    ipv4_address = django_filters.CharFilter(
        field_name="ipv4_address__address",
        label=_("IPv4 Address"),
    )
    ipv6_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_6
        ),
        field_name="ipv6_addresses",
        label=_("IPv6 Address ID"),
    )
    ipv6_address = django_filters.CharFilter(
        field_name="ipv6_addresses__address",
        distinct=True,
        label=_("IPv6 Address"),
    )
    ipv6_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        field_name="ipv6_prefixes",
        label=_("IPv6 Prefix ID"),
    )
    ipv6_prefix = django_filters.CharFilter(
        field_name="ipv6_prefixes__prefix",
        distinct=True,
        label=_("IPv6 Prefix"),
    )
    excluded_ipv6_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        field_name="excluded_ipv6_prefixes",
        label=_("Excluded IPv6 Prefix ID"),
    )
    excluded_ipv6_prefix = django_filters.CharFilter(
        field_name="excluded_ipv6_prefixes__prefix",
        distinct=True,
        label=_("Excluded IPv6 Prefix"),
    )

    parent_dhcp_server_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPServer.objects.all(),
        field_name="parent_dhcpservers",
        label=_("Parent DHCP Server ID"),
    )
    parent_dhcp_server = django_filters.CharFilter(
        field_name="parent_dhcpservers__name",
        distinct=True,
        label=_("Parent DHCP Server"),
    )
    parent_subnet_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Subnet.objects.all(),
        field_name="parent_subnets",
        label=_("Parent Subnet ID"),
    )
    parent_subnet = django_filters.CharFilter(
        field_name="parent_subnets__name",
        distinct=True,
        label=_("Parent Subnet"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
