<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# WAN Settings

## Introduction

**WAN Settings** are global AVD variables that control how all WAN devices in a fabric establish secure tunnels, select the WAN operating mode, and authenticate peers. These settings must be consistent across every device participating in the WAN network — from Pathfinders to Edge routers — because they define the shared IPsec profiles, BGP policies, and session negotiation parameters that enable the WAN overlay.

Without correctly configured WAN settings, WAN devices cannot form DPS tunnels or exchange routing information through the EVPN overlay.

### When to Use WAN Settings

Configure WAN settings when:

- **Deploying CV Pathfinder**: Set `wan_mode: cv-pathfinder` and define IPsec profiles for all WAN devices.
- **Deploying AutoVPN only**: Set `wan_mode: legacy-autovpn` for simpler hub-and-spoke WAN without CloudVision integration.
- **Customizing IPsec**: Override the default IKE policy, SA policy, or profile names for control-plane and data-plane tunnels.
- **Disabling STUN DTLS for lab environments**: Use `wan_stun_dtls_disable: true` to skip certificate requirements in test deployments.
- **Enabling WAN High Availability**: Configure `wan_ha` to set a custom LAN HA path-group name.

## Concepts

**wan_mode**: Selects between `cv-pathfinder` (default, uses CloudVision for metadata and certificate distribution) and `legacy-autovpn` (hub-and-spoke without CloudVision). This must be identical on every WAN device.

**wan_ipsec_profiles**: Defines the IPsec security profiles used for WAN tunnel authentication. Separate profiles exist for `control_plane` (BGP overlay sessions) and `data_plane` (forwarding path tunnels). If `data_plane` is omitted, the control-plane profile is used for both.

**wan_stun_dtls_disable**: By default, STUN connections for DPS path discovery are secured with DTLS and require certificates. Setting this to `true` disables DTLS — acceptable in isolated lab environments but must never be used on internet-connected WAN links.

**wan_encapsulation**: Selects the EVPN encapsulation for WAN BGP peers. The default `path-selection` uses the DPS path-selection overlay. `vxlan` is an alternative when direct VXLAN encapsulation is preferred.

**wan_ha**: Controls WAN High Availability settings. The `lan_ha_path_group_name` key (default: `LAN_HA`) names the auto-injected path-group used for direct LAN HA tunnels between HA-paired WAN routers.

## Minimal WAN Settings Example

The following example shows a complete minimal WAN deployment: one Pathfinder and one Edge router connected over a single ISP path group. The focus is on the global settings that must be defined once and shared across all WAN devices.

### Global Settings

```yaml title="group_vars/HTWS/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTWS/fabric.yml
--8<--
```

1. `wan_mode: cv-pathfinder` selects CV Pathfinder mode. This must be the same on every WAN device.
2. `wan_ipsec_profiles` defines the IPsec credentials. Both `control_plane` and `data_plane` keys are shown; if `data_plane` is omitted, the control-plane profile is reused for data-plane tunnels.
3. `wan_stun_dtls_disable: true` is suitable for lab use. Remove this in production — CloudVision will automatically distribute certificates when using CV Pathfinder.
4. `wan_encapsulation: path-selection` is the default and selects the DPS overlay. This line is optional since it matches the default value.
5. `cv_pathfinder_global_sites` defines sites not tied to any region (typically Pathfinder locations).
6. `cv_pathfinder_regions` defines the WAN hierarchy of regions and sites used by Edge routers.

!!! warning
    All variables in this file must have identical values on every device participating in the WAN fabric. Use a shared group or the `arista.avd.global_vars` plugin when devices span multiple inventories.

### Pathfinder Node

```yaml title="group_vars/HTWS_PATHFINDERS/pathfinders.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTWS_PATHFINDERS/pathfinders.yml
--8<--
```

### Edge Router Node

```yaml title="group_vars/HTWS_EDGES/edges.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTWS_EDGES/edges.yml
--8<--
```

## Generated Configuration

### IPsec Profiles (Edge Router)

The `wan_ipsec_profiles` input produces separate IKE policies, SA policies, and IPsec profiles for control-plane and data-plane traffic:

```cli title="htws-edge1: ip security"
--8<--
docs/howto/wan_settings/artifacts/htws-edge1-ipsec.cfg
--8<--
```

Note that the shared keys are stored as Type 7 obfuscated values in the rendered configuration. The `cleartext_shared_key` input is never written in plaintext to the device — use Ansible Vault to protect the source variable.

### Path Selection (Pathfinder)

On the Pathfinder, AVD generates the `router path-selection` block to register the local WAN interface into the INTERNET path group, configure STUN, and define load-balance policies:

