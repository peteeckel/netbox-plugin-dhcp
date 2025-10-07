from django.test import TestCase

from utilities.testing import ChangeLoggedFilterSetTests

from netbox_dhcp.models import ClientClass
from netbox_dhcp.filtersets import ClientClassFilterSet
from netbox_dhcp.tests.custom import (
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
)


class ClientClassFilterSetTestCase(
    BOOTPFilterSetTests,
    ValidLifetimeFilterSetTests,
    OfferLifetimeFilterSetTests,
    PreferredLifetimeFilterSetTests,
    TestCase,
    ChangeLoggedFilterSetTests,
):
    queryset = ClientClass.objects.all()
    filterset = ClientClassFilterSet

    ignore_fields = (
        "user_context",
        "comment",
        "assign_options",
        "assign_hostreservations",
        "parent_dhcpservers",
        "definition_pdpools",
        "require_pdpools",
        "evaluate_pdpools",
        "definition_pools",
        "require_pools",
        "evaluate_pools",
        "definition_sharednetworks",
        "require_sharednetworks",
        "evaluate_sharednetworks",
        "definition_subnets",
        "require_subnets",
        "evaluate_subnets",
    )

    @classmethod
    def setUpTestData(cls):
        client_classs = (
            ClientClass(
                name="test-client-class-1",
                description="Test Client Class 1",
                test="substring(option[61].hex,0,3) == 'foo'",
                template_test="substring(option[23].hex,0,3)",
                only_if_required=False,
                only_in_additional_list=False,
                **BOOTPFilterSetTests.DATA[0],
                **ValidLifetimeFilterSetTests.DATA[0],
                **PreferredLifetimeFilterSetTests.DATA[0],
                **OfferLifetimeFilterSetTests.DATA[0],
            ),
            ClientClass(
                name="test-client-class-2",
                description="Test Client Class 2",
                test="substring(option[61].hex,0,3) == 'bar'",
                template_test="substring(option[42].hex,0,3)",
                only_if_required=True,
                only_in_additional_list=True,
                **BOOTPFilterSetTests.DATA[1],
                **ValidLifetimeFilterSetTests.DATA[1],
                **PreferredLifetimeFilterSetTests.DATA[1],
                **OfferLifetimeFilterSetTests.DATA[1],
            ),
            ClientClass(
                name="test-client-class-3",
                description="Test Client Class 3",
                test="substring(option[61].hex,0,3) == 'baz'",
                template_test="substring(option[66].hex,0,3)",
                only_if_required=False,
                only_in_additional_list=True,
                **BOOTPFilterSetTests.DATA[2],
                **ValidLifetimeFilterSetTests.DATA[2],
                **PreferredLifetimeFilterSetTests.DATA[2],
                **OfferLifetimeFilterSetTests.DATA[2],
            ),
        )
        ClientClass.objects.bulk_create(client_classs)

    def test_name(self):
        params = {"name__iregex": r"test-client-class-[12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"name": "test-client-class-3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_description(self):
        params = {"description__iregex": r"Test Client Class [12]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"description": "Test Client Class 3"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_test(self):
        params = {"test__iregex": r"== '(foo|bar)'"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"test": "substring(option[61].hex,0,3) == 'baz'"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_template_test(self):
        params = {"template_test__iregex": r"\[(23|42)\]"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"template_test": "substring(option[66].hex,0,3)"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_only_if_required(self):
        params = {"only_if_required": True}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"only_if_required": False}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_only_in_additional_list(self):
        params = {"only_in_additional_list": True}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
        params = {"only_in_additional_list": False}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
