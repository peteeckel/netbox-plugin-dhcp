from netbox.api.routers import NetBoxRouter

from netbox_dhcp.api.views import (
    NetBoxDHCPRootView,
    ClientClassViewSet,
    DDNSViewSet,
    DHCPClusterViewSet,
    DHCPServerViewSet,
    HostReservationViewSet,
    OptionViewSet,
    PDPoolViewSet,
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
router.register("pdpools", PDPoolViewSet)
router.register("sharednetworks", SharedNetworkViewSet)
router.register("subnets", SubnetViewSet)

urlpatterns = router.urls
