from netbox.views import generic
from utilities.views import register_model_view

from netbox_dhcp.models import DDNS
from netbox_dhcp.filtersets import DDNSFilterSet
from netbox_dhcp.forms import (
    DDNSForm,
    DDNSFilterForm,
    DDNSImportForm,
    DDNSBulkEditForm,
)
from netbox_dhcp.tables import DDNSTable


__all__ = (
    "DDNSView",
    "DDNSListView",
    "DDNSEditView",
    "DDNSDeleteView",
    "DDNSBulkImportView",
    "DDNSBulkEditView",
    "DDNSBulkDeleteView",
)


@register_model_view(DDNS, "list", path="", detail=False)
class DDNSListView(generic.ObjectListView):
    queryset = DDNS.objects.all()
    table = DDNSTable
    filterset = DDNSFilterSet
    filterset_form = DDNSFilterForm


@register_model_view(DDNS)
class DDNSView(generic.ObjectView):
    queryset = DDNS.objects.all()


@register_model_view(DDNS, "add", detail=False)
@register_model_view(DDNS, "edit")
class DDNSEditView(generic.ObjectEditView):
    queryset = DDNS.objects.all()
    form = DDNSForm


@register_model_view(DDNS, "delete")
class DDNSDeleteView(generic.ObjectDeleteView):
    queryset = DDNS.objects.all()


@register_model_view(DDNS, "bulk_import", detail=False)
class DDNSBulkImportView(generic.BulkImportView):
    queryset = DDNS.objects.all()
    model_form = DDNSImportForm
    table = DDNSTable


@register_model_view(DDNS, "bulk_edit", path="edit", detail=False)
class DDNSBulkEditView(generic.BulkEditView):
    queryset = DDNS.objects.all()
    filterset = DDNSFilterSet
    table = DDNSTable
    form = DDNSBulkEditForm


@register_model_view(DDNS, "bulk_delete", path="delete", detail=False)
class DDNSBulkDeleteView(generic.BulkDeleteView):
    queryset = DDNS.objects.all()
    filterset = DDNSFilterSet
    table = DDNSTable
