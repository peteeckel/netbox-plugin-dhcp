from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from dcim.models import MACAddress
from ipam.models import IPAddress, Prefix

from .mixins import (
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    CommonModelMixin,
    ClientClassAssignmentModelMixin,
)

__all__ = (
    "HostReservation",
    "HostReservationIndex",
)


class HostReservation(
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    CommonModelMixin,
    ClientClassAssignmentModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("Host Reservation")
        verbose_name_plural = _("Host Reservations")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "circuit_id",
        "flex_id",
        "hostname",
        "assign_client_classes",
        "comment",
    )

    duid = models.CharField(
        verbose_name=_("DUID"),
        blank=True,
        max_length=255,
    )
    hw_address = models.ForeignKey(
        verbose_name=_("Hardware Address"),
        to=MACAddress,
        related_name="netbox_dhcp_host_reservations",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    flex_id = models.CharField(
        verbose_name=_("Flex ID"),
        blank=True,
        max_length=255,
    )
    # IPv4 only
    circuit_id = models.CharField(
        verbose_name=_("Circuit ID"),
        blank=True,
        max_length=255,
    )
    # IPv4 only
    client_id = models.CharField(
        verbose_name=_("Client ID"),
        blank=True,
        max_length=255,
    )

    hostname = models.CharField(
        verbose_name=_("Hostname"),
        blank=True,
        max_length=255,
    )
    ipv4_address = models.ForeignKey(
        verbose_name=_("IPv4 Addresses"),
        to=IPAddress,
        related_name="netbox_dhcp_ipv4_host_reservations",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    ipv6_addresses = models.ManyToManyField(
        verbose_name=_("IPv6 Addresses"),
        to=IPAddress,
        related_name="netbox_dhcp_ipv6_host_reservations",
    )
    ipv6_prefixes = models.ManyToManyField(
        verbose_name=_("IPv6 Prefixes"),
        to=Prefix,
        related_name="netbox_dhcp_ipv6_host_reservations",
    )
    excluded_ipv6_prefixes = models.ManyToManyField(
        verbose_name=_("Excluded IPv6 Prefixes"),
        to=Prefix,
        related_name="netbox_dhcp_excluded_ipv6_host_reservations",
    )


@register_search
class HostReservationIndex(SearchIndex):
    model = HostReservation

    fields = (
        ("name", 100),
        ("duid", 150),
        ("hw_address", 150),
        ("circuit_id", 150),
        ("client_id", 150),
        ("flex_id", 150),
        ("hostname", 180),
        ("description", 200),
        ("comment", 400),
    )
