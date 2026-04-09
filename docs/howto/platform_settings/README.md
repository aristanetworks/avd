<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Platform Settings

## Introduction

**Platform settings** provide platform-specific configurations for different Arista switch models. Instead of manually configuring platform-specific features for each device type, you define platform settings once, and AVD automatically applies the correct configuration based on each device's `platform` setting.

This guide explains how to configure platform settings, understand feature support, and customize platform-specific behaviors.

### When to Use Custom Platform Settings

AVD includes default platform settings for all major Arista platforms. You only need to define `custom_platform_settings` when:

- Overriding default reload delays, TCAM profiles, or feature support for an existing platform
- Adding support for a new or custom platform
- Applying platform-specific structured configuration (QoS, hardware counters, etc.)
- Configuring Digital Twin or hardware validation settings per platform

This configuration is typically defined at the fabric level, but it can be defined elsewhere, depending on your environment.

## Concepts

Platform settings are organized into configuration blocks, where each block targets specific platform models and defines their capabilities and default behaviors. Understanding these settings helps you customize platform-specific features and ensure proper device operation.

The following table describes the key settings available in platform configuration blocks:

| Setting | Description |
| ------- | ----------- |
| **platforms** | List of platform names or regex patterns to match against the device's `platform` setting. |
| **digital_twin** | Settings for Digital Twin mode including alternate platform and ACT node type. |
| **feature_support** | Defines which features are supported on this platform (PoE, queue monitoring, storm control, etc.). |
| **lag_hardware_only** | Forces LAG configuration to hardware-only mode. |
| **management_interface** | Specifies the management interface name (default: Management1). |
| **p2p_uplinks_mtu** | MTU for point-to-point uplink interfaces. |
| **reload_delay** | Configures reload delays for MLAG and non-MLAG scenarios to ensure proper convergence. |
| **tcam_profile** | TCAM profile to apply for this platform (e.g., `vxlan-routing`). |
| **trident_forwarding_table_partition** | Forwarding table partition settings for Trident-based platforms. |

### Platform Matching

AVD uses the first matching entry from the platform settings list:

1. Checks `custom_platform_settings` first (if defined)
2. Then checks the default `platform_settings`
3. Uses regex matching against the device's `platform` value
4. Falls back to the entry with `platforms: [default]` if no match is found

### Digital Twin

Digital Twin settings allow you to run AVD against virtual devices instead of physical hardware:

- `platform`: Alternate platform to use in Digital Twin mode (e.g., `vEOS-lab`)
- `act_node_type`: ACT node type for simulation (veos, cloudeos, generic, etc.)

### Feature Support

The `feature_support` key defines which features are available on a platform:

- `poe`: Power over Ethernet support
- `queue_monitor_length_notify`: Queue monitoring notifications
- `interface_storm_control`: Storm control on interfaces
- `bgp_update_wait_for_convergence`: BGP update wait for convergence
- `bgp_update_wait_install`: BGP update wait install
- `per_interface_mtu`: Per-interface MTU configuration
- `subinterface_mtu`: MTU configuration on subinterfaces
- `evpn_gateway_all_active_multihoming`: EVPN all-active multihoming
- `private_vlan`: Private VLAN support

### Reload Delay

Reload delays ensure proper convergence during device reboots:

- `mlag`: Delay in seconds for MLAG devices (allows peer to take over)
- `non_mlag`: Delay in seconds for non-MLAG devices

## Platforms pre-defined values