```cli title="htws-pf1: router path-selection"
--8<--
docs/howto/wan_settings/artifacts/htws-pf1-path-selection.cfg
--8<--
```

### BGP Overlay (Pathfinder)

The Pathfinder uses a BGP listen range to accept sessions from any Edge router whose DPS IP falls within the configured `listen_range_prefixes`. All WAN devices use the same BGP AS (iBGP):

```cli title="htws-pf1: router bgp 65000"
--8<--
docs/howto/wan_settings/artifacts/htws-pf1-bgp.cfg
--8<--
```

## IPsec Profiles: Control Plane vs. Data Plane

AVD generates two distinct IPsec profiles when both `control_plane` and `data_plane` keys are configured in `wan_ipsec_profiles`:

| Profile | Purpose | Policy names |
| ------- | ------- | ------------ |
| `CP-PROFILE` | Secures EVPN BGP overlay sessions | CP-IKE-POLICY / CP-SA-POLICY |
| `DP-PROFILE` | Secures DPS forwarding tunnels | DP-IKE-POLICY / DP-SA-POLICY |

If only `control_plane` is defined, both profiles share the same credentials. Separating them with different keys is recommended for production so that compromise of one profile does not affect the other.

You can also override the default profile and policy names using the optional `ike_policy_name`, `sa_policy_name`, and `profile_name` sub-keys.

## WAN HA Settings

When WAN HA is enabled at the node level (`wan_ha.enabled: true`), AVD automatically injects a `LAN_HA` path group to form DPS tunnels over the LAN between HA-paired routers. Use `wan_ha.lan_ha_path_group_name` to rename this path group if `LAN_HA` conflicts with existing path-group names in your design:

```yaml
wan_ha:
  lan_ha_path_group_name: MY-HA-PATH-GROUP
```

!!! note
    WAN HA is only supported in `cv-pathfinder` mode. `legacy-autovpn` does not support WAN HA.

## Best Practices

1. **Use Ansible Vault for shared keys**: Both `cleartext_shared_key` and `shared_key` contain sensitive credentials. Encrypt them with Ansible Vault and never commit plaintext keys to source control.
2. **Separate control-plane and data-plane profiles**: Define distinct keys for `control_plane` and `data_plane` so that key rotation on one does not disrupt the other.
3. **Keep wan_mode consistent**: Place all WAN settings in a group that includes every WAN device, or use `arista.avd.global_vars` to share variables across multiple inventories.
4. **Disable STUN DTLS only in isolated labs**: `wan_stun_dtls_disable: true` removes authentication from STUN. Never use it on links exposed to untrusted networks.
5. **Use trusted: true only for private carriers**: Mark a `wan_carrier` as `trusted: true` only for private MPLS or similar circuits. Internet-facing carriers should require `ipv4_acl_in` to restrict inbound traffic on WAN interfaces.

## Troubleshooting

### Edge router fails with "Dps1 IP is not in the Route Reflector listen range prefixes"

**Issue**: Molecule or eos_designs reports that the edge's DPS IP is not covered by the Pathfinder's listen range.

**Solution**:

- The edge's DPS IP is drawn from `vtep_loopback_ipv4_pool`. Ensure `bgp_peer_groups.wan_overlay_peers.listen_range_prefixes` includes this pool:

```yaml
bgp_peer_groups:
  wan_overlay_peers:
    listen_range_prefixes:
      - 10.255.9.0/27  # must match vtep_loopback_ipv4_pool
```

### Pathfinder fails with "data_plane_cpu_allocation_max must be set"

**Issue**: AVD validation rejects the Pathfinder node.

**Solution**:

- Add `data_plane_cpu_allocation_max` to the `wan_rr.defaults` block. A value of `1` is appropriate for vEOS-lab; production hardware typically uses `2` or higher:

```yaml
wan_rr:
  defaults:
    data_plane_cpu_allocation_max: 1
```

### WAN interface fails with "ipv4_acl_in must be set"

**Issue**: AVD rejects a WAN interface because the carrier is not marked as trusted.

**Solution**:

- Either add `trusted: true` to the carrier definition (for private circuits), or define a named ACL and reference it on the interface via `ipv4_acl_in`:

```yaml
wan_carriers:
  - name: ISP1
    path_group: INTERNET
    trusted: true  # use only for private/trusted carriers
```

## Reference

For complete details on all available properties, see:

- [WAN Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#wan-settings)
- [WAN Path Groups and Carriers](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#wan-settings)
- [WAN Virtual Topologies](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#wan-settings)
- [Node Type WAN Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-wan-configuration)
