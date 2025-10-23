from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

from .mixins import (
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    LifetimeModelMixin,
    CommonModelMixin,
)
from .option import Option

__all__ = (
    "ClientClass",
    "ClientClassIndex",
)


class ClientClass(
    NetBoxDHCPModelMixin,
    BOOTPModelMixin,
    LifetimeModelMixin,
    CommonModelMixin,
    NetBoxModel,
):
    class Meta:
        verbose_name = _("Client Class")
        verbose_name_plural = _("Client Classes")

        ordering = ("name",)

    clone_fields = (
        "name",
        "description",
        "test",
        "template_test",
        "only_in_additional_list",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
        "comment",
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
    only_in_additional_list = models.BooleanField(
        verbose_name=_("Only in additional list"),
        help_text=_(
            "Evaluate the client class template test only if it is used in additional lists"
        ),
        null=True,
        blank=True,
    )
    options = GenericRelation(
        to=Option,
        content_type_field="assigned_object_type",
        object_id_field="assigned_object_id",
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
        ("comment", 200),
    )
