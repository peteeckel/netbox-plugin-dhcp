from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import TestObjects, ModelViewTestCase
from netbox_dhcp.models import Pool


class PoolViewTestCase(
    ModelViewTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.BulkImportObjectsViewTestCase,
    ViewTestCases.BulkEditObjectsViewTestCase,
    ViewTestCases.BulkDeleteObjectsViewTestCase,
):
    model = Pool

    @classmethod
    def setUpTestData(cls):
        client_classes = TestObjects.get_client_classes()
        ipv4_ranges = TestObjects.get_ipv4_ranges()
        ipv6_ranges = TestObjects.get_ipv6_ranges()

        pools = (
            Pool(
                name="test-pool-1",
                description="Test Pool 1",
                ip_range=ipv4_ranges[0],
            ),
            Pool(
                name="test-pool-2",
                description="Test Pool 2",
                ip_range=ipv4_ranges[1],
            ),
            Pool(
                name="test-pool-3",
                description="Test Pool 3",
                ip_range=ipv6_ranges[0],
            ),
            Pool(
                name="test-pool-4",
                description="Test Pool 4",
                ip_range=ipv6_ranges[1],
            ),
        )
        Pool.objects.bulk_create(pools)

        cls.form_data = {
            "name": "test-pool-5",
            "description": "Test Pool 5",
            "ip_range": ipv4_ranges[2].pk,
            "client_class": client_classes[0].pk,
            "client_class_definitions": [
                client_class.pk for client_class in client_classes
            ],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "client_class": client_classes[2].pk,
            "require_client_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "client_class_definitions": [],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
        }

        cls.csv_data = (
            "name,description,ip_range,client_class,require_client_classes,client_class_definitions,evaluate_additional_classes",  # noqa: E501
            f'test-pool-6,Test Pool 6,{ipv4_ranges[0].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pool-7,Test Pool 7,{ipv4_ranges[1].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pool-8,Test Pool 8,{ipv6_ranges[2].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,ip_range,client_class,require_client_classes,client_class_definitions,evaluate_additional_classes",  # noqa: E501
            f'{pools[0].pk},Test Pool 1 (updated),{ipv4_ranges[0].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pools[1].pk},Test Pool 2 (updated),{ipv4_ranges[1].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pools[2].pk},Test Pool 3 (updated),{ipv6_ranges[2].pk},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

    maxDiff = None
