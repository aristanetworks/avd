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

**RADIUS server groups**: Named groups of RADIUS servers referenced by `dot1x_settings` for authentication and accounting. Defined under `aaa_settings.radius.servers` with group membership. Server groups are optional — if not provided, all configured RADIUS servers are targeted using `aaa authentication dot1x default group radius` and `aaa accounting dot1x default start-stop group radius`.

**Port control modes**: `auto` (default for 802.1X) requires successful authentication before forwarding traffic. `force-authorized` bypasses authentication. `force-unauthorized` blocks all traffic regardless of authentication.

**Host modes**: `single-host` allows only one authenticated device per port. `multi-host` allows multiple devices after one is authenticated. `multi-host authenticated` requires each device to authenticate individually.

## Global 802.1X Settings

Only two settings are required to enable 802.1X: `dot1x_settings.enabled: true` and a RADIUS server defined under `aaa_settings`. AVD generates sensible defaults for all other options, which is sufficient for most use cases.

### Minimal Configuration

```yaml title="Minimal dot1x configuration"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/fabric.yml:dot1x_minimal
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/fabric.yml:aaa_minimal
--8<--
```

### Full Configuration

The following example customizes authentication, accounting, dynamic authorization, and MAC format settings:

```yaml title="Full dot1x_settings and RADIUS configuration"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTDX/fabric.yml:dot1x_full
--8<--
```

1. RADIUS server group used for 802.1X authentication requests
2. Enables RADIUS accounting with `start-stop` records
3. Enables RADIUS Change of Authorization (CoA) for dynamic policy updates
4. Formats MAC addresses as colon-delimited lowercase for RADIUS attribute-value pairs
5. Allows BPDU packets from unauthenticated ports (prevents spanning-tree issues)
6. Allows LLDP packets from unauthenticated ports (preserves neighbor discovery)
7. Server group name referenced by `dot1x_settings.authentication` and `dot1x_settings.accounting`

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

!!! note "Consult your organization's security policy"
    The recommendations below reflect common deployment patterns. Always defer to your organization's security policies and NAC vendor guidelines when configuring 802.1X, as requirements vary by environment and compliance framework.

1. **Use multi-host authenticated mode**: Set `host_mode.mode: multi-host` with `multi_host_authenticated: true` so every device on the port must individually authenticate. This is the recommended mode for most campus deployments.

2. **Enable reauth-timeout-ignore**: Set `timeout.reauth_timeout_ignore: true` to retain authenticated supplicants when the AAA server is unavailable during reauthentication, preventing network disruption through cached authentication.

3. **Delegate reauthentication period to the RADIUS server**: Set `timeout.reauth_period: server` to let the NAC control reauthentication intervals. For high-scale environments, consider increasing the period on the RADIUS server to reduce authentication load.

4. **Prefer simultaneous MBA and dot1x**: For ports with mixed device types, set `mac_based_authentication.always: true` rather than relying on EAPOL fallback to MBA. This ensures devices without 802.1X supplicants (printers, IoT, cameras) authenticate via MAC address immediately.

5. **Enable dynamic authorization (CoA)**: Set `dot1x_settings.dynamic_authorization.enabled: true` to allow the RADIUS server to push policy changes (VLAN assignment, ACL, session disconnect) to the switch without waiting for reauthentication.

6. **Configure AAA unresponsive fallback**: Use `dot1x.aaa.unresponsive.action.traffic_allow_vlan` with a fallback VLAN and `authentication_failure.action: allow` with a guest VLAN to prevent complete loss of connectivity when the RADIUS server is unreachable.

7. **Use trunk phone mode for VoIP ports**: Access ports do not support phone and data device segregation. Always set `mode: "trunk phone"` on ports connecting IP phones with passthrough data devices.

8. **Enable LLDP and BPDU bypass**: Set `dot1x_settings.bypass_lldp: true` and `dot1x_settings.bypass_bpdu: true` to allow LLDP and BPDU processing on unauthenticated ports. LLDP bypass improves phone detection reliability, and BPDU bypass prevents spanning-tree disruption.

9. **Send service-type in RADIUS requests**: Set `dot1x_settings.radius_av_pairs.service_type: true` to include the Service-Type attribute in RADIUS Access-Request packets, providing the NAC with additional context about each authentication session.

10. **Use port profiles for consistency**: Define standard dot1x profiles (`PP-DOT1X`, `PP-DOT1X-PHONE`) in AVD and apply them via `profile` rather than repeating dot1x configuration on every endpoint.

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
