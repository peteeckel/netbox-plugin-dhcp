# NetBox DHCP

The NetBox DHCP plugin will enable NetBox to manage operational DHCP data.

<div align="center">
<a href="https://pypi.org/project/netbox-plugin-dhcp/"><img src="https://img.shields.io/pypi/v/netbox-plugin-dhcp" alt="PyPi"/></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/stargazers"><img src="https://img.shields.io/github/stars/sys4/netbox-plugin-dhcp?style=flat" alt="Stars Badge"/></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/network/members"><img src="https://img.shields.io/github/forks/sys4/netbox-plugin-dhcp?style=flat" alt="Forks Badge"/></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/issues"><img src="https://img.shields.io/github/issues/sys4/netbox-plugin-dhcp" alt="Issues Badge"/></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/pulls"><img src="https://img.shields.io/github/issues-pr/sys4/netbox-plugin-dhcp" alt="Pull Requests Badge"/></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/sys4/netbox-plugin-dhcp?color=2b9348"></a>
<a href="https://github.com/sys4/netbox-plugin-dhcp/blob/master/LICENSE"><img src="https://img.shields.io/github/license/sys4/netbox-plugin-dhcp?color=2b9348" alt="License Badge"/></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style Black"/></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads" src="https://static.pepy.tech/badge/netbox-plugin-dhcp"></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads/Week" src="https://static.pepy.tech/badge/netbox-plugin-dhcp/month"></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads/Month" src="https://static.pepy.tech/badge/netbox-plugin-dhcp/week"></a>
</div>

> [!WARNING]
> **This is a beta release.**
>
> This plugin may contain bugs and cause data loss and other problems.
> Use caution when using it in production environments.
>
> **Frequent backups are strongly recommended!**

## Requirements

* NetBox 4.5.0 or higher.
* Python 3.12 or higher.

## Installation & Configuration

### Installation

```
$ source /opt/netbox/venv/bin/activate
(venv) $ python3 -m pip install netbox-plugin-dhcp
```

### NetBox Configuration

Add the plugin to the NetBox configuration file `/opt/netbox/netbox/netbox/configuration.py`:

```python
PLUGINS = [
    "netbox_dhcp",
]
```

To permanently keep the plugin installed when updating NetBox via `upgrade.sh`:

```
echo netbox-plugin-dhcp >> /opt/netbox/local_requirements.txt
```

To add the required tables to your database run the following command from your NetBox directory:

```
./manage.py migrate
```

Full documentation on using plugins with NetBox: [Using Plugins - NetBox Documentation](https://netbox.readthedocs.io/en/stable/plugins/).

## Contribute

Contributions are always welcome! Please see the [Contribution Guidelines](CONTRIBUTING.md).

## Documentation

There is no documentation at this point.

## License

MIT

## Known Issues

* There is an issue that sometimes causes a lock conflict while running the test suite. The symptom is that the tests stop at some point and the `./manage.py test netbox_dhcp` command never returns. The issue does not seem to affect normal operation, just the tests. The specific tests have been disabled for the time being until the issue is resolved.
* Validation of input is incomplete, especially when the API or scripting are used.
* Options and Pools cannot be imported via CSV, YAML or JSON.
* Filtering Subnets, Pools etc. by Option is not possible.
* Documentation is still missing.

These issues will be addressed in upcoming Beta releases.
