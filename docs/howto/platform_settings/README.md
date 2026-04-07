<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Platform Settings

## Introduction

**Platform settings** provide platform-specific configurations for different Arista switch models. Instead of manually configuring platform-specific features for each device type, you define platform settings once, and AVD automatically applies the correct configuration based on each device's `platform` setting.

This guide explains how to configure platform settings, understand feature support, and customize platform-specific behaviors.

### When to Use Platform Settings

Use platform settings when:

- You need to configure platform-specific features (TCAM profiles, reload delay, forwarding table partitions, PoE)
- You need to define feature support capabilities for different platforms
- You want to override default platform configurations
- You want to customize reload delays for MLAG and non-MLAG devices
- You need to configure Digital Twin or validation settings per platform

AVD includes comprehensive default platform settings for all major Arista platforms. You typically only need to define `custom_platform_settings` when:

- Adding support for a new or custom platform
- Overriding specific settings for an existing platform
- Applying platform-specific structured configuration

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

Digital Twin settings allow you to run AVD in simulation mode:

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
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPS/fabric.yml
--8<--
```

1. `fabric_name` sets the fabric-wide identifier.
2. `underlay_routing_protocol` selects eBGP for the underlay.
3. `overlay_routing_protocol` selects eBGP for the overlay.
4. `p2p_uplinks_mtu` limits the MTU on point-to-point links (required for vEOS-lab).
5. The `custom_platform_settings` block overrides default settings for the matched platform.
6. Exact match for `vEOS-lab` — takes priority over the built-in default entry.
7. `mlag` reload delay in seconds — how long a rebooting device waits before re-asserting as the MLAG primary.
8. `non_mlag` reload delay in seconds — used on standalone devices.

```cli title="htps-leaf1a MLAG configuration"
--8<--
docs/howto/platform_settings/artifacts/htps-leaf1a-mlag.cfg
--8<--
```

The `reload-delay mlag 180` and `reload-delay non-mlag 210` values come directly from the `custom_platform_settings` override above, replacing the built-in defaults of 300/330.

## Custom Platform Settings

### Assign Default MTU

This example shows how to set a default MTU for the 7280R3 platform using `default_interface_mtu`.

```yaml title="group_vars/FABRIC/fabric.yml"
custom_platform_settings:
  - platforms:
      - 7280R3 # (1)!
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
    default_interface_mtu: 9000 # (2)!

  - platforms:
      - 7280R2 # (3)!
    reload_delay:
      mlag: 900
      non_mlag: 1020
    default_interface_mtu: 9214

  - platforms:
      - 7280R.* # (4)!
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
    default_interface_mtu: 9000 # (5)!

  - platforms:
      - 7050X3 # (6)!
    reload_delay:
      mlag: 300
      non_mlag: 330
    default_interface_mtu: 9000 # (7)!
    p2p_uplinks_mtu: 9214 # (8)!
```

1. Exact platform name match for 7280R3
2. Set `default_interface_mtu` to 9000 — applies to all interfaces via EOS `interface defaults`
3. Different platforms can have different default MTU values
4. Use regex to match all 7280R variants (7280R, 7280R2, 7280R3, etc.)
5. All matching platforms will use MTU 9000 as default
6. A second platform with both `default_interface_mtu` and `p2p_uplinks_mtu`
7. `default_interface_mtu` sets the global default (configured under `interface defaults` in EOS)
8. `p2p_uplinks_mtu` sets MTU specifically for point-to-point uplink interfaces (overrides default)

### TCAM Profile

This example shows platform settings for devices requiring TCAM profiles.

```yaml title="group_vars/FABRIC/fabric.yml"
custom_platform_settings:
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
      queue_monitor_length_notify: true
      interface_storm_control: true
    digital_twin:
      platform: vEOS-lab
      act_node_type: veos

  - platforms:
      - 7280R3
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
    feature_support:
      evpn_gateway_all_active_multihoming: true
      private_vlan: false
      queue_monitor_length_notify: true
    digital_twin:
      platform: vEOS-lab
```

### Hardware Validation

This example shows comprehensive hardware validation requirements.

```yaml title="group_vars/FABRIC/fabric.yml"
custom_platform_settings:
  - platforms:
      - 7280R3
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
    feature_support:
      evpn_gateway_all_active_multihoming: true
      private_vlan: false
    validate_hardware:
      enabled: true
      min_power_supplies: 2
      min_fans: 4
      min_supervisors: 1
      transceiver_manufacturers:
        - Arista Networks
        - Approved Vendor

  - platforms:
      - vEOS.*
      - cEOS.*
    feature_support:
      bgp_update_wait_for_convergence: false
      bgp_update_wait_install: false
      interface_storm_control: false
      queue_monitor_length_notify: false
    reload_delay:
      mlag: 300
      non_mlag: 330
    validate_hardware:
      enabled: false
    digital_twin:
      act_node_type: veos
```

### Platform with Structured Config

This example shows how to apply platform-specific structured configuration.

```yaml title="group_vars/FABRIC/fabric.yml"
custom_platform_settings:
  - platforms:
      - 7280R.*
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
    structured_config:
      hardware:
        access_list:
          mechanism: tcam
        counter:
          default:
            per_interface_ingress: true
      platform:
        sand:
          lag:
            hardware_only: true

  - platforms:
      - 720XP
    management_interface: Management0
    feature_support:
      poe: true
    reload_delay:
      mlag: 300
      non_mlag: 330
    structured_config:
      qos:
        map:
          cos:
            - from: 0
              to: 1
            - from: 1
              to: 0
      priority_flow_control:
        enabled: true
        priorities:
          - priority: 3
            no_drop: true
```

## Common Patterns

### Pattern 1: Regex Platform Matching

Match multiple platform variants with regex:

```yaml
custom_platform_settings:
  - platforms:
      - 7280R.*  # Matches 7280R, 7280R2, 7280R3
    reload_delay:
      mlag: 900
      non_mlag: 1020
    tcam_profile: vxlan-routing
```

### Pattern 2: Digital Twin Configuration

Configure platforms for Digital Twin simulation:

```yaml
custom_platform_settings:
  - platforms:
      - 7050X3
    reload_delay:
      mlag: 300
      non_mlag: 330
    digital_twin:
      platform: vEOS-lab  # Use vEOS-lab in Digital Twin mode
      act_node_type: veos
```

### Pattern 3: Campus Platform with PoE

Configure campus switches with PoE support:

```yaml
custom_platform_settings:
  - platforms:
      - 720XP
      - 750
      - 755
    management_interface: Management0
    feature_support:
      poe: true
      queue_monitor_length_notify: false
    reload_delay:
      mlag: 300
      non_mlag: 330
```

### Pattern 4: Disable Features for Virtual Platforms

Disable unsupported features on virtual platforms:

```yaml
custom_platform_settings:
  - platforms:
      - vEOS.*
      - cEOS.*
    feature_support:
      bgp_update_wait_for_convergence: false
      bgp_update_wait_install: false
      interface_storm_control: false
      queue_monitor_length_notify: false
      hardware_validation: false
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
