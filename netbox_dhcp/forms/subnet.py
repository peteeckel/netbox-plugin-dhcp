from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField
from utilities.forms.rendering import FieldSet, TabbedGroups
from utilities.forms import add_blank_choice
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import Subnet
from .mixins import (
    NetBoxDHCPFilterFormMixin,
    NetBoxDHCPBulkEditFormMixin,
    DHCPServerFormMixin,
    DHCPServerFilterFormMixin,
    DHCPServerImportFormMixin,
    DHCPServerBulkEditFormMixin,
    SharedNetworkFormMixin,
    SharedNetworkFilterFormMixin,
    SharedNetworkImportFormMixin,
    SharedNetworkBulkEditFormMixin,
    ClientClassFormMixin,
    ClientClassFilterFormMixin,
    ClientClassImportFormMixin,
    ClientClassBulkEditFormMixin,
    EvaluateClientClassBulkEditFormMixin,
    EvaluateClientClassFilterFormMixin,
    EvaluateClientClassFormMixin,
    EvaluateClientClassImportFormMixin,
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
    ChildPDPoolFilterFormMixin,
    ChildPoolFilterFormMixin,
    ChildHostReservationFilterFormMixin,
)


__all__ = (
    "SubnetForm",
    "SubnetFilterForm",
    "SubnetImportForm",
    "SubnetBulkEditForm",
)


class SubnetForm(
    DHCPServerFormMixin,
    SharedNetworkFormMixin,
    PrefixFormMixin,
    ClientClassFormMixin,
    EvaluateClientClassFormMixin,
    DDNSUpdateFormMixin,
    NetworkFormMixin,
    LeaseFormMixin,
    NetBoxModelForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "subnet_id",
            *DHCPServerFormMixin.FIELDS,
            *SharedNetworkFormMixin.FIELDS,
            "prefix",
            *NetworkFormMixin.FIELDS,
            *ClientClassFormMixin.FIELDS,
            *EvaluateClientClassFormMixin.FIELDS,
            *BOOTPFormMixin.FIELDS,
            *LifetimeFormMixin.FIELDS,
            *LeaseFormMixin.FIELDS,
            *DDNSUpdateFormMixin.FIELDS,
            "tags",
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            "subnet_id",
            TabbedGroups(
                FieldSet(
                    *DHCPServerFormMixin.FIELDS,
                    name=_("DHCP Server"),
                ),
                FieldSet(
                    *SharedNetworkFormMixin.FIELDS,
                    name=_("Shared Network"),
                ),
            ),
            "prefix",
            name=_("Subnet"),
        ),
        FieldSet(
            *ClientClassFormMixin.FIELDS,
            *EvaluateClientClassFormMixin.FIELDS,
            name=_("Client Classes"),
        ),
        NetworkFormMixin.FIELDSET,
        BOOTPFormMixin.FIELDSET,
        LifetimeFormMixin.FIELDSET,
        LeaseFormMixin.FIELDSET,
        DDNSUpdateFormMixin.FIELDSET,
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class SubnetFilterForm(
    NetBoxDHCPFilterFormMixin,
    DHCPServerFilterFormMixin,
    SharedNetworkFilterFormMixin,
    PrefixFilterFormMixin,
    BOOTPFilterFormMixin,
    ClientClassFilterFormMixin,
    EvaluateClientClassFilterFormMixin,
    LifetimeFilterFormMixin,
    DDNSUpdateFilterFormMixin,
    LeaseFilterFormMixin,
    NetworkFilterFormMixin,
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
            *DHCPServerFilterFormMixin.FIELDS,
            *SharedNetworkFilterFormMixin.FIELDS,
            "prefix_id",
            name=_("Subnet"),
        ),
        FieldSet(
            "child_pool_id",
            "child_pd_pool_id",
            "child_host_reservation_id",
            name=_("Child Objects"),
        ),
        FieldSet(
            *ClientClassFilterFormMixin.FIELDS,
            *EvaluateClientClassFilterFormMixin.FIELDS,
            name=_("Client Classes"),
        ),
        NetworkFilterFormMixin.FIELDSET,
        BOOTPFilterFormMixin.FIELDSET,
        LifetimeFilterFormMixin.FIELDSET,
        LeaseFilterFormMixin.FIELDSET,
        DDNSUpdateFilterFormMixin.FIELDSET,
    )

    family = forms.ChoiceField(
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
        label=_("Address Family"),
    )

    tag = TagFilterField(Subnet)


