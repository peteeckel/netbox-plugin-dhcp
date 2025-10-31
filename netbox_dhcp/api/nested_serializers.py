from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer

from netbox_dhcp.models import (
    DHCPCluster,
    DHCPServer,
    ClientClass,
    Subnet,
    SharedNetwork,
    Pool,
    PDPool,
    HostReservation,
)

__all__ = (
    "NestedDHCPClusterSerializer",
    "NestedDHCPServerSerializer",
    "NestedClientClassSerializer",
    "NestedSubnetSerializer",
    "NestedSharedNetworkSerializer",
    "NestedPoolSerializer",
    "NestedPDPoolSerializer",
    "NestedHostReservationSerializer",
)


class NestedDHCPClusterSerializer(WritableNestedSerializer):
    class Meta:
        model = DHCPCluster

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "status",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:dhcpcluster-detail"
    )


class NestedDHCPServerSerializer(WritableNestedSerializer):
    class Meta:
        model = DHCPServer

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "status",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:dhcpcluster-detail"
    )


class NestedClientClassSerializer(WritableNestedSerializer):
    class Meta:
        model = ClientClass

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "test",
            "template_test",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:clientclass-detail"
    )


class NestedSubnetSerializer(WritableNestedSerializer):
    class Meta:
        model = Subnet

    fields = (
        "id",
        "url",
        "display",
        "name",
        "description",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "offer_lifetime",
        "valid_lifetime",
        "min_valid_lifetime",
        "max_valid_lifetime",
        "preferred_lifetime",
        "min_preferred_lifetime",
        "max_preferred_lifetime",
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:subnet-detail"
    )


class NestedSharedNetworkSerializer(WritableNestedSerializer):
    class Meta:
        model = SharedNetwork

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:sharednetwork-detail"
    )


class NestedPoolSerializer(WritableNestedSerializer):
    class Meta:
        model = Pool

    fields = (
        "id",
        "url",
        "display",
        "name",
        "description",
        "subnet",
        "ip_range",
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:pool-detail"
    )


class NestedPDPoolSerializer(WritableNestedSerializer):
    class Meta:
        model = PDPool

    fields = (
        "id",
        "url",
        "display",
        "name",
        "description",
        "subnet",
        "prefix",
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:pdpool-detail"
    )


class NestedHostReservationSerializer(WritableNestedSerializer):
    class Meta:
        model = HostReservation

    fields = (
        "id",
        "url",
        "display",
        "name",
        "description",
        "duid",
        "hw_address",
        "circuit_id",
        "client_id",
        "flex_id",
        "next_server",
        "server_hostname",
        "boot_file_name",
        "hostname",
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:hostreservation-detail"
    )
