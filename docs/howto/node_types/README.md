<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Node Types

## Introduction

**Node Types** define the role and capabilities of devices in your AVD fabric. They determine what features are enabled on each device, such as EVPN roles, MLAG support, network services, and routing protocols. AVD provides default node types for common architectures, but you can also create custom node types to match your specific requirements.

This guide explains how to use the default node types, create custom node types, and automatically assign node types based on hostname patterns.

## Concepts

**node_type_keys**: The list of node type definitions that specify the properties and capabilities of each node type in the fabric. AVD includes default node types like `spine`, `l3leaf`, `l2leaf`, `pe`, `p`, etc.

**custom_node_type_keys**: Allows you to define additional node types or override default node types without replacing the entire `node_type_keys` list.

**default_node_types**: Automatically assigns node types to devices based on hostname regex patterns, eliminating the need to manually set `type` on each device.

**type**: The variable set on each device (or group) that references a node type defined in `node_type_keys` or `custom_node_type_keys`.

## Default Node Types

AVD provides several built-in node types optimized for different fabric architectures:

### Data Center Fabric Node Types

- **spine**: Spine switches acting as EVPN route servers
- **l3leaf**: Layer 3 leaf switches with VXLAN/EVPN capabilities, MLAG support, and connected endpoints
- **l2leaf**: Layer 2 leaf switches with MLAG support, no routing capabilities
- **super_spine**: Super spine for 5-stage CLOS architectures
- **overlay_controller**: Dedicated EVPN route servers

### MPLS/SR Node Types

- **p**: Provider (P) routers with MPLS LSR capabilities
- **pe**: Provider Edge (PE) routers with MPLS, EVPN, and connected endpoints support
- **rr**: Route reflectors for MPLS networks

### Campus Fabric Node Types

- **l3spine**: Layer 3 spine for campus architectures
- **leaf**: Campus leaf switches with Layer 2 capabilities
- **l2spine**: Layer 2 spine switches

### WAN Node Types

- **wan_router**: WAN edge routers for CV Pathfinder
- **wan_rr**: WAN route reflectors/pathfinders

## Using Default Node Types

The simplest way to use node types is to set the `type` variable on your devices or groups:

```yaml title="group_vars/DC1_SPINES/spines.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_SPINES/spines.yml
--8<--
```

In this example:

- The `type: spine` tells AVD to use the built-in `spine` node type
- The `spine:` key contains the device-specific configuration
- AVD will configure this device as a spine switch with EVPN route server capabilities

## Automatically Assigning Node Types

Instead of manually setting `type` on each group, use `default_node_types` to automatically assign types based on hostname patterns.

```yaml title="group_vars/FABRIC/node_types.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/FABRIC/default_node_types.yml
--8<--
```

With this configuration:

- Devices with hostnames matching `.*-spine.*` (like `dc1-spine1`) automatically get `type: spine`
- Devices matching `.*-svc-leaf.*` (like `dc1-svc-leaf1`) automatically get `type: service_leaf`
- Devices matching `.*-leaf.*` (like `dc1-leaf1a`) automatically get `type: l3leaf`

!!! note

    The regex patterns are automatically bounded by `^` and `$`, so they must match the full hostname.
    Order matters - the first matching pattern wins.

Now you can define devices without explicitly setting `type`:

```yaml title="group_vars/DC1_SERVICE_LEAVES/service_leaves.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_SERVICE_LEAVES/service_leaves.yml
--8<--
```

Notice that there's no `type:` variable - it's automatically assigned based on the hostname pattern!

## Creating Custom Node Types

Use `custom_node_type_keys` to define new node types or modify existing ones.

```yaml title="group_vars/FABRIC/node_types.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/FABRIC/custom_node_types.yml
--8<--
```

This creates a new `service_leaf` node type with:

- **Connected endpoints support**: Servers can connect to these switches
- **EVPN client role**: Participates in EVPN as a client
- **MLAG support**: Can form MLAG pairs
- **Network services**: Supports L2 (VLANs) and L3 (VRFs/SVIs)
- **VXLAN VTEP**: Acts as a VXLAN tunnel endpoint
- **Underlay routing**: Participates in underlay routing
- **P2P uplinks**: Uses point-to-point uplinks to spines

### Using Your Custom Node Type

Once defined, use your custom node type like any default type. Combined with `default_node_types`, devices are automatically assigned the custom type:

```yaml title="group_vars/DC1_SERVICE_LEAVES/service_leafs.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_SERVICE_LEAVES/service_leafs.yml
--8<--
```

## Modifying Default Node Types

To modify a default node type, use `custom_node_type_keys` with the same `key` as the default:

```yaml title="group_vars/FABRIC/override_node_types.yml"
---
custom_node_type_keys:
  # Override the default l3leaf to disable connected endpoints
  - key: l3leaf
    type: l3leaf
    connected_endpoints: false  # Disable connected endpoints
    default_evpn_role: client
    mlag_support: true
    network_services:
      l2: true
      l3: true
    vtep: true
```

!!! warning

    When overriding a default node type, you must specify all required properties, not just the ones you want to change.

## Common Node Type Properties

### Key Properties

| Property | Type | Description |
| ---------- | ------ | ------------- |
| `key` | string | The key used in your data model (e.g., `spine`, `l3leaf`) |
| `type` | string | The type value that devices reference |
| `connected_endpoints` | boolean | Enable connected endpoints configuration |
| `default_evpn_role` | string | Default EVPN role: `none`, `client`, or `server` |
| `default_wan_role` | string | Default WAN role for CV Pathfinder: `client` or `server` |
| `mlag_support` | boolean | Enable MLAG support |
| `vtep` | boolean | Enable VXLAN VTEP functionality |
| `underlay_router` | boolean | Enable Layer 3 routing (default: true) |
| `mpls_lsr` | boolean | Enable MPLS Label Switching Router capabilities |

