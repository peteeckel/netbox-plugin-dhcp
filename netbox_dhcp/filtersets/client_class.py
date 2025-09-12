from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from ..models import ClientClass


__all__ = ("ClientClassFilterSet",)


class ClientClassFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = ClientClass

        fields = (
            "id",
            "name",
            "description",
            "test",
            "template_test",
            "only_if_required",
            "only_in_additional_list",
            "next_server",
            "server_hostname",
            "boot_file_name",
            "comment",
            "offer_lifetime",
            "valid_lifetime",
            "min_valid_lifetime",
            "max_valid_lifetime",
            "preferred_lifetime",
            "min_preferred_lifetime",
            "max_preferred_lifetime",
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(test__icontains=value)
            | Q(template_test__icontains=value)
            | Q(boot_file_name__icontains=value)
            | Q(comment__icontains=value)
        )
        return queryset.filter(qs_filter)
