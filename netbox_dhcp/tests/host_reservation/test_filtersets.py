from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import HostReservation
from netbox_dhcp.filtersets import HostReservationFilterSet
from netbox_dhcp.tests.custom import TestObjects, BOOTPFilterSetTests


class HostReservationFilterSetTestCase(
    BOOTPFilterSetTests,
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = HostReservation.objects.all()
    filterset = HostReservationFilterSet

    # +
    # Because of the misbehaviour mentioned below, ipv6_addresses, ipv6_prefixes
    # and excluded_ipv6_prefixes need to be ignored by the missing_filters
    # test as well
    # -
    ignore_fields = (
        "ipv6_addresses",
        "ipv6_prefixes",
        "excluded_ipv6_prefixes",
    )

    # +
    # This is a dirty hack and does not work for all models.
    #
    # What really needs to be fixed is the get_m2m_filter_name() method in
    # netbox/utilities/testing/filtersets.py, which returns a filter name
    # based on the target model verbose name instead of the field name.
    #
    # Obviously this fails if there are multiple m2m relations to the same
    # class.
    # -
    filter_name_map = {
        "dhcp_server": "parent_dhcp_server",
        "subnet": "parent_subnet",
    }

    @classmethod
    def setUpTestData(cls):
        cls.mac_addresses = TestObjects.get_mac_addresses()
        cls.ipv4_addresses = TestObjects.get_ipv4_addresses()
        cls.ipv6_addresses = TestObjects.get_ipv6_addresses()
        cls.ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        cls.client_classes = TestObjects.get_client_classes()
        cls.dhcp_servers = TestObjects.get_dhcp_servers()
        cls.subnets = TestObjects.get_ipv4_subnets()

        cls.host_reservations = (
            HostReservation(
                name="test-host-reservation-1",
                description="Test Host Reservation 1",
                circuit_id="ge0/0/0:vlan42",
                client_id="sample.client.1",
                duid="00:02:00:00:3e:20:ff:00:00:00:00:01",
                hw_address=cls.mac_addresses[0],
                flex_id="0x42424242",
                hostname="host1.zone1.example.com",
                ipv4_address=cls.ipv4_addresses[0],
                **BOOTPFilterSetTests.DATA[0],
            ),
            HostReservation(
                name="test-host-reservation-2",
                description="Test Host Reservation 2",
                circuit_id="ge0/0/1:vlan42",
                client_id="sample.client.2",
                duid="00:02:00:00:3e:20:ff:00:00:00:00:02",
                hw_address=cls.mac_addresses[1],
                flex_id="0x2323232323",
                hostname="host2.zone1.example.com",
                ipv4_address=cls.ipv4_addresses[1],
                **BOOTPFilterSetTests.DATA[1],
            ),
            HostReservation(
                name="test-host-reservation-3",
                description="Test Host Reservation 3",
                circuit_id="ge0/0/2:vlan43",
                client_id="sample.client.3",
                duid="00:02:00:00:3e:20:ff:00:00:00:00:03",
                hw_address=cls.mac_addresses[2],
                flex_id="0x42424242",
                hostname="host3.zone1.example.com",
                ipv4_address=cls.ipv4_addresses[2],
                **BOOTPFilterSetTests.DATA[2],
            ),
        )
        HostReservation.objects.bulk_create(cls.host_reservations)

        for number, host_reservation in enumerate(cls.host_reservations):
            cls.dhcp_servers[number].child_host_reservations.set([host_reservation])
            cls.subnets[number].child_host_reservations.set([host_reservation])

        cls.host_reservations[0].ipv6_addresses.set(cls.ipv6_addresses[0:2])
        cls.host_reservations[1].ipv6_addresses.set(cls.ipv6_addresses[1:3])
        cls.host_reservations[2].ipv6_addresses.set(
            [cls.ipv6_addresses[0], cls.ipv6_addresses[2]]
        )

        cls.host_reservations[0].ipv6_prefixes.set(cls.ipv6_prefixes[0:2])
        cls.host_reservations[1].ipv6_prefixes.set(cls.ipv6_prefixes[1:3])
        cls.host_reservations[2].ipv6_prefixes.set(
            [cls.ipv6_prefixes[0], cls.ipv6_prefixes[2]]
        )

        cls.host_reservations[0].excluded_ipv6_prefixes.set(cls.ipv6_prefixes[0:2])
        cls.host_reservations[1].excluded_ipv6_prefixes.set(cls.ipv6_prefixes[1:3])
        cls.host_reservations[2].excluded_ipv6_prefixes.set(
            [cls.ipv6_prefixes[0], cls.ipv6_prefixes[2]]
        )

        cls.host_reservations[0].client_classes.set(cls.client_classes[0:2])
        cls.host_reservations[1].client_classes.set(cls.client_classes[1:3])
        cls.host_reservations[2].client_classes.set(
            [cls.client_classes[0], cls.client_classes[2]]
        )

    def test_name(self):
        params = {"name__iregex": r"test-host-reservation-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"name": "test-host-reservation-3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_description(self):
        params = {"description__iregex": r"Test Host Reservation [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"description": "Test Host Reservation 3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_circuit_id(self):
        params = {"circuit_id__iregex": r"vlan42"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"circuit_id": "ge0/0/1:vlan42"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_client_id(self):
        params = {"client_id__iregex": r"sample\.client\.[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"client_id": "sample.client.1"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_duid(self):
        params = {"duid__iregex": r"[23]$"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"duid": "00:02:00:00:3e:20:ff:00:00:00:00:01"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_hw_address(self):
        params = {
            "hw_address__iregex": rf"({self.mac_addresses[0].mac_address}|{self.mac_addresses[1].mac_address})"
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"hw_address_id": [self.mac_addresses[0].pk, self.mac_addresses[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_ipv4_address(self):
        params = {
            "ipv4_address__iregex": rf"({self.ipv4_addresses[0].address}|{self.ipv4_addresses[1].address})"
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {
            "ipv4_address_id": [self.ipv4_addresses[0].pk, self.ipv4_addresses[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_ipv6_address(self):
        params = {"ipv6_address": self.ipv6_addresses[0].address}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"ipv6_address_id": [self.ipv6_addresses[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_ipv6_prefix(self):
        params = {"ipv6_prefix__iregex": r"db8:3::"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"ipv6_prefix_id": [self.ipv6_prefixes[0].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_excluded_ipv6_prefix(self):
        params = {"excluded_ipv6_prefix": self.ipv6_prefixes[0].prefix}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"excluded_ipv6_prefix_id": [self.ipv6_prefixes[0].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_dhcp_server(self):
        params = {"parent_dhcp_server__iregex": r"server-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {
            "parent_dhcp_server_id": [self.dhcp_servers[0].pk, self.dhcp_servers[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_subnet(self):
        params = {"parent_subnet__iregex": r"subnet-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_subnet_id": [self.subnets[0].pk, self.subnets[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