Here are a few examples of pre-defined values for different platforms. You can find the full list in the [AVD Design Data Models](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#platform-settings).

### vEOS and cEOS

```yaml
- platforms:
  - VEOS
  - VEOS-LAB
  - vEOS
  - vEOS-lab
  feature_support:
    bgp_update_wait_for_convergence: false
    bgp_update_wait_install: false
    interface_storm_control: false
    queue_monitor_length_notify: false
    evpn_gateway_all_active_multihoming: true
    hardware_validation: false
  reload_delay:
    mlag: 300
    non_mlag: 330
  digital_twin:
    act_node_type: veos
```

```yaml
- platforms:
  - CEOS
  - cEOS
  - ceos
  - cEOSLab
  feature_support:
    bgp_update_wait_for_convergence: false
    bgp_update_wait_install: false
    interface_storm_control: false
    queue_monitor_length_notify: false
    evpn_gateway_all_active_multihoming: true
    hardware_validation: false
  management_interface: Management0
  reload_delay:
    mlag: 300
    non_mlag: 330
  digital_twin:
    act_node_type: veos
```

### 720XP series

```yaml
- platforms:
  - 720XP
  feature_support:
    poe: true
    queue_monitor_length_notify: false
  reload_delay:
    mlag: 300
    non_mlag: 330
  trident_forwarding_table_partition: flexible exact-match 16000 l2-shared 18000 l3-shared
    22000
  digital_twin:
    platform: vEOS-lab
```

### 7280R series

```yaml
- platforms:
  - 7280R
  - 7280R2
  - 7020R
  lag_hardware_only: true
  reload_delay:
    mlag: 900
    non_mlag: 1020
  tcam_profile: vxlan-routing
  feature_support:
    private_vlan: false
  digital_twin:
    platform: vEOS-lab
```

## Assign platform to devices

You can assign a platform to a device using the `platform` key in the device definition.

- defaults
- node_groups
- nodes

```yaml
l3leaf:
  defaults:
    platform: 7280R3
  node_groups:
    - group: Group1
      platform: 7280R2
      nodes:
        - name: DC1-LEAF1A
          id: 1
        - name: DC1-LEAF1B
          id: 2
  nodes:
    - name: DC1-LEAF2A
      id: 3
      platform: vEOS-lab
    - name: DC1-LEAF2B
      id: 4
```

### Generated configuration

When `custom_platform_settings` overrides the reload delays for a platform, AVD applies them directly to the MLAG configuration. The following shows the MLAG stanza generated for `htps-leaf1a` using the `vEOS-lab` override from the fabric variables:

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:basic
--8<--
```

1. The `custom_platform_settings` block overrides default settings for the matched platform.
2. Exact match for `vEOS-lab` — takes priority over the built-in default entry.
3. `mlag` reload delay in seconds — how long a rebooting device waits before re-asserting as the MLAG primary.
4. `non_mlag` reload delay in seconds — used on standalone devices.

```cli title="htps-leaf1a MLAG configuration"
--8<--
docs/howto/platform_settings/artifacts/htps-leaf1a-mlag.cfg
--8<--
```

The `reload-delay mlag 180` and `reload-delay non-mlag 210` values come directly from the `custom_platform_settings` override above, replacing the built-in defaults of 300/330.

## Custom Platform Settings

### Assign Default MTU

This example shows how to set a default MTU for different platforms using `default_interface_mtu`.

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:mtu
--8<--
```

1. Exact platform name match for 7280R3
2. Set `default_interface_mtu` to 9000 — applies to all interfaces via EOS `interface defaults`
3. Different platforms can have different default MTU values
4. A second platform with both `default_interface_mtu` and `p2p_uplinks_mtu`
5. `default_interface_mtu` sets the global default (configured under `interface defaults` in EOS)
6. `p2p_uplinks_mtu` sets MTU specifically for point-to-point uplink interfaces (overrides default)

### TCAM Profile

This example shows platform settings for devices requiring TCAM profiles.

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:tcam
--8<--
```

### Hardware Validation

Hardware validation checks the physical hardware inventory of each device. Set `feature_support.hardware_validation` to `true` in the platform settings to enable it. The actual validation thresholds (minimum power supplies, fans, supervisors, transceiver manufacturers) are configured separately under `validation_profiles` at the fabric level.

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:hardware_validation
--8<--
```

1. Enables hardware validation for this platform. Configure thresholds under `validation_profiles`.

### Platform with Structured Config

This example shows how to apply platform-specific structured configuration using the `structured_config` key to inject EOS CLI configuration directly.

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:structured_config
--8<--
```

## Common Patterns

### Pattern 1: Digital Twin Configuration

Configure platforms to run AVD against virtual devices instead of physical hardware:

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:digital_twin
--8<--
```

### Pattern 2: Campus Platform with PoE

Configure campus switches with PoE support:

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:campus_poe
--8<--
```

### Pattern 3: Disable Features for Virtual Platforms

Disable unsupported features on virtual platforms:

```yaml title="group_vars/HTPS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml:virtual_features
--8<--
```

## Troubleshooting

### Issue: Platform settings not applied

**Problem:** Device configuration doesn't include expected platform-specific settings.

**Solution:**

- Verify the device's `platform` value matches a pattern in `platforms` list
- Check that `custom_platform_settings` entries come before default entries
- Use regex tester to verify your platform pattern matches correctly
- Review the structured config output to see which platform settings were matched

### Issue: Wrong platform matched

**Problem:** Device is matching the wrong platform settings entry.

**Solution:**

- Remember that the **first match wins** - order matters
- Place more specific patterns before generic ones
- Use exact platform names instead of regex when possible
- Check for overlapping regex patterns

### Issue: Feature not working as expected

**Problem:** A feature is enabled but not working on the device.

**Solution:**

- Verify the platform actually supports the feature in EOS
- Check `feature_support` settings for the matched platform
- Review EOS documentation for platform-specific limitations
- Ensure EOS version supports the feature

### Issue: Hardware validation failing

**Problem:** Devices fail hardware validation checks.

**Solution:**

- Review `validate_hardware` settings for the platform
- Verify actual hardware meets minimum requirements
- Adjust thresholds in platform settings if needed
- Disable validation for lab/virtual environments

## Reference

For complete details on all available properties, see:

- [Platform Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#platform-settings)
- [Custom Platform Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#custom-platform)
- [Platform Speed Groups](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#cplatform-speed-groups)
