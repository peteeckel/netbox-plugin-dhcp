from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import PDPool
from netbox_dhcp.filtersets import PDPoolFilterSet
from netbox_dhcp.tests.custom import TestObjects


class PDPoolFilterSetTestCase(
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = PDPool.objects.all()
    filterset = PDPoolFilterSet

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
        cls.ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        cls.ipv6_subnets = TestObjects.get_ipv6_subnets()
        cls.client_classes = TestObjects.get_client_classes()

        cls.pd_pools = (
            PDPool(
                name="test-pd-pool-1",
                description="Test Prefix Delegation Pool 1",
                prefix=cls.ipv6_prefixes[0],
                delegated_length=64,
                pool_id=42,
                excluded_prefix=cls.ipv6_prefixes[2],
            ),
            PDPool(
                name="test-pd-pool-2",
                description="Test Prefix Delegation Pool 2",
                prefix=cls.ipv6_prefixes[1],
                delegated_length=64,
                pool_id=23,
                excluded_prefix=cls.ipv6_prefixes[0],
            ),
            PDPool(
                name="test-pd-pool-3",
                description="Test Prefix Delegation Pool 3",
                prefix=cls.ipv6_prefixes[2],
                delegated_length=56,
                pool_id=1337,
                excluded_prefix=cls.ipv6_prefixes[1],
            ),
        )
        PDPool.objects.bulk_create(cls.pd_pools)

        for number in range(3):
            cls.ipv6_subnets[number].child_pd_pools.add(cls.pd_pools[number])
            cls.pd_pools[number].client_classes.add(
                cls.client_classes[(number + 1) % 3]
            )
            cls.pd_pools[number].evaluate_additional_classes.add(
                cls.client_classes[(number + 2) % 3]
            )

    def test_name(self):
        params = {"name__iregex": r"test-pd-pool-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"name": "test-pd-pool-3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_description(self):
        params = {"description__iregex": r"Test Prefix Delegation Pool [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"description": "Test Prefix Delegation Pool 3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_pool_id(self):
        params = {"pool_id": 42}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"pool_id__gt": 42}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_prefix(self):
        params = {"prefix_id": [self.ipv6_prefixes[0].pk, self.ipv6_prefixes[1].pk]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"prefix__iregex": r"2001:db8:[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_delegated_length(self):
        params = {"delegated_length": 64}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"delegated_length__lt": 64}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_excluded_prefix(self):
        params = {
            "excluded_prefix_id": [self.ipv6_prefixes[0].pk, self.ipv6_prefixes[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"excluded_prefix__iregex": r"2001:db8:[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_parent_subnet(self):
        params = {
            "parent_subnet_id": [self.ipv6_subnets[0].pk, self.ipv6_subnets[1].pk]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"parent_subnet__iregex": r"ipv6-subnet-[23]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_client_classes(self):
        params = {
            "client_class_id": [
                self.client_classes[0].pk,
                self.client_classes[1].pk,
            ]
        }
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
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
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
