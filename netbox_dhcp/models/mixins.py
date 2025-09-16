from django.db import models
from django.utils.translation import gettext_lazy as _

from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
)

__all__ = (
    "NetBoxDHCPMixin",
    "IPv4BootMixin",
    "ContextCommentMixin",
    "ClientClassesMixin",
    "ClientClassMixin",
    "ValidLifetimeMixin",
    "PreferredLifetimeMixin",
    "OfferLifetimeMixin",
    "DDNSUpdateMixin",
)


class NetBoxDHCPMixin(models.Model):
    class Meta:
        abstract = True

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

    def __str__(self):
        return str(self.name)


class IPv4BootMixin(models.Model):
    class Meta:
        abstract = True

    next_server = models.CharField(
        verbose_name=_("Next Server"),
        blank=True,
        max_length=15,
    )
    server_hostname = models.CharField(
        verbose_name=_("Server Hostname"),
        blank=True,
        max_length=64,
    )
    boot_file_name = models.CharField(
        verbose_name=_("Boot File Name"),
        blank=True,
        max_length=128,
    )


class ContextCommentMixin(models.Model):
    class Meta:
        abstract = True

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


class ClientClassesMixin(models.Model):
    class Meta:
        abstract = True

    client_classes = models.ManyToManyField(
        verbose_name=_("Client Classes"),
        to="ClientClass",
        related_name="%(class)ss",
        blank=True,
    )


class ClientClassMixin(ClientClassesMixin):
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
    evaluate_additional_classes = models.ManyToManyField(
        verbose_name=_("Evaluate Additional Classes"),
        to="ClientClass",
        related_name="evaluate_%(class)ss",
        blank=True,
    )


class ValidLifetimeMixin(models.Model):
    class Meta:
        abstract = True

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


class PreferredLifetimeMixin(models.Model):
    class Meta:
        abstract = True

    preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Preferred Lifetime"),
        null=True,
        blank=True,
    )
    min_preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Minimum Preferred Lifetime"),
        null=True,
        blank=True,
    )
    max_preferred_lifetime = models.PositiveIntegerField(
        verbose_name=_("Maximum Preferred Lifetime"),
        null=True,
        blank=True,
    )


class OfferLifetimeMixin(models.Model):
    class Meta:
        abstract = True

    offer_lifetime = models.PositiveIntegerField(
        verbose_name=_("Offer Lifetime"),
        null=True,
        blank=True,
    )


class DDNSUpdateMixin(models.Model):
    class Meta:
        abstract = True

    enable_updates = models.BooleanField(
        verbose_name=_("Enable DDNS updates"),
        null=False,
        default=False,
    )
    ddns_send_updates = models.BooleanField(
        verbose_name=_("Send DDNS updates"),
        null=False,
        default=True,
    )
    ddns_override_no_update = models.BooleanField(
        verbose_name=_("Override client 'no update' flag"),
        null=False,
        default=False,
    )
    ddns_override_client_update = models.BooleanField(
        verbose_name=_("Override client delegation flags"),
        null=False,
        default=False,
    )
    ddns_replace_client_name = models.CharField(
        verbose_name=_("Replace client name"),
        choices=DDNSReplaceClientNameChoices,
        blank=False,
        null=False,
        default=DDNSReplaceClientNameChoices.NEVER,
    )
    ddns_generated_prefix = models.CharField(
        verbose_name=_("Genrated Prefix"),
        blank=True,
        null=True,
    )
    ddns_qualifying_suffix = models.CharField(
        verbose_name=_("Qualifying Suffix"),
        blank=True,
        null=True,
    )
    ddns_update_on_renew = models.BooleanField(
        verbose_name=_("Update DDNS on renew"),
        null=False,
        default=False,
    )
    ddns_conflict_resolution_mode = models.CharField(
        verbose_name=_("Replace client name"),
        choices=DDNSConflictResolutionModeChoices,
        blank=False,
        null=False,
        default=DDNSConflictResolutionModeChoices.CHECK_WITH_DHCID,
    )
    ddns_ttl_percent = models.PositiveIntegerField(
        verbose_name=_("TTL Percent"),
        null=True,
    )
    ddns_ttl = models.PositiveIntegerField(
        verbose_name=_("TTL"),
        null=True,
    )
    ddns_ttl_min = models.PositiveIntegerField(
        verbose_name=_("Minimum TTL"),
        null=True,
    )
    ddns_ttl_max = models.PositiveIntegerField(
        verbose_name=_("Maximum TTL"),
        null=True,
    )
    hostname_char_set = models.CharField(
        verbose_name=_("Allowed Characters in Host Names"),
        max_length=255,
        blank=True,
    )
    hostname_char_replacement = models.CharField(
        verbose_name=_("Replacement Character for Invalid Host Names"),
        max_length=255,
        blank=True,
    )
