from django.utils.translation import gettext_lazy as _

from netbox.plugins import PluginConfig

__version__ = "0.0.8"


class DHCPConfig(PluginConfig):
    name = "netbox_dhcp"
    verbose_name = _("NetBox DHCP")
    description = _("NetBox plugin for DHCP")
    min_version = "4.3.7"
    version = __version__
    author = "Peter Eckel, sys4 AG"
    author_email = "pe@sys4.de"
    required_settings = []
    default_settings = {}
    base_url = "netbox-dhcp"


#
# Initialize plugin config
#
config = DHCPConfig
