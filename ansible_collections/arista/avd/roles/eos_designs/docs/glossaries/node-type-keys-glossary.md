# Glossary

## Table of Contents

- [C](#c)
- [D](#d)
- [N](#n)
- [U](#u)

## C

### custom_node_type_keys

**Type**: List, items: Dictionary  
**Path**: `custom_node_type_keys`  

Define Custom Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout and functionality.
`custom_node_type_keys` should be defined in top level group_var for the fabric.
These values will be combined with the defaults; custom node type keys named the same as a
default node_type_key will replace the default.

---

## D

### default_evpn_encapsulation

**Type**: String  
**Path**: `custom_node_type_keys.[].default_evpn_encapsulation`  
**Default**: `vxlan`  
**Valid Values**: `mpls`, `vxlan`  

Set the default evpn encapsulation.


---

### default_evpn_encapsulation

**Type**: String  
**Path**: `node_type_keys.[].default_evpn_encapsulation`  
**Default**: `vxlan`  
**Valid Values**: `mpls`, `vxlan`  

Set the default evpn encapsulation.


---

### default_evpn_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_evpn_role`  
**Default**: `none`  
**Valid Values**: `none`, `client`, `server`  

Default evpn_role. Can be overridden in topology vars.

---

### default_evpn_role

**Type**: String  
**Path**: `node_type_keys.[].default_evpn_role`  
**Default**: `none`  
**Valid Values**: `none`, `client`, `server`  

Default evpn_role. Can be overridden in topology vars.

---

### default_flow_tracker_type

**Type**: String  
**Path**: `custom_node_type_keys.[].default_flow_tracker_type`  
**Default**: `sampled`  
**Valid Values**: `sampled`, `hardware`  

Set the default flow tracker type.

---

### default_flow_tracker_type

**Type**: String  
**Path**: `node_type_keys.[].default_flow_tracker_type`  
**Default**: `sampled`  
**Valid Values**: `sampled`, `hardware`  

Set the default flow tracker type.

---

### default_mpls_overlay_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### default_mpls_overlay_role

**Type**: String  
**Path**: `node_type_keys.[].default_mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### default_overlay_routing_protocol

**Type**: String  
**Path**: `custom_node_type_keys.[].default_overlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ibgp`, `her`, `cvx`, `none`  

Set the default overlay routing_protocol.
Can be overridden by setting "overlay_routing_protocol" host/group_vars.


---

### default_overlay_routing_protocol

**Type**: String  
**Path**: `node_type_keys.[].default_overlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ibgp`, `her`, `cvx`, `none`  

Set the default overlay routing_protocol.
Can be overridden by setting "overlay_routing_protocol" host/group_vars.


---

### default_underlay_routing_protocol

**Type**: String  
**Path**: `custom_node_type_keys.[].default_underlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

Set the default underlay routing_protocol.
Can be overridden by setting "underlay_routing_protocol" host/group_vars.


---

### default_underlay_routing_protocol

**Type**: String  
**Path**: `node_type_keys.[].default_underlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

Set the default underlay routing_protocol.
Can be overridden by setting "underlay_routing_protocol" host/group_vars.


---

### default_wan_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_wan_role`  
**Valid Values**: `client`, `server`  

Set the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.


---

### default_wan_role

**Type**: String  
**Path**: `node_type_keys.[].default_wan_role`  
**Valid Values**: `client`, `server`  

Set the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.


---

## N

### node_type_keys

**Type**: List, items: Dictionary  
**Path**: `node_type_keys`  
**Default**: `See documentation`  

Define Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout and functionality.
`node_type_keys` should be defined in top level group_var for the fabric.

The default values will be overridden if this key is defined.
If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.
If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,
custom entries will replace the equivalent default entry.

---

## U

### uplink_type

**Type**: String  
**Path**: `custom_node_type_keys.[].uplink_type`  
**Default**: `p2p`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

`uplink_type` must be `p2p`, `p2p-vrfs` or `lan` if `vtep` or `underlay_router` is true.

For `p2p-vrfs`, the uplinks are configured as L3 interfaces with a subinterface for each VRF
in `network_services` present on both the uplink and the downlink switch.
The subinterface ID is the `vrf_id`.
'underlay_router' and 'network_services.l3' must be set to true.
VRF `default` is always configured on the physical interface using the underlay routing protocol.
All subinterfaces use the same IP address as the physical interface.
Multicast is not supported.
Only BGP is supported for subinterfaces.

For `lan`, a single uplink interface is supported and will be configured as an L3 Interface with
subinterfaces for each SVI defined under the VRFs in `network_services` as long as the uplink switch also
has the VLAN permitted by tag/tenant filtering.

---

### uplink_type

**Type**: String  
**Path**: `node_type_keys.[].uplink_type`  
**Default**: `p2p`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

`uplink_type` must be `p2p`, `p2p-vrfs` or `lan` if `vtep` or `underlay_router` is true.

For `p2p-vrfs`, the uplinks are configured as L3 interfaces with a subinterface for each VRF
in `network_services` present on both the uplink and the downlink switch.
The subinterface ID is the `vrf_id`.
'underlay_router' and 'network_services.l3' must be set to true.
VRF `default` is always configured on the physical interface using the underlay routing protocol.
All subinterfaces use the same IP address as the physical interface.
Multicast is not supported.
Only BGP is supported for subinterfaces.

For `lan`, a single uplink interface is supported and will be configured as an L3 Interface with
subinterfaces for each SVI defined under the VRFs in `network_services` as long as the uplink switch also
has the VLAN permitted by tag/tenant filtering.

---
