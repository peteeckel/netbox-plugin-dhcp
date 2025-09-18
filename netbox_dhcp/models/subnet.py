# from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import (
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    LifetimeModelMixin,
)

__all__ = (
    "Subnet",
    "SubnetIndex",
)


class Subnet(
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    ClientClassModelMixin,
    CommonModelMixin,
    LifetimeModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("Subnet")
        verbose_name_plural = _("Subnets")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "client_class_definitions",
        "client_class",
        "required_client_classes",
        "evaluate_additional_classes",
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
        "comment",
    )


@register_search
class SubnetIndex(SearchIndex):
    model = Subnet

    fields = (
        ("name", 100),
        ("description", 200),
        ("next_server", 300),
        ("server_hostname", 300),
        ("boot_file_name", 300),
        ("comment", 200),
    )
