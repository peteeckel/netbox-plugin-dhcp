# from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import NetBoxDHCPMixin

__all__ = (
    "Option",
    "OptionIndex",
)


class Option(NetBoxDHCPMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
    )


@register_search
class OptionIndex(SearchIndex):
    model = Option

    fields = (
        ("name", 100),
        ("description", 200),
    )
