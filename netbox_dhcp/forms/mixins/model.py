from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms import (
    add_blank_choice,
    get_field_value,
    BOOLEAN_WITH_BLANK_CHOICES,
)
from utilities.forms.rendering import FieldSet
from ipam.models import Prefix

from netbox_dhcp.models import (
    ClientClass,
    Subnet,
    SharedNetwork,
    DHCPServer,
    DHCPServerInterface,
)
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
    AllocatorTypeChoices,
    PDAllocatorTypeChoices,
)

__all__ = (
    "BOOTPFormMixin",
    "ClientClassFormMixin",
    "EvaluateClientClassFormMixin",
    "PrefixFormMixin",
    "DDNSUpdateFormMixin",
    "LeaseFormMixin",
    "LifetimeFormMixin",
    "SubnetFormMixin",
    "DHCPServerFormMixin",
    "SharedNetworkFormMixin",
    "NetworkFormMixin",
)


class BOOTPFormMixin:
    FIELDS = [
        "next_server",
        "server_hostname",
        "boot_file_name",
    ]
    FIELDSET = FieldSet(
        "next_server",
        "server_hostname",
        "boot_file_name",
        name=_("BOOTP"),
    )


class ClientClassFormMixin(forms.Form):
    FIELDS = [
        "client_classes",
    ]
    FIELDSET = FieldSet(
        "client_classes",
        name=_("Client Classes"),
    )

    client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Classes"),
    )


class EvaluateClientClassFormMixin(forms.Form):
    FIELDS = [
        "evaluate_additional_classes",
    ]
    FIELDSET = FieldSet(
        "evaluate_additional_classes",
        name=_("Client Classes"),
    )

    evaluate_additional_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Evaluate Additional Classes"),
    )


class PrefixFormMixin(forms.Form):
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=True,
        selector=True,
        context={
            "depth": None,
        },
        quick_add=True,
        label=_("Prefix"),
    )


