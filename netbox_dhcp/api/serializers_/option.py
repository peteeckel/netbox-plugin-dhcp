from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.fields import ContentTypeField
from utilities.api import get_serializer_for_model

from netbox_dhcp.models import Option

from .mixins import ClientClassAssignmentSerializerMixin


__all__ = ("OptionSerializer",)


OPTION_ASSIGNMENT_MODELS = Q(
    app_label="netbox_dhcp",
    model__in=[
        "dhcpserver",
        "subnet",
        "sharednetwork",
        "pool",
        "pdpool",
        "hostresevration",
        "clientclass",
    ],
)


class OptionSerializer(ClientClassAssignmentSerializerMixin, NetBoxModelSerializer):
    class Meta:
        model = Option

        fields = (
            "id",
            "url",
            "display",
            "definition",
            "description",
            "data",
            "csv_format",
            "always_send",
            "never_send",
            "assign_client_classes",
            "assigned_object",
            "assigned_object_type",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "data",
            "description",
            "csv_format",
            "always_send",
            "never_send",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:option-detail"
    )

    assigned_object_type = ContentTypeField(
        queryset=ContentType.objects.filter(OPTION_ASSIGNMENT_MODELS),
        required=False,
        allow_null=True,
    )
    assigned_object = serializers.SerializerMethodField(
        read_only=True,
    )

    @extend_schema_field(serializers.JSONField(allow_null=True))
    def get_assigned_object(self, obj):
        if obj.assigned_object is None:
            return None
        serializer = get_serializer_for_model(obj.assigned_object)
        context = {"request": self.context["request"]}
        return serializer(obj.assigned_object, nested=True, context=context).data
