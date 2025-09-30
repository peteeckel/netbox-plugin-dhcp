from utilities.testing import APIViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    #   NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import HostReservation


class HostReservationAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    #   NetBoxDHCPGraphQLMixin,
    #   APIViewTestCases.GraphQLTestCase,
):
    model = HostReservation

    brief_fields = [
        "boot_file_name",
        "circuit_id",
        "client_id",
        "comment",
        "description",
        "display",
        "duid",
        "flex_id",
        "hostname",
        "hw_address",
        "id",
        "name",
        "next_server",
        "server_hostname",
        "url",
        "user_context",
    ]

    @classmethod
    def setUpTestData(cls):
        client_classes = TestObjects.get_client_classes()
        mac_addresses = TestObjects.get_mac_addresses()
        ipv4_addresses = TestObjects.get_ipv4_addresses()
        ipv6_addresses = TestObjects.get_ipv6_addresses()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()

        cls.create_data = [
            {
                "name": "test-host-reservation-4",
                "description": "Test Host Reservation 4",
                "circuit_id": None,
                "client_id": None,
                "duid": None,
                "hw_address": mac_addresses[0].pk,
                "flex_id": None,
                "hostname": "host4.zone1.example.com",
                "next_server": "10.0.0.1",
                "server_hostname": "tftp.example.com",
                "boot_file_name": "/tftpboot/file1.img",
                "ipv4_address": ipv4_addresses[0].pk,
                "ipv6_addresses": [address.pk for address in ipv6_addresses[0:2]],
                "ipv6_prefixes": [ipv6_prefixes[0].pk],
                "excluded_ipv6_prefixes": [prefix.pk for prefix in ipv6_prefixes[1:3]],
                "assign_client_classes": [
                    client_class.pk for client_class in client_classes[1:3]
                ],
            },
            {
                "name": "test-host-reservation-5",
                "description": "Test Host Reservation 5",
                "circuit_id": "Test-1234",
                "client_id": "Test-4321",
                "ipv4_address": ipv4_addresses[1].pk,
            },
            {
                "name": "test-host-reservation-6",
                "description": "Test Host Reservation 6",
                "circuit_id": None,
                "client_id": None,
                "hw_address": mac_addresses[2].pk,
                "ipv4_address": ipv4_addresses[2].pk,
                "assign_client_classes": [client_classes[0].pk],
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "assign_client_classes": [
                client_class.pk for client_class in client_classes
            ],
        }

        host_reservations = (
            HostReservation(
                name="test-host-reservation-1",
            ),
            HostReservation(
                name="test-host-reservation-2",
            ),
            HostReservation(
                name="test-host-reservation-3",
            ),
        )
        HostReservation.objects.bulk_create(host_reservations)
