<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Connected Endpoints

## Introduction

**connected_endpoints**  is an endpoint-centric model intended for servers or other use cases where most ports have unique configurations. Instead of manually creating `interface Ethernet...` configurations for every server, you describe the connections using adapters and profiles, and AVD generates the complete, standardized configuration for you.

This key is typically defined in a folder named `CONNECTED_ENPOINTS` but can be defined somewhere else depending on your environment.

## Concepts

**port_profiles**: Port profiles are used to share common settings for connected_endpoints and/or network_ports. Keys are the same as used under endpoint adapters. Keys defined under endpoints adapters take precedence.

**adapters**:  An adapter represents a network interface on the connected_endpoint. They serve as the bridge between the Fabric (the switches) and the Endpoints (the devices). They define how a specific device is cabled and what network services (VLANs, VRFs) it should receive.

### Port Profiles

A **Port Profile** is a reusable template that defines a standard set of switchport configurations. You create a profile once and then apply it to any number of connected endpoints. This ensures consistency and dramatically simplifies configuration.

A port profile can refer to another port profile using parent_profile to inherit settings in up to two levels (adapter->profile->parent_profile).

#### Key settings for a Port Profile

- `mode`: Can be `access` or `trunk`.
- `vlans`: For `access` mode, the single VLAN ID. For `trunk` mode, the list of allowed VLANs.
- `port_channel`: Defines Port-Channel settings like `mode` (`active` for LACP) and `channel_id`.
- `spanning_tree_portfast`: Set to `edge` for server ports.
- `native_vlan`: For trunk ports, defines the native VLAN.
- `storm_control`: To apply storm control policies.
- `flowcontrol`: To configure flowcontrol settings.

### Adapters

**Adapters** serve as the bridge between the Fabric (the switches) and the Endpoints (the devices). They define how a specific device is cabled and what network services (VLANs, VRFs) it should receive.

#### Key settings Adapters

Adapters define the physical mapping between the endpoint and the switch fabric:

- `endpoint_ports`: Port name for the endpoint i.e eth0.
- `switch_ports`: Specifies which physical interface(s) on the switch connect to the adapter.
- `switches`: The switches the interface will connect to.
- `Profiles`: The port profile defined earlier, apply set of similar configuration
- `description`: A brief description of the interface function

Note: The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.

## Running Ansible to Generate the Configuration

### Prerequisites

1. **Ansible & AVD Installed:** You have Ansible and the `arista.avd` collection installed.
2. **Inventory Set Up:** Your inventory (`inventory/` directory) is created with your hosts and group variables.
3. **Playbook Exists:** You have a main Ansible playbook (e.g., `build.yml`) that imports the AVD roles.

### Step 1. Create the two configuration files

Navigate to your inventory folder

```bash
touch group_vars/DC1/port_profiles.yml
touch group_vars/DC1/connected_endpoints.yml
```

### Step 2. Define the port profiles

```yaml title="group_vars/DC1/port_profiles.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1/port_profiles.yml
--8<--
```

1. Profile for a single-homed server in VLAN 10
2. Profile for a dual-homed (LACP) server trunking two VLANs
3. Profile for a trunk port connecting to a firewall

### Step 3. Define your connected endpoints

```yaml title="group_vars/DC1/connected_endpoints.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/CONNECTED_ENDPOINTS/ce1.yml
--8<--
```

### Step 4. Run the build playbook

``` bash
ansible-playbook build.yml
```

``` yaml title="build.yml"
- hosts: FABRIC
  connection: local
  gather_facts: false

  tasks:
    - name: Generate AVD Structured Configuration
      import_role:
        name: arista.avd.eos_designs

    - name: Generate AVD Device Configurations
      import_role:
        name: arista.avd.eos_cli_config_gen
```

### Step 5: Review the Generated Configuration

Device configuration is located `intended/configs/`

```cli title="Code snippet for WEB-SERVER-01"
--8<--
docs/howto/connected_endpoints/artifacts/WEB-SERVER-01.cfg
--8<--
```

```cli title="Code snippet for ESXI-HOST-03"
--8<--
docs/howto/connected_endpoints/artifacts/ESXI-HOST-03.cfg
--8<--
```

This is a critical best practice. Before deploying, verify that the configuration is correct.

Open the generated file for your leaf switch (e.g., `intended/configs/leaf1.cfg`) and you will see the exact EOS CLI commands shown in the "Generated Configuration" section above, ready for deployment.

### Step 4 (Optional): Deploy the Configuration

After reviewing, you can deploy the configuration to your devices. This is typically done with a separate playbook or by integrating with Arista CloudVision. If using Ansible for deployment, a task might use the `arista.avd.eos_config_deploy_eapi` module to push the generated file to the device or `arista.avd.cv_deploy` to deploy with CloudVision.
