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
        dhcp_servers = TestObjects.get_dhcp_servers()
        ipv4_prefixes = TestObjects.get_ipv4_prefixes()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        client_classes = TestObjects.get_client_classes()

        subnets = (
            Subnet(
                name="test-subnet-1",
                dhcp_server=dhcp_servers[0],
                description="Test Subnet 1",
                prefix=ipv4_prefixes[0],
            ),
            Subnet(
                name="test-subnet-2",
                dhcp_server=dhcp_servers[0],
                description="Test Subnet 2",
                prefix=ipv4_prefixes[1],
            ),
            Subnet(
                name="test-subnet-3",
                dhcp_server=dhcp_servers[0],
                description="Test Subnet 3",
                prefix=ipv4_prefixes[2],
            ),
        )
        Subnet.objects.bulk_create(subnets)

        cls.form_data = {
            "name": "test-subnet-4",
            "description": "Test Subnet 4",
            "dhcp_server": dhcp_servers[0].pk,
            "prefix": ipv6_prefixes[0].pk,
            "client_classes": [client_class.pk for client_class in client_classes[0:2]],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "client_classes": [client_classes[0].pk],
            "evaluate_additional_classes": [client_classes[2].pk],
        }

        cls.csv_data = (
            "name,dhcp_server,description,prefix,client_classes,evaluate_additional_classes",  # noqa: E501
            f'test-shared-network-4,{dhcp_servers[1].name},Test Subnet 4,{ipv4_prefixes[0].prefix},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-shared-network-5,{dhcp_servers[1].name},Test Subnet 5,{ipv4_prefixes[1].prefix},"{client_classes[1].name},{client_classes[2].name}","{client_classes[2].name},{client_classes[0].name}"',  # noqa: E501
            f'test-shared-network-6,{dhcp_servers[1].name},Test Subnet 6,{ipv4_prefixes[2].prefix},"{client_classes[2].name},{client_classes[0].name}","{client_classes[0].name},{client_classes[1].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,client_classes,evaluate_additional_classes",  # noqa: E501
            f'{subnets[0].pk},Test Subnet 1 (updated),"{client_classes[1].name},{client_classes[2].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{subnets[1].pk},Test Subnet 2 (updated),"{client_classes[2].name},{client_classes[0].name}","{client_classes[2].name},{client_classes[0].name}"',  # noqa: E501
            f'{subnets[2].pk},Test Subnet 3 (updated),"{client_classes[0].name},{client_classes[1].name}","{client_classes[0].name},{client_classes[1].name}"',  # noqa: E501
        )
