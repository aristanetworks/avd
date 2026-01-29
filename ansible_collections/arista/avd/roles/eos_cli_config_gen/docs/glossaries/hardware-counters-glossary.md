# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [N](#n)

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

## D

### direction

**Type**: String  
**Path**: `hardware_counters.features.[].direction`  
**Valid Values**: `in`, `out`, `cpu`  

Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
Some features DO NOT have any direction.
This validation IS NOT made by the schemas.


---

## N

### name

**Type**: String  
**Path**: `hardware_counters.features.[].name`  
**Valid Values**: `acl`, `decap-group`, `directflow`, `ecn`, `flow-spec`, `gre tunnel interface`, `ip`, `mpls interface`, `mpls lfib`, `mpls tunnel`, `multicast`, `nexthop`, `pbr`, `pdp`, `policing interface`, `qos`, `qos dual-rate-policer`, `route`, `routed-port`, `segment-security`, `subinterface`, `tapagg`, `traffic-class`, `traffic-policy`, `traffic-policy vlan-interface`, `vlan`, `vlan-interface`, `vni decap`, `vni encap`, `vtep decap`, `vtep encap`  
---
