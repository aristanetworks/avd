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

AVD Digital Twin functionality generates all artifacts required to deploy a virtual replica of a production AVD fabric.
The generated artifacts are automatically optimized for the target Digital Twin environment. For example, an EOS configuration generated for an ACT environment will automatically remove or adjust features that are not supported on virtual platforms.

AVD currently supports the following Digital Twin environments:

- **[ACT (Arista Cloud Test)](#act-arista-cloud-test)** - An Arista cloud-based network testing platform

Support for additional Digital Twin platforms will be added in future releases.

## Key Features

- **Configuration Optimization**: Device configurations are adjusted to remove or modify features not supported by EOS in the Digital Twin environment
- **Platform-Specific Optimizations**: Configurations are optimized for each Digital Twin platform (e.g., eAPI access in `default` VRF for ACT)
- **Topology Generation**: Topology information is generated in the format required by the Digital Twin platform
- **Platform Mapping**: Production hardware platforms are mapped to virtual platforms
- **Separate Artifact Management**: Digital Twin artifacts can be generated alongside production artifacts in separate directories
- **Management IP Configuration**: Management IP addresses can be configured separately for Digital Twin devices

## Getting Started

### Basic Configuration

To generate Digital Twin artifacts, you need to:

1. Enable Digital Twin mode in your playbook
2. Configure Digital Twin settings in your fabric variables
3. Run the `eos_designs` and `eos_cli_config_gen` roles

### Enabling Digital Twin Mode

Digital Twin mode is controlled by the `avd_digital_twin_mode` Ansible root-level variable. This is a boolean that tells AVD to generate Digital Twin artifacts instead of production artifacts.

**Key Points:**

- When set to `true`, AVD generates configurations optimized for the Digital Twin environment
- When set to `false` or not set (default), AVD generates standard production configurations
- The same fabric variables are used for both production and Digital Twin runs
- Digital Twin-specific settings in fabric variables (under `digital_twin` Ansible root-level variable) are only applied when `avd_digital_twin_mode` is `True`

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

The following table shows all available global Digital Twin configuration options:

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/digital-twin-configuration.md
--8<--

### Per-Node Digital Twin Configuration

In addition to global settings, you can configure Digital Twin settings per node type or per individual node:

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-digital-twin-configuration.md
--8<--

### Configuring the Digital Twin Environment

The `digital_twin.environment` key in your Ansible variables specifies which Digital Twin platform to target. This key determines the format of generated topology files and platform-specific optimizations.

**Example:**

```yaml
# group_vars/FABRIC.yml
digital_twin:
  environment: act  # Specify the target Digital Twin platform
```

**Supported Values:**

- `act` - Arista Cloud Test platform (currently the only supported environment)

### Platform Mapping

All production hardware platforms are pre-mapped to the appropriate virtual platforms for Digital Twin environments in defaults of the `platform_settings`.

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

When a device uses platform `7050X3` in production, AVD uses `vEOS-lab` platform settings when generating Digital Twin artifacts.
This means things like MLAG `reload-delay` timers, feature supportability, OOB MGMT interface, etc. will be taken from the `vEOS-lab` platform settings profile instead of the `7050X3` profile when running AVD in Digital Twin mode.

You can override these default mappings by defining `custom_platform_settings` items that override the default `digital_twin.platform` setting:

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

- Production platform: `7050X3` with default uplink interfaces `Ethernet49/1, Ethernet40/1`
- Digital Twin platform: `vEOS-lab` with default uplink interfaces `Ethernet1, Ethernet2`

With `use_default_interfaces_of_digital_twin_platform: false` (default):
- Digital Twin config will use `Ethernet49/1, Ethernet50/1`

With `use_default_interfaces_of_digital_twin_platform: true`:
- Digital Twin config will use `Ethernet1, Ethernet2`

## Platform-Specific Settings

### ACT (Arista Cloud Test)

ACT is a cloud-based network testing platform that allows to deploy and test virtual replicas of the production network.

#### ACT Overview

When targeting ACT as a Digital Twin environment, AVD:

- Generates an ACT-compatible topology file (`<FABRIC_NAME>-topology.yml`)
- Automatically assigns appropriate ACT node types to devices
- Optimizes configurations for ACT's virtual environment
- Manages credentials and OS versions for ACT devices

#### ACT Node Types

AVD assigns each device an ACT node type based on the device's platform. The following ACT node types are supported:

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
  - platforms: [7050X3]
    digital_twin:
      # Use platform settings of the `vEOS-lab` platform when generating ACT Digital Twin artifacts
      platform: vEOS-lab

  - platforms:
      - vEOS-lab
    digital_twin:
      act_node_type: veos
```

In the example below a `7050X3` production device will be assigned the `veos` ACT node type since the `vEOS-lab` platform settings (Digital Twin platform for `7050X3`) has `digital_twin.act_node_type: veos`.

#### Management IP Configuration

Each ACT Digital Twin device requires a OOB management IP address to be assinged inside topology file. AVD assigns the management IP in the following priority order:

1. `<node_type_keys.key>.nodes[].digital_twin.mgmt_ip` - Per-node Digital Twin management IP
2. `<node_type_keys.key>.nodes[].mgmt_ip` - Per-node production management IP

**Example:**

```yaml
spine:
  nodes:
    - name: spine1
      mgmt_ip: 192.168.1.11/24  # Used for both production and Digital Twin

    - name: spine2
      mgmt_ip: 192.168.1.12/24          # Used for production
      digital_twin:
        mgmt_ip: 10.255.0.12/24         # Used for ACT Digital Twin
```

!!! note
    If a device does not have a management IP configured (neither `mgmt_ip` nor `digital_twin.mgmt_ip`), AVD will raise an exception.

#### ACT OS Version Configuration

Each ACT node type has a default OS version that will be used if not explicitly configured:

| ACT Node Type | Default OS Version |
|---------------|-------------------|
| `veos` | `4.33.1.1F` |
| `cloudeos` | `4.33.2F` |
| `cvp` | `2024.3.2` |
| `generic` | `ubuntu-2204-lts` |
| `third-party` | `byod` |
| `tools-server` | `ubuntu-2204-lts` |

You can override the OS version at different levels (from lowest to highest priority):

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

# Per-node override (overrides defaults, global fabric settings, and per-node-type settings)
spine:
  nodes:
    - name: spine1
      digital_twin:
        act_os_version: "4.34.4"
```

#### ACT eAPI Access Control

ACT clients connect to device eAPI through ACT's infrastructure. This connectivity requires eAPI to be accessible in the EOS's **default VRF**.

If production configuration uses a dedicated management VRF for eAPI, ACT will not be able to connect to devices. Use the `act_ensure_eapi_access` setting to resolve this:

```yaml
digital_twin:
  fabric:
    act_ensure_eapi_access: true
```

When enabled, AVD:

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

```eos
management api http-commands # will always be added if not already configured
   protocol https # will always be added if not already configured
   no shutdown # will always be added if not already configured
   !
   vrf MGMT
      no shutdown
      ip access-group eapi_acl_in
   !
   vrf default # will always be added if not already configured
      no shutdown # will always be added if not already configured
```

#### ACT Internet Access Configuration

By default, ACT does not provide direct Internet access to `cloudeos` or `veos` devices. To enable Internet access (for example, to download software or access external services):

```yaml
digital_twin:
  fabric:
    act_internet_access: true
```

This setting only applies to ACT `cloudeos` and `veos` node types and will be ignored for other node types.

#### ACT Examples

##### Example 1: Separate Management IPs for ACT

```yaml
spine:
  nodes:
    - name: dc1-spine1
      mgmt_ip: 10.10.1.11/24  # Production management IP
      digital_twin:
        mgmt_ip: 172.16.1.11/24  # Digital Twin management IP
```

##### Example 2: Per-Node OS Version Override

```yaml
spine:
  nodes:
    - name: spine1
      mgmt_ip: 192.168.1.11/24
      # Uses default 4.33.1.1F

    - name: spine2
      mgmt_ip: 192.168.1.12/24
      digital_twin:
        act_os_version: "4.34.0F"  # Override for this device
```

##### Example 3: eAPI Access and Internet Access

```yaml
digital_twin:
  fabric:
    act_ensure_eapi_access: true  # Ensure eAPI in default VRF
    act_internet_access: true     # Enable Internet access for veos/cloudeos

spine:
  nodes:
    - name: spine1
      mgmt_ip: 192.168.1.11/24
```

#### ACT Best Practices

##### 1. Enable eAPI Access for ACT Automation

Enable `act_ensure_eapi_access` when running automation against ACT:

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
- Review differences between production and Digital Twin
- Roll back to previous versions when needed

### 3. Platform Mapping

Define platform mappings (when changes to the default mappings are needed) in a central location (e.g., `custom_platform_settings`) to ensure consistency across the fabric.

### 4. Testing Workflow

Establish a testing workflow:

1. Generate production artifacts
2. Generate Digital Twin artifacts
3. Deploy Digital Twin topology to the target Digital Twin platform
4. Run tests (ANAT, etc.) in the Digital Twin environment
5. Apply validated changes to production

## General Troubleshooting

### Issue: Wrong Interface Names in Digital Twin

**Symptom**: Digital Twin configuration uses different interface names than expected.

**Possible Causes**:

1. `use_default_interfaces_of_digital_twin_platform` setting doesn't match your requirements
2. Platform mapping is incorrect

**Solution**:

- If you want to use Digital Twin platform interfaces, set `use_default_interfaces_of_digital_twin_platform: true`
- If you want to use original platform interfaces (default), set `use_default_interfaces_of_digital_twin_platform: false`
- Verify platform mapping in `platform_settings.[].digital_twin.platform`

### Issue: Unsupported Features in Digital Twin Configuration

**Symptom**: Digital Twin configuration contains features not supported by the virtual platform.

**Solution**:

- Verify that the Digital Twin platform mapping in `platform_settings.[].digital_twin.platform` is correct
- Verify that the `feature_support` settings for the selected Digital Twin platform are correct

## Additional Resources

- [AVD Documentation](https://avd.arista.com)
- [AVD GitHub Discussions](https://github.com/aristanetworks/avd/discussions)
- [AVD GitHub Issues](https://github.com/aristanetworks/avd/issues)
