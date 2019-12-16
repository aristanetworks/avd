# Ansible Collection For Arista Validate Designs - arista.avd

- [Ansible Collection For Arista Validate Designs - arista.avd](#ansible-collection-for-arista-validate-designs---aristaavd)
  - [About](#about)
  - [Roles Overview](#roles-overview)
  - [Installation](#installation)
    - [Dependencies](#dependencies)
    - [Installation from ansible-galaxy](#installation-from-ansible-galaxy)
  - [Resources](#resources)
  - [License](#license)
  - [Ask a question](#ask-a-question)
  - [Contributing](#contributing)

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system natively through eapi or [CloudVision platform (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision). This collection includes a set of ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are design to be customized and extended to your needs!

## Roles Overview

This repository provides roles for Ansible's collection __arista.avd__ with following content:

- [__arista.avd.eos_l3ls_evpn__](roles/eos_l3ls_evpn/README.md) - Opiniated Data model for deployment of L3 Leaf and Spine Fabric with VXLAN data-plane with an EVPN Control plane.
- [__arista.avd.eos_cli_config_gen__](roles/eos_cli_config_gen/README.md) - Generate eos cli syntax and device documentation.
- [__arista.avd.eos_config_deploy_eapi__](roles/eos_config_deploy_eapi/README.md) - deploys intended configuration via eapi.

## Installation

### Dependencies

This collection requires the following to be installed on the Ansible control machine:

- python `3.x`
- ansible  `2.9.0` or later
- requests `2.22.0` or later
- treelib version `1.5.5` or later

### Installation from ansible-galaxy

Ansible galaxy hosts all stable version of this collection. Installation from ansible-galaxy is the most convenient approach for consuming `arista.avd` content

```shell
ansible-galaxy collection install arista.avd
```

## Resources

- Ansible [EOS modules](https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#eos) on ansible documentation.
- Ansible [CloudVision modules](https://github.com/aristanetworks/ansible-cvp)
- [CloudVision Platform](https://www.arista.com/en/products/eos/eos-cloudvision)

## License

Project is published under [Apache 2.0 License](../../../LICENSE)

## Ask a question

Support for this `arista.avd` collection is provided by the community directly in this repository. Easiest way to get support is to open [an issue](https://github.com/aristanetworks/ansible-avd/issues).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we’ll be able to merge it.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problem or to submit enhancement.

A more complete [guide for contribution](contributing.md) is available in the repository