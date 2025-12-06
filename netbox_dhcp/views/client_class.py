from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

from netbox.views import generic
from utilities.views import register_model_view, ViewTab

from netbox_dhcp.models import ClientClass, Option, OptionDefinition, DHCPServer
from netbox_dhcp.filtersets import (
    ClientClassFilterSet,
    OptionFilterSet,
    OptionDefinitionFilterSet,
)
from netbox_dhcp.forms import (
    ClientClassForm,
    ClientClassFilterForm,
    ClientClassImportForm,
    ClientClassBulkEditForm,
)
from netbox_dhcp.tables import ClientClassTable, ChildOptionTable, OptionDefinitionTable


__all__ = (
    "ClientClassView",
    "ClientClassListView",
    "ClientClassEditView",
    "ClientClassDeleteView",
    "ClientClassBulkImportView",
    "ClientClassBulkEditView",
    "ClientClassBulkDeleteView",
    "ClientClassOptionListView",
    "ClientClassOptionDefinitionListView",
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

    def alter_object(self, obj, request, url_args, url_kwargs):
        if not obj.pk:
            if "dhcp_server" in request.GET:
                obj.dhcp_server = get_object_or_404(
                    DHCPServer, pk=request.GET.get("dhcp_server")
                )

            obj.user = request.user

        return obj


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


@register_model_view(ClientClass, "options")
class ClientClassOptionListView(generic.ObjectChildrenView):
    queryset = ClientClass.objects.all()
    child_model = Option
    table = ChildOptionTable
    filterset = OptionFilterSet
    template_name = "netbox_dhcp/clientclass/options.html"

    tab = ViewTab(
        label=_("Options"),
        permission="netbox_dhcp.view_option",
        badge=lambda obj: obj.options.count(),
        hide_if_empty=True,
    )

    def get_children(self, request, parent):
        return parent.options.restrict(request.user, "view")


@register_model_view(ClientClass, "option_definitions")
class ClientClassOptionDefinitionListView(generic.ObjectChildrenView):
    queryset = ClientClass.objects.all()
    child_model = OptionDefinition
    table = OptionDefinitionTable
    filterset = OptionDefinitionFilterSet
    template_name = "netbox_dhcp/clientclass/option_definitions.html"

    tab = ViewTab(
        label=_("Option Definitions"),
        permission="netbox_dhcp.view_optiondefinition",
        badge=lambda obj: obj.option_definitions.count(),
        hide_if_empty=True,
    )

    def get_children(self, request, parent):
        return parent.option_definitions.restrict(request.user, "view")
