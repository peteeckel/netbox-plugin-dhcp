from django.utils.translation import gettext_lazy as _

from utilities.choices import ChoiceSet


__all__ = ("DHCPServerStatusChoices",)


class DHCPServerStatusChoices(ChoiceSet):
    key = "DHCPServer.status"

    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    CHOICES = [
        (STATUS_ACTIVE, _("Active"), "blue"),
        (STATUS_INACTIVE, _("Inactive"), "red"),
    ]
