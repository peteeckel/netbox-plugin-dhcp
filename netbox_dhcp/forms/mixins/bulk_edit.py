from django import forms
from django.utils.translation import gettext as _

from utilities.forms import add_blank_choice
from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.widgets import BulkEditNullBooleanSelect
from ipam.models import Prefix

from netbox_dhcp.models import ClientClass
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
    AllocatorTypeChoices,
    PDAllocatorTypeChoices,
)

__all__ = (
    "NetBoxDHCPBulkEditFormMixin",
    "BOOTPBulkEditFormMixin",
    "ClientClassAssignmentBulkEditFormMixin",
    "ClientClassDefinitionBulkEditFormMixin",
    "ClientClassBulkEditFormMixin",
    "OfferLifetimeBulkEditFormMixin",
    "LifetimeBulkEditFormMixin",
    "CommonBulkEditFormMixin",
    "PrefixBulkEditFormMixin",
    "DDNSUpdateBulkEditFormMixin",
    "LeaseBulkEditFormMixin",
)


class NetBoxDHCPBulkEditFormMixin(forms.Form):
    description = forms.CharField(
        required=False,
        label=_("Description"),
    )


class BOOTPBulkEditFormMixin(forms.Form):
    next_server = forms.CharField(
        required=False,
        label=_("Next Server"),
    )
    server_hostname = forms.CharField(
        required=False,
        label=_("Server Hostname"),
    )
    boot_file_name = forms.CharField(
        required=False,
        label=_("Boot File Name"),
    )


class ClientClassAssignmentBulkEditFormMixin(forms.Form):
    assign_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Classes"),
    )


class ClientClassDefinitionBulkEditFormMixin(forms.Form):
    client_class_definitions = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Class Definitions"),
    )


class ClientClassBulkEditFormMixin(ClientClassDefinitionBulkEditFormMixin):
    client_class = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Class"),
    )
    required_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Required Client Classes"),
    )
    evaluate_additional_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Evaluate Additional Classes"),
    )


class OfferLifetimeBulkEditFormMixin(forms.Form):
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Offer Lifetime"),
    )


class LifetimeBulkEditFormMixin(OfferLifetimeBulkEditFormMixin):
    valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Valid Lifetime"),
    )
    min_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Minimum Valid Lifetime"),
    )
    max_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Maximum Valid Lifetime"),
    )
    preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Preferred Lifetime"),
    )
    min_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Minimum Preferred Lifetime"),
    )
    max_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Maximum Preferred Lifetime"),
    )


class CommonBulkEditFormMixin(forms.Form):
    # TODO: option_data_list
    user_context = forms.JSONField(
        required=False,
        label=_("User Context"),
    )
    comment = forms.CharField(
        required=False,
        label=_("Comment"),
    )


class PrefixBulkEditFormMixin(forms.Form):
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
        selector=True,
        label=_("Prefix"),
    )


class DDNSUpdateBulkEditFormMixin(forms.Form):
    ddns_send_updates = forms.NullBooleanField(
        label=_("Send DDNS updates"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    ddns_override_no_update = forms.NullBooleanField(
        label=_("Override client 'no update' flag"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    ddns_override_client_update = forms.NullBooleanField(
        label=_("Override client delegation flags"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    ddns_replace_client_name = forms.ChoiceField(
        choices=add_blank_choice(DDNSReplaceClientNameChoices),
        required=False,
        label=_("Replace Client Name"),
    )
    ddns_generated_prefix = forms.CharField(
        required=False,
        label=_("Generated Prefix"),
    )
    ddns_qualifying_suffix = forms.CharField(
        required=False,
        label=_("Qualifying Suffix"),
    )
    ddns_update_on_renew = forms.NullBooleanField(
        label=_("Update DDNS on renew"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    ddns_qualifying_suffix = forms.CharField(
        label=_("Replace client name"),
        required=False,
    )
    ddns_conflict_resolution_mode = forms.ChoiceField(
        label=_("Conflict Resolution Mode"),
        choices=add_blank_choice(DDNSConflictResolutionModeChoices),
        required=False,
    )
    ddns_ttl_percent = forms.DecimalField(
        label=_("TTL Percent"),
        help_text=_("Enter a decimal value between 0.00 and 1.00"),
        min_value=0.0,
        max_value=1.0,
        max_digits=4,
        decimal_places=3,
        required=False,
    )
    ddns_ttl = forms.IntegerField(
        label=_("TTL"),
        required=False,
    )
    ddns_ttl_min = forms.IntegerField(
        label=_("Minimum TTL"),
        required=False,
    )
    ddns_ttl_max = forms.IntegerField(
        label=_("Maximum TTL"),
        required=False,
    )
    hostname_char_set = forms.CharField(
        label=_("Allowed Characters in Host Names"),
        required=False,
    )
    hostname_char_replacement = forms.CharField(
        label=_("Replacement Character for Invalid Host Names"),
        required=False,
    )


class LeaseBulkEditFormMixin(forms.Form):
    renew_timer = forms.IntegerField(
        label=_("Renew Timer"),
        required=False,
    )
    rebind_timer = forms.IntegerField(
        label=_("Rebind Timer"),
        required=False,
    )
    match_client_id = forms.NullBooleanField(
        label=_("Match Client ID"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    authoritative = forms.NullBooleanField(
        label=_("Authoritative"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    reservations_global = forms.NullBooleanField(
        label=_("Global reservations"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    reservations_out_of_pool = forms.NullBooleanField(
        label=_("Out-of-pool reservations"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    reservations_in_subnet = forms.NullBooleanField(
        label=_("In-subnet reservations"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    calculate_tee_times = forms.NullBooleanField(
        label=_("Calculate T times"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    t1_percent = forms.DecimalField(
        label=_("T1 Percent"),
        help_text=_("Enter a decimal value between 0.000 and 1.000"),
        max_digits=4,
        decimal_places=3,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    t2_percent = forms.DecimalField(
        label=_("T2 Percent"),
        max_digits=4,
        decimal_places=3,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    cache_threshold = forms.DecimalField(
        label=_("Cache Threshold"),
        help_text=_("Enter a decimal value between 0.00 and 1.00"),
        max_digits=3,
        decimal_places=2,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    cache_max_age = forms.IntegerField(
        label=_("Maximum Cache Age"),
        required=False,
    )
    adaptive_lease_time_threshold = forms.DecimalField(
        label=_("Adaptive Lease Time Threshold"),
        help_text=_("Enter a decimal value between 0.00 and 1.00"),
        max_digits=3,
        decimal_places=2,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    store_extended_info = forms.NullBooleanField(
        label=_("Store Extended Info"),
        widget=BulkEditNullBooleanSelect(),
        required=False,
    )
    allocator = forms.ChoiceField(
        choices=add_blank_choice(AllocatorTypeChoices),
        required=False,
        label=_("Allocator"),
    )
    pd_allocator = forms.ChoiceField(
        choices=add_blank_choice(PDAllocatorTypeChoices),
        required=False,
        label=_("Prefix Delegation Allocator"),
    )
