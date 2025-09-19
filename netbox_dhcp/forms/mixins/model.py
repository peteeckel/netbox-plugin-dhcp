from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)

from ipam.models import Prefix

from netbox_dhcp.models import ClientClass
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


class PrefixFormMixin(forms.Form):
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=True,
        selector=True,
        quick_add=True,
        label=_("Prefix"),
    )


class DDNSUpdateFormMixin(forms.Form):
    ddns_replace_client_name = forms.ChoiceField(
        choices=DDNSReplaceClientNameChoices,
        required=True,
        label=_("Replace Client Name"),
    )
    ddns_conflict_resolution_mode = forms.ChoiceField(
        choices=DDNSConflictResolutionModeChoices,
        required=True,
        label=_("Conflict Resolution Mode"),
    )
    ddns_ttl_percent = forms.DecimalField(
        label=_("TTL Percent"),
        help_text=_("Enter a decimal value between 0.000 and 1.000"),
        min_value=0.0,
        max_value=1.0,
        max_digits=4,
        decimal_places=3,
        required=False,
    )


class LeaseFormMixin(forms.Form):
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
        label=_("T2"),
        help_text=_("Enter a decimal value between 0.000 and 1.000"),
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
    adaptive_lease_time_threshold = forms.DecimalField(
        label=_("Adaptive Lease Time Threshold"),
        help_text=_("Enter a decimal value between 0.00 and 1.00"),
        max_digits=3,
        decimal_places=2,
        min_value=0.0,
        max_value=1.0,
        required=False,
    )
    allocator = forms.ChoiceField(
        choices=AllocatorTypeChoices,
        required=True,
        label=_("Allocator"),
    )
    pd_allocator = forms.ChoiceField(
        choices=PDAllocatorTypeChoices,
        required=True,
        label=_("Prefix Delegation Allocator"),
    )
