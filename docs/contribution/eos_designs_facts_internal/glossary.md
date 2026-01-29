# Glossary

## Table of Contents

- [C](#c)
- [D](#d)
- [E](#e)
- [I](#i)
- [L](#l)
- [M](#m)
- [P](#p)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)
- [W](#w)

## C

### connected_endpoints_keys

**Type**: List, items: Dictionary  
**Path**: `connected_endpoints_keys`  

List of connected_endpoints_keys in use on this device.
Used for fabric docs.

---

## D

### direction

**Type**: String  
**Path**: `uplinks.[].link_tracking_groups.[].direction`  
**Valid Values**: `upstream`, `downstream`  
---

### downlink_pools

**Type**: List, items: Dictionary  
**Path**: `downlink_pools`  

IPv4 pools used for links to downlink switches. Set this on the parent switch. Cannot be combined with `uplink_ipv4_pool` set on the downlink switch.

---

## E

### endpoint_trunk_groups

**Type**: List, items: String  
**Path**: `endpoint_trunk_groups`  

List of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches.

---

### endpoint_vlans

**Type**: String  
**Path**: `endpoint_vlans`  

Compressed list of vlans in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches.

---

### evpn_route_servers

**Type**: List, items: String  
**Path**: `evpn_route_servers`  

For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
For all other evpn roles there is no default.

---

## I

### inband_mgmt_interface

**Type**: String  
**Path**: `inband_mgmt_interface`  

Used for fabric docs.

---

### inband_mgmt_ip

**Type**: String  
**Path**: `inband_mgmt_ip`  

Used for fabric docs.

---

## L

### local_endpoint_trunk_groups

**Type**: List, items: String  
**Path**: `local_endpoint_trunk_groups`  

List of trunk_groups in use by endpoints connected to this switch.

---

## M

### max_parallel_uplinks

**Type**: Integer  
**Path**: `max_parallel_uplinks`  
**Default**: `1`  

Number of parallel links towards uplink switches.
Changing this value may change interface naming on uplinks (and corresponding downlinks).
Can be used to reserve interfaces for future parallel uplinks.


---

### mlag_switch_ids

**Type**: Dictionary  
**Path**: `mlag_switch_ids`  

The switch ids of both primary and secondary switches for a this node group.

---

### mlag_underlay_multicast

**Type**: Dictionary  
**Path**: `mlag_underlay_multicast`  

Should multicast be enabled on the mlag peer-l3-vlan.

---

### mpls_route_reflectors

**Type**: List, items: String  
**Path**: `mpls_route_reflectors`  

List of inventory hostname acting as MPLS route-reflectors.

---

## P

### peer_spanning_tree_portfast

**Type**: String  
**Path**: `uplinks.[].peer_spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### peer_speed

**Type**: String  
**Path**: `uplinks.[].peer_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### pod

**Type**: String  
**Path**: `pod`  

Used for fabric docs.

---

### port_profile_names

**Type**: List, items: Dictionary  
**Path**: `port_profile_names`  

List of port_profiles configured - including the ones not in use.
Used for fabric docs.

---

## S

### spanning_tree_portfast

**Type**: String  
**Path**: `uplinks.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### speed

**Type**: String  
**Path**: `uplinks.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

## T

### type

**Type**: String  
**Path**: `uplinks.[].type`  
**Valid Values**: `underlay_p2p`, `underlay_l2`  
---

## U

### uplinks

**Type**: List, items: Dictionary  
**Path**: `uplinks`  

List of uplinks with all parameters
These facts are leveraged by templates for this device when rendering uplinks
and by templates for peer devices when rendering downlinks

---

## V

### vlans

**Type**: String  
**Path**: `vlans`  

Compressed list of vlans to be defined on this switch after filtering network services.
The filter is based on filter.tenants, filter.tags but not filter.only_vlans_in_use.

Ex. "1-100, 201-202"

This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
This is to ensure that native vlan is not necessarily permitted on the uplink trunk.

---

## W

### wan_path_groups

**Type**: List, items: Dictionary  
**Path**: `wan_path_groups`  

List of path-groups used for the WAN configuration.

---
