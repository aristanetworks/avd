# Glossary

## Table of Contents

- [C](#c)
- [I](#i)
- [M](#m)
- [R](#r)
- [S](#s)

## C

### channel_id_algorithm

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

### channel_id_algorithm

**Type**: String  
**Path**: `l3_edge.p2p_links.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

## I

### isis_authentication_mode

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_circuit_type

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_circuit_type

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_network_type

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

### isis_network_type

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

## M

### mode

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `l3_edge.p2p_links.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

## R

### routing_protocol

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

### routing_protocol

**Type**: String  
**Path**: `l3_edge.p2p_links.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

## S

### speed

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `l3_edge.p2p_links.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---
