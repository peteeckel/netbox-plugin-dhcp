from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_dhcp.models import Subnet


__all__ = ("SubnetSerializer",)


class SubnetSerializer(NetBoxModelSerializer):
    class Meta:
        model = Subnet

        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "client_class_definitions",
            "client_class",
            "required_client_classes",
            "evaluate_additional_classes",
            "tags",
        )

        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
        )

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dhcp-api:subnet-detail"
    )

    def create(self, validated_data):
        client_class_definitions = validated_data.pop("client_class_definitions", None)
        required_client_classes = validated_data.pop("required_client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        subnet = super().create(validated_data)

        if client_class_definitions is not None:
            subnet.client_class_definitions.set(client_class_definitions)
        if required_client_classes is not None:
            subnet.required_client_classes.set(required_client_classes)
        if evaluate_additional_classes is not None:
            subnet.evaluate_additional_classes.set(evaluate_additional_classes)

        return subnet

    def update(self, instance, validated_data):
        client_class_definitions = validated_data.pop("client_class_definitions", None)
        required_client_classes = validated_data.pop("required_client_classes", None)
        evaluate_additional_classes = validated_data.pop(
            "evaluate_additional_classes", None
        )

        subnet = super().update(instance, validated_data)

        if client_class_definitions is not None:
            subnet.client_class_definitions.set(client_class_definitions)
        if required_client_classes is not None:
            subnet.required_client_classes.set(required_client_classes)
        if evaluate_additional_classes is not None:
            subnet.evaluate_additional_classes.set(evaluate_additional_classes)

        return subnet
