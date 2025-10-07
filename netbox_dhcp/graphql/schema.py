from typing import List

import strawberry
import strawberry_django

from .types import (
    NetBoxDHCPClientClassType,
    NetBoxDHCPDHCPClusterType,
    NetBoxDHCPDHCPServerType,
    NetBoxDHCPHostReservationType,
)


@strawberry.type(name="Query")
class NetBoxDHCPClusterQuery:
    netbox_dhcp_dhcp_cluster: NetBoxDHCPDHCPClusterType = strawberry_django.field()
    netbox_dhcp_dhcp_cluster_list: List[NetBoxDHCPDHCPClusterType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPServerQuery:
    netbox_dhcp_dhcp_server: NetBoxDHCPDHCPServerType = strawberry_django.field()
    netbox_dhcp_dhcp_server_list: List[NetBoxDHCPDHCPServerType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPClientClassQuery:
    netbox_dhcp_client_class: NetBoxDHCPClientClassType = strawberry_django.field()
    netbox_dhcp_client_class_list: List[NetBoxDHCPClientClassType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPHostReservationQuery:
    netbox_dhcp_host_reservation: NetBoxDHCPHostReservationType = strawberry_django.field()
    netbox_dhcp_host_reservation_list: List[NetBoxDHCPHostReservationType] = (
        strawberry_django.field()
    )
