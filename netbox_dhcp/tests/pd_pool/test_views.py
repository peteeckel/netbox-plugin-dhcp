from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import TestObjects, ModelViewTestCase
from netbox_dhcp.models import PDPool


class PDPoolViewTestCase(
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
    model = PDPool

    @classmethod
    def setUpTestData(cls):
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        client_classes = TestObjects.get_client_classes()

        pd_pools = (
            PDPool(
                name="test-pd-pool-1",
                description="Test Prefix Delegation Pool 1",
                prefix=ipv6_prefixes[0],
                delegated_length=64,
                excluded_prefix=ipv6_prefixes[1],
            ),
            PDPool(
                name="test-pd-pool-2",
                description="Test Prefix Delegation Pool 2",
                prefix=ipv6_prefixes[1],
                delegated_length=64,
            ),
            PDPool(
                name="test-pd-pool-3",
                description="Test Prefix Delegation Pool 3",
                prefix=ipv6_prefixes[2],
                delegated_length=64,
            ),
        )
        PDPool.objects.bulk_create(pd_pools)

        cls.form_data = {
            "name": "test-pd-pool-7",
            "description": "Test Prefix Delegation Pool 7",
            "prefix": ipv6_prefixes[0].pk,
            "delegated_length": 64,
            "excluded_prefix": ipv6_prefixes[1].pk,
            "required_client_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "client_class_definitions": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Bulk Update",
            "delegated_length": 56,
            "excluded_prefix": ipv6_prefixes[2].pk,
            "client_class": client_classes[0].pk,
            "required_client_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "client_class_definitions": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "user_context": '{"test_key": "test_value"}',
            "comment": "test comment",
        }

        cls.csv_data = (
            "name,description,prefix,delegated_length,excluded_prefix,client_class,required_client_classes,client_class_definitions,evaluate_additional_classes",  # noqa: E501
            f'test-pd-pool-4,Test Prefix Delegation Pool 4),{ipv6_prefixes[0].prefix},64,{ipv6_prefixes[1].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pd-pool-5,Test Prefix Delegation Pool 5),{ipv6_prefixes[1].prefix},64,{ipv6_prefixes[2].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pd-pool-6,Test Prefix Delegation Pool 6),{ipv6_prefixes[2].prefix},64,{ipv6_prefixes[0].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,prefix,delegated_length,excluded_prefix,client_class,required_client_classes,client_class_definitions,evaluate_additional_classes",  # noqa: E501
            f'{pd_pools[0].pk},Test Prefix Delegation Pool 4),{ipv6_prefixes[0].prefix},64,{ipv6_prefixes[1].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pd_pools[1].pk},Test Prefix Delegation Pool 5),{ipv6_prefixes[1].prefix},64,{ipv6_prefixes[2].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pd_pools[2].pk},Test Prefix Delegation Pool 6),{ipv6_prefixes[2].prefix},64,{ipv6_prefixes[0].prefix},{client_classes[0].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

    maxDiff = None
