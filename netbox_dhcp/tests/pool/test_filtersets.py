from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import Pool
from netbox_dhcp.filtersets import PoolFilterSet
from netbox_dhcp.tests.custom import TestObjects, DDNSUpdateFilterSetTests


class PoolFilterSetTestCase(
    DDNSUpdateFilterSetTests,
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = Pool.objects.all()
    filterset = PoolFilterSet

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
        "subnet": "parent_subnet",
    }

    @classmethod
    def setUpTestData(cls):
        cls.client_classes = TestObjects.get_client_classes()
        cls.ipv4_subnets = TestObjects.get_ipv4_subnets()
        cls.ipv6_subnets = TestObjects.get_ipv6_subnets()
        cls.ipv4_ranges = TestObjects.get_ipv4_ranges()
        cls.ipv6_ranges = TestObjects.get_ipv6_ranges()

        pools = (
            Pool(
                name="test-pool-1",
                description="Test Pool 1",
                ip_range=cls.ipv4_ranges[0],
                pool_id=23,
                client_class=cls.client_classes[0],
                **DDNSUpdateFilterSetTests.DATA[0],
            ),
            Pool(
                name="test-pool-2",
                description="Test Pool 2",
                ip_range=cls.ipv4_ranges[1],
                pool_id=42,
                client_class=cls.client_classes[1],
                **DDNSUpdateFilterSetTests.DATA[1],
            ),
            Pool(
                name="test-pool-3",
                description="Test Pool 3",
                ip_range=cls.ipv6_ranges[0],
                pool_id=1337,
                client_class=cls.client_classes[1],
                **DDNSUpdateFilterSetTests.DATA[2],
            ),
            Pool(
                name="test-pool-4",
                description="Test Pool 4",
                ip_range=cls.ipv6_ranges[1],
                pool_id=4711,
                client_class=cls.client_classes[2],
            ),
        )
        Pool.objects.bulk_create(pools)

        cls.ipv4_subnets[0].child_pools.add(pools[0])
        cls.ipv4_subnets[1].child_pools.add(pools[1])
        cls.ipv6_subnets[0].child_pools.add(pools[2])
        cls.ipv6_subnets[1].child_pools.add(pools[3])

        for number in range(4):
            pools[number].require_client_classes.add(
                cls.client_classes[(number + 1) % 3]
            )
            pools[number].evaluate_additional_classes.add(
                cls.client_classes[(number + 2) % 3]
            )
            pools[number].client_class_definitions.add(cls.client_classes[number % 3])

    def test_name(self):
        params = {"name__iregex": r"test-pool-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"name": "test-pool-3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_description(self):
        params = {"description__iregex": r"Test Pool [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"description": "Test Pool 3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_pool_id(self):
        params = {"pool_id": 42}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"pool_id__gt": 42}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_ip_range(self):
        params = {"ip_range_id": [self.ipv6_ranges[0].pk, self.ipv4_ranges[0].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_subnet(self):
        params = {
            "parent_subnet_id": [self.ipv6_subnets[0].pk, self.ipv6_subnets[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_subnet__iregex": r"ipv6-subnet-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_client_class(self):
        params = {"client_class_id": [self.client_classes[0].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"client_class": "client-class-2"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_require_client_classes(self):
        params = {
            "required_client_class_id": [
                self.client_classes[0].pk,
                self.client_classes[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 3)
        params = {"required_client_class__iregex": r"client-class-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 3)

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

    def test_client_class_definitions(self):
        params = {
            "client_class_definition_id": [
                self.client_classes[0].pk,
                self.client_classes[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 3)
        params = {"client_class_definition__iregex": r"client-class-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
