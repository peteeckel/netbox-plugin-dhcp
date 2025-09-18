# from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField
from utilities.forms.rendering import FieldSet

from netbox_dhcp.models import Subnet
from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    CommonFilterFormMixin,
    CommonBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
    LifetimeFilterFormMixin,
    LifetimeBulkEditFormMixin,
    BOOTPFilterFormMixin,
    BOOTPBulkEditFormMixin,
    PrefixFormMixin,
    PrefixFilterFormMixin,
    PrefixImportFormMixin,
    PrefixBulkEditFormMixin,
    DDNSUpdateFormMixin,
    DDNSUpdateFilterFormMixin,
    DDNSUpdateImportFormMixin,
    DDNSUpdateBulkEditFormMixin,
)


__all__ = (
    "SubnetForm",
    "SubnetFilterForm",
    "SubnetImportForm",
    "SubnetBulkEditForm",
)


class SubnetForm(
    PrefixFormMixin,
    ClientClassFormMixin,
    DDNSUpdateFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "prefix",
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
            "user_context",
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
            "comment",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "prefix",
            name=_("Subnet"),
        ),
        FieldSet(
            "client_class_definitions",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class",
            "required_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "user_context",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "comment",
            "evaluate_additional_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
            name=_("Dynamic DNS Update"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class SubnetFilterForm(
    NetBoxDHCPFilterFormMixin,
    PrefixFilterFormMixin,
    BOOTPFilterFormMixin,
    ClientClassFilterFormMixin,
    LifetimeFilterFormMixin,
    CommonFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = Subnet

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "prefix_id",
            name=_("Subnet"),
        ),
        FieldSet(
            "network_client_class_id",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class_id",
            "required_client_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "comment",
            "evaluate_additional_class_id",
            name=_("Assignment"),
        ),
        FieldSet(
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
            name=_("Dynamic DNS Update"),
        ),
    )

    tag = TagFilterField(Subnet)


class SubnetImportForm(
    PrefixImportFormMixin,
    ClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "prefix",
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
            "user_context",
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
            "comment",
            "tags",
        )


class SubnetBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    PrefixBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    LifetimeBulkEditFormMixin,
    CommonBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Subnet

    fieldsets = (
        FieldSet(
            "description",
            "prefix",
            name=_("Subnet"),
        ),
        FieldSet(
            "client_class_definitions",
            name=_("Client Class Definitions"),
        ),
        FieldSet(
            "client_class",
            "required_client_classes",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "user_context",
            "comment",
            "evaluate_additional_classes",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            name=_("Assignment"),
        ),
        FieldSet(
            "hostname_char_set",
            "hostname_char_replacement",
            "ddns_send_updates",
            "ddns_override_no_update",
            "ddns_override_client_update",
            "ddns_replace_client_name",
            "ddns_generated_prefix",
            "ddns_qualifying_suffix",
            "ddns_update_on_renew",
            "ddns_conflict_resolution_mode",
            "ddns_ttl_percent",
            "ddns_ttl",
            "ddns_ttl_min",
            "ddns_ttl_max",
            name=_("Dynamic DNS Update"),
        ),
    )

    nullable_fields = (
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
        "hostname_char_set",
        "hostname_char_replacement",
        "ddns_send_updates",
        "ddns_override_no_update",
        "ddns_override_client_update",
        "ddns_replace_client_name",
        "ddns_generated_prefix",
        "ddns_qualifying_suffix",
        "ddns_update_on_renew",
        "ddns_conflict_resolution_mode",
        "ddns_ttl_percent",
        "ddns_ttl",
        "ddns_ttl_min",
        "ddns_ttl_max",
        "user_context",
        "comment",
    )
