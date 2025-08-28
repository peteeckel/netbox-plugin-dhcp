from netbox.views import generic

from utilities.views import register_model_view

from netbox_dhcp.models import Option
from netbox_dhcp.filtersets import OptionFilterSet
from netbox_dhcp.forms import (
    OptionForm,
    OptionFilterForm,
    OptionImportForm,
    OptionBulkEditForm,
)
from netbox_dhcp.tables import OptionTable


__all__ = (
    "OptionView",
    "OptionListView",
    "OptionEditView",
    "OptionDeleteView",
    "OptionBulkImportView",
    "OptionBulkEditView",
    "OptionBulkDeleteView",
)


@register_model_view(Option, "list", path="", detail=False)
class OptionListView(generic.ObjectListView):
    queryset = Option.objects.all()
    table = OptionTable
    filterset = OptionFilterSet
    filterset_form = OptionFilterForm


@register_model_view(Option)
class OptionView(generic.ObjectView):
    queryset = Option.objects.all()


@register_model_view(Option, "add", detail=False)
@register_model_view(Option, "edit")
class OptionEditView(generic.ObjectEditView):
    queryset = Option.objects.all()
    form = OptionForm


@register_model_view(Option, "delete")
class OptionDeleteView(generic.ObjectDeleteView):
    queryset = Option.objects.all()


@register_model_view(Option, "bulk_import", detail=False)
class OptionBulkImportView(generic.BulkImportView):
    queryset = Option.objects.all()
    model_form = OptionImportForm
    table = OptionTable


@register_model_view(Option, "bulk_edit", path="edit", detail=False)
class OptionBulkEditView(generic.BulkEditView):
    queryset = Option.objects.all()
    filterset = OptionFilterSet
    table = OptionTable
    form = OptionBulkEditForm


@register_model_view(Option, "bulk_delete", path="delete", detail=False)
class OptionBulkDeleteView(generic.BulkDeleteView):
    queryset = Option.objects.all()
    filterset = OptionFilterSet
    table = OptionTable
