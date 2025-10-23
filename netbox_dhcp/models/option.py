import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from netbox_dhcp.choices import OptionTypeChoices, OptionSendChoices
from netbox_dhcp.validators import validate_data

from .mixins import ClientClassModelMixin

__all__ = (
    "Option",
    "OptionIndex",
)


class Option(ClientClassModelMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

        ordering = (
            "definition__space",
            "definition__code",
            "definition__name",
        )

    definition = models.ForeignKey(
        verbose_name=_("Option Definition"),
        to="OptionDefinition",
        related_name="options",
        on_delete=models.PROTECT,
        null=False,
    )
    assigned_object_type = models.ForeignKey(
        to="contenttypes.ContentType",
        on_delete=models.PROTECT,
        related_name="+",
    )
    assigned_object_id = models.PositiveBigIntegerField()
    assigned_object = GenericForeignKey(
        ct_field="assigned_object_type",
        fk_field="assigned_object_id",
    )
    data = models.CharField(
        verbose_name=_("Option Data"),
        null=False,
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
        null=True,
        blank=True,
    )
    send_option = models.CharField(
        verbose_name=_("Send Option"),
        choices=OptionSendChoices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.definition}"

    @property
    def family(self):
        return self.definition.family

    def get_family_display(self):
        return self.definition.get_family_display()

    def clean(self):
        super().clean()

        try:
            definition = self.definition
        except ObjectDoesNotExist:
            raise ValidationError({"definition": _("Option definition is required")})

        if definition is None:
            raise ValidationError({"definition": _("Option definition is required")})

        if definition.type == OptionTypeChoices.TYPE_BINARY:
            self.csv_format = False

        if definition.type == OptionTypeChoices.TYPE_RECORD:
            data_array = re.split(r"\s*,\s*", self.data)
            record_types = definition.record_types

            if (definition.array and len(record_types) > len(data_array)) or (
                not definition.array and len(record_types) != len(data_array)
            ):
                raise ValidationError(
                    {
                        "data": _(
                            "Lengths of record type list and data elements do not match"
                        )
                    }
                )

            for mapping in zip(data_array, record_types):
                validate_data(*mapping)

            if definition.array:
                for data_field in data_array[len(record_types) :]:
                    validate_data(data_field, record_types[-1])

        elif definition.array:
            data_array = re.split(r"\s*,\s*", self.data)
            for data_field in data_array:
                validate_data(data_field, definition.type)

        else:
            validate_data(self.data, definition.type)


@register_search
class OptionIndex(SearchIndex):
    model = Option

    fields = (("data", 100),)
