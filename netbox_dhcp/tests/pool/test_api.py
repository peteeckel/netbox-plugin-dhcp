from utilities.testing import APIViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import Pool


class PoolAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    NetBoxDHCPGraphQLMixin,
    APIViewTestCases.GraphQLTestCase,
):
    model = Pool

    brief_fields = [
        "comment",
        "description",
        "display",
        "id",
        "ip_range",
        "name",
        "url",
    ]

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

        cls.create_data = [
            {
                "name": "test-pool-5",
                "description": "Test Pool 5",
                "ip_range": ipv4_ranges[2].pk,
                "client_class": client_classes[0].pk,
                "client_class_definitions": [
                    client_class.pk for client_class in client_classes
                ],
            },
            {
                "name": "test-pool-6",
                "description": "Test Pool 6",
                "ip_range": ipv6_ranges[2].pk,
                "client_class": client_classes[1].pk,
                "client_class_definitions": [
                    client_class.pk for client_class in client_classes
                ],
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "client_class": client_classes[2].pk,
            "required_client_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "client_class_definitions": [],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
        }
