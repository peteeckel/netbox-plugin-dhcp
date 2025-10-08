from typing import List

import strawberry
import strawberry_django

from .types import (
    NetBoxDHCPClientClassType,
    NetBoxDHCPDHCPClusterType,
    NetBoxDHCPDHCPServerType,
    NetBoxDHCPHostReservationType,
    NetBoxDHCPOptionDefinitionType,
    NetBoxDHCPOptionType,
    NetBoxDHCPPDPoolType,
    NetBoxDHCPPoolType,
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


@strawberry.type(name="Query")
class NetBoxDHCPOptionDefinitionQuery:
    netbox_dhcp_option_definition: NetBoxDHCPOptionDefinitionType = strawberry_django.field()
    netbox_dhcp_option_definition_list: List[NetBoxDHCPOptionDefinitionType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPOptionQuery:
    netbox_dhcp_option: NetBoxDHCPOptionType = strawberry_django.field()
    netbox_dhcp_option_list: List[NetBoxDHCPOptionType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPPDPoolQuery:
    netbox_dhcp_prefix_delegation_pool: NetBoxDHCPPDPoolType = strawberry_django.field()
    netbox_dhcp_prefix_delegation_pool_list: List[NetBoxDHCPPDPoolType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDHCPPoolQuery:
    netbox_dhcp_pool: NetBoxDHCPPoolType = strawberry_django.field()
    netbox_dhcp_pool_list: List[NetBoxDHCPPoolType] = (
        strawberry_django.field()
    )
