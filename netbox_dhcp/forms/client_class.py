from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES

from netbox_dhcp.models import ClientClass


__all__ = (
    "ClientClassForm",
    "ClientClassFilterForm",
    "ClientClassImportForm",
    "ClientClassBulkEditForm",
)


class ClientClassForm(NetBoxModelForm):
    class Meta:
        model = ClientClass

        fields = (
            "name",
            "description",
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "user_context",
            "comment",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "comment",
            name=_("Client Class"),
        ),
        FieldSet(
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            name=_("Evaluation"),
        ),
        FieldSet(
            "user_context",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            name=_("Common"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            name=_("IPv4"),
        ),
        FieldSet(
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            name=_("IPv6"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class ClientClassFilterForm(NetBoxModelFilterSetForm):
    model = ClientClass

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "comment",
            name=_("Client Class"),
        ),
        FieldSet(
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            name=_("Evaluation"),
        ),
        FieldSet(
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            name=_("Common"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            name=_("IPv4"),
        ),
        FieldSet(
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            name=_("IPv6"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    test = forms.CharField(
        required=False,
        label=_("Test"),
    )
    only_if_required = forms.NullBooleanField(
        required=False,
        label=_("Only if required"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    only_in_additional_list = forms.NullBooleanField(
        required=False,
        label=_("Only in additional list"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    test = forms.CharField(
        required=False,
        label=_("Test"),
    )
    valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    min_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    max_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
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
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    min_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    max_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )

    tag = TagFilterField(ClientClass)


class ClientClassImportForm(NetBoxModelImportForm):
    class Meta:
        model = ClientClass

        fields = (
            "name",
            "description",
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "user_context",
            "comment",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            "tags",
        )


class ClientClassBulkEditForm(NetBoxModelBulkEditForm):
    model = ClientClass

    fieldsets = (
        FieldSet(
            "description",
            "comment",
            name=_("Client Class"),
        ),
        FieldSet(
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            name=_("Evaluation"),
        ),
        FieldSet(
            "user_context",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            name=_("Common"),
        ),
        FieldSet(
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            name=_("IPv4"),
        ),
        FieldSet(
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
            name=_("IPv6"),
        ),
    )

    nullable_fields = (
        "description",
        "comment",
        "test",
        "template_test",
        "user_context",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "offer_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
    )

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
    test = forms.CharField(
        required=False,
        max_length=255,
        label=_("Test"),
    )
    template_test = forms.CharField(
        required=False,
        max_length=255,
        label=_("Template Test"),
    )
    only_if_required = forms.NullBooleanField(
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        label=_("Only if required"),
    )
    only_in_additional_list = forms.NullBooleanField(
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        label=_("Only in additional list"),
    )
    offer_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    min_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    max_valid_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
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
    preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    min_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
    max_preferred_lifetime = forms.IntegerField(
        required=False,
        min_value=1,
    )
