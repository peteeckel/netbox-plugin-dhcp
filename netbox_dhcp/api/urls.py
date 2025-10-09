from netbox.api.routers import NetBoxRouter

from netbox_dhcp.api.views import (
    NetBoxDHCPRootView,
    ClientClassViewSet,
    DDNSViewSet,
    DHCPClusterViewSet,
    DHCPServerViewSet,
    HostReservationViewSet,
    OptionViewSet,
    OptionDefinitionViewSet,
    PDPoolViewSet,
    PoolViewSet,
    SharedNetworkViewSet,
    SubnetViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetBoxDHCPRootView

router.register("clientclasses", ClientClassViewSet)
router.register("ddns", DDNSViewSet)
router.register("dhcpclusters", DHCPClusterViewSet)
router.register("dhcpservers", DHCPServerViewSet)
router.register("hostreservations", HostReservationViewSet)
router.register("options", OptionViewSet)
router.register("optiondefinitions", OptionDefinitionViewSet)
router.register("pdpools", PDPoolViewSet)
router.register("pools", PoolViewSet)
router.register("sharednetworks", SharedNetworkViewSet)
router.register("subnets", SubnetViewSet)

urlpatterns = router.urls
