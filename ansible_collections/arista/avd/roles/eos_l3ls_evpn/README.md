# Ansible Role: eos_l3ls_evpn

- [Ansible Role: eos_l3ls_evpn](#ansible-role-eosl3lsevpn)
  - [Overview](#overview)
  - [Role Inputs and Outputs](#role-inputs-and-outputs)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Example Playbook](#example-playbook)
  - [License](#license)

## Overview

**eos_l3ls_evpn** is a role that provides an abstrated data model to deploy a L3 VXLAN/EVPN Leaf and Spine Fabric. The role helps network engineers deploy Arista L3 Leaf & Spine fabric underlay and overlay network services with consistency. The role is designed to easily be extended leveraging a __*"stackable template architecture"*__. The role is design to be used with the **eos_l3ls_config_gen** role to generate a complete switch configuration, and applied using a config replace strategy with with either the **eos_config_deploy_eapi** or **eos_config_deploy_cvp** roles. The role is design to work completely offline and doesn't require connectivity to any devices.

## Role Inputs and Outputs

Figure 1 below, provides a visualization of the roles inputs and outputs and tasks in order executed by the role.

**Inputs:**

- Desired variables are defined in: role defaults, group_vars and host_vars variables.
- As mentionned in the overview, if desired, the role can be extended to leverage data from dynamic sources such as an IPAM.

**Outputs:**

- A structure EOS configuration file in yaml format. This provides the follow benefits:
  - First, this allows to naturally detect duplicate entries from input, as yaml dictionaries don't process duplicate keys.
  - Leverage the structure data to create near perfect eos cli configuration.
  - Leverage the structure data to create end user documentation.
  - Leverage the structure data to for pre and post fabric tests.
- Fabric Documentation in Markdown format.
- Leaf and Spine Point-To-Point Links summary in csv format.

**Tasks:**

1. Generate device configuration in structured format (yaml).
2. Include device structured configuration, that was previously generated.
3. Generate EVPN fabric documentation in Markdown Format.
4. Generate Leaf and Spine Point-To-Point Links summary in csv format.

<p align="center">
  <img src='media/figure-1-role-eos_l3ls_evpn.png' alt='figure 1: ansible role eos_l3ls_evpn'/>
</p>

## Requirements

**Ansible Collections:**

- arista.avd collection
- arista.cvp collection, if deploying via cvp

```bash
ansible-galaxy collection install arista.avd
ansible-galaxy collection install arista.cvp
```

**Python:** Python 3.6.8 or later

**Python Libraries:**

- ansible 2.9.x
- requests 2.22.0
- treelib 1.5.5

```bash
pip3 install ansible==2.9.2
pip3 instal requests==2.22.0
pip3 instal treelib==1.5.5
```

## Role Variables

## Example Playbook

## License

Project is published under [Apache 2.0 License](../../../../../LICENSE)