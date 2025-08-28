from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import PDPool
from netbox_dhcp.filtersets import PDPoolFilterSet
from netbox_dhcp.forms import (
    PDPoolForm,
    PDPoolFilterForm,
    PDPoolImportForm,
    PDPoolBulkEditForm,
)
from netbox_dhcp.tables import PDPoolTable


__all__ = (
    "PDPoolView",
    "PDPoolListView",
    "PDPoolEditView",
    "PDPoolDeleteView",
    "PDPoolBulkImportView",
    "PDPoolBulkEditView",
    "PDPoolBulkDeleteView",
)


@register_model_view(PDPool, "list", path="", detail=False)
class PDPoolListView(generic.ObjectListView):
    queryset = PDPool.objects.all()
    table = PDPoolTable
    filterset = PDPoolFilterSet
    filterset_form = PDPoolFilterForm


@register_model_view(PDPool)
class PDPoolView(generic.ObjectView):
    queryset = PDPool.objects.all()


@register_model_view(PDPool, "add", detail=False)
@register_model_view(PDPool, "edit")
class PDPoolEditView(generic.ObjectEditView):
    queryset = PDPool.objects.all()
    form = PDPoolForm


@register_model_view(PDPool, "delete")
class PDPoolDeleteView(generic.ObjectDeleteView):
    queryset = PDPool.objects.all()


@register_model_view(PDPool, "bulk_import", detail=False)
class PDPoolBulkImportView(generic.BulkImportView):
    queryset = PDPool.objects.all()
    model_form = PDPoolImportForm
    table = PDPoolTable


@register_model_view(PDPool, "bulk_edit", path="edit", detail=False)
class PDPoolBulkEditView(generic.BulkEditView):
    queryset = PDPool.objects.all()
    filterset = PDPoolFilterSet
    table = PDPoolTable
    form = PDPoolBulkEditForm


@register_model_view(PDPool, "bulk_delete", path="delete", detail=False)
class PDPoolBulkDeleteView(generic.BulkDeleteView):
    queryset = PDPool.objects.all()
    filterset = PDPoolFilterSet
    table = PDPoolTable