### Network Services

```yaml
network_services:
  l1: true  # Point-to-point services
  l2: true  # VLANs
  l3: true  # VRFs and SVIs (requires l2: true and underlay_router: true)
```

### Routing Protocols

```yaml
default_underlay_routing_protocol: ebgp  # ebgp, ibgp, ospf, ospf-ldp, isis, isis-sr, isis-ldp, isis-sr-ldp, none
default_overlay_routing_protocol: ebgp   # ebgp, ibgp, her, cvx, none
default_mpls_overlay_role: client        # client, server, none
```

### Uplink Configuration

```yaml
uplink_type: p2p  # p2p, port-channel, p2p-vrfs, lan
```

- **p2p**: Point-to-point Layer 3 uplinks (default for most routed node types)
- **port-channel**: LACP port-channel uplinks (default for l2leaf)
- **p2p-vrfs**: Layer 3 uplinks with subinterfaces per VRF
- **lan**: LAN uplinks for campus designs

## Advanced Example: MPLS PE Router

Create a custom PE router with specific MPLS and EVPN settings:

```yaml title="group_vars/FABRIC/mpls_node_types.yml"
---
custom_node_type_keys:
  - key: custom_pe
    type: custom_pe
    mpls_lsr: true
    connected_endpoints: true
    default_mpls_overlay_role: client
    default_evpn_role: client
    network_services:
      l1: true  # Point-to-point services
      l2: true  # VLANs
      l3: true  # VRFs
    default_overlay_routing_protocol: ibgp
    default_underlay_routing_protocol: isis-sr
    default_overlay_address_families:
      - evpn
      - vpn-ipv4
    default_evpn_encapsulation: mpls
```

## Best Practices

1. **Use `custom_node_type_keys` for additions**: When adding new node types, use `custom_node_type_keys` instead of replacing the entire `node_type_keys` list.

2. **Leverage `default_node_types`**: Use hostname patterns to automatically assign types, reducing manual configuration and errors.

3. **Consistent naming conventions**: Establish clear hostname patterns that align with your `default_node_types` configuration.

4. **Document custom types**: When creating custom node types, document their purpose and intended use cases.

5. **Test incrementally**: When modifying node types, test changes on a small subset of devices first.

6. **Review default properties**: Before overriding a default node type, review all its properties to ensure you maintain necessary functionality.

## Troubleshooting

### Device type not found

**Error**: `No device type found. Either set 'type' or 'default_node_types'.`

**Solution**: Ensure either:

- The device has `type` set in its group_vars, or
- A `default_node_types` pattern matches the device hostname

### Node type key not found

**Error**: `Could not find the given type 'X' in node_type_keys or custom_node_type_keys.`

**Solution**: Verify the `type` value matches a `type` field in either `node_type_keys` or `custom_node_type_keys`.

### Configuration not applied

**Issue**: Custom node type defined but configuration not applied.

**Solution**:

- Verify the `key` in `custom_node_type_keys` matches the key used in your data model
- Check that devices reference the correct `type` value
- Ensure `custom_node_type_keys` is defined at the fabric level (not per-device)

## Quick Reference

### Three Ways to Assign Node Types

#### Manual Assignment (Explicit)

Set `type` explicitly on the device group:

```yaml title="group_vars/DC1_SPINES/spines.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_SPINES/spines.yml
--8<--
```

#### Automatic Assignment (Pattern-Based)

Use `default_node_types` to assign types based on hostname patterns:

```yaml title="group_vars/FABRIC/node_types.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/FABRIC/default_node_types.yml
--8<--
```

Then define devices without explicit `type`:

```yaml title="group_vars/DC1_SERVICE_LEAVES/service_leaves.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_SERVICE_LEAVES/service_leaves.yml
--8<--
```

#### Custom Node Type

Use `custom_node_type_keys` to define new node types:

```yaml title="group_vars/FABRIC/node_types.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/FABRIC/custom_node_types.yml
--8<--
```

### Common Properties Reference

| Property | Values | Description |
| ---------- | -------- | ------------- |
| `key` | string | Data model key (e.g., `spine:`) |
| `type` | string | Type devices reference |
| `connected_endpoints` | true/false | Enable connected endpoints |
| `default_evpn_role` | none/client/server | EVPN role |
| `mlag_support` | true/false | Enable MLAG |
| `vtep` | true/false | Enable VXLAN VTEP |
| `underlay_router` | true/false | Enable L3 routing |
| `uplink_type` | p2p/port-channel/p2p-vrfs/lan | Uplink configuration |

### Default Node Types Comparison (high-level)

| Node Type | EVPN Role | VTEP | MLAG | Connected Endpoints | Use Case |
| ----------- | ----------- | ------ | ------ | --------------------- | ---------- |
| spine | server | ❌ | ❌ | ❌ | Spine switches |
| l3leaf | client | ✅ | ✅ | ✅ | L3 leaf switches |
| l2leaf | none | ❌ | ✅ | ✅ | L2 leaf switches |
| pe | client | ❌ | ❌ | ✅ | MPLS PE routers |
| p | none | ❌ | ❌ | ❌ | MPLS P routers |
| wan_router | client | ❌ | ❌ | ✅ | WAN edge routers |
| wan_rr | server | ❌ | ❌ | ❌ | WAN route reflectors |

## Reference

For complete details on all available node type properties, see:

- [Default Node Types Variables](../../../ansible_collections/arista/avd/roles/eos_designs/docs/input-variables.md#node-type-variables)
- [Node Type Customization](../../../ansible_collections/arista/avd/roles/eos_designs/docs/input-variables.md#node-type-customization)
