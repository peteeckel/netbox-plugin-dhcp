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
from utilities.forms import add_blank_choice
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import SharedNetwork
from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    CommonFilterFormMixin,
    CommonBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
    LifetimeFormMixin,
    LifetimeFilterFormMixin,
    LifetimeImportFormMixin,
    LifetimeBulkEditFormMixin,
    BOOTPFormMixin,
    BOOTPFilterFormMixin,
    BOOTPImportFormMixin,
    BOOTPBulkEditFormMixin,
    PrefixFormMixin,
    PrefixFilterFormMixin,
    PrefixImportFormMixin,
    PrefixBulkEditFormMixin,
    DDNSUpdateFormMixin,
    DDNSUpdateFilterFormMixin,
    DDNSUpdateImportFormMixin,
    DDNSUpdateBulkEditFormMixin,
    LeaseFormMixin,
    LeaseFilterFormMixin,
    LeaseImportFormMixin,
    LeaseBulkEditFormMixin,
    NetworkFormMixin,
    NetworkFilterFormMixin,
    NetworkImportFormMixin,
    NetworkBulkEditFormMixin,
    ChildSubnetFormMixin,
    ChildSubnetFilterFormMixin,
    ChildSubnetImportFormMixin,
    ChildSubnetBulkEditFormMixin,
)


__all__ = (
    "SharedNetworkForm",
    "SharedNetworkFilterForm",
    "SharedNetworkImportForm",
    "SharedNetworkBulkEditForm",
)


class SharedNetworkForm(
    PrefixFormMixin,
    ClientClassFormMixin,
    DDNSUpdateFormMixin,
    LeaseFormMixin,
    ChildSubnetFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "prefix",
            "child_subnets",
            *NetworkFormMixin.FIELDS,
            *ClientClassFormMixin.FIELDS,
            *BOOTPFormMixin.FIELDS,
            *LifetimeFormMixin.FIELDS,
            *LeaseFormMixin.FIELDS,
            *DDNSUpdateFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "prefix",
            name=_("Shared Network"),
        ),
        FieldSet(
            "child_subnets",
            name=_("Child Objects"),
        ),
        NetworkFormMixin.FIELDSET,
        ClientClassFormMixin.FIELDSET,
        BOOTPFormMixin.FIELDSET,
        LifetimeFormMixin.FIELDSET,
        LeaseFormMixin.FIELDSET,
        DDNSUpdateFormMixin.FIELDSET,
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


class SharedNetworkFilterForm(
    NetBoxDHCPFilterFormMixin,
    PrefixFilterFormMixin,
    BOOTPFilterFormMixin,
    ClientClassFilterFormMixin,
    CommonFilterFormMixin,
    LifetimeFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    LeaseFilterFormMixin,
    NetworkFilterFormMixin,
    ChildSubnetFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = SharedNetwork

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "family",
            "prefix_id",
            name=_("Shared Network"),
        ),
        FieldSet(
            "child_subnet_id",
            name=_("Child Objects"),
        ),
        NetworkFilterFormMixin.FIELDSET,
        ClientClassFilterFormMixin.FIELDSET,
        BOOTPFilterFormMixin.FIELDSET,
        LifetimeFilterFormMixin.FIELDSET,
        LeaseFilterFormMixin.FIELDSET,
        DDNSUpdateFilterFormMixin.FIELDSET,
        FieldSet(
            "comment",
            name=_("Assignment"),
        ),
    )

    family = forms.ChoiceField(
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
        label=_("Address Family"),
    )

    tag = TagFilterField(SharedNetwork)


class SharedNetworkImportForm(
    PrefixImportFormMixin,
    ClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    LeaseImportFormMixin,
    ChildSubnetImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = SharedNetwork

        fields = (
            "name",
            "description",
            "prefix",
            "child_subnets",
            *NetworkImportFormMixin.FIELDS,
            *ClientClassImportFormMixin.FIELDS,
            *BOOTPImportFormMixin.FIELDS,
            *LifetimeImportFormMixin.FIELDS,
            *LeaseImportFormMixin.FIELDS,
            *DDNSUpdateImportFormMixin.FIELDS,
            "user_context",
            "comment",
            "tags",
        )


class SharedNetworkBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    PrefixBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    LifetimeBulkEditFormMixin,
    CommonBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    LeaseBulkEditFormMixin,
    NetworkBulkEditFormMixin,
    ChildSubnetBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = SharedNetwork

    fieldsets = (
        FieldSet(
            "description",
            "prefix",
            name=_("Shared Network"),
        ),
        FieldSet(
            "child_subnets",
            name=_("Child Objects"),
        ),
        NetworkBulkEditFormMixin.FIELDSET,
        ClientClassBulkEditFormMixin.FIELDSET,
        BOOTPBulkEditFormMixin.FIELDSET,
        LifetimeBulkEditFormMixin.FIELDSET,
        LeaseBulkEditFormMixin.FIELDSET,
        DDNSUpdateBulkEditFormMixin.FIELDSET,
        FieldSet(
            "user_context",
            "comment",
            name=_("Assignment"),
        ),
    )

    nullable_fields = (
        "description",
        *NetworkBulkEditFormMixin.NULLABLE_FIELDS,
        *ClientClassBulkEditFormMixin.NULLABLE_FIELDS,
        *BOOTPBulkEditFormMixin.NULLABLE_FIELDS,
        *LifetimeBulkEditFormMixin.NULLABLE_FIELDS,
        *LeaseBulkEditFormMixin.NULLABLE_FIELDS,
        *DDNSUpdateBulkEditFormMixin.NULLABLE_FIELDS,
        "user_context",
        "comment",
    )
