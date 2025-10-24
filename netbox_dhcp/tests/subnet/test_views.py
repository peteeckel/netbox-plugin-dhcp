from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import (
    TestObjects,
    ModelViewTestCase,
)
from netbox_dhcp.models import Subnet


class SubnetViewTestCase(
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
    model = Subnet

    @classmethod
    def setUpTestData(cls):
        ipv4_prefixes = TestObjects.get_ipv4_prefixes()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        client_classes = TestObjects.get_client_classes()
        ipv6_subnets = TestObjects.get_ipv6_subnets()
        host_reservations = TestObjects.get_host_reservations()

        subnets = (
            Subnet(
                name="test-subnet-1",
                description="Test Subnet 1",
                prefix=ipv4_prefixes[0],
            ),
            Subnet(
                name="test-subnet-2",
                description="Test Subnet 2",
                prefix=ipv4_prefixes[1],
            ),
            Subnet(
                name="test-subnet-3",
                description="Test Subnet 3",
                prefix=ipv4_prefixes[2],
            ),
        )
        Subnet.objects.bulk_create(subnets)

        cls.form_data = {
            "name": "test-subnet-4",
            "description": "Test Subnet 4",
            "prefix": ipv6_prefixes[0].pk,
            "client_classes": [client_class.pk for client_class in client_classes[0:2]],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
            "child_subnets": [ipv6_subnets[1].pk],
            "child_host_reservations": [
                host_reservation.pk for host_reservation in host_reservations[0:2]
            ],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "client_classes": [client_classes[0].pk],
            "evaluate_additional_classes": [client_classes[2].pk],
        }

        cls.csv_data = (
            "name,description,prefix,client_classes,evaluate_additional_classes,child_subnets",  # noqa: E501
            f'test-shared-network-4,Test Subnet 4,{ipv4_prefixes[0].prefix},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}","{subnets[0].name},{subnets[2].name}"',  # noqa: E501
            f'test-shared-network-5,Test Subnet 5,{ipv4_prefixes[1].prefix},"{client_classes[1].name},{client_classes[2].name}","{client_classes[2].name},{client_classes[0].name}","{subnets[1].name},{subnets[0].name}"',  # noqa: E501
            f'test-shared-network-6,Test Subnet 6,{ipv4_prefixes[2].prefix},"{client_classes[2].name},{client_classes[0].name}","{client_classes[0].name},{client_classes[1].name}","{subnets[2].name},{subnets[1].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,client_classes,evaluate_additional_classes,child_subnets",  # noqa: E501
            f'{subnets[0].pk},Test Subnet 1 (updated),"{client_classes[1].name},{client_classes[2].name}","{client_classes[1].name},{client_classes[2].name}","{subnets[1].name},{subnets[0].name}"',  # noqa: E501
            f'{subnets[1].pk},Test Subnet 2 (updated),"{client_classes[2].name},{client_classes[0].name}","{client_classes[2].name},{client_classes[0].name}","{subnets[2].name},{subnets[1].name}"',  # noqa: E501
            f'{subnets[2].pk},Test Subnet 3 (updated),"{client_classes[0].name},{client_classes[1].name}","{client_classes[0].name},{client_classes[1].name}","{subnets[0].name},{subnets[2].name}"',  # noqa: E501
        )
