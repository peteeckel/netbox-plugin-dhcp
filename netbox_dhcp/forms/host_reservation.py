from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import (
    TagFilterField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet

from ipam.models import IPAddress, Prefix
from ipam.choices import IPAddressFamilyChoices
from dcim.models import MACAddress

from netbox_dhcp.models import HostReservation

from .mixins import (
    BOOTPBulkEditFormMixin,
    BOOTPFilterFormMixin,
    ClientClassAssignmentBulkEditFormMixin,
    ClientClassAssignmentFilterFormMixin,
    ClientClassAssignmentImportFormMixin,
    CommonBulkEditFormMixin,
    CommonFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetBoxDHCPFilterFormMixin,
)


__all__ = (
    "HostReservationForm",
    "HostReservationFilterForm",
    "HostReservationImportForm",
    "HostReservationBulkEditForm",
)


class HostReservationForm(NetBoxModelForm):
    class Meta:
        model = HostReservation

        fields = (
            "name",
            "description",
            "duid",
            "hw_address",
            "circuit_id",
            "client_id",
            "flex_id",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "hostname",
            "ipv4_address",
            "ipv6_addresses",
            "ipv6_prefixes",
            "excluded_ipv6_prefixes",
            "user_context",
            "comment",
            "assign_client_classes",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Host Reservation"),
        ),
        FieldSet(
            "duid",
            "hw_address",
            "circuit_id",
            "client_id",
            "flex_id",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "ipv4_address",
            "ipv6_addresses",
            "ipv6_prefixes",
            "excluded_ipv6_prefixes",
            "hostname",
            "user_context",
            "comment",
            "assign_client_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    hw_address = DynamicModelChoiceField(
        queryset=MACAddress.objects.all(),
        required=False,
        quick_add=True,
        selector=True,
        label=_("Hardware Address"),
    )

    ipv4_address = DynamicModelChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_4
        ),
        query_params={"family": IPAddressFamilyChoices.FAMILY_4},
        required=False,
        selector=True,
        label=_("IPv4 Address"),
    )
    ipv6_addresses = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_6
        ),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("IPv6 Addresses"),
    )
    ipv6_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        context={
            "depth": None,
        },
        required=False,
        selector=True,
        label=_("IPv6 Prefixes"),
    )
    excluded_ipv6_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        context={
            "depth": None,
        },
        required=False,
        selector=True,
        label=_("Excluded IPv6 Prefixes"),
    )


class HostReservationFilterForm(
    NetBoxDHCPFilterFormMixin,
    BOOTPFilterFormMixin,
    ClientClassAssignmentFilterFormMixin,
    CommonFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = HostReservation

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            name=_("Host Reservation"),
        ),
        FieldSet(
            "duid",
            "hw_address_id",
            "circuit_id",
            "client_id",
            "flex_id",
            "client_class_id",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "ipv4_address_id",
            "ipv6_address_id",
            "ipv6_prefix_id",
            "excluded_ipv6_prefix_id",
            "hostname",
            "comment",
            "assign_client_classes",
            name=_("Assignment"),
        ),
    )

    duid = forms.CharField(
        required=False,
        label=_("DUID"),
    )
    hw_address_id = DynamicModelMultipleChoiceField(
        queryset=MACAddress.objects.all(),
        required=False,
        selector=True,
        label=_("Hardware Address"),
    )
    circuit_id = forms.CharField(
        required=False,
        label=_("Circuit ID"),
    )
    client_id = forms.CharField(
        required=False,
        label=_("Client ID"),
    )
    flex_id = forms.CharField(
        required=False,
        label=_("Flex ID"),
    )

    hostname = forms.CharField(
        required=False,
        label=_("Host Name"),
    )
    ipv4_address_id = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_4
        ),
        query_params={"family": IPAddressFamilyChoices.FAMILY_4},
        required=False,
        selector=True,
        label=_("IPv4 Address"),
    )
    ipv6_address_id = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_6
        ),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("IPv6 Address"),
    )
    ipv6_prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("IPv6 Prefix"),
    )
    excluded_ipv6_prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("Excluded IPv6 Prefix"),
    )

    tag = TagFilterField(HostReservation)


class HostReservationImportForm(
    ClientClassAssignmentImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = HostReservation

        fields = (
            "name",
            "description",
            "duid",
            "hw_address",
            "circuit_id",
            "client_id",
            "flex_id",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "hostname",
            "ipv4_address",
            "ipv6_addresses",
            "ipv6_prefixes",
            "excluded_ipv6_prefixes",
            "user_context",
            "comment",
            "assign_client_classes",
            "tags",
        )

    hw_address = CSVModelChoiceField(
        queryset=MACAddress.objects.all(),
        required=False,
        to_field_name="mac_address",
        help_text=_("Hardware address in xx:xx:xx:xx:xx:xx format"),
        error_messages={
            "invalid_choice": _("Hardware address %(value)s not found"),
        },
        label=_("Hardware Address"),
    )

    ipv4_address = CSVModelChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_4
        ),
        required=False,
        to_field_name="address",
        error_messages={
            "invalid_choice": _("IPv4 address %(value)s not found"),
        },
        label=_("IPv4 Address"),
    )
    ipv6_addresses = CSVModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(
            address__family=IPAddressFamilyChoices.FAMILY_6
        ),
        required=False,
        to_field_name="address",
        error_messages={
            "invalid_choice": _("IPv6 address %(value)s not found"),
        },
        label=_("IPv6 Addresses"),
    )
    ipv6_prefixes = CSVModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        required=False,
        to_field_name="prefix",
        error_messages={
            "invalid_choice": _("IPv6 prefix %(value)s not found"),
        },
        label=_("IPv6 Prefixes"),
    )
    excluded_ipv6_prefixes = CSVModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        required=False,
        to_field_name="prefix",
        error_messages={
            "invalid_choice": _("IPv6 prefix %(value)s not found"),
        },
        label=_("Excluded IPv6 Prefixes"),
    )


class HostReservationBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    CommonBulkEditFormMixin,
    ClientClassAssignmentBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = HostReservation

    fieldsets = (
        FieldSet(
            "description",
            name=_("Host Reservation"),
        ),
        FieldSet(
            "circuit_id",
            "flex_id",
            name=_("Selection"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            name=_("BOOTP"),
        ),
        FieldSet(
            "ipv6_prefixes",
            "excluded_ipv6_prefixes",
            "user_context",
            "comment",
            "assign_client_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    nullable_fields = (
        "description",
        "flex_id",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "ipv6_prefixes",
        "excluded_ipv6_prefixes",
        "user_context",
        "comment",
        "assign_client_classes",
    )

    circuit_id = forms.CharField(
        required=False,
        label=_("Circuit ID"),
    )
    flex_id = forms.CharField(
        required=False,
        label=_("Flex ID"),
    )

    ipv6_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("IPv6 Prefixes"),
    )
    excluded_ipv6_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.filter(prefix__family=IPAddressFamilyChoices.FAMILY_6),
        query_params={"family": IPAddressFamilyChoices.FAMILY_6},
        required=False,
        selector=True,
        label=_("Excluded IPv6 Prefixes"),
    )
