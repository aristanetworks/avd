<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# 802.1X Port Authentication

## Introduction

**802.1X** is the IEEE standard for port-based network access control (PNAC). It allows network switches to authenticate devices before granting them access to the network, using a RADIUS server as the authentication backend. AVD provides two complementary data models to configure 802.1X: `dot1x_settings` for global switch-level settings and per-port `dot1x` under connected endpoints for interface-level configuration.

This guide explains how to enable 802.1X globally, define RADIUS servers, create port profiles with dot1x settings, and configure connected endpoints for common use cases like workstations, IP phones, and printers.

### When to Use 802.1X

- **Securing access ports**: Authenticate users and devices before granting network access on edge ports
- **VoIP deployments**: Combine phone and data traffic on trunk phone ports with multi-host authentication
- **Device onboarding**: Use MAC-based authentication as a fallback for devices that do not support 802.1X supplicants
- **Guest network isolation**: Redirect unauthenticated traffic to a guest VLAN using authentication failure actions

## Concepts

**dot1x_settings**: Global switch-level 802.1X configuration applied via `eos_designs`. Enables system-wide authentication control, configures RADIUS server groups, accounting, dynamic authorization (CoA), and MAC address format for RADIUS attribute-value pairs.

**dot1x (per-port)**: Interface-level 802.1X configuration applied through `connected_endpoints` or `network_ports` adapters. Controls port-control mode, PAE role, host mode, reauthentication, and authentication failure actions.

**RADIUS server groups**: Named groups of RADIUS servers referenced by `dot1x_settings` for authentication and accounting. Defined under `aaa_settings.radius.servers` with group membership.

**Port control modes**: `auto` (default for 802.1X) requires successful authentication before forwarding traffic. `force-authorized` bypasses authentication. `force-unauthorized` blocks all traffic regardless of authentication.

**Host modes**: `single-host` allows only one authenticated device per port. `multi-host` allows multiple devices after one is authenticated. `multi-host authenticated` requires each device to authenticate individually.

## Global 802.1X Settings

The `dot1x_settings` key configures switch-wide 802.1X behavior. It must be paired with RADIUS server definitions under `aaa_settings`.

```yaml title="Global dot1x_settings and RADIUS configuration"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/fabric.yml:10:35
--8<--
```

1. Top-level key for global 802.1X configuration
2. Enables `dot1x system-auth-control` on the switch
3. RADIUS server group used for 802.1X authentication requests
4. Enables RADIUS accounting with `start-stop` records
5. Enables RADIUS Change of Authorization (CoA) for dynamic policy updates
6. Formats MAC addresses as colon-delimited lowercase for RADIUS attribute-value pairs
7. Allows BPDU packets from unauthenticated ports (prevents spanning-tree issues)
8. Allows LLDP packets from unauthenticated ports (preserves neighbor discovery)
9. Defines the RADIUS server infrastructure
10. RADIUS server hostname or IP address
11. Server group name referenced by `dot1x_settings.authentication` and `dot1x_settings.accounting`

### Generated Global Configuration

AVD generates the following global dot1x and AAA configuration:

```cli title="Global dot1x configuration on htdx-leaf1a"
--8<--
docs/howto/dot1x/artifacts/htdx-leaf1a-dot1x-global.cfg
--8<--
```

This includes RADIUS server definitions, AAA authentication and accounting policies, MAC-based authentication format, and the four global dot1x system commands.

## Port Profiles for 802.1X

Port profiles define reusable dot1x configurations that can be applied to multiple connected endpoints. This guide defines two profiles: one for standard access ports and one for phone/data trunk ports.

```yaml title="Port profiles with dot1x settings"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/fabric.yml:37:74
--8<--
```

1. Reusable port profile definitions
2. Profile for standard 802.1X access ports (workstations, printers)
3. `auto` requires successful authentication before forwarding
4. Enables periodic reauthentication of connected devices
5. Sets the port as an 802.1X authenticator (switch-side role)
6. `single-host` allows only one device per port
7. Enables MAC-based authentication as a fallback for non-supplicant devices
8. Delegates reauthentication period to the RADIUS server
9. Profile for VoIP deployments with data and voice VLANs
10. `multi-host` allows both phone and workstation on the same port
11. Requires each host to authenticate individually

## Connected Endpoints with 802.1X

Connected endpoints reference port profiles and can override or extend dot1x settings per adapter.

```yaml title="Connected endpoints with dot1x"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/connected_endpoints.yml
--8<--
```