class DDNSUpdateFormMixin(forms.Form):
    FIELDS = [
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
        "hostname_char_set",
        "hostname_char_replacement",
    ]
    FIELDSET = FieldSet(
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
        "hostname_char_set",
        "hostname_char_replacement",
        name=_("Dynamic DNS Update"),
    )

    def init_ddns_fields(self):
        self.fields["ddns_send_updates"].widget.attrs.update(
            {
                "hx-get": ".",
                "hx-include": "#form_fields",
                "hx-target": "#form_fields",
            }
        )

        if not bool(get_field_value(self, "ddns_send_updates")):
            for field_name in DDNSUpdateFormMixin.FIELDS:
                if field_name != "ddns_send_updates":
                    del self.fields[field_name]

    ddns_send_updates = forms.NullBooleanField(
        label=_("Send DDNS updates"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    ddns_override_no_update = forms.NullBooleanField(
        label=_("Override client 'no update' flag"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    ddns_override_client_update = forms.NullBooleanField(
        label=_("Override client delegation flags"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    ddns_replace_client_name = forms.ChoiceField(
        choices=add_blank_choice(DDNSReplaceClientNameChoices),
        required=False,
        label=_("Replace Client Name"),
    )
    ddns_generated_prefix = forms.CharField(
        label=_("Generated Prefix"),
        empty_value=None,
        required=False,
    )
    ddns_qualifying_suffix = forms.CharField(
        label=_("Qualifying Suffix"),
        empty_value=None,
        required=False,
    )
    ddns_update_on_renew = forms.NullBooleanField(
        label=_("Update DDNS on renew"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    ddns_conflict_resolution_mode = forms.ChoiceField(
        choices=add_blank_choice(DDNSConflictResolutionModeChoices),
        required=False,
        label=_("Conflict Resolution Mode"),
    )
    ddns_ttl_percent = forms.DecimalField(
        label=_("TTL Percent"),
        help_text=_("A decimal value between 0.000 and 1.000"),
        min_value=0.0,
        max_value=1.0,
        max_digits=4,
        decimal_places=3,
        required=False,
    )


class LifetimeFormMixin(forms.Form):
    FIELDS = [
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
    ]
    FIELDSET = FieldSet(
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
        name=_("Lifetimes"),
    )


class LeaseFormMixin(forms.Form):
    FIELDS = [
        "renew_timer",
        "rebind_timer",
        "calculate_tee_times",
        "t1_percent",
        "t2_percent",
        "adaptive_lease_time_threshold",
        "match_client_id",
        "reservations_global",
        "reservations_out_of_pool",
        "reservations_in_subnet",
        "cache_threshold",
        "cache_max_age",
        "authoritative",
        "store_extended_info",
        "allocator",
        "pd_allocator",
    ]
    FIELDSET = FieldSet(
        "renew_timer",
        "rebind_timer",
        "calculate_tee_times",
        "t1_percent",
        "t2_percent",
        "adaptive_lease_time_threshold",
        "match_client_id",
        "reservations_global",
        "reservations_out_of_pool",
        "reservations_in_subnet",
        "cache_threshold",
        "cache_max_age",
        "authoritative",
        "store_extended_info",
        "allocator",
        "pd_allocator",
        name=_("Lease"),
    )

    calculate_tee_times = forms.NullBooleanField(
        label=_("Calculate T Times"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    match_client_id = forms.NullBooleanField(
        label=_("Match Client ID"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    authoritative = forms.NullBooleanField(
        label=_("Authoritative"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    reservations_global = forms.NullBooleanField(
        label=_("Global reservations"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    reservations_out_of_pool = forms.NullBooleanField(
        label=_("Out-of-pool reservations"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    reservations_in_subnet = forms.NullBooleanField(
        label=_("In-subnet reservations"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    store_extended_info = forms.NullBooleanField(
        label=_("Store extended info"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
    t1_percent = forms.DecimalField(
        label=_("T1"),
        help_text=_("A decimal value between 0.000 and 1.000"),
        max_digits=4,
        decimal_places=3,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    t2_percent = forms.DecimalField(
        label=_("T2"),
        help_text=_("A decimal value between 0.000 and 1.000"),
        max_digits=4,
        decimal_places=3,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    cache_threshold = forms.DecimalField(
        label=_("Cache Threshold"),
        help_text=_("A decimal value between 0.00 and 1.00"),
        max_digits=3,
        decimal_places=2,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    adaptive_lease_time_threshold = forms.DecimalField(
        label=_("Adaptive Lease Time Threshold"),
        help_text=_("A decimal value between 0.00 and 1.00"),
        max_digits=3,
        decimal_places=2,
        min_value=0.0,
        max_value=1.0,
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


class SubnetFormMixin(forms.Form):
    FIELDS = [
        "subnet",
    ]

    subnet = DynamicModelChoiceField(
        queryset=Subnet.objects.all(),
        required=False,
        context={
            "description": "prefix_display",
        },
        label=_("Subnet"),
    )


class DHCPServerFormMixin(forms.Form):
    FIELDS = [
        "dhcp_server",
    ]

    dhcp_server = DynamicModelChoiceField(
        queryset=DHCPServer.objects.all(),
        required=False,
        label=_("DHCP Server"),
    )


class SharedNetworkFormMixin(forms.Form):
    FIELDS = [
        "shared_network",
    ]

    shared_network = DynamicModelChoiceField(
        queryset=SharedNetwork.objects.all(),
        required=False,
        context={
            "description": "prefix_display",
        },
        label=_("Shared Network"),
    )


class NetworkFormMixin(forms.Form):
    FIELDS = [
        "server_interfaces",
        "relay",
        "interface_id",
        "rapid_commit",
    ]
    FIELDSET = FieldSet(
        "server_interfaces",
        "relay",
        "interface_id",
        "rapid_commit",
        name=_("Network"),
    )

    server_interfaces = DynamicModelMultipleChoiceField(
        queryset=DHCPServerInterface.objects.all(),
        required=False,
        label=_("Interfaces"),
        context={
            "parent": "dhcp_server",
        },
    )
    rapid_commit = forms.NullBooleanField(
        label=_("Rapid Commit"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        required=False,
    )
