from django.utils.translation import gettext_lazy as _

from utilities.choices import ChoiceSet


__all__ = (
    "AllocatorTypeChoices",
    "PDAllocatorTypeChoices",
)


class AllocatorTypeChoices(ChoiceSet):
    key = "NetBoxDHCP.allocator_types"

    ITERATIVE = "iterative"
    RANDOM = "random"

    CHOICES = [
        (ITERATIVE, _("Iterative"), "red"),
        (RANDOM, _("Random"), "green"),
    ]


class PDAllocatorTypeChoices(AllocatorTypeChoices):
    key = "NetBoxDHCP.pd_allocator_types"

    FREE_LEASE_QUEUE = "flq"

    CHOICES = AllocatorTypeChoices.CHOICES + [
        (FREE_LEASE_QUEUE, _("Free Lease Queue"), "blue")
    ]
