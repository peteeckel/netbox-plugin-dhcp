from utilities.testing import ViewTestCases

from netbox_dhcp.tests.custom import (
    ModelViewTestCase,
)
from netbox_dhcp.models import ClientClass


class ClientClassViewTestCase(
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
    model = ClientClass

    @classmethod
    def setUpTestData(cls):
        client_classes = (
            ClientClass(
                name="test-client-class-1",
                description="Test Client Class 1",
            ),
            ClientClass(
                name="test-client-class-2",
                description="Test Client Class 2",
            ),
            ClientClass(
                name="test-client-class-3",
                description="Test Client Class 3",
            ),
        )
        ClientClass.objects.bulk_create(client_classes)

        cls.form_data = {
            "name": "test-client-class-4",
            "description": "Test Client Class 4",
            "test": "substring(option[61].hex,0,3) == 'foo'",
            "only_in_additional_list": False,
        }

        cls.bulk_edit_data = {
            "description": "Test Description Update",
            "test": "substring(option[61].hex,0,3) == 'bar'",
            "template_test": "",
            "only_in_additional_list": False,
        }

        cls.csv_data = (
            "name,description,test,template_test,only_in_additional_list",
            "test-client-class-5,Test Client Class 5,\"substring(option[42].hex,0,3) == 'baz'\",,true",
            "test-client-class-6,Test Client Class 6,\"substring(option[23].hex,0,3) == 'foo'\",,false",
            'test-client-class-7,Test Client Class 7,,"substring(option[23].hex,0,3)",true',
        )

        cls.csv_update_data = (
            "id,name,description,test,template_test,only_in_additional_list",
            f"{client_classes[0].pk},test-client-class-5,Test Client Class 5,\"substring(option[42].hex,0,3) == 'baz'\",,true",  # noqa: E501
            f"{client_classes[1].pk},test-client-class-6,Test Client Class 6,\"substring(option[23].hex,0,3) == 'foo'\",,false",  # noqa: E501
            f'{client_classes[2].pk},test-client-class-7,Test Client Class 7,,"substring(option[23].hex,0,3)",true',  # noqa: E501
        )

    maxDiff = None
