from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import TestObjects, ModelViewTestCase
from netbox_dhcp.models import Pool, Subnet


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
        dhcp_servers = TestObjects.get_dhcp_servers()
        client_classes = TestObjects.get_client_classes()
        ipv4_prefixes = TestObjects.get_ipv4_prefixes()
        ipv6_prefixes = TestObjects.get_ipv6_prefixes()
        ipv4_ranges = TestObjects.get_ipv4_ranges()
        ipv6_ranges = TestObjects.get_ipv6_ranges()

        ipv4_subnet = Subnet.objects.create(
            name="test-ipv4-subnet-1",
            dhcp_server=dhcp_servers[0],
            prefix=ipv4_prefixes[0],
        )
        ipv6_subnet = Subnet.objects.create(
            name="test-ipv6-subnet-1",
            dhcp_server=dhcp_servers[0],
            prefix=ipv6_prefixes[0],
        )

        pools = (
            Pool(
                name="test-pool-1",
                description="Test Pool 1",
                subnet=ipv4_subnet,
                ip_range=ipv4_ranges[0],
            ),
            Pool(
                name="test-pool-2",
                description="Test Pool 2",
                subnet=ipv4_subnet,
                ip_range=ipv4_ranges[1],
            ),
            Pool(
                name="test-pool-3",
                description="Test Pool 3",
                subnet=ipv6_subnet,
                ip_range=ipv6_ranges[0],
            ),
            Pool(
                name="test-pool-4",
                description="Test Pool 4",
                subnet=ipv6_subnet,
                ip_range=ipv6_ranges[1],
            ),
        )
        Pool.objects.bulk_create(pools)

        cls.form_data = {
            "name": "test-pool-5",
            "description": "Test Pool 5",
            "weight": 100,
            "subnet": ipv4_subnet.pk,
            "ip_range": ipv4_ranges[2].pk,
            "client_classes": [client_class.pk for client_class in client_classes],
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "weight": 100,
            "subnet": ipv6_subnet.pk,
            "client_class": client_classes[2].pk,
            "client_classes": [],
            "evaluate_additional_classes": [
                client_class.pk for client_class in client_classes[0:2]
            ],
        }

        cls.csv_data = (
            "name,description,weight,subnet,ip_range,client_classes,evaluate_additional_classes",  # noqa: E501
            f'test-pool-6,Test Pool 6,100,{ipv4_subnet.name},{ipv4_ranges[0].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pool-7,Test Pool 7,23,{ipv4_subnet.name},{ipv4_ranges[1].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'test-pool-8,Test Pool 8,42,{ipv6_subnet.name},{ipv6_ranges[2].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

        cls.csv_update_data = (
            "id,description,weight,ip_range,client_classes,evaluate_additional_classes",  # noqa: E501
            f'{pools[0].pk},Test Pool 1 (updated),42,{ipv4_ranges[0].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pools[1].pk},Test Pool 2 (updated),23,{ipv4_ranges[1].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
            f'{pools[2].pk},Test Pool 3 (updated),100,{ipv6_ranges[2].pk},"{client_classes[0].name},{client_classes[1].name}","{client_classes[1].name},{client_classes[2].name}"',  # noqa: E501
        )

    maxDiff = None
