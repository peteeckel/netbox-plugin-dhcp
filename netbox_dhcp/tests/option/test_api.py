from utilities.testing import APIViewTestCases
from django.contrib.contenttypes.models import ContentType

from netbox_dhcp.tests.custom import (
    TestObjects,
    APITestCase,
    NetBoxDHCPGraphQLMixin,
)
from netbox_dhcp.models import Option, OptionDefinition, DHCPServer
from netbox_dhcp.choices import OptionSpaceChoices


class OptionAPITestCase(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    NetBoxDHCPGraphQLMixin,
    APIViewTestCases.GraphQLTestCase,
):
    model = Option

    brief_fields = [
        "always_send",
        "csv_format",
        "data",
        "description",
        "display",
        "id",
        "never_send",
        "url",
    ]

    user_permissions = ("netbox_dhcp.view_optiondefinition",)

    @classmethod
    def setUpTestData(cls):
        cls.client_classes = TestObjects.get_client_classes()
        cls.dhcp_servers = TestObjects.get_dhcp_servers()
        cls.dhcp_server = cls.dhcp_servers[0]
        cls.dhcp_server_type = ContentType.objects.get_for_model(DHCPServer)
        cls.dhcp_server_contenttype = (
            f"{cls.dhcp_server_type.app_label}.{cls.dhcp_server_type.model}"
        )

        cls.option_definitions = (
            OptionDefinition.objects.get(
                space=OptionSpaceChoices.DHCPV4,
                name="routers",
            ),
            OptionDefinition.objects.get(
                space=OptionSpaceChoices.DHCPV4,
                name="domain-name-servers",
            ),
            OptionDefinition.objects.get(
                space=OptionSpaceChoices.DHCPV4,
                name="interface-mtu",
            ),
            OptionDefinition.objects.get(
                space=OptionSpaceChoices.DHCPV4,
                name="ip-forwarding",
            ),
        )

        cls.options = (
            Option(
                description="Test Option 1",
                definition=cls.option_definitions[3],
                assigned_object=cls.dhcp_server,
                data="true",
                always_send=False,
                never_send=False,
            ),
            Option(
                description="Test Option 2",
                definition=cls.option_definitions[2],
                assigned_object=cls.dhcp_server,
                data="1480",
                always_send=False,
                never_send=True,
            ),
            Option(
                description="Test Option 3",
                definition=cls.option_definitions[2],
                assigned_object=cls.dhcp_server,
                data="1320",
                always_send=True,
                never_send=False,
            ),
        )
        Option.objects.bulk_create(cls.options)

        cls.create_data = [
            {
                "definition": cls.option_definitions[0].pk,
                "description": "Test Option 4",
                "assigned_object_id": cls.dhcp_server.pk,
                "assigned_object_type": cls.dhcp_server_contenttype,
                "data": "192.0.2.1, 192.0.2.2",
                "always_send": True,
                "never_send": False,
                "assign_client_classes": [
                    client_class.pk for client_class in cls.client_classes[0:2]
                ],
            },
            {
                "definition": cls.option_definitions[1].pk,
                "description": "Test Option 4",
                "assigned_object_id": cls.dhcp_server.pk,
                "assigned_object_type": cls.dhcp_server_contenttype,
                "data": "192.0.2.3, 192.0.2.4",
                "assign_client_classes": [cls.client_classes[2].pk],
            },
            {
                "definition": cls.option_definitions[2].pk,
                "description": "Test Option 4",
                "assigned_object_id": cls.dhcp_server.pk,
                "assigned_object_type": cls.dhcp_server_contenttype,
                "data": "1380",
                "always_send": False,
                "never_send": True,
            },
        ]

        cls.bulk_update_data = {
            "description": "Test Description Update",
            "assign_client_classes": [],
            "always_send": None,
            "never_send": None,
        }
