# from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import (
    NetBoxDHCPModelMixin,
    ClientClassModelMixin,
)

__all__ = (
    "SharedNetwork",
    "SharedNetworkIndex",
)


class SharedNetwork(NetBoxDHCPModelMixin, ClientClassModelMixin, NetBoxModel):
    class Meta:
        verbose_name = _("Shared Network")
        verbose_name_plural = _("Shared Networks")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "client_class_definitions",
        "client_class",
        "required_client_classes",
        "evaluate_additional_classes",
    )


@register_search
class SharedNetworkIndex(SearchIndex):
    model = SharedNetwork

    fields = (
        ("name", 100),
        ("description", 200),
    )
