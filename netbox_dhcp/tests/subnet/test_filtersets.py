from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import Subnet
from netbox_dhcp.filtersets import SubnetFilterSet
from netbox_dhcp.tests.custom import (
    TestObjects,
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
    LeaseFilterSetTests,
    DDNSUpdateFilterSetTests,
)


class SubnetFilterSetTestCase(
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
    LeaseFilterSetTests,
    DDNSUpdateFilterSetTests,
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = Subnet.objects.all()
    filterset = SubnetFilterSet

    # +
    # Because of the misbehaviour mentioned below, ipv6_addresses, ipv6_prefixes
    # and excluded_ipv6_prefixes need to be ignored by the missing_filters
    # test as well
    # -
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
        "pool": "child_pool",
        "prefix_delegation_pool": "child_pd_pool",
        "subnet": "child_subnet",
        "host_reservation": "child_host_reservation",
        "dhcp_server": "parent_dhcp_server",
        "shared_network": "parent_shared_network",
    }

    @classmethod
    def setUpTestData(cls):
        cls.ipv4_prefixes = TestObjects.get_ipv4_prefixes()
        cls.ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        cls.client_classes = TestObjects.get_client_classes()
        cls.ipv4_subnets = TestObjects.get_ipv4_subnets()
        cls.ipv6_subnets = TestObjects.get_ipv6_subnets()
        cls.ipv4_shared_networks = TestObjects.get_ipv4_shared_networks()
        cls.host_reservations = TestObjects.get_host_reservations()

        cls.subnets = (
            Subnet(
                name="test-subnet-1",
                description="Test Subnet 1",
                prefix=cls.ipv4_prefixes[0],
                **DDNSUpdateFilterSetTests.DATA[0],
                **BOOTPFilterSetTests.DATA[0],
                **ValidLifetimeFilterSetTests.DATA[0],
                **OfferLifetimeFilterSetTests.DATA[0],
                **LeaseFilterSetTests.DATA[0],
            ),
            Subnet(
                name="test-subnet-2",
                description="Test Subnet 2",
                prefix=cls.ipv4_prefixes[1],
                **BOOTPFilterSetTests.DATA[1],
                **OfferLifetimeFilterSetTests.DATA[1],
            ),
            Subnet(
                name="test-subnet-3",
                description="Test Subnet 3",
                prefix=cls.ipv4_prefixes[2],
                **BOOTPFilterSetTests.DATA[2],
                **DDNSUpdateFilterSetTests.DATA[1],
                **ValidLifetimeFilterSetTests.DATA[1],
                **OfferLifetimeFilterSetTests.DATA[2],
                **LeaseFilterSetTests.DATA[1],
            ),
            Subnet(
                name="test-subnet-4",
                description="Test Subnet 4",
                prefix=cls.ipv6_prefixes[0],
                **PreferredLifetimeFilterSetTests.DATA[0],
            ),
            Subnet(
                name="test-subnet-5",
                description="Test Subnet 5",
                prefix=cls.ipv6_prefixes[1],
                **DDNSUpdateFilterSetTests.DATA[2],
                **ValidLifetimeFilterSetTests.DATA[2],
                **PreferredLifetimeFilterSetTests.DATA[1],
                **LeaseFilterSetTests.DATA[2],
            ),
            Subnet(
                name="test-subnet-6",
                description="Test Subnet 6",
                prefix=cls.ipv6_prefixes[2],
                **PreferredLifetimeFilterSetTests.DATA[2],
            ),
        )
        Subnet.objects.bulk_create(cls.subnets)

        for number in range(3):
            cls.subnets[number].child_subnets.add(cls.ipv4_subnets[number])
            cls.subnets[number + 3].child_subnets.add(cls.ipv6_subnets[number])
            cls.subnets[number + 3].child_host_reservations.add(
                cls.host_reservations[number]
            )
            cls.ipv4_shared_networks[number].child_subnets.add(cls.subnets[number])
            cls.ipv4_subnets[number].child_subnets.add(cls.subnets[number])

        for number in range(4):
            cls.subnets[number].client_classes.add(cls.client_classes[number % 3])
            cls.subnets[number].evaluate_additional_classes.add(
                cls.client_classes[(number + 2) % 3]
            )

    def test_name(self):
        params = {"name__iregex": r"test-subnet-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"name": "test-subnet-3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_description(self):
        params = {"description__iregex": r"Test Subnet [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"description": "Test Subnet 3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_prefix(self):
        params = {"prefix_id": [self.ipv6_prefixes[0].pk, self.ipv6_prefixes[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"prefix__iregex": r"2001:db8:[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"prefix_id": [self.ipv4_prefixes[0].pk, self.ipv4_prefixes[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"prefix__iregex": r"192.0.2.(0|64)/26"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_child_subnet(self):
        params = {"child_subnet_id": [self.ipv6_subnets[0].pk, self.ipv6_subnets[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_subnet__iregex": r"ipv6-subnet-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_subnet_id": [self.ipv4_subnets[0].pk, self.ipv4_subnets[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_subnet__iregex": r"ipv4-subnet-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_child_host_reservations(self):
        params = {
            "child_host_reservation_id": [
                self.host_reservations[0].pk,
                self.host_reservations[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"child_host_reservation__iregex": r"host-reservation-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_subnet(self):
        params = {
            "parent_subnet_id": [self.ipv4_subnets[0].pk, self.ipv4_subnets[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_subnet__iregex": r"test-subnet-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_subnet__iregex": r"test-subnet-[56]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_shared_network(self):
        params = {
            "parent_shared_network_id": [
                self.ipv4_shared_networks[0].pk,
                self.ipv4_shared_networks[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_shared_network__iregex": r"ipv4-shared-network-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_client_classes(self):
        params = {
            "client_class_id": [
                self.client_classes[0].pk,
                self.client_classes[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 3)
        params = {"client_class__iregex": r"client-class-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_evaluate_additional_classes(self):
        params = {
            "evaluate_additional_class_id": [
                self.client_classes[0].pk,
                self.client_classes[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"evaluate_additional_class__iregex": r"client-class-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 3)
