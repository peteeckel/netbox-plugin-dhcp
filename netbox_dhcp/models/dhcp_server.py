from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox_dhcp.choices import (
    DHCPServerStatusChoices,
    HostReservationIdentifierChoices,
    DHCPServerIDTypeChoices,
)
from netbox_dhcp.fields import ChoiceArrayField

from .mixins import (
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    CommonModelMixin,
    LeaseModelMixin,
    DDNSUpdateModelMixin,
    LifetimeModelMixin,
    ChildSubnetModelMixin,
    ChildSharedNetworkModelMixin,
    ChildHostReservationModelMixin,
    ChildClientClassModelMixin,
)
from .option import Option

__all__ = (
    "DHCPServer",
    "DHCPServerIndex",
)


class DHCPServer(
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    CommonModelMixin,
    LeaseModelMixin,
    DDNSUpdateModelMixin,
    LifetimeModelMixin,
    ChildSubnetModelMixin,
    ChildSharedNetworkModelMixin,
    ChildHostReservationModelMixin,
    ChildClientClassModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("DHCP Server")
        verbose_name_plural = _("DHCP Servers")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "status",
        "dhcp_cluster",
    )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=50,
        choices=DHCPServerStatusChoices,
        default=DHCPServerStatusChoices.STATUS_ACTIVE,
        blank=True,
    )

    dhcp_cluster = models.ForeignKey(
        to="DHCPCluster",
        verbose_name=_("DHCP Cluster"),
        on_delete=models.SET_NULL,
        related_name="dhcp_servers",
        blank=True,
        null=True,
    )
    device = models.ForeignKey(
        to=Device,
        verbose_name=_("Device"),
        on_delete=models.SET_NULL,
        related_name="netbox_dhcp_dhcp_servers",
        blank=True,
        null=True,
    )
    virtual_machine = models.ForeignKey(
        to=VirtualMachine,
        verbose_name=_("Virtual Machine"),
        on_delete=models.SET_NULL,
        related_name="netbox_dhcp_dhcp_servers",
        blank=True,
        null=True,
    )

    # TODO: option_definitions, interfaces
    decline_probation_period = models.PositiveIntegerField(
        verbose_name=_("Decline Probation Period"),
        blank=True,
        null=True,
    )
    host_reservation_identifiers = ChoiceArrayField(
        base_field=models.CharField(
            choices=HostReservationIdentifierChoices,
        ),
        verbose_name=_("Host Reservation Identifiers"),
        blank=True,
        null=True,
        default=list,
    )
    echo_client_id = models.BooleanField(
        verbose_name=_("Echo Client ID"),
        blank=True,
        null=True,
    )
    relay_supplied_options = ArrayField(
        verbose_name=_("Relay Supplied Options"),
        base_field=models.PositiveIntegerField(
            validators=[
                MinValueValidator(0),
                MaxValueValidator(255),
            ]
        ),
        blank=True,
        default=list,
    )
    server_id = models.CharField(
        verbose_name=_("Server ID"),
        choices=DHCPServerIDTypeChoices,
        blank=True,
        null=True,
    )
    options = GenericRelation(
        to=Option,
        content_type_field="assigned_object_type",
        object_id_field="assigned_object_id",
    )

    def get_status_color(self):
        return DHCPServerStatusChoices.colors.get(self.status)

    def get_server_id_color(self):
        return DHCPServerIDTypeChoices.colors.get(self.server_id)


@register_search
class DHCPServerIndex(SearchIndex):
    model = DHCPServer

    fields = (
        ("name", 100),
        ("description", 200),
    )
