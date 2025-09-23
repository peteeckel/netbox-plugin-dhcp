from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from netbox_dhcp.choices import OptionSpaceChoices

from .mixins import ClientClassAssignmentModelMixin

__all__ = (
    "Option",
    "OptionIndex",
)


class Option(ClientClassAssignmentModelMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    definition = models.ForeignKey(
        verbose_name=_("Option Definition"),
        to="OptionDefinition",
        on_delete=models.PROTECT,
        null=False,
    )
    assigned_object_type = models.ForeignKey(
        to="contenttypes.ContentType",
        on_delete=models.PROTECT,
        related_name="+",
        blank=False,
        null=True,
    )
    assigned_object_id = models.PositiveBigIntegerField(
        blank=False,
        null=True,
    )
    assigned_object = GenericForeignKey(
        ct_field="assigned_object_type", fk_field="assigned_object_id"
    )
    data = models.CharField(
        verbose_name=_("Option Data"),
        null=True,
        blank=True,
    )
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=255,
        blank=True,
        null=True,
    )
    csv_format = models.BooleanField(
        verbose_name=_("CSV Format"),
        blank=True,
        null=True,
    )
    always_send = models.BooleanField(
        verbose_name=_("Always Send"),
        blank=True,
        null=True,
    )
    never_send = models.BooleanField(
        verbose_name=_("Never Send"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.definition.name} ({self.definition.code})"

    def get_space_color(self):
        return OptionSpaceChoices.colors.get(self.definition.space)


@register_search
class OptionIndex(SearchIndex):
    model = Option

    fields = (("data", 100),)
