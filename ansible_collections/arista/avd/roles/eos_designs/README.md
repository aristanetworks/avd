# Ansible Role: eos_designs

**Table of Contents:**

- [Ansible Role: eos_designs](#ansible-role-eos_designs)
  - [Overview](#overview)
  - [Role Inputs and Outputs](#role-inputs-and-outputs)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [vEOS-LAB Know Caveats and Recommendations](#veos-lab-know-caveats-and-recommendations)
  - [License](#license)

## Overview

**eos_designs**, is a role that provides an abstracted data model to deploy the following design:

- [**l3ls-evpn** design](doc/l3ls-evpn.md): Configure various Layer 3 Leaf & Spine topologies leveraging a VXLAN data-plane with an EVPN control-plane.

The **eos_designs** role:

- Enables network engineers to deploy Arista Leaf & Spine fabrics with underlay and overlay network services effectively and with consistency.
- Designed to be extended easily, leveraging a __*"stackable template architecture"*__.
- Designed to be used with the **eos_cli_config_gen** role to generate a complete switch configuration and applied using a config replace strategy with either
  - **eos_config_deploy_eapi** role.
  - **eos_config_deploy_cvp** role.
- Designed to generate the intended configuration offline, without relying on switch current state information.
- Facilitates the evaluation of the configuration post-deployment with [eos_validate_state](../eos_validate_state/README.md) role.
- Facilitates the evaluation of the configuration prior to deployment with tools like [Batfish](https://www.batfish.org/)

## Role Inputs and Outputs

Figure 1 below provides a visualization of the roles inputs, outputs and tasks in order executed by the role.

<!-- ![Figure 1: Ansible Role eos_designs](../../media/role_eos_designs.gif) -->

<div style="text-align:center">
  <img src="../../media/role_eos_designs.gif" />
</div>

**Inputs:**

- Desired variables are defined in: role defaults, group_vars, and host_vars variables.
- If desired, the role can be extended to leverage data from dynamic sources such as an IPAM or CMDB.

**Outputs:**

- A structured EOS configuration file in YAML format. This provides the following benefits:
  - First, this allows us to naturally detect duplicate entries from inputs, as YAML dictionaries don't process duplicate keys.
  - Leverage the structured data to create eos CLI configuration.
  - Leverage the structured data to create end-user documentation.
  - Leverage the structured data for pre and post fabric validation.
- Fabric Documentation in Markdown format.
- Leaf and Spine Topology summary in CSV format.

**Tasks:**

1. Set AVD facts.
2. Generate YAML file with host variables (Optional for debuging/development with tag -> debug).
3. Set device configuration facts.
4. Write device structured configuration to YAML file.
5. Include device structured configuration that was previously generated.
6. Generate fabric documentation in Markdown format.
7. Generate fabric point-to-point links summary in CSV format.
8. Generate fabric physical topology summary in CSV format.

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## Role Variables

The role variables are documented inline within YAML formatted output with: "< >"
Some variables are required, while others are optional.
Default values, are stored in the role defaults [main.yml](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/roles/eos_designs/defaults) file.

Role variables are grouped by configuration elements and are typically stored in different group_vars files.

## vEOS-LAB Know Caveats and Recommendations

- vEOS-LAB is a great tool to learn and test ansible-avd automation framework.This is the primary tool leveraged by Arista Ansible Team for development and testing efforts.
- vEOS-lab enables you to create and run replicas of physical networks within a risk-free virtual environment.
- Virtual networks created with vEOS-lab can be used for network modeling, planning for new services, or validating new features and functionality for the installed network.
- vEOS-lab is not a network simulator but the exact EOS implementation that runs on the hardware platforms.
- Supported features are documented here: [Arista EOS overview](https://www.arista.com/en/products/eos)

However, because vEOS-LAB implements a virtual data plane, there are known caveats and adjustments required to default arista.avd settings:

**Variables adjustments required for vEOS-LAB:**

```yaml
# Disable update wait-for-convergence and update wait-for-install, which is not supported in vEOS-LAB.
spine_bgp_defaults:
#  - update wait-for-convergence
#  - update wait-install
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart

leaf_bgp_defaults:
#  - update wait-install
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart

# Update p2p mtu 9000 -> 1500, MTU 9000 not supported in vEOS-LAB.
p2p_uplinks_mtu: 1500

# Adjust default bfd values, to avoid high CPU.
bfd_multihop:
  interval: 1200
  min_rx: 1200
  multiplier: 3
```

## License

Project is published under [Apache 2.0 License](../../LICENSE)
