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
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTNS/services.yml
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

### SVI Profiles

Use **SVI profiles** to share common settings across multiple SVIs, reducing duplication and ensuring consistency.

```yaml title="SVI Profiles"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTNS/svi_profiles.yml
--8<--
```

1. Define reusable SVI configurations
2. Profiles can inherit from parent profiles for layered configuration

!!! note
    We see the `HIGH_MTU` profile applied to the SVIs in the generated configuration above.

### Generated Configuration

AVD generates the complete configuration including VLANs, VRFs, and SVIs:

```cli title="VLAN, VRF, and SVI Configuration"
--8<--
docs/howto/network_services/artifacts/htns-l3-leaf1-services.cfg
--8<--
```

## Filtering Network Services

Control which services are deployed to specific devices using the `filter` settings.

!!! note
    By default, if no `filter` is defined, all network services are deployed to the device. You can use `filter` at different levels: node_types, node_groups, nodes, device_profiles and devices.

### Filter Options Reference

| Option | Description | Default |
| -------- | ------------- | --------- |
| `tenants` | Limit configured Network Services to those defined under these tenants. Also limits tenants included by `always_include_vrfs_in_tenants`. | `['all']` |
| `tags` | Limit configured VLANs/SVIs to those matching the given tags. Tags are matched against the `tags` list on SVIs and L2VLANs. | `['all']` |
| `allow_vrfs` | Limit configured Network Services to those defined under these VRFs. Also limits VRFs included by `always_include_vrfs_in_tenants`. | `['all']` |
| `deny_vrfs` | Prevent configuration of Network Services defined under these VRFs. **Takes precedence over all other filters.** | `[]` |
| `always_include_vrfs_in_tenants` | List of tenants where VRFs will be configured even if VLANs are not included in tags. Useful for L3 "border" leafs. | `[]` |
| `only_vlans_in_use` | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches. | `false` |

!!! warning "Filter Precedence"
    `deny_vrfs` takes precedence over all other filters including `allow_vrfs` and `always_include_vrfs_in_tenants`. If a VRF is listed in `deny_vrfs`, it will **never** be configured on the device.

### Dynamic Filtering with `only_vlans_in_use`

The `only_vlans_in_use` filter dynamically limits VLANs, SVIs, and VRFs to only those actually in use by connected endpoints or downstream L2 switches. This is useful for keeping switch configurations minimal and avoiding unused VLANs.

```yaml title="only_vlans_in_use Example"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTNS_L2_LEAFS/all.yml
--8<--
```

1. Enable `only_vlans_in_use` to filter VLANs based on actual endpoint usage
2. The server uses VLANs 100-101 on its trunk port - only these VLANs will be configured on `htns-l2-leaf1`

With this configuration, only VLANs that are actually in use by connected endpoints will be configured on the L2 leaf. Any VLANs defined in tenants but not used by endpoints will be excluded from the device configuration.

```cli title="htns-leaf2 configuration"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/intended/configs/htns-l2-leaf1.cfg
--8<--
```

!!! note
    The `only_vlans_in_use` filter only considers configuration managed by eos_designs. It does not account for `structured_config`, `custom_structured_configuration_`, `raw_eos_cli`, `eos_cli`, custom templates, or configlets.

### Filter with Tags

```yaml title="Filtering at the node level"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTNS_L3_LEAFS/l3leaf.yml
--8<--
```

1. Filter settings control which network services are deployed
2. Limit to specific tenants, by default all tenants are included
3. Filter SVIs and L2 VLANs by tags, by default all tags are included
4. Filter which VRFs are deployed (use `deny_vrfs` to exclude specific VRFs), by default all VRFs are included

### Using Tags for Granular Control

=== "Services on htns-l3-leaf2"

    Earlier we saw SVI 200 is tagged with `development`, and the `htns-l3-leaf2` is filtering on the `development` tag. Therefore, the `htns-l3-leaf2` will only receive the `VRF_DEVELOPMENT` VRF and the SVI 200.

    ```cli title="Services on htns-l3-leaf2"
    --8<--
    docs/howto/network_services/artifacts/htns-l3-leaf2-services.cfg
    --8<--
    ```

=== "Services on htns-l3-leaf1"

    Since `htns-l3-leaf1` is not filtering on tags, it receives all services defined for the `TENANT1` tenant.

    ```cli title="Services on htns-l3-leaf1"
    --8<--
    docs/howto/network_services/artifacts/htns-l3-leaf1-services.cfg
    --8<--
    ```

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

- [Network Services Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#network-services)
- [SVI Profiles Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#svi-profiles-settings)
- [Node Type Network Services Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-network-services-configuration)
