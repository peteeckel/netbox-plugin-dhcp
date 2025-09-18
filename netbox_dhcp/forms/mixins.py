from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
)

from netbox_dhcp.models import ClientClass

__all__ = (
    "BOOTPBulkEditFormMixin",
    "BOOTPFilterFormMixin",
    "ClientClassAssignmentFormMixin",
    "ClientClassAssignmentFilterFormMixin",
    "ClientClassAssignmentImportFormMixin",
    "ClientClassAssignmentBulkEditFormMixin",
    "ClientClassDefinitionFormMixin",
    "ClientClassDefinitionFilterFormMixin",
    "ClientClassDefinitionBulkEditFormMixin",
    "ClientClassDefinitionImportFormMixin",
    "ClientClassFormMixin",
    "ClientClassFilterFormMixin",
    "ClientClassImportFormMixin",
    "ClientClassBulkEditFormMixin",
    "CommonFilterFormMixin",
    "CommonBulkEditFormMixin",
    "NetBoxDHCPFilterFormMixin",
    "NetBoxDHCPBulkEditFormMixin",
    "OfferLifetimeFilterFormMixin",
    "OfferLifetimeBulkEditFormMixin",
    "PreferredLifetimeFilterFormMixin",
    "PreferredLifetimeBulkEditFormMixin",
    "ValidLifetimeFilterFormMixin",
    "ValidLifetimeBulkEditFormMixin",
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


class ValidLifetimeFilterFormMixin(forms.Form):
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


class OfferLifetimeFilterFormMixin(forms.Form):
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Offer Lifetime"),
    )


class PreferredLifetimeFilterFormMixin(forms.Form):
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


class ClientClassAssignmentImportFormMixin(forms.Form):
    assign_client_classes = CSVModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Assign Client Classes"),
    )


class ClientClassDefinitionImportFormMixin(forms.Form):
    client_class_definitions = CSVModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Client Class Definitions"),
    )


class ClientClassImportFormMixin(ClientClassDefinitionImportFormMixin):
    client_class = CSVModelChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Client Class"),
    )
    required_client_classes = CSVModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Required Client Classes"),
    )
    evaluate_additional_classes = CSVModelMultipleChoiceField(
        queryset=ClientClass.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        label=_("Required Client Classes"),
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


class ValidLifetimeBulkEditFormMixin(forms.Form):
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


class OfferLifetimeBulkEditFormMixin(forms.Form):
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
        label=_("Offer Lifetime"),
    )


class PreferredLifetimeBulkEditFormMixin(forms.Form):
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
