from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import DHCPServer
from netbox_dhcp.filtersets import DHCPServerFilterSet
from netbox_dhcp.choices import (
    DHCPServerStatusChoices,
    DHCPServerIDTypeChoices,
    HostReservationIdentifierChoices,
)
from netbox_dhcp.tests.custom import (
    TestObjects,
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
    LeaseFilterSetTests,
    DDNSUpdateFilterSetTests,
)


class DHCPServerFilterSetTestCase(
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
    LeaseFilterSetTests,
    DDNSUpdateFilterSetTests,
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = DHCPServer.objects.all()
    filterset = DHCPServerFilterSet

    ignore_fields = (
        "user_context",
        "comment",
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
        "host_reservation": "child_host_reservation",
        "subnet": "child_subnet",
        "shared_network": "child_shared_network",
        "client_class": "child_client_class",
    }

    @classmethod
    def setUpTestData(cls):
        cls.dhcp_clusters = TestObjects.get_dhcp_clusters()
        cls.devices = TestObjects.get_devices()
        cls.virtual_machines = TestObjects.get_virtual_machines()
        cls.subnets = TestObjects.get_ipv4_subnets()
        cls.shared_networks = TestObjects.get_ipv4_shared_networks()
        cls.host_reservations = TestObjects.get_host_reservations()
        cls.client_classes = TestObjects.get_client_classes()

        cls.dhcp_servers = (
            DHCPServer(
                name="test-server-1",
                status=DHCPServerStatusChoices.STATUS_ACTIVE,
                description="Test Server 1",
                server_id=DHCPServerIDTypeChoices.ID_EN,
                host_reservation_identifiers=[HostReservationIdentifierChoices.DUID],
                echo_client_id=True,
                relay_supplied_options=[1, 2, 3],
                dhcp_cluster=cls.dhcp_clusters[0],
                device=cls.devices[0],
                decline_probation_period=43200,
                **BOOTPFilterSetTests.DATA[0],
                **ValidLifetimeFilterSetTests.DATA[0],
                **PreferredLifetimeFilterSetTests.DATA[0],
                **OfferLifetimeFilterSetTests.DATA[0],
                **LeaseFilterSetTests.DATA[0],
                **DDNSUpdateFilterSetTests.DATA[0],
            ),
            DHCPServer(
                name="test-server-2",
                status=DHCPServerStatusChoices.STATUS_INACTIVE,
                description="Test Server 2",
                server_id=DHCPServerIDTypeChoices.ID_LL,
                host_reservation_identifiers=[
                    HostReservationIdentifierChoices.HW_ADDRESS,
                    HostReservationIdentifierChoices.DUID,
                ],
                echo_client_id=True,
                relay_supplied_options=[2, 3, 4],
                dhcp_cluster=cls.dhcp_clusters[1],
                device=cls.devices[1],
                decline_probation_period=86400,
                **BOOTPFilterSetTests.DATA[1],
                **ValidLifetimeFilterSetTests.DATA[1],
                **PreferredLifetimeFilterSetTests.DATA[1],
                **OfferLifetimeFilterSetTests.DATA[1],
                **LeaseFilterSetTests.DATA[1],
                **DDNSUpdateFilterSetTests.DATA[1],
            ),
            DHCPServer(
                name="test-server-3",
                status=DHCPServerStatusChoices.STATUS_ACTIVE,
                description="Test Server 3",
                server_id=DHCPServerIDTypeChoices.ID_LLT,
                host_reservation_identifiers=[
                    HostReservationIdentifierChoices.CLIENT_ID
                ],
                echo_client_id=False,
                relay_supplied_options=[4, 5, 6],
                dhcp_cluster=cls.dhcp_clusters[2],
                virtual_machine=cls.virtual_machines[2],
                decline_probation_period=86400,
                **BOOTPFilterSetTests.DATA[2],
                **ValidLifetimeFilterSetTests.DATA[2],
                **PreferredLifetimeFilterSetTests.DATA[2],
                **OfferLifetimeFilterSetTests.DATA[2],
                **LeaseFilterSetTests.DATA[2],
                **DDNSUpdateFilterSetTests.DATA[2],
            ),
        )
        DHCPServer.objects.bulk_create(cls.dhcp_servers)

        cls.dhcp_servers[0].child_subnets.set(cls.subnets[0:2])
        cls.dhcp_servers[1].child_subnets.set(cls.subnets[1:3])
        cls.dhcp_servers[2].child_subnets.set([cls.subnets[0], cls.subnets[2]])

        cls.dhcp_servers[0].child_shared_networks.set(cls.shared_networks[0:2])
        cls.dhcp_servers[1].child_shared_networks.set(cls.shared_networks[1:3])
        cls.dhcp_servers[2].child_shared_networks.set(
            [cls.shared_networks[0], cls.shared_networks[2]]
        )

        cls.dhcp_servers[0].child_host_reservations.set(cls.host_reservations[0:2])
        cls.dhcp_servers[1].child_host_reservations.set(cls.host_reservations[1:3])
        cls.dhcp_servers[2].child_host_reservations.set(
            [cls.host_reservations[0], cls.host_reservations[2]]
        )

        cls.dhcp_servers[0].child_client_classes.set(cls.client_classes[0:2])
        cls.dhcp_servers[1].child_client_classes.set(cls.client_classes[1:3])
        cls.dhcp_servers[2].child_client_classes.set(
            [cls.client_classes[0], cls.client_classes[2]]
        )

    def test_name(self):
        params = {"name__iregex": r"test-server-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_description(self):
        params = {"description__iregex": r"Test Server [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_status(self):
        params = {"status": [DHCPServerStatusChoices.STATUS_ACTIVE]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"status": [DHCPServerStatusChoices.STATUS_INACTIVE]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_server_id(self):
        params = {
            "server_id": [DHCPServerIDTypeChoices.ID_EN, DHCPServerIDTypeChoices.ID_LL]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_host_reservation_identifiers(self):
        params = {
            "host_reservation_identifiers": [
                HostReservationIdentifierChoices.DUID,
                HostReservationIdentifierChoices.HW_ADDRESS,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_echo_client_id(self):
        params = {"echo_client_id": True}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_relay_supplied_options(self):
        params = {"relay_supplied_options": [2, 3]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"relay_supplied_options": [4]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_dhcp_cluster(self):
        params = {
            "dhcp_cluster": [self.dhcp_clusters[0].name, self.dhcp_clusters[1].name]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {
            "dhcp_cluster_id": [self.dhcp_clusters[2].pk, self.dhcp_clusters[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_device(self):
        params = {"device": [self.devices[0].name, self.devices[1].name]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"device_id": [self.devices[1].pk, self.devices[2].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_virtual_machine(self):
        params = {
            "virtual_machine": [
                self.virtual_machines[0].name,
                self.virtual_machines[1].name,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
        params = {
            "virtual_machine_id": [
                self.virtual_machines[1].pk,
                self.virtual_machines[2].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_decline_probation_period(self):
        params = {"decline_probation_period": 86400}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"decline_probation_period": 43200}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_child_subnets(self):
        params = {"child_subnet": [self.subnets[0].name]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_subnet_id": [self.subnets[2].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_child_shared_networks(self):
        params = {"child_shared_network": [self.shared_networks[0].name]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_shared_network_id": [self.shared_networks[2].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_child_host_reservations(self):
        params = {"child_host_reservation": [self.host_reservations[0].name]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_host_reservation_id": [self.host_reservations[2].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_child_client_classes(self):
        params = {"child_client_class": [self.client_classes[0].name]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_client_class_id": [self.client_classes[2].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
