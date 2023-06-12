=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | `False` |  | Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.<br>Only supported in combination with MPLS overlay. |
    | [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  | On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology).<br>The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1.<br>Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.<br>The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.<br> |
    | [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | `3000` | Min: 1<br>Max: 4093 |  |
    | [<samp>overlay_cvx_servers</samp>](## "overlay_cvx_servers") | List, items: String |  |  |  | List of CVX vxlan overlay controllers.<br>Required if overlay_routing_protocol == CVX.<br>CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.<br> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "overlay_cvx_servers.[].&lt;str&gt;") | String |  |  |  | 'inventory_hostname' of CVX server |
    | [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | `False` |  | When using Head-End Replication, configure flood-lists per VNI.<br>By default HER will be configured with a common flood-list containing all VTEPs.<br>This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.<br>This will make `eos_designs` consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.<br> |
    | [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | `fabric` | Valid Values:<br>- fabric<br>- dc | When using Head-End Replication, set the scope of flood-lists to Fabric or DC.<br>By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.<br>This can be changed to all VTEPs in the DC (sharing the same "dc_name" value).<br>This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.<br> |
    | [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  | Customize the description on overlay interface Loopback0. |
    | [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | `False` |  | IPv6 Unnumbered for MLAG iBGP connections.<br>Requires "underlay_rfc5549: true".<br> |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  | Specify RD type.<br>Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.<br>By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.<br>Note:<br>RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  | `overlay_loopback_ip` |  | "vtep_loopback" or "bgp_as" or <IPv4 Address> or interger between <0-65535> or integer between <0-4294967295> or "overlay_loopback_ip".<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield_offset</samp>](## "overlay_rd_type.admin_subfield_offset") | String |  |  |  | Offset can only be used if admin_subfield is an interger between <0-4294967295> or "switch_id".<br>Total value of admin_subfield + admin_subfield_offset must be <= 4294967295. |
    | [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | `ebgp` | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ibgp<br>- cvx<br>- her<br>- none | - The following overlay routing protocols are supported:<br>  - eBGP: Configures fabric with eBGP, default for l3ls-evpn design.<br>  - iBGP: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.<br>  - CVX: Configures fabric to leverage CloudVision eXchange as the overlay controller.<br>  - HER: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.<br>  - none: No overlay configuration will be generated, default for l2ls design.<br> |
    | [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | `ipv4` | Valid Values:<br>- ipv4<br>- ipv6 | When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.<br>This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.<br> |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  | Specify RT type.<br>Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default.<br>By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.<br>Notes:<br>RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  | `mac_vrf_id` |  | "bgp_as" or interger between <0-65535> or integer between <0-4294967295>.<br> |
    | [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  |  | IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.<br>This is only needed for centralized routing designs.<br> |

=== "YAML"

    ```yaml
    bgp_mesh_pes: <bool>
    mlag_ibgp_peering_vrfs:
      base_vlan: <int>
    overlay_cvx_servers:
      - <str>
    overlay_her_flood_list_per_vni: <bool>
    overlay_her_flood_list_scope: <str>
    overlay_loopback_description: <str>
    overlay_mlag_rfc5549: <bool>
    overlay_rd_type:
      admin_subfield: <str>
      admin_subfield_offset: <str>
    overlay_routing_protocol: <str>
    overlay_routing_protocol_address_family: <str>
    overlay_rt_type:
      admin_subfield: <str>
    vtep_vvtep_ip: <str>
    ```
