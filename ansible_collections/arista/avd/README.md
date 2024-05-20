<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# arista.avd - A Complete Network Automation Solution

## Description

Arista Validated Designs (AVD) is an extensible data model that defines Arista's Unified Cloud Network architecture as "code".

AVD Documentation:

- [Stable version](https://avd.arista.com/stable/)
- [Development version](https://avd.arista.com/devel/)

## Requirements

The AVD collection has the following collections:

- Python 3.9+
- Ansible Core 2.14.0 to 2.16.x
- Install the arista.avd collection
- [Additional Python packages](#additional-python-dependencies)
- Modify the `ansible.cfg` file to support additional jinja2 extensions

## Installations

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```shell
ansible-galaxy collection install arista.avd
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:

```yaml
collections:
  - name: arista.avd
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the Ansible package.

To upgrade the collection to the latest available version, run the following command:

```shell
ansible-galaxy collection install arista.avd --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 4.7.1:

```shell
ansible-galaxy collection install arista.avd:==4.7.1
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/collections_guide/index.html) for more details.

### Additional Python Dependencies

The AVD collection requires the installation of additional Python packages. To ensure you install the correct versions, run the following commands:

```shell
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt
```

### Enable jinja2 extensions

In your `ansible.cfg` file, add the following modifications:

```shell
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

## Use Cases

Please see the official documentation for examples in data center, campus, and WAN environments.

- [Getting started](https://avd.arista.com/stable/docs/getting-started/intro-to-ansible-and-avd.html)
- [Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

### Testing

Please see our [pipeline workflows](https://github.com/aristanetworks/avd/actions) to view the in-depth testing performed against the collection.

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it. Please see [contribution guide](docs/contribution/overview.md) for additional details.

You can also open an [issue](https://github.com/aristanetworks/avd/issues) to report any problems or submit requests for enhancements.

## Support

Support for this `arista.avd` collection is provided by the community directly in this repository. If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/avd/discussions).

## Release Notes and Roadmap

Please see the [release notes](https://github.com/aristanetworks/avd/releases) for the latest updates to the AVD collection.

## Related Information

- [Official arista.avd documentation](https://avd.arista.com)
- [Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

## License Information

The project is published under [Apache 2.0 License]([./LICENSE](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/LICENSE))
