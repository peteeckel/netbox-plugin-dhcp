import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, ChoiceFieldColumn

from netbox_dhcp.models import OptionDefinition

from .mixins import NetBoxDHCPTableMixin

__all__ = ("OptionDefinitionTable",)


class OptionDefinitionTable(NetBoxDHCPTableMixin, NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = OptionDefinition

        fields = (
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
        )

        default_columns = (
            "space",
            "name",
            "code",
        )

    space = ChoiceFieldColumn(
        verbose_name=_("Space"),
    )
    code = tables.Column(
        verbose_name=_("Option Code"),
    )
    type = ChoiceFieldColumn(
        verbose_name=_("Data Type"),
    )
    record_types = tables.TemplateColumn(
        verbose_name=_("Record Types"),
        template_code="{% for record_type in value %}{% badge record_type %}{% endfor %}",
    )
