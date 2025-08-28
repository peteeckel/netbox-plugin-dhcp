from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import SharedNetwork
from netbox_dhcp.filtersets import SharedNetworkFilterSet
from netbox_dhcp.forms import (
    SharedNetworkForm,
    SharedNetworkFilterForm,
    SharedNetworkImportForm,
    SharedNetworkBulkEditForm,
)
from netbox_dhcp.tables import SharedNetworkTable


__all__ = (
    "SharedNetworkView",
    "SharedNetworkListView",
    "SharedNetworkEditView",
    "SharedNetworkDeleteView",
    "SharedNetworkBulkImportView",
    "SharedNetworkBulkEditView",
    "SharedNetworkBulkDeleteView",
)


@register_model_view(SharedNetwork, "list", path="", detail=False)
class SharedNetworkListView(generic.ObjectListView):
    queryset = SharedNetwork.objects.all()
    table = SharedNetworkTable
    filterset = SharedNetworkFilterSet
    filterset_form = SharedNetworkFilterForm


@register_model_view(SharedNetwork)
class SharedNetworkView(generic.ObjectView):
    queryset = SharedNetwork.objects.all()


@register_model_view(SharedNetwork, "add", detail=False)
@register_model_view(SharedNetwork, "edit")
class SharedNetworkEditView(generic.ObjectEditView):
    queryset = SharedNetwork.objects.all()
    form = SharedNetworkForm


@register_model_view(SharedNetwork, "delete")
class SharedNetworkDeleteView(generic.ObjectDeleteView):
    queryset = SharedNetwork.objects.all()


@register_model_view(SharedNetwork, "bulk_import", detail=False)
class SharedNetworkBulkImportView(generic.BulkImportView):
    queryset = SharedNetwork.objects.all()
    model_form = SharedNetworkImportForm
    table = SharedNetworkTable


@register_model_view(SharedNetwork, "bulk_edit", path="edit", detail=False)
class SharedNetworkBulkEditView(generic.BulkEditView):
    queryset = SharedNetwork.objects.all()
    filterset = SharedNetworkFilterSet
    table = SharedNetworkTable
    form = SharedNetworkBulkEditForm


@register_model_view(SharedNetwork, "bulk_delete", path="delete", detail=False)
class SharedNetworkBulkDeleteView(generic.BulkDeleteView):
    queryset = SharedNetwork.objects.all()
    filterset = SharedNetworkFilterSet
    table = SharedNetworkTable
