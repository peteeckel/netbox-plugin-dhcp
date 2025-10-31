from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.contrib.contenttypes.fields import GenericRelation

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.models import Prefix
from ipam.choices import IPAddressFamilyChoices

from .mixins import (
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    EvaluateClientClassModelMixin,
)
from .option import Option

__all__ = (
    "PDPool",
    "PDPoolIndex",
)


class PDPool(
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
    EvaluateClientClassModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("Prefix Delegation Pool")
        verbose_name_plural = _("Prefix Delegation Pools")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "delegated_length",
        "client_classes",
        "evaluate_additional_classes",
    )

    subnet = models.ForeignKey(
        verbose_name=_("Parent Subnet"),
        to="netbox_dhcp.Subnet",
        on_delete=models.CASCADE,
        related_name="child_pd_pools",
    )

    pool_id = models.PositiveIntegerField(
        verbose_name=_("Pool ID"),
        blank=True,
        null=True,
    )
    prefix = models.ForeignKey(
        verbose_name=_("IPv6 Prefix"),
        to=Prefix,
        related_name="netbox_dhcp_pd_pools",
        on_delete=models.PROTECT,
    )
    delegated_length = models.IntegerField(
        verbose_name=_("Delegated Length"),
        validators=[MinValueValidator(0), MaxValueValidator(128)],
    )
    excluded_prefix = models.ForeignKey(
        verbose_name=_("Excluded IPv6 Prefix"),
        to=Prefix,
        related_name="netbox_dhcp_pd_excluded_pools",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    options = GenericRelation(
        to=Option,
        content_type_field="assigned_object_type",
        object_id_field="assigned_object_id",
    )

    @property
    def family(self):
        return IPAddressFamilyChoices.FAMILY_6


@register_search
class PDPoolIndex(SearchIndex):
    model = PDPool

    fields = (
        ("name", 100),
        ("description", 200),
    )
