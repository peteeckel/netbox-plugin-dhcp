import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from netbox_dhcp.choices import OptionSpaceChoices, OptionTypeChoices
from netbox_dhcp.validators import validate_data

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
    @property
    def family(self):
        return self.definition.family

    def get_family_display(self):
        return self.definition.get_family_display()

    def clean(self):
        super().clean()

        if self.definition.type == OptionTypeChoices.TYPE_BINARY:
            self.csv_format = False

        if self.definition.type == OptionTypeChoices.TYPE_RECORD:
            data_array = re.split(r"\s*,\s*", self.data)
            record_types = self.definition.record_types

            if (self.definition.array and len(record_types) > len(data_array)) or (
                not self.definition.array and len(record_types) != len(data_array)
            ):
                raise ValidationError(
                    _("Lengths of record type list and data elements do not match")
                )

            for mapping in zip(data_array, record_types):
                validate_data(*mapping)

            if self.definition.array:
                for data_field in data_array[len(record_types) :]:
                    validate_data(data_field, record_types[-1])

        elif self.definition.array:
            data_array = re.split(r"\s*,\s*", self.data)
            for data_field in data_array:
                validate_data(data_field, self.definition.type)

        else:
            validate_data(self.data, self.definition.type)


@register_search
class OptionIndex(SearchIndex):
    model = Option

    fields = (("data", 100),)
