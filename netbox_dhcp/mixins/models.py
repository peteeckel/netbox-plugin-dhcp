from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = (
    "IPv4ModelFields",
    "CommonModelFields",
)


class IPv4ModelFields(models.Model):
    class Meta:
        abstract = True

    next_server = models.CharField(
        verbose_name=_("Next Server"),
        blank=True,
        max_length=255,
    )
    server_hostname = models.CharField(
        verbose_name=_("Server Hostname"),
        blank=True,
        max_length=255,
    )
    boot_file_name = models.CharField(
        verbose_name=_("Boot File Name"),
        blank=True,
        max_length=255,
    )
    offer_lifetime = models.PositiveIntegerField(
        verbose_name=_("Offer Lifetime"),
        null=True,
        blank=True,
    )


class CommonModelFields(models.Model):
    class Meta:
        abstract = True

    # +
    # TODO: option_data_list
    # -
    user_context = models.JSONField(
        verbose_name=_("User Context"),
        blank=True,
        default=dict,
    )
    comment = models.CharField(
        verbose_name=_("Comment"),
        blank=True,
        max_length=255,
    )
