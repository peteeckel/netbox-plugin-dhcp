import django_filters

from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox_dhcp.models import DHCPServer, DHCPCluster
from netbox_dhcp.choices import DHCPServerStatusChoices


__all__ = ("DHCPServerFilterSet",)


class DHCPServerFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DHCPServer

        fields = (
            "id",
            "name",
            "description",
            "status",
            "dhcp_cluster",
            "device",
            "virtual_machine",
        )

    status = django_filters.MultipleChoiceFilter(
        choices=DHCPServerStatusChoices,
    )

    dhcp_cluster_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPCluster.objects.all(),
        label=_("DHCP Cluster ID"),
    )
    dhcp_cluster = django_filters.ModelMultipleChoiceFilter(
        queryset=DHCPCluster.objects.all(),
        field_name="dhcp_cluster__name",
        to_field_name="name",
        label=_("DHCP Cluster"),
    )

    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name="device",
        label=_("Device ID"),
    )
    device = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name="device__name",
        to_field_name="name",
        label=_("Device"),
    )
    virtual_machine_id = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        field_name="virtual_machine",
        label=_("Virtual Machine ID"),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        field_name="virtual_machine__name",
        to_field_name="name",
        label=_("Virtual Machine"),
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(dhcp_cluster__name__icontains=value)
            | Q(device__name__icontains=value)
            | Q(virtual_machine__name__icontains=value)
        )
        return queryset.filter(qs_filter)
