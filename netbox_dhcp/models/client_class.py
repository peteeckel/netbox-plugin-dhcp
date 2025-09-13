from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from netbox_dhcp.mixins import IPv4ModelFields, CommonModelFields


__all__ = (
    "ClientClass",
    "ClientClassIndex",
)


class ClientClass(IPv4ModelFields, CommonModelFields, NetBoxModel):
    class Meta:
        verbose_name = _("Client Class")
        verbose_name_plural = _("Client Classes")

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
        max_length=255,
    )

    test = models.CharField(
        verbose_name=_("Test"),
        blank=True,
        max_length=255,
    )
    template_test = models.CharField(
        verbose_name=_("Template Test"),
        blank=True,
        max_length=255,
    )
    only_if_required = models.BooleanField(
        verbose_name=_("Only if required"),
        help_text=_("Evaluate the client class test only if it is required"),
        default=True,
    )
    only_in_additional_list = models.BooleanField(
        verbose_name=_("Only in additional list"),
        help_text=_(
            "Evaluate the client class template test only if it is used in additional lists"
        ),
        default=True,
    )
    valid_lifetime = models.PositiveIntegerField(
        verbose_name=_("Valid Lifetime"),
        null=True,
        blank=True,
    )
    min_valid_lifetime = models.PositiveIntegerField(
        verbose_name=_("Minimum Valid Lifetime"),
        null=True,
        blank=True,
    )
    max_valid_lifetime = models.PositiveIntegerField(
        verbose_name=_("Maximum Valid Lifetime"),
        null=True,
        blank=True,
    )
    # IPv6 only
    preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Preferred Lifetime"),
        null=True,
        blank=True,
    )
    # IPv6 only
    min_preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Minimum Preferred Lifetime"),
        null=True,
        blank=True,
    )
    # IPv6 only
    max_preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Maximum Preferred Lifetime"),
        null=True,
        blank=True,
    )


@register_search
class ClientClassIndex(SearchIndex):
    model = ClientClass

    fields = (
        ("name", 100),
        ("description", 200),
        ("next_server", 300),
        ("server_hostname", 300),
        ("boot_file_name", 300),
        ("comment", 400),
    )