1. Standard workstation with 802.1X authentication
2. Applies the basic `PP-DOT1X` profile with single-host mode
3. IP phone with voice and data VLANs
4. Applies the `PP-DOT1X-PHONE` profile with multi-host mode
5. Native (data) VLAN for the workstation behind the phone
6. Voice VLAN for the IP phone
7. Phone traffic is untagged on the phone VLAN
8. Per-adapter dot1x overrides extend the profile settings
9. On authentication failure, traffic is allowed on a guest VLAN
10. Printer using MAC-based authentication only
11. Inherits base settings from `PP-DOT1X`
12. Per-adapter dot1x overrides for MAC auth
13. `always` uses MAC authentication instead of 802.1X EAP, suitable for devices without supplicants
14. `multi-host` allows the printer and any passthrough devices

### Generated Interface Configuration

=== "Workstation (single-host)"

    ```cli title="htdx-leaf1a Ethernet5 — WORKSTATION-01"
    --8<--
    docs/howto/dot1x/artifacts/htdx-leaf1a-dot1x-workstation.cfg
    --8<--
    ```

    A standard access port with single-host 802.1X. The device must authenticate via EAP or fall back to MAC-based authentication before traffic is forwarded.

=== "IP Phone (multi-host)"

    ```cli title="htdx-leaf1a Ethernet6 — IP-PHONE-01"
    --8<--
    docs/howto/dot1x/artifacts/htdx-leaf1a-dot1x-phone.cfg
    --8<--
    ```

    A trunk phone port carrying both data (native VLAN 100) and voice (VLAN 200). On authentication failure, traffic is redirected to guest VLAN 999.

=== "Printer (MAC auth always)"

    ```cli title="htdx-leaf1b Ethernet5 — PRINTER-01"
    --8<--
    docs/howto/dot1x/artifacts/htdx-leaf1b-dot1x-printer.cfg
    --8<--
    ```

    An access port using `mac based authentication always`, bypassing EAP entirely. This is ideal for devices like printers that lack 802.1X supplicant support.

## Best Practices

1. **Enable dot1x_settings at the leaf group level**: Apply `dot1x_settings` to the leaf switch group rather than individual nodes to ensure consistent RADIUS and authentication behavior across all access switches.

2. **Use port profiles for consistency**: Define standard dot1x profiles (`PP-DOT1X`, `PP-DOT1X-PHONE`) and apply them via `profile` rather than repeating dot1x configuration on every endpoint.

3. **Always configure a RADIUS server**: 802.1X requires at least one RADIUS server defined under `aaa_settings.radius.servers`. AVD validates this and will raise an error if RADIUS is missing.

4. **Set authentication failure actions for critical ports**: Use `authentication_failure.action: allow` with a guest VLAN to prevent complete loss of connectivity when RADIUS is unreachable.

5. **Use MAC-based authentication for non-supplicant devices**: Printers, cameras, and IoT devices typically lack 802.1X supplicants. Enable `mac_based_authentication.always: true` for these ports.

6. **Keep bypass_bpdu and bypass_lldp enabled**: These defaults (both `true`) prevent spanning-tree and LLDP disruption on unauthenticated ports. Only disable them if your security policy explicitly requires it.

## Troubleshooting

### dot1x configuration not generated

**Issue**: Interface configs do not contain dot1x commands.

**Solution**:

- Verify `dot1x_settings.enabled: true` is set at the group or host level for the leaf switches
- Check that the connected endpoint references a port profile with `dot1x` settings, or has `dot1x` defined directly on the adapter
- Ensure the switch is part of the inventory and included in the playbook run

### RADIUS server not reachable

**Issue**: Devices fail to authenticate and the switch logs RADIUS timeout errors.

**Solution**:

- Verify the RADIUS server hostname or IP is correct in `aaa_settings.radius.servers`
- Check that the management VRF and source interface are correctly configured
- Ensure the RADIUS shared secret matches between the switch and server
- Confirm network connectivity from the switch management interface to the RADIUS server

### MAC-based authentication not working

**Issue**: Devices without supplicants are not authenticated via MAC address.

**Solution**:

- Ensure `mac_based_authentication.enabled: true` is set in the port profile or adapter
- For devices that should never attempt EAP, set `mac_based_authentication.always: true`
- Verify the MAC address format in `dot1x_settings.mac_based_authentication.username_format` matches the RADIUS server expectations

### Phone not getting voice VLAN

**Issue**: IP phone is authenticated but does not receive the voice VLAN.

**Solution**:

- Verify the port mode is set to `trunk phone` in the port profile
- Check that `phone_vlan` and `phone_trunk_mode` are configured on the adapter
- Ensure `host_mode.mode: multi-host` is set to allow both phone and workstation

## Reference

For complete details on all available properties, see:

- [802.1X Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#8021x-settings)
- [Port Profiles Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#port-profiles-settings)
- [Connected Endpoints Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#connected-endpoints-settings)
