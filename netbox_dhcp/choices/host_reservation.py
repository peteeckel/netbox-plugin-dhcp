from django.utils.translation import gettext_lazy as _

from utilities.choices import ChoiceSet


__all__ = ("HostReservationIdentifierChoices",)


class HostReservationIdentifierChoices(ChoiceSet):
    key = "HostReservation.identifiers"

    CIRCUIT_ID = "circuit-id"
    HW_ADDRESS = "hw-address"
    DUID = "duid"
    CLIENT_ID = "client-id"

    CHOICES = [
        (CIRCUIT_ID, _("Circuit ID"), "red"),
        (HW_ADDRESS, _("Hardware Address"), "green"),
        (DUID, "DUID", "blue"),
        (CLIENT_ID, _("Client ID"), "orange"),
    ]
