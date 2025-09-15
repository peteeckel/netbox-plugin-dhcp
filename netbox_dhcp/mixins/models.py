from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = (
    "IPv4ModelFields",
    "CommonModelFields",
    "PoolModelFields",
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


class PoolModelFields(models.Model):
    class Meta:
        abstract = True

    client_class = models.ForeignKey(
        verbose_name=_("Client Class"),
        to="ClientClass",
        related_name="%(class)s",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    require_client_classes = models.ManyToManyField(
        verbose_name=_("Require Client Classes"),
        to="ClientClass",
        related_name="require_%(class)ss",
        blank=True,
    )
