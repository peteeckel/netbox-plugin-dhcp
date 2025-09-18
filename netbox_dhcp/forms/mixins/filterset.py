from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelMultipleChoiceField,
)

from ipam.models import Prefix

from netbox_dhcp.models import ClientClass
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
)

__all__ = (
    "BOOTPFilterFormMixin",
    "ClientClassAssignmentFilterFormMixin",
    "ClientClassDefinitionFilterFormMixin",
    "ClientClassFilterFormMixin",
    "CommonFilterFormMixin",
    "NetBoxDHCPFilterFormMixin",
    "OfferLifetimeFilterFormMixin",
    "LifetimeFilterFormMixin",
    "PrefixFilterFormMixin",
    "DDNSUpdateFilterFormMixin",
)


class NetBoxDHCPFilterFormMixin(forms.Form):
    name = forms.CharField(
        required=False,
        label=_("Name"),
    )
    description = forms.CharField(
        required=False,
        label=_("Description"),
    )


class BOOTPFilterFormMixin(forms.Form):
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


class OfferLifetimeFilterFormMixin(forms.Form):
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Offer Lifetime"),
    )


class LifetimeFilterFormMixin(OfferLifetimeFilterFormMixin):
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


class ClientClassAssignmentFilterFormMixin(forms.Form):
    assign_client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Classes"),
    )


class ClientClassDefinitionFilterFormMixin(forms.Form):
    network_client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Class Definitions"),
    )


class ClientClassFilterFormMixin(ClientClassDefinitionFilterFormMixin):
    client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Client Class"),
    )
    required_client_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Required Client Classes"),
    )
    evaluate_additional_class_id = DynamicModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        label=_("Evaluate Additional Classes"),
    )


class CommonFilterFormMixin(forms.Form):
    # TODO: option_data_list
    comment = forms.CharField(
        required=False,
        label=_("Comment"),
    )


class PrefixFilterFormMixin(forms.Form):
    prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
        label=_("Prefix"),
    )


class DDNSUpdateFilterFormMixin(forms.Form):
    ddns_replace_client_name = forms.ChoiceField(
        choices=DDNSReplaceClientNameChoices,
        required=False,
        label=_("Replace Client Name"),
    )
    ddns_conflict_resolution_mode = forms.ChoiceField(
        choices=DDNSConflictResolutionModeChoices,
        required=False,
        label=_("Conflict Resolution Mode"),
    )
