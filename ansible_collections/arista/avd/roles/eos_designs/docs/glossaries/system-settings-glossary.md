# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [I](#i)
- [N](#n)
- [P](#p)
- [R](#r)
- [S](#s)

## A

### address_type

**Type**: String  
**Path**: `hardware_counters.features.[].address_type`  
**Valid Values**: `ipv4`, `ipv6`, `mac`  

Supported only for the following features:
- acl: [ipv4, ipv6, mac] if direction is 'out'
- multicast: [ipv4, ipv6]
- route: [ipv4, ipv6]
This validation IS NOT made by the schemas.


---

### allocation

**Type**: String  
**Path**: `internal_vlan_order.allocation`  
**Valid Values**: `ascending`, `descending`  
---

## D

### default_igmp_snooping_enabled

**Type**: Boolean  
**Path**: `default_igmp_snooping_enabled`  
**Default**: `True`  

When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.


---

### default_interface_mtu

**Type**: Integer  
**Path**: `default_interface_mtu`  

Default interface MTU configured on EOS under "interface defaults".
Can be overridden per platform under platform settings.


---

### direction

**Type**: String  
**Path**: `hardware_counters.features.[].direction`  
**Valid Values**: `in`, `out`, `cpu`  

Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
Some features DO NOT have any direction.
This validation IS NOT made by the schemas.


---

## I

### internal_vlan_order

**Type**: Dictionary  
**Path**: `internal_vlan_order`  
**Default**: `See documentation`  

Internal vlan allocation order and range.

---

## N

### name

**Type**: String  
**Path**: `hardware_counters.features.[].name`  
**Valid Values**: `acl`, `decap-group`, `directflow`, `ecn`, `flow-spec`, `gre tunnel interface`, `ip`, `mpls interface`, `mpls lfib`, `mpls tunnel`, `multicast`, `nexthop`, `pbr`, `pdp`, `policing interface`, `qos`, `qos dual-rate-policer`, `route`, `routed-port`, `segment-security`, `subinterface`, `tapagg`, `traffic-class`, `traffic-policy`, `traffic-policy vlan-interface`, `vlan`, `vlan-interface`, `vni decap`, `vni encap`, `vtep decap`, `vtep encap`  
---

## P

### protocol

**Type**: String  
**Path**: `redundancy.protocol`  
**Valid Values**: `sso`, `rpr`  
---

## R

### redundancy

**Type**: Dictionary  
**Path**: `redundancy`  

Redundancy for chassis platforms with dual supervisors | Optional.

---

## S

### serial_number

**Type**: String  
**Path**: `serial_number`  

Serial Number of the device.
Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.
"serial_number" can also be set directly under node type settings.
If both are set, the value under node type settings takes precedence.


---

### system_mac_address

**Type**: String  
**Path**: `system_mac_address`  

Set to the same MAC address as available in "show version" on the device.
"system_mac_address" can also be set under node type settings.
If both are set, the value under node type settings takes precedence.


---
