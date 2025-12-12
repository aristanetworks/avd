<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# How-to Guide: Connected Endpoints

## Introduction to Connected Endpoints

The **`connected_endpoints`** data model in AVD is a structured way to define the interfaces that connect to your leaf switches. Instead of manually creating `interface Ethernet...` configurations for every server, you describe the connections using a data model, and AVD generates the complete, standardized configuration for you.

This model is typically defined directly under the leaf switch's data model, for example, in `host_vars/<leaf_name>.yml` or a group file like `group_vars/LEAFS.yml`.

The core of this model revolves around the concept called **Port Profiles**.

## Core Concept: Port Profiles

A **Port Profile** is a reusable template that defines a standard set of switchport configurations. You create a profile once and then apply it to any number of connected endpoints. This ensures consistency and dramatically simplifies configuration.

Profiles are defined under the `port_profiles` key.

### Key settings for a Port Profile

- `mode`: Can be `access` or `trunk`.
- `vlans`: For `access` mode, the single VLAN ID. For `trunk` mode, the list of allowed VLANs.
- `port_channel`: Defines Port-Channel settings like `mode` (`active` for LACP) and `channel_id`.
- `spanning_tree_portfast`: Set to `edge` for server ports.
- `native_vlan`: For trunk ports, defines the native VLAN.
- `storm_control`: To apply storm control policies.
- `flowcontrol`: To configure flowcontrol settings.

### Example: Defining several Port Profiles

This would typically be in a shared file like `group_vars/FABRIC.yml` or in a dedicated file `group_vars/PROFILES.yml` if you have a large fabric.

```yaml
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1/port_profiles.yml
--8<--
```

1. Profile for a single-homed server in VLAN 10
2. Profile for a dual-homed (LACP) server trunking two VLANs
3. Profile for a trunk port connecting to a firewall

## How-To: Define a Connected Endpoint

Once you have your profiles, you can define the actual endpoint connections under a specific leaf switch. This is done using the `connected_endpoints` key.

For each endpoint, you define its **adapters**. An adapter represents a network interface on the server.

### Key settings for an Adapter

- `switch_ports`: The list of physical Ethernet ports on the leaf switch this adapter connects to.
- `profile`: **The name of the Port Profile to apply.** This is the critical link.
- `description`: A custom description for the interface(s).
- `port_channel`: If using LACP, you must define the `channel_id` here to match the interfaces.

### Example: Connecting servers to a leaf switch

This would typically be in `host_vars/leaf1.yml`.

``` yaml
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/CONNECTED_ENDPOINTS/ce1.yml
--8<--
```

1. Endpoint 1: A single-homed web server
2. Endpoint 2: A dual-homed ESXi host using LACP
3. Must be unique on the switch

## Generated Configuration

By combining the `port_profiles` and `connected_endpoints` models, AVD generates the final switch configuration.

Using the examples above, AVD would generate the following EOS configuration on `leaf1`:

### Code snippet for WEB-SERVER-01

```cli
--8<--
docs/howto/connected_endpoints/artifacts/WEB-SERVER-01.cfg
--8<--
```

### Code snippet for ESXI-HOST-03

```cli
--8<--
docs/howto/connected_endpoints/artifacts/ESXI-HOST-03.cfg
--8<--
```

*(Note: `mlag 3` is automatically added by AVD if the Port-Channel ID is also configured on another MLAG peer.)*

## Running Ansible to Generate the Configuration

To get from your YAML files to the final EOS configuration shown above, you follow the standard AVD workflow.

### Prerequisites

1. **Ansible & AVD Installed:** You have Ansible and the `arista.avd` collection installed.

2. **Inventory Set Up:** Your inventory (`inventory/` directory) is created with your hosts and group variables, including the `port_profiles` and `connected_endpoints` definitions.

3. **Playbook Exists:** You have a main Ansible playbook (e.g., `build.yml`) that imports the AVD roles.

A typical playbook might look like this:

#### `build.yml`

``` yaml
- hosts: FABRIC
  connection: local
  gather_facts: false

  tasks:
    - name: Generate AVD Structured Configuration
      import_role:
        name: arista.avd.eos_designs
      tags: ['build']

    - name: Generate AVD Device Configurations
      import_role:
        name: arista.avd.eos_cli_config_gen
      tags: ['configure']
```

### Step 1: Build the Structured Configuration

This step runs the `eos_designs` role, which takes all your YAML variables and builds a structured data model for each device.

Run the playbook with the `build` tag:

``` bash
ansible-playbook build.yml -t build
```

After this command completes, AVD will have created detailed YAML files for each device under `inventory/intended/structured_configs/`.

### Step 2: Generate the Final Device Configuration

This step runs the `eos_cli_config_gen` role. It reads the structured configuration files created in the previous step and converts them into the final EOS CLI commands.

Run the playbook with the `configure` tag:

``` bash
ansible-playbook build.yml -t configure
```

This command generates the device configuration files and saves them under `intended/configs/`.

### Step 3: Review the Generated Configuration

This is a critical best practice. Before deploying, verify that the configuration is correct.

Open the generated file for your leaf switch (e.g., `intended/configs/leaf1.cfg`) and you will see the exact EOS CLI commands shown in the "Generated Configuration" section above, ready for deployment.

### Step 4 (Optional): Deploy the Configuration

After reviewing, you can deploy the configuration to your devices. This is typically done with a separate playbook or by integrating with Arista CloudVision. If using Ansible for deployment, a task might use the `arista.avd.eos_config_deploy_eapi` module to push the generated file to the device or `arista.avd.cv_deploy` to deploy with CloudVision.
