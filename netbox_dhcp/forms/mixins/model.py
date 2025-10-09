from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms import add_blank_choice, BOOLEAN_WITH_BLANK_CHOICES

from ipam.models import Prefix

from netbox_dhcp.models import (
    ClientClass,
    Subnet,
    SharedNetwork,
    Pool,
    PDPool,
    HostReservation,
)
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
    AllocatorTypeChoices,
    PDAllocatorTypeChoices,
)

__all__ = (
    "ClientClassAssignmentFormMixin",
    "ClientClassDefinitionFormMixin",
    "ClientClassFormMixin",
    "PrefixFormMixin",
    "DDNSUpdateFormMixin",
    "LeaseFormMixin",
    "ChildSubnetFormMixin",
    "ChildSharedNetworkFormMixin",
    "ChildPoolFormMixin",
    "ChildPDPoolFormMixin",
    "ChildHostReservationFormMixin",
    "ChildClientClassFormMixin",
)


class ClientClassAssignmentFormMixin(forms.Form):
    assign_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Classes"),
    )


class ClientClassDefinitionFormMixin(forms.Form):
    client_class_definitions = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Class Definitions"),
    )


class ClientClassFormMixin(ClientClassDefinitionFormMixin):
    client_class = DynamicModelChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Client Class"),
    )
    require_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        quick_add=True,
        label=_("Require Client Classes"),
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


class LeaseFormMixin(forms.Form):
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
    rapid_commit = forms.NullBooleanField(
        label=_("Rapid Commit"),
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


class ChildSubnetFormMixin(forms.Form):
    child_subnets = DynamicModelMultipleChoiceField(
        queryset=Subnet.objects.all(),
        required=False,
        label=_("Subnets"),
    )


class ChildSharedNetworkFormMixin(forms.Form):
    child_shared_networks = DynamicModelMultipleChoiceField(
        queryset=SharedNetwork.objects.all(),
        required=False,
        label=_("Shared Networks"),
    )


class ChildPoolFormMixin(forms.Form):
    child_pools = DynamicModelMultipleChoiceField(
        queryset=Pool.objects.all(),
        required=False,
        label=_("Pools"),
    )


class ChildPDPoolFormMixin(forms.Form):
    child_pd_pools = DynamicModelMultipleChoiceField(
        queryset=PDPool.objects.all(),
        required=False,
        label=_("Prefix Delegation Pools"),
    )


class ChildHostReservationFormMixin(forms.Form):
    child_host_reservations = DynamicModelMultipleChoiceField(
        queryset=HostReservation.objects.all(),
        required=False,
        label=_("Host Reservations"),
    )


class ChildClientClassFormMixin(forms.Form):
    child_client_classes = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Classes"),
    )
