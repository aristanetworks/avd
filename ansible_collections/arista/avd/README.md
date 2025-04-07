<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# arista.avd - Design Driven Network Automation

## Description

- **Flexibility with Open Data Models:** Extensible fabric-wide network models, simplifying configuration, delivering consistency, and reducing errors
- **Simplification through Multi-Domain Automation:** A framework that can automate the data center, campus or wide area network, enabled by a consistent EOS software image and management platform
- **Comprehensive Workflows:** Automating the full life cycle of network provisioning from config generation to pre- and post-deployment validation and self-documentation of the network

AVD Documentation:

- [Stable version](https://avd.arista.com/stable/)
- [Development version](https://avd.arista.com/devel/)

## Requirements

The AVD collection has the following requirements:

- Python 3.10 or above
- Ansible Core 2.16.0 to 2.18.x
- the Python package `pyavd[ansible-collection]` matching the collection version
- Modify the `ansible.cfg` file to support additional Jinja2 extensions

## Installation

Follow the [installation guide](https://avd.arista.com/stable/docs/installation/collection-installation.html) to install the requirements.

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```shell
ansible-galaxy collection install arista.avd
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

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
ansible-galaxy collection install arista.avd:==5.2.3
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/collections_guide/index.html) for more details.

### Additional Python Dependencies

The AVD collection requires the installation of additional Python packages. To ensure you install the correct versions, run the following commands:

```shell
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt
```

### Enable Jinja2 Extensions

In your `ansible.cfg` file, add the following modifications:

```ini
[defaults]
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

## Use Cases

Please see the documentation for examples in data center, campus, and wide area network environments.

- [Getting started](https://avd.arista.com/stable/docs/getting-started/intro-to-ansible-and-avd.html)
- [Examples](https://avd.arista.com/stable/ansible_collections/arista/avd/examples/single-dc-l3ls/index.html)

### Testing

Every pull request is thoroughly tested by our extensive CI pipeline and reviewed by the AVD Maintainer team.

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a significant change, please start a discussion first to ensure we can merge it. Please see [contribution guide](https://avd.arista.com/stable/docs/contribution/overview.html) for additional details.

You can also open an [issue](https://github.com/aristanetworks/avd/issues) to report any problems or submit requests for enhancements.

## Support

- AVD version 4.x releases with full support from Arista TAC. If your organization has the [A-Care subscription](https://www.arista.com/assets/data/pdf/AVD-A-Care-TAC-Support-Overview.pdf) please don't hesitate to contact TAC with any questions or issues.
- Community support is provided via [Github discussions board](https://github.com/aristanetworks/avd/discussions).

## Release Notes and Roadmap

<!--
  TODO: should we add a symlink to our latest release notes to make this link less useless?
-->
Please see the [release notes](https://avd.arista.com) for the latest updates to the AVD collection.

## Related Information

- [arista.avd documentation](https://avd.arista.com)

## License Information

Copyright (c) 2019-2024 Arista Networks, Inc.

The project is published under [Apache 2.0 License](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/LICENSE)
