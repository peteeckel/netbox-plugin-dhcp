from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import (
    TagFilterField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVModelChoiceField,
)
from utilities.forms import add_blank_choice
from utilities.forms.rendering import FieldSet
from ipam.models import IPRange
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Pool

from .mixins import (
    ClientClassBulkEditFormMixin,
    ClientClassFilterFormMixin,
    ClientClassFormMixin,
    ClientClassImportFormMixin,
    CommonBulkEditFormMixin,
    CommonFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetBoxDHCPFilterFormMixin,
    DDNSUpdateFormMixin,
    DDNSUpdateFilterFormMixin,
    DDNSUpdateImportFormMixin,
    DDNSUpdateBulkEditFormMixin,
)


__all__ = (
    "PoolForm",
    "PoolFilterForm",
    "PoolImportForm",
    "PoolBulkEditForm",
)


class PoolForm(
    ClientClassFormMixin,
    DDNSUpdateFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "evaluate_additional_classes",
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
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "ip_range",
            name=_("Address Pool"),
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
            "user_context",
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

    ip_range = DynamicModelChoiceField(
        queryset=IPRange.objects.all(),
        required=True,
        quick_add=True,
        selector=True,
        label=_("IP Range"),
    )


class PoolFilterForm(
    NetBoxDHCPFilterFormMixin,
    ClientClassFilterFormMixin,
    CommonFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = Pool

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "family",
            "ip_range_id",
            name=_("Address Pool"),
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

    family = forms.ChoiceField(
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
        label=_("Address Family"),
    )
    ip_range_id = DynamicModelMultipleChoiceField(
        queryset=IPRange.objects.all(),
        query_params={
            "family": "$family",
        },
        required=False,
        label=_("IP Range"),
    )

    tag = TagFilterField(Pool)


class PoolImportForm(
    ClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Pool

        fields = (
            "name",
            "description",
            "ip_range",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "evaluate_additional_classes",
            "user_context",
            "comment",
            "tags",
        )

    # TODO: Specify IP ranges by (start_address,end_address)
    ip_range = CSVModelChoiceField(
        queryset=IPRange.objects.all(),
        required=True,
        error_messages={
            "invalid_choice": _("IP range %(value)s not found"),
        },
        label=_("IP Ramhe"),
    )


class PoolBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    CommonBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Pool

    fieldsets = (
        FieldSet(
            "description",
            name=_("Address Pool"),
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
            "user_context",
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
    )

    nullable_fields = (
        "description",
        "client_class_definitions",
        "client_class",
        "required_client_classes",
        "evaluate_additional_classes",
        "user_context",
        "comment",
    )
