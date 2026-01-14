<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Network Services

## Introduction

**Network Services** provide an abstracted model to define VRFs, VLANs, SVIs, and L2/L3 services across your AVD fabric. Services are organized by **tenants**, allowing you to logically group network resources by organization, department, or application. AVD then generates the complete switch configuration including VLANs, VRFs, SVIs, VXLAN mappings, and BGP EVPN route targets.

This guide explains how to define tenants, VRFs, SVIs, L2 VLANs, and leverage filtering to control which services are deployed to specific devices.

### When to Use Network Services

Network services define what gets transported across your fabric:

- **VRFs**: Layer 3 routing domains
- **SVIs**: Layer 3 interfaces for VLAN gateways
- **L2 VLANs**: Pure Layer 2 VLANs
- **L3 Interfaces**: Routed interfaces within VRFs

## Concepts

**tenants**: A logical grouping of network services. Tenants provide abstraction above VRFs and VLANs, enabling multi-tenancy and service filtering.

**vrfs**: Virtual Routing and Forwarding instances within a tenant. Each VRF has its own routing table and can contain multiple SVIs and L3 interfaces.

**svis**: Switched Virtual Interfaces that provide Layer 3 gateway functionality for VLANs within a VRF.

**l2vlans**: Pure Layer 2 VLANs that are bridged across the VXLAN fabric without an SVI.

**filter**: Node-level settings that control which tenants, VRFs, and tags are deployed to specific devices.

**svi_profiles**: Reusable templates for common SVI settings.

## Basic Network Services

The example shows a network services configuration which defines a tenant with VRFs and SVIs:

```yaml title="Network Services"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HOW_TO_NETWORK_SERVICES/services.yml
--8<--
```

1. Tenant name used for grouping and filtering
2. Base VNI for MAC-VRFs - VLAN ID is added to this value (VLAN 100 = VNI 10100)
3. VRF VNI used for L3 VNI in EVPN Type-5 routes
4. VTEP diagnostic creates a loopback for troubleshooting connectivity
5. Virtual IP address shared across all leaf switches (anycast gateway)
6. SVI profile applied to services that share common settings (enabled, mtu, etc.)
7. Tags can be assigned to network services to control which devices receive the configuration.
8. L2 VLANs are bridged across VXLAN without an SVI

### Generated Configuration

AVD generates the complete configuration including VLANs, VRFs, and SVIs:

```cli title="VLAN, VRF, and SVI Configuration"
--8<--
docs/howto/network_services/artifacts/howto-l3-leaf1-services.cfg
--8<--
```

## SVI Profiles

Use **SVI profiles** to share common settings across multiple SVIs, reducing duplication and ensuring consistency.

```yaml title="SVI Profiles"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HOW_TO_NETWORK_SERVICES/svi_profiles.yml
--8<--
```

1. Define reusable SVI configurations
2. Profiles can inherit from parent profiles for layered configuration

!!! note
    We see the `HIGH_MTU` profile applied to the SVIs in the generated configuration above.

## Filtering Network Services

Control which services are deployed to specific devices using the `filter` settings under node type configuration.

```yaml title="group_vars/DC1_L3_LEAVES/filter.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/DC1_L3_LEAVES/filter.yml
--8<--
```

1. Filter settings control which network services are deployed
2. Limit to specific tenants or use `all` for all tenants
3. Filter SVIs and L2 VLANs by tags
4. Filter which VRFs are deployed (use `deny_vrfs` to exclude specific VRFs)

### Using Tags for Granular Control

Tags provide fine-grained control over which SVIs and L2 VLANs are deployed to each device:

```yaml title="group_vars/NETWORK_SERVICES/tagged_services.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/NETWORK_SERVICES/tagged_services.yml
--8<--
```

1. Tags control which devices receive this SVI

Then filter by tags on specific node groups:

```yaml title="Production Leaves Filter"
l3leaf:
  node_groups:
    - group: PRODUCTION_LEAVES
      filter:
        tags:
          - production
          - app_servers
```

## L3 Interfaces in VRFs

Configure routed interfaces within VRFs for external connectivity:

```yaml title="group_vars/NETWORK_SERVICES/l3_interfaces.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/NETWORK_SERVICES/l3_interfaces.yml
--8<--
```

1. L3 interfaces create routed interfaces inside the VRF
2. Interfaces, IP addresses, and nodes lists must have the same length

## Best Practices

1. **Organize by tenant**: Group related services under logical tenants for easier management and filtering.

2. **Use SVI profiles**: Define common settings once and apply to multiple SVIs for consistency.

3. **Leverage tags**: Use tags to control service deployment at a granular level without creating complex tenant structures.

4. **Plan VNI allocation**: Establish a consistent `mac_vrf_vni_base` strategy across tenants to avoid VNI conflicts.

5. **Use VTEP diagnostics**: Enable `vtep_diagnostic` on VRFs for troubleshooting VXLAN connectivity.

6. **Document your tenants**: Clearly document the purpose and scope of each tenant in your organization.

## Troubleshooting

### VLAN not appearing on device

**Issue**: A VLAN defined in network services is not configured on the device.

**Solution**:

- Verify the tenant is included in `filter.tenants` on the node
- Check that the SVI/L2VLAN tags match `filter.tags` on the node
- Ensure the VRF is not excluded by `filter.deny_vrfs`

### VRF not created

**Issue**: VRF is defined but not appearing in configuration.

**Solution**:

- VRFs are only created if they have at least one SVI, L3 interface, or loopback on the device
- Check that SVIs within the VRF pass the tag and tenant filters
- Verify the node type has `network_services.l3: true` enabled

### Duplicate VNI error

**Issue**: Error about duplicate or conflicting VNIs.

**Solution**:

- Review `mac_vrf_vni_base` values across tenants to ensure VLANs don't result in the same VNI
- Check for `vni_override` settings that may conflict
- Verify `vrf_vni` values are unique across all VRFs

### SVI not getting virtual IP

**Issue**: SVI is created but missing the virtual IP address.

**Solution**:

- Verify `ip_virtual_router_mac_address` is set at the fabric level
- Check that `ip_address_virtual` is correctly specified on the SVI
- Ensure the node type supports L3 network services (`network_services.l3: true`)

## Reference

For complete details on all available properties, see:

- [Network Services Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/input-variables.md#network-services)
- [SVI Profiles Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/input-variables.md#svi-profiles-settings)
- [Node Type Network Services Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/input-variables.md#node-type-network-services-configuration)
