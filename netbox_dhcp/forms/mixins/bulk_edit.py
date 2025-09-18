from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from ipam.models import Prefix

from netbox_dhcp.models import ClientClass

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
