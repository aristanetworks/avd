# Ansible Collection For Arista Validated Designs

<center><img src="media/avd-logo.png" alt="Arista AVD Overview" width="800"/></center>

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running Arista's **Extensible Operating System (EOS)** natively through it's **EOS API (eAPI)** or [**CloudVision Portal (CVP)**](https://www.arista.com/en/products/eos/eos-cloudvision). This collection includes a set of Ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs.

Full documentation for the collection is available on read-the-docs:

- [latest stable version](https://www.avd.sh/en/latest/)
- [collection development version](https://www.avd.sh/en/devel/)

## Reference Designs

The arista.avd collection provides abstracted data models and framework to build, document, deploy and validate the following designs:

The following table lists underlay and overlay combinations that can be leveraged to deploy a **layer three leaf spine (L3LS) Ethernet VPN (EVPN) fabric**:

| Underlay | Overlay | Topology |
| -------- | ------- | ---------- |
| eBGP | eBGP | Multi-Stage + L2 Leafs |
| ISIS | eBGP | Multi-Stage + L2 Leafs  |
| ISIS | iBGP | Multi-Stage + L2 Leafs  |
| OSPF | eBGP | Multi-Stage + L2 Leafs |
| OSPF | iBGP | Multi-Stage + L2 Leafs  |
| RFC5549(eBGP) | eBGP | Multi-Stage + L2 Leafs |

<div style="text-align:center">
  <img src="media/5-stage-topology.gif" />
</div>

## Roles Overview

This repository provides roles for Aristas's collection, **arista.avd**, with the following content:

- [**arista.avd.eos_designs**](roles/eos_designs/README.md) - Opinionated Data model to assist with the deployment of Arista Validated Designs.
- [**arista.avd.eos_cli_config_gen**](roles/eos_cli_config_gen/README.md) - Generate Arista EOS cli syntax and device documentation.
- [**arista.avd.eos_config_deploy_cvp**](roles/eos_config_deploy_cvp/README.md) - Deploys intended configuration via CloudVision.
- [**arista.avd.eos_config_deploy_eapi**](roles/eos_config_deploy_eapi/README.md) - Deploys intended configuration via eAPI.
- [**arista.avd.cvp_configlet_upload**](roles/cvp_configlet_upload/README.md) - Uploads configlets from a local folder to CloudVision Server.
- [**arista.avd.eos_validate_state**](roles/eos_validate_state/README.md) - Validate operational states of Arista EOS devices.
- [**arista.avd.eos_snapshot**](roles/eos_snapshot/README.md) - Collect commands on EOS devices and generate reports.
- [**arista.avd.dhcp_provisioner**](roles/dhcp_provisioner/README.md) - Configure an ISC-DHCP server to provide ZTP services and CloudVision registration.

![Arista AVD Overview](media/example-playbook-deploy-cvp.gif)

## Custom Plugins & Modules

This repository provides custom plugins for Arista's AVD collection:

- [Arista AVD Plugins](plugins/README.md)

## Installation

### Collection Installation

Ansible Galaxy hosts all stable versions of this collection. Installation from ansible-galaxy is the most convenient approach for consuming arista.avd content. Please follow [this](https://avd.sh/en/latest/docs/installation/collection-installation.html) guide.

### Requirements

Please follow the [requirements](https://avd.sh/en/latest/docs/installation/requirements.html) guide to install dependencies.

**Ansible Configuration INI file:**

- Enable the following jinja2 extensions:
  - loop controls
  - do

  !!! tip
  [Jinja2 Extensions Documentation](https://jinja.palletsprojects.com/extensions/)

By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend changing this to error instead and stop playbook execution when a duplicate key is detected.

```ini title="ansible.cfg"
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

!!! note
    When using ansible-cvp modules, the user who is executing the ansible-playbook must have access to both CVP and the EOS CLI.

## Example Playbooks

**Example playbook to deploy an Arista Validated Design via CloudVision:**

![Figure 1: Example Playbook CloudVision Deployment](media/example-playbook-deploy-cvp.gif)

```yaml
# Play to build EOS configuration from EOS_DESIGNS
- hosts: DC1_FABRIC
  tasks:

    # BUILD EOS configuration
    - name: generate intended variables
      import_role:
         name: arista.avd.eos_designs
    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

# Play to configure CloudVision
- hosts: CVP
  tasks:

  # Generate CloudVision configuration & deployment
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

!!! note
Running this playbook requires the following:

- `ansible_host` **must** be configured in your inventory for every EOS device.
- eAPI access **must** be configured and allowed in your networks.

```yaml
# EOS eAPI state validation
- hosts: DC1_FABRIC
  tasks:
    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

**Example playbook to deploy an Arista Validated Design via EOS eAPI:**

![Figure 2: Example Playbook CloudVision Deployment](media/example-playbook-deploy-eapi.gif)

```yaml
# Play to build EOS configuration from EOS_DESIGNS + Deploy using eAPI
- hosts: DC1_FABRIC
  tasks:

    # BUILD EOS configuration
    - name: generate intended variables
      import_role:
         name: arista.avd.eos_designs
    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    # EOS eAPI deploy
    - name: deploy configuration via eAPI
      import_role:
         name: arista.avd.eos_config_deploy_eapi

    # EOS eAPI state validation
    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

**Full examples with variables and outputs, are located here:**

[Arista NetDevOps Examples](https://github.com/arista-netdevops-community)

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problem or to submit enhancement.

## License

Project is published under [Apache 2.0 License](LICENSE)
