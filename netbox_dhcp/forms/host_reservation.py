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

from netbox_dhcp.models import HostReservation


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
        )

    fieldsets = (
        FieldSet(
            "name",
            "description",
            name=_("Host Reservation"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )


class HostReservationFilterForm(NetBoxModelFilterSetForm):
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
    )

    name = forms.CharField(
        required=False,
        label=_("Name"),
    )
    description = forms.CharField(
        required=False,
        label=_("Description"),
    )

    tag = TagFilterField(HostReservation)


class HostReservationImportForm(NetBoxModelImportForm):
    class Meta:
        model = HostReservation

        fields = (
            "name",
            "description",
            "tags",
        )


class HostReservationBulkEditForm(NetBoxModelBulkEditForm):
    model = HostReservation

    fieldsets = (
        FieldSet(
            "description",
            name=_("Host Reservation"),
        ),
    )

    nullable_fields = ("description",)

    description = forms.CharField(
        required=False,
        label=_("Description"),
    )
