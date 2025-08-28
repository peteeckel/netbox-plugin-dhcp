from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet

from netbox_dhcp.api.serializers import (
    ClientClassSerializer,
    DDNSSerializer,
    DHCPClusterSerializer,
    DHCPServerSerializer,
    HostReservationSerializer,
    OptionSerializer,
    PDPoolSerializer,
    SharedNetworkSerializer,
    SubnetSerializer,
)
from netbox_dhcp.filtersets import (
    ClientClassFilterSet,
    DDNSFilterSet,
    DHCPClusterFilterSet,
    DHCPServerFilterSet,
    HostReservationFilterSet,
    OptionFilterSet,
    PDPoolFilterSet,
    SharedNetworkFilterSet,
    SubnetFilterSet,
)
from netbox_dhcp.models import (
    ClientClass,
    DDNS,
    DHCPCluster,
    DHCPServer,
    HostReservation,
    Option,
    PDPool,
    SharedNetwork,
    Subnet,
)


class NetBoxDHCPRootView(APIRootView):
    def get_view_name(self):
        return "NetBoxDHCP"


class ClientClassViewSet(NetBoxModelViewSet):
    queryset = ClientClass.objects.all()
    serializer_class = ClientClassSerializer
    filterset_class = ClientClassFilterSet


class DDNSViewSet(NetBoxModelViewSet):
    queryset = DDNS.objects.all()
    serializer_class = DDNSSerializer
    filterset_class = DDNSFilterSet


class DHCPClusterViewSet(NetBoxModelViewSet):
    queryset = DHCPCluster.objects.all()
    serializer_class = DHCPClusterSerializer
    filterset_class = DHCPClusterFilterSet


class DHCPServerViewSet(NetBoxModelViewSet):
    queryset = DHCPServer.objects.all()
    serializer_class = DHCPServerSerializer
    filterset_class = DHCPServerFilterSet


class HostReservationViewSet(NetBoxModelViewSet):
    queryset = HostReservation.objects.all()
    serializer_class = HostReservationSerializer
    filterset_class = HostReservationFilterSet


class OptionViewSet(NetBoxModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filterset_class = OptionFilterSet


class PDPoolViewSet(NetBoxModelViewSet):
    queryset = PDPool.objects.all()
    serializer_class = PDPoolSerializer
    filterset_class = PDPoolFilterSet


class SharedNetworkViewSet(NetBoxModelViewSet):
    queryset = SharedNetwork.objects.all()
    serializer_class = SharedNetworkSerializer
    filterset_class = SharedNetworkFilterSet


class SubnetViewSet(NetBoxModelViewSet):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer
    filterset_class = SubnetFilterSet
