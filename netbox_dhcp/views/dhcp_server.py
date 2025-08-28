from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import DHCPServer
from netbox_dhcp.filtersets import DHCPServerFilterSet
from netbox_dhcp.forms import (
    DHCPServerForm,
    DHCPServerFilterForm,
    DHCPServerImportForm,
    DHCPServerBulkEditForm,
)
from netbox_dhcp.tables import DHCPServerTable


__all__ = (
    "DHCPServerView",
    "DHCPServerListView",
    "DHCPServerEditView",
    "DHCPServerDeleteView",
    "DHCPServerBulkImportView",
    "DHCPServerBulkEditView",
    "DHCPServerBulkDeleteView",
)


@register_model_view(DHCPServer, "list", path="", detail=False)
class DHCPServerListView(generic.ObjectListView):
    queryset = DHCPServer.objects.all()
    table = DHCPServerTable
    filterset = DHCPServerFilterSet
    filterset_form = DHCPServerFilterForm


@register_model_view(DHCPServer)
class DHCPServerView(generic.ObjectView):
    queryset = DHCPServer.objects.all()


@register_model_view(DHCPServer, "add", detail=False)
@register_model_view(DHCPServer, "edit")
class DHCPServerEditView(generic.ObjectEditView):
    queryset = DHCPServer.objects.all()
    form = DHCPServerForm


@register_model_view(DHCPServer, "delete")
class DHCPServerDeleteView(generic.ObjectDeleteView):
    queryset = DHCPServer.objects.all()


@register_model_view(DHCPServer, "bulk_import", detail=False)
class DHCPServerBulkImportView(generic.BulkImportView):
    queryset = DHCPServer.objects.all()
    model_form = DHCPServerImportForm
    table = DHCPServerTable


@register_model_view(DHCPServer, "bulk_edit", path="edit", detail=False)
class DHCPServerBulkEditView(generic.BulkEditView):
    queryset = DHCPServer.objects.all()
    filterset = DHCPServerFilterSet
    table = DHCPServerTable
    form = DHCPServerBulkEditForm


@register_model_view(DHCPServer, "bulk_delete", path="delete", detail=False)
class DHCPServerBulkDeleteView(generic.BulkDeleteView):
    queryset = DHCPServer.objects.all()
    filterset = DHCPServerFilterSet
    table = DHCPServerTable
