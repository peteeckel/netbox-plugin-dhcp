from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import HostReservation
from netbox_dhcp.filtersets import HostReservationFilterSet
from netbox_dhcp.forms import (
    HostReservationForm,
    HostReservationFilterForm,
    HostReservationImportForm,
    HostReservationBulkEditForm,
)
from netbox_dhcp.tables import HostReservationTable


__all__ = (
    "HostReservationView",
    "HostReservationListView",
    "HostReservationEditView",
    "HostReservationDeleteView",
    "HostReservationBulkImportView",
    "HostReservationBulkEditView",
    "HostReservationBulkDeleteView",
)


@register_model_view(HostReservation, "list", path="", detail=False)
class HostReservationListView(generic.ObjectListView):
    queryset = HostReservation.objects.all()
    table = HostReservationTable
    filterset = HostReservationFilterSet
    filterset_form = HostReservationFilterForm


@register_model_view(HostReservation)
class HostReservationView(generic.ObjectView):
    queryset = HostReservation.objects.all()


@register_model_view(HostReservation, "add", detail=False)
@register_model_view(HostReservation, "edit")
class HostReservationEditView(generic.ObjectEditView):
    queryset = HostReservation.objects.all()
    form = HostReservationForm


@register_model_view(HostReservation, "delete")
class HostReservationDeleteView(generic.ObjectDeleteView):
    queryset = HostReservation.objects.all()


@register_model_view(HostReservation, "bulk_import", detail=False)
class HostReservationBulkImportView(generic.BulkImportView):
    queryset = HostReservation.objects.all()
    model_form = HostReservationImportForm
    table = HostReservationTable


@register_model_view(HostReservation, "bulk_edit", path="edit", detail=False)
class HostReservationBulkEditView(generic.BulkEditView):
    queryset = HostReservation.objects.all()
    filterset = HostReservationFilterSet
    table = HostReservationTable
    form = HostReservationBulkEditForm


@register_model_view(HostReservation, "bulk_delete", path="delete", detail=False)
class HostReservationBulkDeleteView(generic.BulkDeleteView):
    queryset = HostReservation.objects.all()
    filterset = HostReservationFilterSet
    table = HostReservationTable
