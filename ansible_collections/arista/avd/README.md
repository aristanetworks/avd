# Ansible Collection For Arista Validate Designs - arista.avd

**Table of Contents:**

- [Ansible Collection For Arista Validate Designs - arista.avd](#ansible-collection-for-arista-validate-designs---aristaavd)
  - [Roles Overview](#roles-overview)
  - [Custom Plugins](#custom-plugins)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation from ansible-galaxy](#installation-from-ansible-galaxy)
  - [Example Playbooks](#example-playbooks)
  - [License](#license)

## Roles Overview

This repository provides roles for Ansible's collection __arista.avd__ with the following content:

- [__arista.avd.eos_l3ls_evpn__](roles/eos_l3ls_evpn/README.md) - Opinionated Data model for deployment of L3 Leaf and Spine Fabric with VXLAN data-plane with an EVPN Control plane.
- [__arista.avd.eos_cli_config_gen__](roles/eos_cli_config_gen/README.md) - Generate Arista EOS cli syntax and device documentation.
- [__arista.avd.eos_config_deploy_cvp__](roles/eos_config_deploy_cvp/README.md) - deploys intended configuration via CloudVision.
- [__arista.avd.eos_config_deploy_eapi__](roles/eos_config_deploy_eapi/README.md) - deploys intended configuration via eAPI.

## Custom Plugins

This repository provides custom plugins for Ansible's collection __arista.avd__ :

- [Arista AVD Plugins](plugins/README.md)

## Installation

### Requirements

**Arista EOS:**

- EOS 4.21.8M or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

**Python:**

- Python 3.6.8 or later

**Supported Ansible Versions:**

- ansible 2.9.2 or later

**Additional Python Libraries required:**

- Jinja2  `2.10.3`
- netaddr `0.7.19`
- requests `2.22.0`
- treelib `1.5.5`
- pytest `5.3.4`
- pytest-html `2.0.1`

**Ansible + Additional Python Libraries Installation:**

```shell
pip3 install -r requirements.txt
```

requirements.txt content:

```text
ansible==2.9.2
Jinja2==2.10.3
netaddr==0.7.19
requests==2.22.0
treelib==1.5.5
pytest==5.3.4
pytest-html==2.0.1
```

**Ansible Configuration INI file:**

- enable jinja2 extensions: loop controls and do
  - [Jinja2 Extensions Documentation](https://svn.python.org/projects/external/Jinja-2.1.1/docs/_build/html/extensions.html)
- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

### Installation from ansible-galaxy

Ansible galaxy hosts all stable version of this collection. Installation from ansible-galaxy is the most convenient approach for consuming `arista.avd` content

```shell
ansible-galaxy collection install arista.avd
```

## Example Playbooks

**An example playbook to deploy VXLAN/EVPN Fabric via CloudVision:**

![Figure 1: Example Playbook CloudVision Deployment](media/figure-1-example-playbook-evpn-deploy-cvp.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration via CVP
      import_role:
         name: arista.avd.eos_config_deploy_cvp
```

**An example playbook to deploy VXLAN/EVPN Fabric via eAPI:**

![Figure 2: Example Playbook CloudVision Deployment](media/figure-2-example-playbook-evpn-deploy-eapi.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration to device
      import_role:
         name: arista.avd.eos_config_deploy_eapi
```

**Full examples with variables and outputs, are located here:**

[Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

## License

Project is published under [Apache 2.0 License](LICENSE)
