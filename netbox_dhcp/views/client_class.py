from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import ClientClass
from netbox_dhcp.filtersets import ClientClassFilterSet
from netbox_dhcp.forms import (
    ClientClassForm,
    ClientClassFilterForm,
    ClientClassImportForm,
    ClientClassBulkEditForm,
)
from netbox_dhcp.tables import ClientClassTable


__all__ = (
    "ClientClassView",
    "ClientClassListView",
    "ClientClassEditView",
    "ClientClassDeleteView",
    "ClientClassBulkImportView",
    "ClientClassBulkEditView",
    "ClientClassBulkDeleteView",
)


@register_model_view(ClientClass, "list", path="", detail=False)
class ClientClassListView(generic.ObjectListView):
    queryset = ClientClass.objects.all()
    table = ClientClassTable
    filterset = ClientClassFilterSet
    filterset_form = ClientClassFilterForm


@register_model_view(ClientClass)
class ClientClassView(generic.ObjectView):
    queryset = ClientClass.objects.all()


@register_model_view(ClientClass, "add", detail=False)
@register_model_view(ClientClass, "edit")
class ClientClassEditView(generic.ObjectEditView):
    queryset = ClientClass.objects.all()
    form = ClientClassForm


@register_model_view(ClientClass, "delete")
class ClientClassDeleteView(generic.ObjectDeleteView):
    queryset = ClientClass.objects.all()


@register_model_view(ClientClass, "bulk_import", detail=False)
class ClientClassBulkImportView(generic.BulkImportView):
    queryset = ClientClass.objects.all()
    model_form = ClientClassImportForm
    table = ClientClassTable


@register_model_view(ClientClass, "bulk_edit", path="edit", detail=False)
class ClientClassBulkEditView(generic.BulkEditView):
    queryset = ClientClass.objects.all()
    filterset = ClientClassFilterSet
    table = ClientClassTable
    form = ClientClassBulkEditForm


@register_model_view(ClientClass, "bulk_delete", path="delete", detail=False)
class ClientClassBulkDeleteView(generic.BulkDeleteView):
    queryset = ClientClass.objects.all()
    filterset = ClientClassFilterSet
    table = ClientClassTable
