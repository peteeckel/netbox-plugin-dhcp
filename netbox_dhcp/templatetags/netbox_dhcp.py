from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.inclusion_tag("netbox_dhcp/inc/null_checkmark.html")
def null_checkmark(value, true=_("Yes"), false=_("No")):
    return {
        "value": value,
        "true_label": true,
        "false_label": false,
    }
