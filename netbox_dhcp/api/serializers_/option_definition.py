from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import OptionDefinition


__all__ = ("OptionDefinitionSerializer",)


class OptionDefinitionSerializer(NetBoxModelSerializer):
    class Meta:
        model = OptionDefinition

        fields = (
            "id",
            "url",
            "display",
            "family",
            "space",
            "name",
            "code",
            "description",
            "type",
            "record_types",
            "encapsulate",
            "array",
            "standard",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:optiondefinition-detail"
    )
