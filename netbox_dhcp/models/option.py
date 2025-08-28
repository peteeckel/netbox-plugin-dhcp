from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


__all__ = (
    "Option",
    "OptionIndex",
)


class Option(NetBoxModel):
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

        ordering = ("name",)

    def __str__(self):
        return str(self.name)

    name = models.CharField(
        verbose_name=_("Name"),
        unique=True,
        max_length=255,
        db_collation="natural_sort",
    )
    description = models.CharField(
        verbose_name=_("Description"),
        blank=True,
        max_length=200,
    )


@register_search
class OptionIndex(SearchIndex):
    model = Option

    fields = (
        ("name", 100),
        ("description", 200),
    )
