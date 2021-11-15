# Ansible Collection For Arista Validated Designs - arista.avd

![Arista AVD](https://img.shields.io/badge/Arista-AVD%20Automation-blue) ![collection version](https://img.shields.io/github/v/release/aristanetworks/ansible-avd) ![continuous integration](https://github.com/aristanetworks/ansible-avd/actions/workflows/continuous_integration.yml/badge.svg) ![License](https://img.shields.io/github/license/aristanetworks/ansible-avd)

**Table of Contents:**

- [Ansible Collection For Arista Validated Designs - arista.avd](#ansible-collection-for-arista-validated-designs---aristaavd)
  - [About](#about)
  - [Reference Designs](#reference-designs)
  - [Project Documentation](#project-documentation)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation from ansible-galaxy](#installation-from-ansible-galaxy)
  - [Example Playbooks](#example-playbooks)
  - [Examples](#examples)
  - [Additional Resources](#additional-resources)
  - [Ask a question](#ask-a-question)
  - [Contributing](#contributing)
  - [Branching Model](#branching-model)
  - [License](#license)

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system natively through eapi or [CloudVision Portal (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision).
This collection includes a set of ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs!

<center><img src="ansible_collections/arista/avd/media/avd-logo.png" alt="Arista AVD Overview" width="800"/></center>

## Reference Designs

The arista.avd collection provides abstracted data models and framework to build, document, deploy and validate the following designs:

**L3LS EVPN:**

| Underlay | Overlay | Topology |
| -------- | ------- | ---------- |
| eBGP | eBGP | Multi-Stage + L2 Leafs |
| ISIS | eBGP | Multi-Stage + L2 Leafs  |
| ISIS | iBGP | Multi-Stage + L2 Leafs  |
| OSPF | eBGP | Multi-Stage + L2 Leafs |
| OSPF | iBGP | Multi-Stage + L2 Leafs  |
| RFC5549(eBGP) | eBGP | Multi-Stage + L2 Leafs |

<center><img src="ansible_collections/arista/avd/media/5-stage-topology.gif" alt="Arista AVD Overview" width="800"/></center>

## Project Documentation

The documentation how to leverage ansible-avd collection is located here:
  - **[Read The Docs](https://avd.sh/en/latest/)**
  - **[GitHub](./ansible_collections/arista/avd/README.md)**

## Installation

### Requirements

**Arista EOS:**

- EOS 4.21.8M or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

**Python:**

- Python 3.8 or later

**Supported Ansible Versions:**

- ansible-core from __2.11.3__ to __2.12.x__

**Additional Python Libraries required:**

- netaddr
- Jinja2
- treelib
- cvprac
- paramiko
- jsonschema
- requests
- PyYAML
- md-toc

**Ansible + Additional Python Libraries Installation:**

```shell
$ pip3 install ansible-core>=2.11.3,<2.13.0

$ pip3 install -r ansible_collections/arista/avd/requirements.txt
```

**Ansible Configuration INI file:**

- enable jinja2 extensions: loop controls and do
  - [Jinja2 Extensions Documentation](https://jinja.palletsprojects.com/extensions/)
- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

> **_NOTE:_** When using ansible-cvp modules, the user that is executing the ansible-playbook has to have access to both CVP and the EOS CLI.

### Installation from ansible-galaxy

Ansible galaxy hosts all stable version of this collection. Installation from ansible-galaxy is the most convenient approach for consuming `arista.avd` content

```shell
ansible-galaxy collection install arista.avd
```

## Example Playbooks

**An example playbook to deploy VXLAN/EVPN Fabric via CloudVision:**

![Figure 1: Example Playbook CloudVision Deployment](media/example-playbook-deploy-cvp.gif)

```yml
- hosts: DC1_FABRIC
  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_designs

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

- hosts: CVP
  tasks:

  - name: upload cvp configlets
    import_role:
        name: arista.avd.cvp_configlet_upload
    vars:
      configlet_directory: 'configlets/'
      file_extension: 'txt'
      configlets_cvp_prefix: 'DC1-AVD'

    - name: deploy configuration via CVP
      import_role:
         name: arista.avd.eos_config_deploy_cvp
```

Execute eos_state_validation playbook once change control has been approved and deployed to devices in CVP.
Note: To run this playbook, ansible_host **must** be configured in your inventory for every EOS device. eAPI access **must** be configured and allowed in your networks.

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

**An example playbook to deploy VXLAN/EVPN Fabric via eAPI:**

![Figure 2: Example Playbook CloudVision Deployment](media/example-playbook-deploy-eapi.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_designs

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration via eAPI
      import_role:
         name: arista.avd.eos_config_deploy_eapi

    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

## Examples

**Full examples with variables and outputs, are located here:**

[Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

## Additional Resources

- Ansible [EOS modules](https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#eos) on ansible documentation.
- Ansible [CloudVision modules](https://github.com/aristanetworks/ansible-cvp)
- [CloudVision Portal](https://www.arista.com/en/products/eos/eos-cloudvision)
- [Arista Design and Deployment Guides](https://www.arista.com/en/solutions/design-guides)

## Ask a question

Support for this `arista.avd` collection is provided by the community directly in this repository. Easiest way to get support is to open [an issue](https://github.com/aristanetworks/ansible-avd/issues).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problem or to submit enhancement.

## Branching Model

- The __`devel`__ branch corresponds to the release actively under development.
- The __`releases/x.x.x`__ branches correspond to stable releases.
- Fork repository and create a branch based on __`devel`__ to set up a dev environment if you want to open a PR.
- See the ansible-avd release for information about active branches.

## License

Project is published under [Apache 2.0 License](LICENSE)
