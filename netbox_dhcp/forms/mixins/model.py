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
)

__all__ = (
    "ClientClassAssignmentFormMixin",
    "ClientClassDefinitionFormMixin",
    "ClientClassFormMixin",
    "PrefixFormMixin",
    "DDNSUpdateFormMixin",
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
