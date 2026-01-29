# Glossary

## Table of Contents

- [D](#d)
- [E](#e)
- [M](#m)
- [O](#o)
- [P](#p)
- [S](#s)
- [U](#u)

## D

### default_underlay_p2p_ethernet_description

**Type**: String  
**Path**: `default_underlay_p2p_ethernet_description`  
**Default**: `P2P_{peer}_{peer_interface}{vrf?<_VRF_}`  

The default description or description template to be used on L3 point-to-point ethernet interfaces.
The interfaces using this are the routed uplinks and `p2p_links` defined under `l3_edge` or `core_interfaces`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `vrf`: The name of the VRF if set (Only applicable for `uplink_type: p2p-vrfs`).

By default the description is templated from the name and interface of the peer.

---

### default_underlay_p2p_port_channel_description

**Type**: String  
**Path**: `default_underlay_p2p_port_channel_description`  
**Default**: `P2P_{peer}_{peer_interface}`  

The default description or description template to be used on L3 point-to-point port-channel interfaces.
The port-channels using this are `p2p_links` defined under `l3_edge` or `core_interfaces`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `port_channel_id`: The local port-channel ID.
  - `peer_port_channel_id`: The ID of the port-channel on the peer.

By default the description is templated from the name and interface of the peer.

---

### default_vrf_diag_loopback_description

**Type**: String  
**Path**: `default_vrf_diag_loopback_description`  
**Default**: `DIAG_VRF_{vrf}`  

The default description or description template to be used on VRF diagnostic loopback interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `interface`: The Loopback interface name.
  - `vrf`: The VRF name.
  - `tenant`: The tenant name.

By default the description is templated from the VRF name.

---

## E

### enable_trunk_groups

**Type**: Boolean  
**Path**: `enable_trunk_groups`  
**Default**: `False`  

Enable Trunk Group support across eos_designs.
Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature.


---

## M

### mlag_bgp_peer_description

**Type**: String  
**Path**: `mlag_bgp_peer_description`  
**Default**: `{mlag_peer}_{peer_interface}`  

Description or description template to be used on the MLAG BGP peers including those in VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG L3 VLAN interface.
  - `peer_interface`: The MLAG L3 VLAN interface on the MLAG peer.
  - `vrf`: The name of the VRF. Not available for the underlay peering.

The default description is built from the name and interface of the MLAG peer and optionally the VRF.

---

### mlag_bgp_peer_group_description

**Type**: String  
**Path**: `mlag_bgp_peer_group_description`  
**Default**: `{mlag_peer}`  

Description or description template to be used on the MLAG BGP peer-group.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.

The default description is the name of the MLAG peers.

---

### mlag_member_description

**Type**: String  
**Path**: `mlag_member_description`  
**Default**: `MLAG_{mlag_peer}_{peer_interface}`  

Description or description template to be used on MLAG peer-link ethernet interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG port-channel interface.
  - `peer_interface`: The port-channel interface on the MLAG peer.
  - `mlag_port_channel_id`: The local MLAG port-channel ID.
  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.

By default the description is templated from the name and interface of the MLAG peer.

---

### mlag_on_orphan_port_channel_downlink

**Type**: Boolean  
**Path**: `mlag_on_orphan_port_channel_downlink`  
**Default**: `False`  

If `true` an MLAG ID will always be configured on a Port-Channel downlink even if the downlink is only on one node in the MLAG pair.
If `false` (default) an MLAG ID will only be configured on Port-Channel downlinks dual-homed to two MLAG switches.

---

### mlag_peer_l3_svi_description

**Type**: String  
**Path**: `mlag_peer_l3_svi_description`  
**Default**: `MLAG_L3`  

Description or description template to be used on MLAG L3 peering SVI (Interface Vlan4093 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG L3 peering SVI name.
  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.

---

### mlag_peer_l3_vlan_name

**Type**: String  
**Path**: `mlag_peer_l3_vlan_name`  
**Default**: `MLAG_L3`  

Name or name template to be used on MLAG L3 VLAN (VLAN 4093 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.

---

### mlag_peer_l3_vrf_svi_description

**Type**: String  
**Path**: `mlag_peer_l3_vrf_svi_description`  
**Default**: `MLAG_L3_VRF_{vrf}`  

Description or description template to be used on MLAG L3 peering SVI for VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG L3 VRF peering SVI name.
  - `vlan`: The MLAG L3 VRF peering VLAN ID.
  - `vrf`: The VRF name.

---

### mlag_peer_l3_vrf_vlan_name

**Type**: String  
**Path**: `mlag_peer_l3_vrf_vlan_name`  
**Default**: `MLAG_L3_VRF_{vrf}`  

Name or name template to be used on MLAG L3 peering VLAN for VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `vlan`: The MLAG L3 VRF peering VLAN ID.
  - `vrf`: The VRF name.

---

### mlag_peer_svi_description

**Type**: String  
**Path**: `mlag_peer_svi_description`  
**Default**: `MLAG`  

Description or description template to be used on MLAG peering SVI (Interface Vlan4094 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG peering SVI name.
  - `mlag_peer_vlan`: The MLAG peering VLAN ID.

---

### mlag_peer_vlan_name

**Type**: String  
**Path**: `mlag_peer_vlan_name`  
**Default**: `MLAG`  

Name or name template to be used on MLAG peering VLAN (VLAN 4094 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `mlag_peer_vlan`: The MLAG peering VLAN ID.

---

### mlag_port_channel_description

**Type**: String  
**Path**: `mlag_port_channel_description`  
**Default**: `MLAG_{mlag_peer}_{peer_interface}`  

Description or description template to be used on MLAG peer-link port-channel interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG port-channel interface.
  - `peer_interface`: The port-channel interface on the MLAG peer.
  - `mlag_port_channel_id`: The local MLAG port-channel ID.
  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.

By default the description is templated from the name and port-channel interface of the MLAG peer.

---

### mode

**Type**: String  
**Path**: `underlay_multicast_anycast_rp.mode`  
**Default**: `pim`  
**Valid Values**: `pim`, `msdp`  
---

## O

### only_local_vlan_trunk_groups

**Type**: Boolean  
**Path**: `only_local_vlan_trunk_groups`  
**Default**: `False`  

A vlan can have many trunk_groups assigned.
To avoid unneeded configuration changes on all leaf switches when a new trunk group is added,
this feature will only configure the vlan trunk groups matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true".


---

## P

### p2p_uplinks_mtu

**Type**: Integer  
**Path**: `p2p_uplinks_mtu`  
**Default**: `9214`  

Point to Point Links MTU.
Precedence: <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214

---

### p2p_uplinks_qos_profile

**Type**: String  
**Path**: `p2p_uplinks_qos_profile`  

QOS Profile assigned on all infrastructure links.

---

## S

### shutdown_bgp_towards_undeployed_peers

**Type**: Boolean  
**Path**: `shutdown_bgp_towards_undeployed_peers`  
**Default**: `True`  

Administratively shuts down BGP peerings towards devices marked with `is_deployed: false`.

---

### shutdown_interfaces_towards_undeployed_peers

**Type**: Boolean  
**Path**: `shutdown_interfaces_towards_undeployed_peers`  
**Default**: `True`  

Administratively shuts down interfaces on deployed devices that connect to a peer marked with `is_deployed: false`.

---

## U

### underlay_filter_peer_as

**Type**: Boolean  
**Path**: `underlay_filter_peer_as`  
**Default**: `False`  

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note that this setting cannot be used while there are EVPN services present in the default VRF.


---

### underlay_filter_redistribute_connected

**Type**: Boolean  
**Path**: `underlay_filter_redistribute_connected`  
**Default**: `True`  

Filter redistribution of connected into the underlay routing protocol.
Only applicable when overlay_routing_protocol != 'none' and underlay_routing_protocol == BGP.
Creates a route-map and prefix-list assigned to redistribute connected permitting only loopbacks and inband management subnets.


---

### underlay_ipv6

**Type**: Boolean  
**Path**: `underlay_ipv6`  
**Default**: `False`  

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the node type settings.


---

### underlay_ipv6_numbered

**Type**: Boolean  
**Path**: `underlay_ipv6_numbered`  
**Default**: `False`  

This feature allows pure IPv6 underlay routing protocol with numbered addresses.
Currently sets both underlay and overlay, including MLAG, to use IPv6 addresses.
Currently BGP peer-groups are named with IPv4 by default. This can be modified under `bgp_peer_groups`.
Requires:
  - "underlay_ipv6: true"
  - "loopback_ipv6_pool"
  - "underlay_routing_protocol: ebgp"
Some settings are not yet supported with IPv6 underlay:
  - underlay_multicast_pim_sm
  - underlay_multicast_rp_interfaces
  - underlay_rfc5549
  - wan_role
  - vtep_vvtep_ip
  - inband_ztp


---

### underlay_l2_ethernet_description

**Type**: String  
**Path**: `underlay_l2_ethernet_description`  
**Default**: `L2_{peer}_{peer_interface}`  

The description or description template to be used on L2 ethernet interfaces.
The interfaces using this are the member interfaces of port-channel uplinks.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.

By default the description is templated from the hostname and interface of the peer.

---

### underlay_l2_port_channel_description

**Type**: String  
**Path**: `underlay_l2_port_channel_description`  
**Default**: `L2_{peer_node_group_or_peer}_{peer_interface}`  

The description or description template to be used on L2 port-channel interfaces.
The interfaces using this are port-channel uplinks.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `port_channel_id`: The local port-channel ID.
  - `peer_port_channel_id`: The ID of the port-channel on the peer.
  - `peer_node_group`: The node group of the peer if the peer is an MLAG member or running EVPN A/A.
  - `peer_node_group_or_peer`: Helper alias of the peer_node_group or peer.
  - `peer_node_group_or_uppercase_peer`: Helper alias of the peer_node_group or peer hostname in uppercase.

By default the description is templated from the peer's node group (for MLAG or EVPN A/A) or hostname and port-channel interface of the peer.

---

### underlay_multicast_anycast_rp

**Type**: Dictionary  
**Path**: `underlay_multicast_anycast_rp`  

If multiple nodes are configured under 'underlay_multicast_rps.[].nodes' for the same RP address, they will be configured
with one of the following methods:
- Anycast RP using PIM (RFC4610).
- Anycast RP using MSDP (RFC4611).

NOTE: When using MSDP, all nodes across all MSDP enabled RPs will be added to a single MSDP mesh group named "ANYCAST-RP".


---

### underlay_multicast_pim_sm

**Type**: Boolean  
**Path**: `underlay_multicast_pim_sm`  
**Default**: `False`  

When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
  - P2P uplink interfaces if enabled on uplink peer
  - MLAG L3 peer interface if also enabled on MLAG peer
  - l3_edge and core interfaces

Note: This changes the default behavior for l3_edge / core_interfaces to automatically include the interfaces
in multicast, unless `include_in_underlay_protocol: false` or `multicast_pim_sm: false`.

---

### underlay_multicast_rps

**Type**: List, items: Dictionary  
**Path**: `underlay_multicast_rps`  

List of PIM Sparse-Mode Rendevouz Points configured for underlay multicast on all devices.
The device(s) listed under 'nodes', will be configured as the Rendevouz point router(s).
If multiple nodes are configured under 'nodes' for the same RP address, they will be configured
according to the 'underlay_multicast_anycast_rp.mode' setting.

Requires 'underlay_multicast_pim_sm: true'.


---

### underlay_multicast_static

**Type**: Boolean  
**Path**: `underlay_multicast_static`  
**Default**: `False`  

When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
  - P2P uplink interfaces if enabled on uplink peer
  - MLAG L3 peer interface if also enabled on MLAG peer
  - l3_edge and core interfaces

---

### underlay_rfc5549

**Type**: Boolean  
**Path**: `underlay_rfc5549`  
**Default**: `False`  

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
Requires "underlay_routing_protocol: ebgp".


---

### underlay_routing_protocol

**Type**: String  
**Path**: `underlay_routing_protocol`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - OSPF-LDP*.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - No underlay routing protocol (none)
- The variables should be applied to all devices in the fabric.
*Only supported with core_interfaces data model.


---

### uplink_ptp

**Type**: Dictionary  
**Path**: `uplink_ptp`  

Enable PTP on all infrastructure links.

---

### use_router_general_for_router_id

**Type**: Boolean  
**Path**: `use_router_general_for_router_id`  
**Default**: `False`  

Use `router general` to set router ID for all routing protocols and VRFs.

---
