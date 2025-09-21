from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import (
    CSVChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
)

from ipam.models import Prefix

from netbox_dhcp.models import ClientClass, Subnet, Pool, PDPool, HostReservation
from netbox_dhcp.choices import (
    DDNSReplaceClientNameChoices,
    DDNSConflictResolutionModeChoices,
    AllocatorTypeChoices,
    PDAllocatorTypeChoices,
)

__all__ = (
    "ClientClassAssignmentImportFormMixin",
    "ClientClassDefinitionImportFormMixin",
    "ClientClassImportFormMixin",
    "PrefixImportFormMixin",
    "DDNSUpdateImportFormMixin",
    "LeaseImportFormMixin",
    "ChildSubnetImportFormMixin",
    "ChildPoolImportFormMixin",
    "ChildPDPoolImportFormMixin",
    "ChildHostReservationImportFormMixin",
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


class LeaseImportFormMixin(forms.Form):
    allocator = CSVChoiceField(
        choices=AllocatorTypeChoices,
        required=False,
        label=_("Allocator"),
    )
    pd_allocator = CSVChoiceField(
        choices=PDAllocatorTypeChoices,
        required=False,
        label=_("Prefix Delegation Allocator"),
    )


class ChildSubnetImportFormMixin(forms.Form):
    child_subnets = CSVModelMultipleChoiceField(
        queryset=Subnet.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Subnet %(value)s not found"),
        },
        label=_("Subnets"),
    )


class ChildPoolImportFormMixin(forms.Form):
    child_pools = CSVModelMultipleChoiceField(
        queryset=Pool.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Pool %(value)s not found"),
        },
        label=_("Pools"),
    )


class ChildPDPoolImportFormMixin(forms.Form):
    child_pd_pools = CSVModelMultipleChoiceField(
        queryset=PDPool.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Prefix Delegation Pool %(value)s not found"),
        },
        label=_("Prefix Delegation Pools"),
    )


class ChildHostReservationImportFormMixin(forms.Form):
    child_host_reservations = CSVModelMultipleChoiceField(
        queryset=HostReservation.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("Host Reservation %(value)s not found"),
        },
        label=_("Host Reservations"),
    )
