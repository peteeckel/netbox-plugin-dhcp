from utilities.testing import APIViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    #   NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import DHCPServer, DHCPCluster
from netbox_dhcp.choices import (
    DHCPServerStatusChoices,
    DHCPServerIDTypeChoices,
    HostReservationIdentifierChoices,
)


class DHCPServerAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    #   NetBoxDHCPGraphQLMixin,
    #   APIViewTestCases.GraphQLTestCase,
):
    model = DHCPServer

    brief_fields = [
        "description",
        "display",
        "id",
        "name",
        "status",
        "url",
    ]

    @classmethod
    def setUpTestData(cls):
        dhcp_cluster = DHCPCluster.objects.create(
            name="test-cluster-1",
        )

        subnets = TestObjects.get_ipv6_subnets()
        shared_networks = TestObjects.get_ipv6_shared_networks()
        host_reservations = TestObjects.get_host_reservations()
        client_classes = TestObjects.get_client_classes()

        cls.create_data = [
            {
                "name": "test-server-4",
            },
            {
                "name": "test-server-5",
            },
            {
                "name": "test-server-6",
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "status": DHCPServerStatusChoices.STATUS_INACTIVE,
            "dhcp_cluster": dhcp_cluster.pk,
            "server_id": DHCPServerIDTypeChoices.ID_EN,
            "host_reservation_identifiers": [
                HostReservationIdentifierChoices.HW_ADDRESS,
                HostReservationIdentifierChoices.DUID,
            ],
            "echo_client_id": True,
            "relay_supplied_options": [110, 120, 130],
            "child_subnets": [subnet.pk for subnet in subnets],
            "child_shared_networks": [
                shared_network.pk for shared_network in shared_networks
            ],
            "child_host_reservations": [
                host_reservation.pk for host_reservation in host_reservations
            ],
            "child_client_classes": [
                client_class.pk for client_class in client_classes
            ],
        }

        dhcp_servers = (
            DHCPServer(
                name="test-server-1",
            ),
            DHCPServer(
                name="test-server-2",
            ),
            DHCPServer(
                name="test-server-3",
            ),
        )
        DHCPServer.objects.bulk_create(dhcp_servers)
