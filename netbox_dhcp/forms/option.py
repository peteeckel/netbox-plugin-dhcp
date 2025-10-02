from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms.fields import TagFilterField, CSVModelChoiceField, CSVChoiceField
from utilities.forms.rendering import FieldSet
from utilities.forms import add_blank_choice, BOOLEAN_WITH_BLANK_CHOICES
from ipam.choices import IPAddressFamilyChoices

from netbox_dhcp.models import (
    Option,
    OptionDefinition,
    DHCPServer,
    Subnet,
    SharedNetwork,
    Pool,
    PDPool,
    HostReservation,
    ClientClass,
)
from netbox_dhcp.choices import OptionSpaceChoices

from .mixins import (
    ClientClassAssignmentFormMixin,
    ClientClassAssignmentImportFormMixin,
    ClientClassAssignmentFilterFormMixin,
    ClientClassAssignmentBulkEditFormMixin,
)


__all__ = (
    "OptionForm",
    "OptionFilterForm",
    "OptionImportForm",
    "OptionBulkEditForm",
)


class OptionForm(ClientClassAssignmentFormMixin, NetBoxModelForm):
    class Meta:
        model = Option

        fields = (
            "definition",
            "description",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            "tags",
        )

    fieldsets = (
        FieldSet(
            "definition",
            "description",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            name=_("Option"),
        ),
        FieldSet(
            "assign_client_classes",
            name=_("Assignment"),
        ),
        FieldSet(
            "tags",
            name=_("Tags"),
        ),
    )

    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )


class OptionFilterForm(ClientClassAssignmentFilterFormMixin, NetBoxModelFilterSetForm):
    model = Option

    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "name",
            "description",
            "family",
            "space",
            "code",
            "definition_id",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_class_id",
            name=_("Option"),
        ),
    )

    name = forms.CharField(
        label=_("Name"),
        required=False,
    )
    description = forms.CharField(
        label=_("Description"),
        required=False,
    )
    family = forms.ChoiceField(
        label=_("Address Family"),
        choices=add_blank_choice(IPAddressFamilyChoices),
        required=False,
    )
    space = forms.ChoiceField(
        label=_("Space"),
        choices=add_blank_choice(OptionSpaceChoices),
        required=False,
    )
    data = forms.CharField(
        label=_("Data"),
        help_text=_("Case-insensitive substring match"),
        required=False,
    )
    code = forms.CharField(
        label=_("Code"),
        required=False,
    )
    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )

    tag = TagFilterField(Option)


class OptionImportForm(ClientClassAssignmentImportFormMixin, NetBoxModelImportForm):
    class Meta:
        model = Option

        fields = (
            "definition",
            "space",
            "name",
            "code",
            "dhcp_server",
            "subnet",
            "shared_network",
            "pool",
            "pd_pool",
            "host_reservation",
            "client_class",
            "description",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            "tags",
        )

    definition = CSVModelChoiceField(
        label=_("Definition"),
        queryset=OptionDefinition.objects.all(),
        required=False,
    )
    space = CSVChoiceField(
        label=_("Space"),
        choices=OptionSpaceChoices,
        required=True,
    )
    name = CSVModelChoiceField(
        label=_("Name"),
        queryset=OptionDefinition.objects.all(),
        required=False,
        to_field_name="name",
        error_messages={
            "invalid_choice": _("No option definition with name %(value)s found"),
        },
    )
    code = CSVModelChoiceField(
        label=_("Code"),
        queryset=OptionDefinition.objects.all(),
        required=False,
        to_field_name="code",
        error_messages={
            "invalid_choice": _("No option definition with code %(value)s found"),
        },
        help_text=_("If code is present, name will be ignored"),
    )

    dhcp_server = CSVModelChoiceField(
        label=_("DHCP Server"),
        queryset=DHCPServer.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("DHCP Server %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    subnet = CSVModelChoiceField(
        label=_("Subnet"),
        queryset=Subnet.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Subnet %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    shared_network = CSVModelChoiceField(
        label=_("Shared Network"),
        queryset=SharedNetwork.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Shared network %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    pool = CSVModelChoiceField(
        label=_("Pool"),
        queryset=Pool.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Pool %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    pd_pool = CSVModelChoiceField(
        label=_("Prefix Delegation Pool"),
        queryset=PDPool.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Prefix delegation pool %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    host_reservation = CSVModelChoiceField(
        label=_("Host Reservation"),
        queryset=HostReservation.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Host reservation %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )
    client_class = CSVModelChoiceField(
        label=_("Client Class"),
        queryset=ClientClass.objects.all(),
        to_field_name="name",
        required=False,
        error_messages={
            "invalid_choice": _("Client class %(value)s not found"),
        },
        help_text=_(
            "Specify exactly one of dhcp_server, subnet, shared_network, "
            "pool, pd_pool, host_reservation or client_class per line"
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.is_bound and "space" in self.data:
            self.fields["code"].queryset = OptionDefinition.objects.filter(
                space=self.data.get("space")
            )
            self.fields["name"].queryset = OptionDefinition.objects.filter(
                space=self.data.get("space")
            )

        del self.fields["definition"]

    def clean(self):
        super().clean()

        name = self.cleaned_data.get("name")
        code = self.cleaned_data.get("code")

        self.cleaned_data["definition"] = code if code else name

        objects = [
            self.cleaned_data.get(object_name)
            for object_name in (
                "dhcp_server",
                "subnet",
                "shared_network",
                "pool",
                "pd_pool",
                "host_reservation",
                "client_class",
            )
            if self.cleaned_data.get(object_name) is not None
        ]
        if len(objects) != 1:
            raise forms.ValidationError(_("Exactly one assigned object is required"))

        self.cleaned_data["assigned_object"] = objects[0]

        return self.cleaned_data

    def save(self, *args, **kwargs):
        self.instance.definition = self.cleaned_data.get("definition")
        self.instance.assigned_object = self.cleaned_data.get("assigned_object")

        return super().save(*args, **kwargs)


class OptionBulkEditForm(
    ClientClassAssignmentBulkEditFormMixin, NetBoxModelBulkEditForm
):
    model = Option

    fieldsets = (
        FieldSet(
            "definition",
            "description",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            name=_("Option"),
        ),
    )

    nullable_fields = (
        "data",
        "description",
        "csv_format",
        "always_send",
        "never_send",
        "assign_client_classes",
    )

    description = forms.CharField(
        label=_("Description"),
        required=False,
    )
    definition = forms.ModelChoiceField(
        label=_("Option Definition"),
        queryset=OptionDefinition.objects.all(),
        required=False,
    )
    data = forms.CharField(
        label=_("Data"),
        required=False,
    )
    csv_format = forms.NullBooleanField(
        label=_("CSV Format"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    always_send = forms.NullBooleanField(
        label=_("Always Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    never_send = forms.NullBooleanField(
        label=_("Never Send"),
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
