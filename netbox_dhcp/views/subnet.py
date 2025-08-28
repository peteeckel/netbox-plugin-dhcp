from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import Subnet
from netbox_dhcp.filtersets import SubnetFilterSet
from netbox_dhcp.forms import (
    SubnetForm,
    SubnetFilterForm,
    SubnetImportForm,
    SubnetBulkEditForm,
)
from netbox_dhcp.tables import SubnetTable


__all__ = (
    "SubnetView",
    "SubnetListView",
    "SubnetEditView",
    "SubnetDeleteView",
    "SubnetBulkImportView",
    "SubnetBulkEditView",
    "SubnetBulkDeleteView",
)


@register_model_view(Subnet, "list", path="", detail=False)
class SubnetListView(generic.ObjectListView):
    queryset = Subnet.objects.all()
    table = SubnetTable
    filterset = SubnetFilterSet
    filterset_form = SubnetFilterForm


@register_model_view(Subnet)
class SubnetView(generic.ObjectView):
    queryset = Subnet.objects.all()


@register_model_view(Subnet, "add", detail=False)
@register_model_view(Subnet, "edit")
class SubnetEditView(generic.ObjectEditView):
    queryset = Subnet.objects.all()
    form = SubnetForm


@register_model_view(Subnet, "delete")
class SubnetDeleteView(generic.ObjectDeleteView):
    queryset = Subnet.objects.all()


@register_model_view(Subnet, "bulk_import", detail=False)
class SubnetBulkImportView(generic.BulkImportView):
    queryset = Subnet.objects.all()
    model_form = SubnetImportForm
    table = SubnetTable


@register_model_view(Subnet, "bulk_edit", path="edit", detail=False)
class SubnetBulkEditView(generic.BulkEditView):
    queryset = Subnet.objects.all()
    filterset = SubnetFilterSet
    table = SubnetTable
    form = SubnetBulkEditForm


@register_model_view(Subnet, "bulk_delete", path="delete", detail=False)
class SubnetBulkDeleteView(generic.BulkDeleteView):
    queryset = Subnet.objects.all()
    filterset = SubnetFilterSet
    table = SubnetTable
