from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    CSVChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
)

from ipam.models import Prefix

from netbox_dhcp.models import ClientClass
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
)

__all__ = (
    "ClientClassAssignmentImportFormMixin",
    "ClientClassDefinitionImportFormMixin",
    "ClientClassImportFormMixin",
    "PrefixImportFormMixin",
    "DDNSUpdateImportFormMixin",
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


class PrefixImportFormMixin(forms.Form):
    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.all(),
        required=True,
        to_field_name="prefix",
        label=_("Prefix"),
    )


class DDNSUpdateImportFormMixin(forms.Form):
    ddns_replace_client_name = CSVChoiceField(
        choices=DDNSReplaceClientNameChoices,
        required=False,
        label=_("Replace Client Name"),
    )
    ddns_conflict_resolution_mode = CSVChoiceField(
        choices=DDNSConflictResolutionModeChoices,
        required=False,
        label=_("Conflict Resolution Mode"),
    )
