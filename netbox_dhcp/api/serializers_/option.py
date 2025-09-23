from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import Option

from .mixins import ClientClassAssignmentSerializerMixin


__all__ = ("OptionSerializer",)


class OptionSerializer(ClientClassAssignmentSerializerMixin, NetBoxModelSerializer):
    class Meta:
        model = Option

        fields = (
            "id",
            "url",
            "display",
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "definition",
            "data",
            "csv_format",
            "always_send",
            "never_send",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:option-detail"
    )
