from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import ClientClass


__all__ = ("ClientClassSerializer",)


class ClientClassSerializer(NetBoxModelSerializer):
    class Meta:
        model = ClientClass

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "user_context",
            "comment",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "test",
            "template_test",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:clientclass-detail"
    )
