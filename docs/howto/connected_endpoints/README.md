<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Connected Endpoints

## Introduction

**connected_endpoints**  is an endpoint-centric model intended for servers or other select cases where most ports have unique configurations. Instead of manually creating `interface Ethernet...` configurations for every server, you describe the connections using adapters and profiles, and AVD generates the complete, standardized configuration for you.

This key is typically defined in a folder named `CONNECTED_ENDPOINTS`, but it can be defined elsewhere, depending on your environment.

## Concepts

**port_profiles**: Port profiles are used to share common settings for connected_endpoints and network_ports. Keys are the same as those used under endpoint adapters. Keys defined under endpoint adapters take precedence.

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
- `flowcontrol`: To configure flow control settings.

### Adapters

**Adapters** serve as the bridge between the Fabric (the switches) and the Endpoints (the devices). They define how a specific device is cabled and what network services (VLANs, VRFs) it should receive.

#### Key settings Adapters

Adapters define the physical mapping between the endpoint and the switch fabric:

- `endpoint_ports`: Port name for the endpoint, i.e, eth0.
- `switch_ports`: Specifies which physical interface(s) on the switch connect to the adapter.
- `switches`: The switches to which the interface will connect.
- `Profiles`: The port profile defined earlier applies to a set of similar configurations.
- `description`: A brief description of the interface function.

Note: The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.

## Running Ansible to Generate the Configuration

### Prerequisites

1. **Ansible and AVD Installed:** You have Ansible and the `arista.avd` collection installed.
2. **Inventory Set Up:** Your inventory is created with your host and group variables.
3. **Playbook Exists:** You have a main Ansible playbook (e.g., `build.yml`) that imports the AVD roles.

### Step 1. Define the port profiles

```yaml title="group_vars/DC1/port_profiles.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1/port_profiles.yml
--8<--
```

1. Profile for a single-homed server in VLAN 10
2. Profile for a dual-homed (LACP) server trunking two VLANs
3. Profile for a trunk port connecting to a firewall

### Step 2. Define your connected endpoints

```yaml title="group_vars/CONNECTED_ENDPOINTS/ce.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/CONNECTED_ENDPOINTS/ce.yml
--8<--
```

1. Within `port_channel`, we define its existence and what mode we would like to use, but there is no additional requirement like setting the Port Channel ID. That is done automatically. You can always override the default by setting the `channel_id` key within your Port Channel definition. The default Port Channel selected will be derived from the first switch port in the adapter.

!!! note

    Run your specific `build` playbook to generate the configuration.

### Step 3: Review the Generated Configuration

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
