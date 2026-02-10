<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Connected Endpoints

## Introduction

**connected_endpoints** is an endpoint-centric model intended for servers or other devices where most ports have unique configurations. Instead of manually creating `interface Ethernet` configurations for every server, you describe the connections using adapters and profiles, and AVD generates the complete, standardized configuration for you.

This guide explains how to define port profiles, configure adapters for your endpoints, and generate the final switch configuration.

### When to Use Connected Endpoints

Use `connected_endpoints` when:

- Each server or device has a unique configuration (specific VLANs, port-channels, descriptions)
- You need to document the endpoint name and connection details
- You want to track which device connects to which switch port

Use `network_ports` instead when:

- Many ports share identical configurations
- You want to apply the same profile to a range of interfaces
- Endpoint-specific details are not required

!!! warning
    Both data models share the same underlying implementation and can coexist without conflicts. If a switch port is defined in both “Connected Endpoints” and “Network Ports”, the “Connected Endpoints” configuration will take precedence.

## Concepts

**port_profiles**: Port profiles are used to share common settings for connected_endpoints and network_ports. Keys are the same as those used under endpoint adapters. Keys defined under endpoint adapters take precedence.

**adapters**:  An adapter represents a network interface on the connected_endpoint.

### Port Profiles

A **Port Profile** is a reusable template that defines a standard set of switchport configurations. You create a profile once and then apply it to any number of connected endpoints. This ensures consistency and dramatically simplifies configuration.

A port profile can refer to another port profile using parent_profile to inherit settings in up to two levels (adapter->profile->parent_profile).

#### Key Settings for a Port Profile

- `mode`: Can be `access` or `trunk`.
- `vlans`: For `access` mode, the single VLAN ID. For `trunk` mode, the list of allowed VLANs.
- `port_channel`: Defines Port-Channel settings like `mode` (`active` for LACP) and `channel_id`.
- `spanning_tree_portfast`: Set to `edge` for server ports.
- `native_vlan`: For trunk ports, defines the native VLAN.
- `storm_control`: To apply storm control policies.
- `flowcontrol`: To configure flow control settings.

Please consult the [User Manual](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#port-profiles-settings) for all available keys.

### Adapters

**Adapters** serve as the bridge between the Fabric (the switches) and the Endpoints (the devices). They define how a specific device is cabled and what network services (VLANs, VRFs) it should receive.

#### Key settings Adapters

Adapters define the physical mapping between the endpoint and the switch fabric:

- `endpoint_ports`: Port name for the endpoint, e.g., eth0.
- `switch_ports`: Specifies which physical interface(s) on the switch connect to the adapter.
- `switches`: The switches to which the interface will connect.
- `Profiles`: The port profile to apply for this adapter's configuration.
- `description`: A brief description of the interface function.

!!! note
    The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.

Please consult [User Manual](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#connected-endpoints-settings) for all available keys.

### Define port profiles

```yaml title="group_vars/DC1/port_profiles.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1/port_profiles.yml
--8<--
```

1. Profile for a single-homed server in VLAN 10
2. Profile for a dual-homed (LACP) server trunking two VLANs
3. Profile for a trunk port connecting to a firewall

### Define your connected endpoints

```yaml title="group_vars/CONNECTED_ENDPOINTS/ce.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/CONNECTED_ENDPOINTS/ce.yml
--8<--
```

1. Within `port_channel`, we define its existence and what mode we would like to use, but there is no additional requirement like setting the Port Channel ID. That is done automatically. You can always override the default by setting the `channel_id` key within your Port Channel definition. The default Port Channel selected will be derived from the first switch port in the adapter.

### Generated Configuration

Device configuration is located in `intended/configs/`

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

## Best Practices

1. **Use port profiles for consistency**: Define reusable profiles for common configurations like single-homed servers, dual-homed servers, or firewall connections.

2. **Leverage parent profiles**: Use `parent_profile` to create a hierarchy of profiles, reducing duplication and simplifying updates.

3. **Consistent naming conventions**: Establish clear naming patterns for endpoints and profiles to improve readability and maintenance.

4. **Connected endpoints description**: AVD uses a default pattern to create the description `{endpoint_type}_{endpoint}_{endpoint_port(if defined)}`. To customize this pattern please refer to the [Custom Descriptions and Names](../../../ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.md) documentation.

5. **Validate list lengths**: Ensure `endpoint_ports`, `switch_ports`, and `switches` lists have the same length to avoid configuration errors.

6. **Test incrementally**: When adding new endpoints, test changes on a small subset before applying to the entire fabric.

## Troubleshooting

### VLAN not applied to interface

**Issue**: The expected VLAN is not configured on the interface.

**Solution**:

- Verify the VLAN is defined in `network_services` for the tenant
- Check that the switch has the VLAN assigned via `filter.tags` or `filter.tenants`
- Ensure the `vlans` key in the port profile or adapter is correct

### Port-channel not forming

**Issue**: Port-channel is configured but not forming between server and switches.

**Solution**:

- Verify both sides have matching `port_channel.mode` (e.g., both set to `active`)
- Check that the physical interfaces are correctly mapped in `switch_ports`
- Ensure MLAG is properly configured if using MLAG port-channels

### Adapter/switch list length mismatch

**Error**: Lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.

**Solution**: Ensure all three lists have exactly the same number of elements. Each index represents one connection.

### Configuration not generated

**Issue**: Endpoint defined but no configuration appears in output.

**Solution**:

- Verify the endpoint is defined under a valid `<connected_endpoints_key>` (e.g., `servers`, `firewalls`)
- Check that the switches referenced in `switches` are part of the fabric
- Ensure the playbook includes the switches where endpoints are connected

## Reference

For complete details on all available properties, see:

- [Port Profiles Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#port-profiles-settings)
- [Connected Endpoints Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#connected-endpoints-settings)
- [Network Ports Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#network-ports-settings)
