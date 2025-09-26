import json
from pathlib import Path

from django.db import migrations

IMPORT_FILE = Path(__file__).parent / "initial_data" / "option_definitions.json"


def load_option_definitions(apps, schema_editor):
    OptionDefinition = apps.get_model("netbox_dhcp", "OptionDefinition")
    db_alias = schema_editor.connection.alias

    with IMPORT_FILE.open("r") as initial_data:
        try:
            for definition in json.load(initial_data):
                OptionDefinition.objects.using(db_alias).create(
                    standard=True, **definition
                )
        except Exception as exc:
            print(f"Error loading initiall data from {IMPORT_FILE}")
            raise exc


class Migration(migrations.Migration):
    dependencies = [
        ("netbox_dhcp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_option_definitions),
    ]
