# NetBox DNS
The NetBox DHCP plugin will enable NetBox to manage operational DHCP data.

<div align="center">
<a href="https://pypi.org/project/netbox-plugin-dhcp/"><img src="https://img.shields.io/pypi/v/netbox-plugin-dhcp" alt="PyPi"/></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads" src="https://static.pepy.tech/badge/netbox-plugin-dhcp"></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads/Week" src="https://static.pepy.tech/badge/netbox-plugin-dhcp/month"></a>
<a href="https://pepy.tech/project/netbox-plugin-dhcp"><img alt="Downloads/Month" src="https://static.pepy.tech/badge/netbox-plugin-dhcp/week"></a>
</div>

[!DANGER]
** This is a beta release. It may contain bugs, cause data loss and other problems. Use caution when using it in production environments.
Frequent backups are strongly recommended! **

## Requirements

* NetBox 4.5.0 or higher
* Python 3.12 or higher

## Compatibility with NetBox Versions

NetBox Version | NetBox DHCP Version | Comment
-------------- | ------------------- | -------
4.5            | 0.1                 |

## Installation & Configuration

### Installation

```
$ source /opt/netbox/venv/bin/activate
(venv) $ python3 -m pip install netbox-plugin-dhcp
```

### NetBox Configuration

Add the plugin to the NetBox config. `~/netbox/configuration.py`

```python
PLUGINS = [
    "netbox_dhcp",
]
```

To permanently keep the plugin installed when updating NetBox via `upgrade.sh`:

```
echo netbox-plugin-dhcp >> ~/netbox/local_requirements.txt
```

To add the required netbox_dns tables to your database run the following command from your NetBox directory:

```
./manage.py migrate
```

Full documentation on using plugins with NetBox: [Using Plugins - NetBox Documentation](https://netbox.readthedocs.io/en/stable/plugins/)

## Contribute

Contributions are always welcome! Please see the [Contribution Guidelines](CONTRIBUTING.md)

## Documentation

There is no documentation at this point.

## License

No license is granted at this point.

## Known Issues

* There is currently an issue that sometimes causes a lock conflict while running the test suite. The symptom is that the tests stop at some point and the `./manage.py test netbox_dhcp` command never returns. In some cases it helps to re-run the tests.
* Validation of input is incomplete, especially when the API or scripting are used.
* Options and Pools currently cannot be imported via CSV, YAML or JSON
* Filtering Subnets, Pools etc. by Option is not possible

These issues will be addressed in upcoming Beta releases.
