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
from .mixins import (
    BOOTPFormMixin,
    BOOTPFilterFormMixin,
    BOOTPImportFormMixin,
    BOOTPBulkEditFormMixin,
    LifetimeFormMixin,
    LifetimeFilterFormMixin,
    LifetimeImportFormMixin,
    LifetimeBulkEditFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    NetBoxDHCPFilterFormMixin,
)


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
            "only_in_additional_list",
            *BOOTPFormMixin.FIELDS,
            *LifetimeFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "test",
            "template_test",
            "only_in_additional_list",
            name=_("Client Class"),
        ),
        BOOTPFormMixin.FIELDSET,
        LifetimeFormMixin.FIELDSET,
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    only_in_additional_list = forms.NullBooleanField(
        required=False,
        label=_("Only in additional list"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )


class ClientClassFilterForm(
    NetBoxDHCPFilterFormMixin,
    BOOTPFilterFormMixin,
    LifetimeFilterFormMixin,
    NetBoxModelFilterSetForm,
):
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
            "test",
            "template_test",
            "only_in_additional_list",
            name=_("Client Class"),
        ),
        BOOTPFilterFormMixin.FIELDSET,
        LifetimeFilterFormMixin.FIELDSET,
        FieldSet(
            "comment",
            name=_("Assignment"),
        ),
    )

    test = forms.CharField(
        required=False,
        label=_("Test"),
    )
    template_test = forms.CharField(
        required=False,
        label=_("Template Test"),
    )
    only_in_additional_list = forms.NullBooleanField(
        required=False,
        label=_("Only in additional list"),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
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
            "only_in_additional_list",
            *BOOTPImportFormMixin.FIELDS,
            *LifetimeImportFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )


class ClientClassBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    LifetimeBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = ClientClass

    fieldsets = (
        FieldSet(
            "description",
            name=_("Client Class"),
        ),
        FieldSet(
            "test",
            "template_test",
            "only_in_additional_list",
            name=_("Selection"),
        ),
        BOOTPBulkEditFormMixin.FIELDSET,
        LifetimeBulkEditFormMixin.FIELDSET,
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
    )

    nullable_fields = (
        "description",
        "comment",
        "test",
        "template_test",
        *BOOTPBulkEditFormMixin.NULLABLE_FIELDS,
        *LifetimeBulkEditFormMixin.NULLABLE_FIELDS,
        "user_context",
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
    only_in_additional_list = forms.NullBooleanField(
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        label=_("Only in additional list"),
    )
