from utilities.testing import APIViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import PDPool


class PDPoolAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    NetBoxDHCPGraphQLMixin,
    APIViewTestCases.GraphQLTestCase,
):
    model = PDPool

    brief_fields = [
        "comment",
        "description",
        "display",
        "id",
        "name",
        "prefix",
        "url",
    ]

    @classmethod
    def setUpTestData(cls):
        client_classes = TestObjects.get_client_classes()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()

        pd_pools = (
            PDPool(
                name="test-pd-pool-1",
                description="Test Prefix Delegation Pool 1",
                prefix=ipv6_prefixes[0],
                delegated_length=64,
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

        cls.create_data = [
            {
                "name": "test-pd-pool-4",
                "description": "Test Prefix Delegation Pool 4",
                "prefix": ipv6_prefixes[0].pk,
                "delegated_length": 64,
                "excluded_prefix": ipv6_prefixes[1].pk,
                "client_class": client_classes[0].pk,
                "require_client_classes": [
                    client_class.pk for client_class in client_classes[1:3]
                ],
            },
            {
                "name": "test-pd-pool-5",
                "description": "Test Prefix Delegation Pool 5",
                "prefix": ipv6_prefixes[1].pk,
                "delegated_length": 64,
                "client_class": client_classes[1].pk,
            },
            {
                "name": "test-pd-pool-6",
                "description": "Test Prefix Delegation Pool 6",
                "prefix": ipv6_prefixes[2].pk,
                "delegated_length": 64,
                "client_class": client_classes[1].pk,
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "client_class": client_classes[0].pk,
            "require_client_classes": [
                client_class.pk for client_class in client_classes
            ],
        }
