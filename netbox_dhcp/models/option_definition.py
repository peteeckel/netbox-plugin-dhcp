from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.choices import OptionSpaceChoices, OptionTypeChoices
from netbox_dhcp.fields import ChoiceArrayField

__all__ = (
    "OptionDefinition",
    "OptionDefinitionIndex",
)


class OptionDefinition(NetBoxModel):
    class Meta:
        verbose_name = _("Option Definition")
        verbose_name_plural = _("Option Definitions")

        ordering = (
            "space",
            "code",
            "name",
        )

        unique_together = ("space", "code")

    clone_fields = ("space",)

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        blank=False,
        null=False,
    )
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=255,
        blank=True,
        null=True,
    )
    family = models.PositiveIntegerField(
        verbose_name=_("Address Family"),
        choices=IPAddressFamilyChoices,
        blank=False,
        null=False,
        default=IPAddressFamilyChoices.FAMILY_4,
    )
    space = models.CharField(
        verbose_name=_("Space"),
        choices=OptionSpaceChoices,
        blank=False,
        null=False,
        default=OptionSpaceChoices.DHCPV4,
    )
    code = models.PositiveIntegerField(
        verbose_name=_("Code"),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(255),
        ],
        blank=False,
        null=False,
    )
    type = models.CharField(
        verbose_name=_("Type"),
        choices=OptionTypeChoices,
        blank=False,
        null=False,
    )
    record_types = ChoiceArrayField(
        base_field=models.CharField(
            choices=OptionTypeChoices,
        ),
        verbose_name=_("Record Types"),
        blank=True,
        null=True,
    )
    encapsulate = models.CharField(
        verbose_name=_("Encapsulate"),
        blank=True,
        null=True,
    )
    array = models.BooleanField(
        verbose_name=_("Array"),
        null=True,
        blank=True,
    )
    standard = models.BooleanField(
        verbose_name=_("Standard Option Type"),
        blank=False,
        null=False,
        default=False,
    )

    def __str__(self):
        return f"{self.space} {self.name} ({self.code})"

    def get_space_color(self):
        return OptionSpaceChoices.colors.get(self.space)


@register_search
class OptionDefinitionIndex(SearchIndex):
    model = OptionDefinition

    fields = (("name", 100),)
