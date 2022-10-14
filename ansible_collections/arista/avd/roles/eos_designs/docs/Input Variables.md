---
search:
  boost: 2
---

# Input Variables

## Overlay Her Flood List Per Vni

When using Head-End Replication, configure flood-lists per VNI. | Optional
By default HER will be configured with a common flood-list containing all VTEPs. This behavior can be changed
to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`. This will make `eos_designs` consider
configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    overlay_her_flood_list_per_vni: <bool>
    ```

## Overlay Her Flood List Scope

When using Head-End Replication, set the scope of flood-lists to Fabric or DC
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added
to the flood-lists. This can be changed to all VTEPs in the DC (part of the inventory group referenced
by "dc_name")
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | fabric | Valid Values:<br>- fabric<br>- dc |  |

=== "YAML"

    ```yaml
    overlay_her_flood_list_scope: <str>
    ```

## Overlay Loopback Description

Customizable overlay loopback description

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  |  |

=== "YAML"

    ```yaml
    overlay_loopback_description: <str>
    ```

## Overlay MLAG Rfc5549

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    overlay_mlag_rfc5549: <bool>
    ```

## Overlay Rd Type

Specify RD type
Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  |  |  | < "vtep_loopback" or "bgp_as" or < IPv4 Address > or <0-65535> or <0-4294967295>, default -> <overlay_loopback_ip> > |

=== "YAML"

    ```yaml
    overlay_rd_type:
      admin_subfield: <str>
    ```

## Overlay Routing Protocol Address Family

Enable overlay EVPN peering with IPv6 addresses | Optional
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | ipv4 | Valid Values:<br>- ipv4<br>- ipv6 |  |

=== "YAML"

    ```yaml
    overlay_routing_protocol_address_family: <str>
    ```

## Overlay Routing Protocol

- The following overlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - IBGP (only with OSPF or ISIS variants in underlay)

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ibgp<br>- BGP |  |

=== "YAML"

    ```yaml
    overlay_routing_protocol: <str>
    ```

## Overlay Rt Type

Specify RT type
Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default
By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  |  |  | < "bgp_as" or <0-65535> or <0-4294967295>, default -> <mac_vrf_id> > |

=== "YAML"

    ```yaml
    overlay_rt_type:
      admin_subfield: <str>
    ```

## Vtep Vvtep IP

IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1
This is only needed for centralized routing designs

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  | Format: ipv4_cidr |  |

=== "YAML"

    ```yaml
    vtep_vvtep_ip: <str>
    ```
