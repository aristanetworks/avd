# Glossary

## Table of Contents

- [B](#b)
- [O](#o)
- [R](#r)
- [V](#v)

## B

### bgp_mesh_pes

**Type**: Boolean  
**Path**: `bgp_mesh_pes`  
**Default**: `False`  

Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
Only supported in combination with MPLS overlay.


---

## O

### overlay_bgp_peer_description

**Type**: String  
**Path**: `overlay_bgp_peer_description`  
**Default**: `{peer}{peer_interface?<_}`  

Description or description template to be used on the overlay BGP peers.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the BGP peer.
  - `peer_interface`: The interface on the BGP peer if available.

The default description is built from the name and interface of the BGP peer.

---

### overlay_cvx_servers

**Type**: List, items: String  
**Path**: `overlay_cvx_servers`  

List of CVX vxlan overlay controllers.
Required if overlay_routing_protocol == CVX.
CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.


---

### overlay_her_flood_list_per_vni

**Type**: Boolean  
**Path**: `overlay_her_flood_list_per_vni`  
**Default**: `False`  

When using Head-End Replication, configure flood-lists per VNI.
By default HER will be configured with a common flood-list containing all VTEPs.
This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.
This will make Arista AVD consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.


---

### overlay_her_flood_list_scope

**Type**: String  
**Path**: `overlay_her_flood_list_scope`  
**Default**: `fabric`  
**Valid Values**: `fabric`, `dc`  

When using Head-End Replication, set the scope of flood-lists to Fabric or DC.
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.
This can be changed to all VTEPs in the DC (sharing the same "dc_name" value).
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.


---

### overlay_mlag_rfc5549

**Type**: Boolean  
**Path**: `overlay_mlag_rfc5549`  
**Default**: `False`  

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true".


---

### overlay_rd_type

**Type**: Dictionary  
**Path**: `overlay_rd_type`  

Configuration options for the Administrator subfield (first part of RD) and the Assigned Number subfield (second part of RD).

By default Route Distinguishers (RD) are set to:
- `<overlay_loopback>:<mac_vrf_id_base + vlan_id or mac_vrf_vni_base + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
- `<overlay_loopback>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
- `<overlay_loopback>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
- `<overlay_loopback>:<vrf_id>` for VRFs.

Note:
RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
When using loopback or 32-bit ASN/number the assigned number can only be a 16-bit number. This may be a problem with large VNIs.
For 16-bit ASN/number the assigned number can be a 32-bit number.


---

### overlay_routing_protocol

**Type**: String  
**Path**: `overlay_routing_protocol`  
**Valid Values**: `ebgp`, `ibgp`, `cvx`, `her`, `none`  

- The following overlay routing protocols are supported:
  - ebgp: Configures fabric with eBGP, default for l3ls-evpn design.
  - ibgp: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.
  - cvx: Configures fabric to leverage CloudVision eXchange as the overlay controller.
  - her: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.
  - none: No overlay configuration will be generated, default for l2ls design.

  If not set, the default_overlay_routing_protocol defined under the node_type_keys will be used (default is "ebgp").


---

### overlay_routing_protocol_address_family

**Type**: String  
**Path**: `overlay_routing_protocol_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.


---

### overlay_rt_type

**Type**: Dictionary  
**Path**: `overlay_rt_type`  

Configuration options for the Administrator subfield (first part of RT) and the Assigned Number subfield (second part of RT).

By default Route Targets (RT) are set to:
- `<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>:<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
- `<vlan_aware_bundle_number_base + vrf_id>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
- `<vlan_aware_bundle_number_base + id>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
- `<vrf_id>:<vrf_id>` for VRFs.

Notes:
RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
When using 32-bit ASN/number the VNI can only be a 16-bit number. Alternatively use vlan_id/vrf_id as assigned number.
For 16-bit ASN/number the assigned number can be a 32-bit number.


---

## R

### router_id_loopback_description

**Type**: String  
**Path**: `router_id_loopback_description`  
**Default**: `ROUTER_ID`  

Customize the description on Router ID interface Loopback0.

---

## V

### vlan_assigned_number_subfield

**Type**: String  
**Path**: `overlay_rd_type.vlan_assigned_number_subfield`  
**Default**: `mac_vrf_id`  
**Valid Values**: `mac_vrf_id`, `mac_vrf_vni`, `vlan_id`  

The method for deriving RD Assigned Number subfield for VLAN services (second part of RD):
- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
- 'vlan_id' will only use the 'vlan_id' and ignores all base values.

These methods can be overridden per VLAN if either 'rd_override', 'rt_override' or 'vni_override' is set (preferred in this order).


---

### vlan_assigned_number_subfield

**Type**: String  
**Path**: `overlay_rt_type.vlan_assigned_number_subfield`  
**Default**: `mac_vrf_id`  
**Valid Values**: `mac_vrf_id`, `mac_vrf_vni`, `vlan_id`  

The method for deriving RT Assigned Number subfield for VLAN services (second part of RT):
- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
- 'vlan_id' will only use the 'vlan_id' and ignores all base values.

These methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).


---

### vtep_loopback_description

**Type**: String  
**Path**: `vtep_loopback_description`  
**Default**: `VXLAN_TUNNEL_SOURCE`  

Customize the description on the VTEP interface, typically Loopback1.

---

### vtep_vvtep_ip

**Type**: String  
**Path**: `vtep_vvtep_ip`  

IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.
This is only needed for centralized routing designs.


---