class SubnetImportForm(
    DHCPServerImportFormMixin,
    SharedNetworkImportFormMixin,
    PrefixImportFormMixin,
    ClientClassImportFormMixin,
    EvaluateClientClassImportFormMixin,
    DDNSUpdateImportFormMixin,
    NetBoxModelImportForm,
):
    class Meta:
        model = Subnet

        fields = (
            "name",
            "description",
            "subnet_id",
            *DHCPServerImportFormMixin.FIELDS,
            *SharedNetworkImportFormMixin.FIELDS,
            "prefix",
            *NetworkImportFormMixin.FIELDS,
            *ClientClassImportFormMixin.FIELDS,
            *EvaluateClientClassImportFormMixin.FIELDS,
            *BOOTPImportFormMixin.FIELDS,
            *LifetimeImportFormMixin.FIELDS,
            *LeaseImportFormMixin.FIELDS,
            *DDNSUpdateImportFormMixin.FIELDS,
            "tags",
        )


class SubnetBulkEditForm(
    NetBoxDHCPBulkEditFormMixin,
    DHCPServerBulkEditFormMixin,
    SharedNetworkBulkEditFormMixin,
    BOOTPBulkEditFormMixin,
    ClientClassBulkEditFormMixin,
    EvaluateClientClassBulkEditFormMixin,
    LifetimeBulkEditFormMixin,
    DDNSUpdateBulkEditFormMixin,
    LeaseBulkEditFormMixin,
    NetworkBulkEditFormMixin,
    NetBoxModelBulkEditForm,
):
    model = Subnet

    fieldsets = (
        FieldSet(
            "description",
            TabbedGroups(
                FieldSet(
                    *DHCPServerBulkEditFormMixin.FIELDS,
                    name=_("DHCP Server"),
                ),
                FieldSet(
                    *SharedNetworkBulkEditFormMixin.FIELDS,
                    name=_("Shared Network"),
                ),
            ),
            name=_("Subnet"),
        ),
        FieldSet(
            *ClientClassBulkEditFormMixin.FIELDS,
            *EvaluateClientClassBulkEditFormMixin.FIELDS,
            name=_("Client Classes"),
        ),
        NetworkBulkEditFormMixin.FIELDSET,
        BOOTPBulkEditFormMixin.FIELDSET,
        LifetimeBulkEditFormMixin.FIELDSET,
        LeaseBulkEditFormMixin.FIELDSET,
        DDNSUpdateBulkEditFormMixin.FIELDSET,
    )

    nullable_fields = (
        "description",
        *DHCPServerBulkEditFormMixin.NULLABLE_FIELDS,
        *SharedNetworkBulkEditFormMixin.NULLABLE_FIELDS,
        *NetworkBulkEditFormMixin.NULLABLE_FIELDS,
        *ClientClassBulkEditFormMixin.NULLABLE_FIELDS,
        *EvaluateClientClassBulkEditFormMixin.NULLABLE_FIELDS,
        *BOOTPBulkEditFormMixin.NULLABLE_FIELDS,
        *LifetimeBulkEditFormMixin.NULLABLE_FIELDS,
        *LeaseBulkEditFormMixin.NULLABLE_FIELDS,
        *DDNSUpdateBulkEditFormMixin.NULLABLE_FIELDS,
    )
