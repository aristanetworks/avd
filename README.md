# Ansible Collection For Arista Validated Designs - arista.avd

![Arista AVD](https://img.shields.io/badge/Arista-AVD%20Automation-blue) ![collection version](https://img.shields.io/github/v/release/aristanetworks/ansible-avd) ![License](https://img.shields.io/github/license/aristanetworks/ansible-avd)

<center><img src="ansible_collections/arista/avd/media/avd-logo.png" alt="Arista AVD Overview" width="800"/></center>

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the Extensible Operating System (EOS) operating system natively through EOS API (eAPI) or [CloudVision Portal (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision).
This collection includes a set of ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs!

Full documentation for the collection:

- [Stable version](https://www.avd.sh/en/stable/)
- [Development version](https://www.avd.sh/en/devel/)

## Features

- **Flexibility with Open Data Models:** Extensible fabric-wide network models, simplifying configuration, delivering consistency, and reducing errors
- **Simplification through Multi-Domain Automation:** A framework that can automate the data center, campus or wide area network, enabled by a consistent EOS software image and management platform
- **Comprehensive Workflows:** Automating the full life cycle of network provisioning from config generation to pre and post-deployment validation, and self-documentation of the network

## Reference designs

- [L3LS VXLAN-EVPN, L2LS, and MPLS (beta)](./ansible_collections/arista/avd/roles/eos_designs/README.md)

## Collection installation

Ansible galaxy hosts all stable versions of this collection. Installation from ansible-galaxy is the most convenient approach for consuming `arista.avd` content. Please follow the collection installation [guide](./ansible_collections/arista/avd/docs/installation/collection-installation.md).

## Examples

- [Getting started examples](./ansible_collections/arista/avd/docs/getting-started/intro-to-ansible-and-avd.md)
- [Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

## Additional resources

- Ansible [EOS modules](https://docs.ansible.com/ansible/latest/collections/arista/eos/index.html) on ansible documentation.
- Ansible [CloudVision modules](https://cvp.avd.sh/en/stable/)
- [CloudVision Portal](https://www.arista.com/en/products/eos/eos-cloudvision)
- [Arista Design and Deployment Guides](https://www.arista.com/en/solutions/design-guides)

## Ask a question

Support for this `arista.avd` collection is provided by the community directly in this repository. If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it. Please see [contribution guide](./ansible_collections/arista/avd/docs/contribution/overview.md) for additional details.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problems or submit requests for enhancements.

## License

The project is published under [Apache 2.0 License](./LICENSE)
