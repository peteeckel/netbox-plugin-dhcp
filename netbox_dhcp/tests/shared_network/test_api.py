from utilities.testing import APIViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import SharedNetwork


class SharedNetworkAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    NetBoxDHCPGraphQLMixin,
    APIViewTestCases.GraphQLTestCase,
):
    model = SharedNetwork

    brief_fields = [
        "description",
        "display",
        "id",
        "name",
        "url",
    ]

    @classmethod
    def setUpTestData(cls):
        ipv4_prefixes = TestObjects.get_ipv4_prefixes()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        client_classes = TestObjects.get_client_classes()
        subnets = TestObjects.get_ipv6_subnets()

        shared_networks = (
            SharedNetwork(
                name="test-shared-network-1",
                description="Test Shared Network 1",
                prefix=ipv4_prefixes[0],
            ),
            SharedNetwork(
                name="test-shared-network-2",
                description="Test Shared Network 2",
                prefix=ipv4_prefixes[1],
            ),
            SharedNetwork(
                name="test-shared-network-3",
                description="Test Shared Network 3",
                prefix=ipv4_prefixes[2],
            ),
        )
        SharedNetwork.objects.bulk_create(shared_networks)

        cls.create_data = [
            {
                "name": "test-shared-network-4",
                "description": "Test Shared Network 4",
                "prefix": ipv6_prefixes[0].pk,
                "client_class": client_classes[0].pk,
                "client_class_definitions": [
                    client_class.pk for client_class in client_classes[0:2]
                ],
                "require_client_classes": [
                    client_class.pk for client_class in client_classes[1:3]
                ],
                "evaluate_additional_classes": [
                    client_class.pk for client_class in client_classes[0:2]
                ],
                "child_subnets": [subnets[0].pk],
            },
            {
                "name": "test-shared-network-5",
                "description": "Test Shared Network 5",
                "prefix": ipv6_prefixes[1].pk,
                "client_class_definitions": [
                    client_class.pk for client_class in client_classes[1:3]
                ],
                "require_client_classes": [
                    client_class.pk for client_class in client_classes[0:3]
                ],
                "evaluate_additional_classes": [
                    client_class.pk for client_class in client_classes[0:2]
                ],
                "child_subnets": [subnets[0].pk, subnets[1].pk],
            },
            {
                "name": "test-shared-network-6",
                "description": "Test Shared Network 6",
                "prefix": ipv6_prefixes[2].pk,
                "client_class_definitions": [
                    client_class.pk for client_class in client_classes[0:3]
                ],
                "require_client_classes": [
                    client_class.pk for client_class in client_classes[1:3]
                ],
                "evaluate_additional_classes": [
                    client_class.pk for client_class in client_classes[1:2]
                ],
                "child_subnets": [subnet.pk for subnet in subnets],
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "prefix": ipv6_prefixes[1].pk,
            "client_class_definitions": [client_classes[0].pk],
            "require_client_classes": [client_classes[1].pk],
            "evaluate_additional_classes": [client_classes[2].pk],
            "child_subnets": [subnet.pk for subnet in subnets[0:2]],
        }
