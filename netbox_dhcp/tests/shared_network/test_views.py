from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    ModelViewTestCase,
)
from netbox_dhcp.models import SharedNetwork


class SharedNetworkViewTestCase(
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
    model = SharedNetwork

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

        cls.form_data = {
            "name": "test-shared-network-4",
            "description": "Test Shared Network 4",
            "prefix": ipv6_prefixes[0].pk,
            "client_class": client_classes[0].pk,
            "client_class_definitions": [
                client_class.pk for client_class in client_classes[0:2]
            ],
            "required_client_classes": [
                client_class.pk for client_class in client_classes[1:3]
            ],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
            "child_subnets": [subnets[0].pk],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "prefix": ipv6_prefixes[1].pk,
            "client_class_definitions": [client_classes[0].pk],
            "required_client_classes": [client_classes[1].pk],
            "evaluate_additional_classes": [client_classes[2].pk],
            "child_subnets": [subnet.pk for subnet in subnets[0:2]],
        }

        cls.csv_data = (
            "name,description,prefix,client_class_definitions,required_client_classes,evaluate_additional_classes,child_subnets",  # noqa: E501
            f'test-shared-network-4,Test Shared Network 4,{ipv4_prefixes[0].prefix},{client_classes[0].name},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}","{subnets[0].name},{subnets[2].name}"',  # noqa: E501
            f'test-shared-network-5,Test Shared Network 5,{ipv4_prefixes[1].prefix},{client_classes[1].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[2].name},{client_classes[0].name}","{subnets[1].name},{subnets[0].name}"',  # noqa: E501
            f'test-shared-network-6,Test Shared Network 6,{ipv4_prefixes[2].prefix},{client_classes[2].name},"{client_classes[2].name},{client_classes[0].name}","{client_classes[0].name},{client_classes[1].name}","{subnets[2].name},{subnets[1].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,client_class_definitions,required_client_classes,evaluate_additional_classes,child_subnets",  # noqa: E501
            f'{shared_networks[0].pk},Test Shared Network 1 (updated),{client_classes[1].name},"{client_classes[1].name},{client_classes[2].name}","{client_classes[2].name},{client_classes[0].name}","{subnets[1].name},{subnets[0].name}"',  # noqa: E501
            f'{shared_networks[1].pk},Test Shared Network 2 (updated),{client_classes[2].name},"{client_classes[2].name},{client_classes[0].name}","{client_classes[0].name},{client_classes[1].name}","{subnets[2].name},{subnets[1].name}"',  # noqa: E501
            f'{shared_networks[2].pk},Test Shared Network 3 (updated),{client_classes[0].name},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}","{subnets[0].name},{subnets[2].name}"',  # noqa: E501
        )

    maxDiff = None
