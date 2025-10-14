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

from netbox_dhcp.models import Subnet
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
    LeaseImportFormMixin,
    LeaseFilterFormMixin,
    LeaseBulkEditFormMixin,
    NetworkFormMixin,
    NetworkFilterFormMixin,
    NetworkImportFormMixin,
    NetworkBulkEditFormMixin,
    ChildSubnetFormMixin,
    ChildSubnetFilterFormMixin,
    ChildSubnetImportFormMixin,
    ChildPoolFormMixin,
    ChildPoolFilterFormMixin,
    ChildPoolImportFormMixin,
    ChildPDPoolFormMixin,
    ChildPDPoolFilterFormMixin,
    ChildPDPoolImportFormMixin,
    ChildHostReservationFormMixin,
    ChildHostReservationFilterFormMixin,
    ChildHostReservationImportFormMixin,
)


__all__ = (
    "SubnetForm",
    "SubnetFilterForm",
    "SubnetImportForm",
    "SubnetBulkEditForm",
)


class SubnetForm(
    PrefixFormMixin,
    ClientClassFormMixin,
    DDNSUpdateFormMixin,
    NetworkFormMixin,
    LeaseFormMixin,
    ChildSubnetFormMixin,
    ChildPoolFormMixin,
    ChildPDPoolFormMixin,
    ChildHostReservationFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "subnet_id",
            "prefix",
            "child_subnets",
            "child_pools",
            "child_pd_pools",
            "child_host_reservations",
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
            "subnet_id",
            "prefix",
            name=_("Subnet"),
        ),
        FieldSet(
            "child_subnets",
            "child_pools",
            "child_pd_pools",
            "child_host_reservations",
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


class SubnetFilterForm(
    NetBoxDHCPFilterFormMixin,
    PrefixFilterFormMixin,
    BOOTPFilterFormMixin,
    ClientClassFilterFormMixin,
    LifetimeFilterFormMixin,
    CommonFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    LeaseFilterFormMixin,
    NetworkFilterFormMixin,
    ChildSubnetFilterFormMixin,
    ChildPoolFilterFormMixin,
    ChildPDPoolFilterFormMixin,
    ChildHostReservationFilterFormMixin,
    NetBoxModelFilterSetForm,
):
    model = Subnet

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
            "subnet_id",
            "prefix_id",
            name=_("Subnet"),
        ),
        FieldSet(
            "child_subnet_id",
            "child_pool_id",
            "child_pd_pool_id",
            "child_host_reservation_id",
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

    tag = TagFilterField(Subnet)


class SubnetImportForm(
    PrefixImportFormMixin,
    ClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    ChildSubnetImportFormMixin,
    ChildPoolImportFormMixin,
    ChildPDPoolImportFormMixin,
    ChildHostReservationImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "subnet_id",
            "prefix",
            "child_subnets",
            "child_pools",
            "child_pd_pools",
            "child_host_reservations",
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


class SubnetBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    PrefixBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    LifetimeBulkEditFormMixin,
    CommonBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    LeaseBulkEditFormMixin,
    NetworkBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Subnet

    fieldsets = (
        FieldSet(
            "description",
            "prefix",
            name=_("Subnet"),
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
