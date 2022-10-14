---
search:
  boost: 2
---

# Input Variables

## DC Name

Optional DC Name, only used in SNMP location and Fabric Documentation.
Recommended to be common between all devices within a Site

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    dc_name: <str>
    ```

## Default IGMP Snooping Enabled

Disable IGMP snooping at fabric level.
If set, it overrides per vlan settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    default_igmp_snooping_enabled: <bool>
    ```

## Design

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | l3ls-evpn | Valid Values:<br>- l3ls-evpn<br>- mpls | By setting the `design.type` to `mpls`,<br>the default node-types and templates described in these documents will be used.<br> |

=== "YAML"

    ```yaml
    design:
      type: <str>
    ```

## Enable Trunk Groups

Enable Trunk Group support across eos_designs
Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    enable_trunk_groups: <bool>
    ```

## Fabric Name

Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    fabric_name: <str>
    ```

## Internal VLAN Order

Internal vlan allocation order and range

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String |  | ascending | Valid Values:<br>- ascending<br>- descending |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer |  | 1006 |  | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer |  | 1199 |  | VLAN ID |

=== "YAML"

    ```yaml
    internal_vlan_order:
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    ```

## MAC Address Table

MAC address-table aging time
Use to change the EOS default of 300.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  |  | Time in seconds |

=== "YAML"

    ```yaml
    mac_address_table:
      aging_time: <int>
    ```

## MLAG Ibgp Peering VRFs

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when mlag leafs in topology)
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1
Depending on the values of vrf_id / vrf_id it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | 3000 | Min: 1<br>Max: 4000 |  |

=== "YAML"

    ```yaml
    mlag_ibgp_peering_vrfs:
      base_vlan: <int>
    ```

## Only Local VLAN Trunk Groups

A vlan can have many trunk_groups assigned. To avoid unneeded configuration changes on all leaf
switches when a new trunk group is added, this feature will only configure the vlan trunk groups
matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    only_local_vlan_trunk_groups: <bool>
    ```

## Pod Name

POD Name, only used in Fabric Documentation (Optional), fallback to dc_name and then to fabric_name.
Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    pod_name: <str>
    ```

## Shutdown Interfaces Towards Undeployed Peers

- It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.

```yaml
# Use at the host level
is_deployed: < true or false or default -> true >
```

- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.
- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.
- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests. Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    shutdown_interfaces_towards_undeployed_peers: <bool>
    ```

## Trunk Groups

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | "mlag" is the Trunk Group used for MLAG VLAN (Typically VLAN 4094)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | MLAG |  |  |
    | [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | "mlag_l3" is the Trunk Group used for MLAG L3 peering VLAN (Typically VLAN 4093)<br>"mlag_l3" is also the Trunk Group used for VRF L3 peering VLANs<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | LEAF_PEER_L3 |  |  |
    | [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | "uplink" is the Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | UPLINK |  |  |

=== "YAML"

    ```yaml
    trunk_groups:
      mlag:
        name: <str>
      mlag_l3:
        name: <str>
      uplink:
        name: <str>
    ```
