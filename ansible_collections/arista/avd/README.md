# Ansible Collection For Arista Validate Designs - arista.avd

- [Ansible Collection For Arista Validate Designs - arista.avd](#ansible-collection-for-arista-validate-designs---aristaavd)
  - [Roles Overview](#roles-overview)
  - [Installation](#installation)
    - [Dependencies](#dependencies)
    - [Installation from ansible-galaxy](#installation-from-ansible-galaxy)
  - [License](#license)

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

## License

Project is published under [Apache 2.0 License](../../../LICENSE)