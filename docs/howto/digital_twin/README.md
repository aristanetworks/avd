<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Configuring Digital Twin

!!! warning "PREVIEW"

    The AVD Digital Twin functionality is in preview mode. Everything is subject to change, is not supported and may not be complete.

    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/avd/discussions)

## Overview

AVD Digital Twin functionality natively generates all artifacts required to deploy a virtual replica of a production AVD fabric.
The generated artifacts are automatically optimized for the target Digital Twin environment. For example, an EOS configuration generated for an ACT environment will automatically remove or adjust features that are not supported on virtual platforms.

AVD currently supports the following Digital Twin environments:

- **[ACT (Arista Cloud Test)](#act-arista-cloud-test)** - An Arista cloud-based network testing platform

!!! note
    Support for additional Digital Twin platforms will be added in future releases.

## Key Features

- **Configuration Optimization**: Device configurations are adjusted to remove or modify features not supported by EOS in the Digital Twin environment
- **Platform-Specific Optimizations**: Configurations are optimized for each Digital Twin platform (e.g., eAPI access in `default` VRF for ACT)
- **Topology Generation**: Topology information is generated in the format required by the target Digital Twin platform
- **Platform Mapping**: Production hardware platforms are mapped to virtual platforms supported by target Digital Twin environment
- **Separate Artifact Management**: Digital Twin artifacts can be generated alongside production artifacts in separate directories
- **Management IP Configuration**: Management IP addresses can be configured separately for Digital Twin devices (if supported by Digital Twin environment)

## Getting Started

### Basic Configuration

To generate Digital Twin artifacts, you need to:

1. Enable Digital Twin mode in your playbook
2. Configure Digital Twin settings in your fabric variables
3. Run the `eos_designs` and `eos_cli_config_gen` roles

### Enabling Digital Twin Mode

Digital Twin mode is controlled by the `avd_digital_twin_mode` variable. This is a boolean setting that tells AVD to generate Digital Twin artifacts instead of production artifacts.

**Key Points:**

- When set to `true`, AVD generates configurations optimized for the Digital Twin environment
- When set to `false` or not set (default), AVD generates standard production configurations
- The same fabric variables are used for both production and Digital Twin runs
- Digital Twin-specific settings in fabric variables (under `digital_twin`) are only applied when `avd_digital_twin_mode` is `true`

**Example:**

```yaml
---
avd_digital_twin_mode: true
```

### Playbook Configuration

!!! note
    To easily switch between production mode and digital twin mode, it is recommended to create a dedicated playbook/play where `avd_digital_twin_mode: true` is set in the playbook vars.

    By default, Digital Twin artifacts (such as the topology file, adjusted structured and EOS configuration, device and fabric documentation)
    will replace original fabric artifacts.

    To keep Digital Twin artifacts separate, adjust the `output_dir_name` and `documentation_dir_name` variables for both `eos_designs`
    and `eos_cli_config_gen` to point to a dedicated output location.

Create a playbook that generates both production and Digital Twin artifacts:

```yaml
---
# Production playbook to generate production fabric artifacts
- name: Build Production Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

# Digital Twin playbook to generate Digital Twin mode artifacts
- name: Build Digital Twin Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  vars:
    # Adjust the output dirs to keep Digital Twin artifacts in a separate directory
    output_dir_name: "digital_twin/intended"
    documentation_dir_name: "digital_twin/documentation"
    # Set this flag to True to enable AVD Digital Twin mode
    avd_digital_twin_mode: true
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen
```

### Generated Artifacts

When AVD Digital Twin mode is enabled, AVD generates the following artifacts:

```text
.
├── <documentation_dir_name>
│   ├── devices
│   │   ├── <DEVICE_NAME>.md
│   │   └── ...
│   └── fabric
│       ├── <FABRIC_NAME>-documentation.md
│       ├── <FABRIC_NAME>-p2p-links.csv
│       ├── <FABRIC_NAME>-topology.csv
│       └── <FABRIC_NAME>-topology.yml  # Digital Twin platform-specific topology file
└── <output_dir_name>
    ├── configs
    │   ├── <DEVICE_NAME>.cfg
    │   └── ...
    └── structured_configs
        ├── <DEVICE_NAME>.yml
        └── ...
```

The topology file format depends on the target Digital Twin platform (e.g., `<FABRIC_NAME>-topology.yml` for ACT).

## Common Configuration

### Global Digital Twin Settings

Global Digital Twin settings are configured under the `digital_twin` key in the fabric variables.

For a complete list of all available global Digital Twin configuration options, see the [Digital Twin Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#preview---digital-twin-configuration) section in the eos_designs data models documentation.

### Per-Node Digital Twin Configuration

In addition to global settings, Digital Twin settings can be configured per node type, node group or per individual node.

For a complete list of all available per-node Digital Twin configuration options, see the [Node Type Digital Twin Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#preview---node-type-digital-twin-configuration) section in the eos_designs data models documentation.

### Configuring the Digital Twin Environment

The `digital_twin.environment` key in the Ansible variables specifies which Digital Twin platform to target. This key determines the format of the generated topology file(s) and platform-specific optimizations.

**Example:**

```yaml
# group_vars/FABRIC.yml
digital_twin:
  environment: act  # Specify the target Digital Twin platform (default: act)
```

**Supported Values:**

- `act` - Arista Cloud Test platform (currently the only supported environment)

### Platform Mapping

All production hardware platforms are pre-mapped to the appropriate virtual platforms for Digital Twin environments in defaults of the `platform_settings`.

**Example:**

```yaml
- platforms:
    - 7050X3
  feature_support:
    queue_monitor_length_notify: false
    sflow_subinterfaces: false
    subinterface_mtu: false
    per_interface_l2_mru: false
  reload_delay:
    mlag: 300
    non_mlag: 330
  trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared 131072
  digital_twin:
    # Platform 7050X3 is pre-mapped to vEOS-lab for ACT Digital Twin
    platform: vEOS-lab
```

When a device uses platform `7050X3` in production, AVD uses `vEOS-lab` platform settings when generating ACT Digital Twin artifacts.
This means things like MLAG `reload-delay` timers, feature supportability, OOB MGMT interface, etc.. will be taken from the `vEOS-lab` platform settings item instead of the `7050X3` item when running AVD in Digital Twin mode.

It is possible to override these default mappings by defining `custom_platform_settings` items that override the default `digital_twin.platform` settings:

```yaml
# Example: Mapping 7050X3 platform to cEOSLab for ACT Digital Twin
custom_platform_settings:
  - platforms:
      - 7050X3
    feature_support:
      queue_monitor_length_notify: false
      sflow_subinterfaces: false
      subinterface_mtu: false
      per_interface_l2_mru: false
    reload_delay:
      mlag: 300
      non_mlag: 330
    trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared 131072
    digital_twin:
      # Platform 7050X3 is now mapped to cEOSLab platform for ACT Digital Twin instead of default vEOS-lab
      platform: cEOSLab
```

### Default Interfaces Selection

By default, AVD uses the default interfaces of the **original platform** when generating Digital Twin configurations. This ensures interface names and numbering match the production configuration.

To use the default interfaces of the **Digital Twin platform** instead set the following key to `True`:

```yaml
digital_twin:
  use_default_interfaces_of_digital_twin_platform: true
```

**Example scenario:**

- Production platform: `7050X3` with default uplink interfaces `Ethernet49/1, Ethernet50/1`
- Digital Twin platform: `vEOS-lab` with default uplink interfaces `Ethernet1, Ethernet2`

With `use_default_interfaces_of_digital_twin_platform: false` (default):

- Digital Twin config will use `Ethernet49/1, Ethernet50/1` as uplink interfaces

With `use_default_interfaces_of_digital_twin_platform: true`:

- Digital Twin config will use `Ethernet1, Ethernet2` as uplink interfaces

## Platform-Specific Settings

### ACT (Arista Cloud Test)

ACT is a cloud-based network testing platform that allows to deploy and test virtual replicas of the production network.

#### ACT Overview

When targeting ACT as a Digital Twin environment, AVD:

- Generates an ACT-compatible topology file (`<FABRIC_NAME>-topology.yml`)
- Automatically assigns appropriate ACT node types to fabric devices
- Optimizes configurations for ACT's virtual environment
- Manages credentials and OS versions for ACT devices
- Optionally assigns OOB MGMT IP addresses to devices when configured (required by ACT for all node types except `veos` and `cloudeos`)

#### ACT Default values

If not specified otherwise, AVD uses the following default values when generating ACT Digital Twin artifacts:

| Attribute | Description | Default value | Source of information |
| --------- | ----------- | ------------- | --------------------- |
| act_os_version | OS version of the replica device | `cloudeos`: `4.33.2F`<br>`cvp`: `2024.3.2`<br>`generic`: `ubuntu-2204-lts`<br>`third-party`: `byod`<br>`tools-server`: `ubuntu-2204-lts`<br>`veos`: `4.33.1.1F` | `node_config.digital_twin.act_os_version` or `digital_twin.fabric.act_os_version` |
| act_username | username of the default account deployed on the replica device | `cvpadmin` | `digital_twin.fabric.act_username` |
| act_password | password of the default account deployed on the replica device | `cvp123!` | `digital_twin.fabric.act_password` |

#### ACT Node Types

AVD assigns each device an ACT node type based on the device's original platform. The following ACT node types are supported:

- **`veos`** - Virtual EOS devices (vEOS-lab)
- **`cloudeos`** - CloudEOS devices
- **`cvp`** - CloudVision Portal devices
- **`generic`** - Generic Linux devices
- **`third-party`** - Third-party network devices
- **`tools-server`** - Tools and test servers

The ACT node type is determined by the `digital_twin.act_node_type` setting of the `platform_settings` (or `custom_platform_settings` if set) item matching the Digital Twin's platform (`digital_twin.platform`) of the production device.

**Example platform mapping for ACT:**

```yaml
# Only relevant keys are shown
platform_settings:
  - platforms:
      - 7050X3
    digital_twin:
      # Use platform settings of the `vEOS-lab` platform when generating ACT Digital Twin artifacts
      platform: vEOS-lab

  - platforms:
      - vEOS-lab
    digital_twin:
      # Virtual platform `vEOS-lab` is mapped to the ACT node type `veos`
      act_node_type: veos
```

In the example below a `7050X3` production device will be assigned the `veos` ACT node type since the `vEOS-lab` platform settings (Digital Twin platform for `7050X3`) has `digital_twin.act_node_type` set to `veos`.

#### Management IP Configuration

ACT Digital Twin devices can optionally have an OOB management IP address assigned in the topology file. AVD assigns the ACT management IP in the following priority order:

1. `<node_type_keys.key>.nodes[].digital_twin.mgmt_ip` - Per-node Digital Twin management IP
2. `<node_type_keys.key>.nodes[].mgmt_ip` - Per-node production management IP

When neither key is set, AVD behaviour depends on the ACT node type:

- **`veos` and `cloudeos`**: `ip_addr` is omitted from the topology entry.
- **All other node types**: AVD raises an error because ACT requires `ip_addr` for those node types.

**Example:**

```yaml
spine:
  nodes:
    - name: spine1
      mgmt_ip: 192.168.1.11/24  # Used for both production and Digital Twin OOB MGMT IP

    - name: spine2
      mgmt_ip: 192.168.1.12/24          # Used for `spine2` in production
      digital_twin:
        mgmt_ip: 10.255.0.12/24         # Used as OOB MGMT IP for `spine2` in ACT Digital Twin topology file
```

!!! note
    For `veos` and `cloudeos` ACT node types, `mgmt_ip` is optional. For all other node types (e.g., `generic`, `third-party`, `cvp`), `mgmt_ip` must be configured, otherwise AVD will raise an exception.

#### ACT OS Version Configuration

Each ACT node type has a default OS version that will be used if not explicitly configured (please see [AT Default Values](#act-default-values) for details).

You can override the OS version at different levels (shown below from lowest to highest priority):

```yaml
# Global override for all fabric devices
digital_twin:
  fabric:
    act_os_version: "4.33.2"

# Per-node-type override (overrides defaults and global fabric settings)
spine:
  defaults:
    digital_twin:
      act_os_version: "4.33.3"

# Per-node (can be as well applied on a node group level) override (overrides defaults, global fabric settings, and per-node-type settings)
spine:
  nodes:
    - name: spine1
      digital_twin:
        act_os_version: "4.34.4"
```

#### ACT eAPI Access Control

ACT users connect to device eAPI through ACT's infrastructure. This connectivity requires eAPI to be accessible in the EOS's **default VRF**.

If production configuration uses a dedicated management VRF for eAPI, ACT will not be able to connect to devices. Use the `act_ensure_eapi_access` setting to resolve this for all fabric nodes:

```yaml
digital_twin:
  fabric:
    act_ensure_eapi_access: true
```

When enabled, AVD makes the following adjustments to the generated Digital Twin configuration:

1. Enables eAPI over HTTPS in the default VRF
2. Removes any IPv4 ACLs from the default VRF eAPI configuration (IPv6 ACLs are preserved)

This setting only applies to ACT `veos` and `cloudeos` node types.

**Example - Production Configuration:**

```eos
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
      ip access-group eapi_acl_in
```

**Example - Digital Twin Configuration with `act_ensure_eapi_access: true`:**

```diff
  management api http-commands
     protocol https
     no shutdown
     !
     vrf MGMT
        no shutdown
        ip access-group eapi_acl_in
     !
+    vrf default
+       no shutdown
```

#### ACT Internet Access Configuration

By default, ACT does not provide direct Internet access to `cloudeos` or `veos` devices. To enable Internet access (for example, to download software or access CVaaS or other external services) for all fabric nodes:

```yaml
digital_twin:
  fabric:
    act_internet_access: true
```

This setting can be specified per-node-type, node-group or per-node as well:

```yaml
spine:
  nodes:
    - name: spine1
      digital_twin:
        act_internet_access: true
```

!!! note
    This setting only applies to ACT `cloudeos` and `veos` node types and will be ignored for other node types.

#### ACT Examples

Each example below demonstrates a specific use case with two devices: one using default values and one using customized values.

##### Example 1: Topology Management IP Configuration

This example shows how to configure topology management IPs for ACT Digital Twin devices.

```yaml
spine:
  nodes:
    # Device using production management IP (default behavior)
    - name: spine1
      mgmt_ip: 10.10.1.11/24  # Used for both production and ACT Digital Twin topology file

    # Device using separate ACT Digital Twin management IP
    - name: spine2
      mgmt_ip: 10.10.1.12/24  # Production management IP
      digital_twin:
        mgmt_ip: 172.16.1.12/24  # ACT Digital Twin management IP (overrides production IP) in topology file

    # Device with no management IP — valid only for veos and cloudeos ACT node types
    - name: spine3
      # No mgmt_ip set; ip_addr will be omitted from the ACT topology entry
```

**Result:**

- `spine1`: Uses `10.10.1.11/24` as OOB MGMT IP in ACT Digital Twin topology file
- `spine2`: Uses `172.16.1.12/24` as OOB MGMT IP in ACT Digital Twin topology file
- `spine3`: No `ip_addr` in ACT Digital Twin topology file (only valid for `veos`/`cloudeos` node types)

##### Example 2: OS Version Configuration

This example demonstrates OS version configuration at different levels.

```yaml
digital_twin:
  fabric:
    act_os_version: "4.33.2"  # Global default for all fabric devices

spine:
  nodes:
    # Device using global default OS version
    - name: spine1
      mgmt_ip: 192.168.1.11/24
      # Will use 4.33.2 from global setting

    # Device using custom OS version
    - name: spine2
      mgmt_ip: 192.168.1.12/24
      digital_twin:
        act_os_version: "4.34.0F"  # Override for testing newer version
```

**Result:**

- `spine1`: Uses OS version `4.33.2` (global default)
- `spine2`: Uses OS version `4.34.0F` (per-node override)

##### Example 3: Internet Access Configuration

This example demonstrates Internet access configuration for ACT devices.

```yaml
spine:
  nodes:
    # Device without Internet access (default)
    - name: spine1
      mgmt_ip: 192.168.1.11/24
      # No Internet access in ACT

    # Device with Internet access enabled
    - name: spine2
      mgmt_ip: 192.168.1.12/24
      digital_twin:
        act_internet_access: true  # Enable direct Internet access
```

**Result:**

- `spine1`: No Internet access in ACT (default)
- `spine2`: Internet access enabled in ACT

**Note:** `act_internet_access` only applies to `veos` and `cloudeos` ACT node types.

#### ACT Best Practices

##### 1. Enable eAPI Access for ACT Automation

Enable `act_ensure_eapi_access` when production configuration has eAPI disabled or restricted in `default` VRF:

```yaml
digital_twin:
  fabric:
    act_ensure_eapi_access: true
```

##### 2. Version Consistency

Keep ACT OS versions consistent with your production environment where possible, or use specific versions for testing new features.

## General Best Practices

### 1. Separate Output Directories

Use separate output directories for production and Digital Twin artifacts:

```yaml
# Production play
vars:
  output_dir_name: "intended"
  documentation_dir_name: "documentation"

# Digital Twin play
vars:
  output_dir_name: "digital_twin/intended"
  documentation_dir_name: "digital_twin/documentation"
  avd_digital_twin_mode: true
```

### 2. Version Control

Keep Digital Twin artifacts in version control alongside production artifacts to:

- Track changes to Digital Twin configurations
- Review historical differences between production and Digital Twin artifacts
- Roll back to previous versions when needed

### 3. Platform Mapping

Define platform mappings (when changes to the default mappings are needed) in a central location (e.g., `custom_platform_settings` under fabric-level variables) to ensure consistency across the fabric.

### 4. Testing Workflow

Establish general testing workflow for all complex fabric configuration changes:

1. Generate proposed production artifacts
2. Generate proposed Digital Twin artifacts
3. Deploy Digital Twin topology and proposed artifacts to the target Digital Twin platform
4. Run extensive tests (ANTA, etc..) in the Digital Twin environment to confirm compliance with intended fabric state and expected impact/behavior
5. Adjust proposed production and Digital Twin artifacts based on test results (if needed) until satisfied with test results
6. Follow established internal change management process to apply validated changes to production fabric

## General Troubleshooting

### Issue: Wrong Interface Names in Digital Twin

**Symptom**: Digital Twin configuration uses different interface names than expected.

**Possible Causes**:

1. `use_default_interfaces_of_digital_twin_platform` setting doesn't match your requirements
2. Platform mapping is incorrect

**Solution**:

- If you want to use Digital Twin platform interfaces, set `use_default_interfaces_of_digital_twin_platform: true`
- If you want to use original platform interfaces (default), set `use_default_interfaces_of_digital_twin_platform: false`
- Verify platform mapping in `platform_settings.[].digital_twin.platform` (or `custom_platform_settings` if set)

### Issue: Unsupported Features in Digital Twin Configuration

**Symptom**: Digital Twin configuration contains features not supported by the virtual platform.

**Solution**:

- Verify that the Digital Twin platform mapping in `platform_settings` (or `custom_platform_settings` if set) is correct
- Verify that the `feature_support` settings for the selected Digital Twin platform are correct

## Additional Resources

- [AVD Documentation](https://avd.arista.com)
- [AVD GitHub Discussions](https://github.com/aristanetworks/avd/discussions)
- [AVD GitHub Issues](https://github.com/aristanetworks/avd/issues)
