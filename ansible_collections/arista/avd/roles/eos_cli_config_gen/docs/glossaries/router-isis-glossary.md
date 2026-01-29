# Glossary

## Table of Contents

- [A](#a)
- [I](#i)
- [K](#k)
- [L](#l)
- [M](#m)
- [O](#o)
- [S](#s)

## A

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

## I

### interval_unit

**Type**: String  
**Path**: `router_isis.spf_interval.interval_unit`  
**Valid Values**: `seconds`, `milliseconds`  

If interval unit is not defined EOS takes `seconds` by default.

---

### IS Type

**Type**: String  
**Path**: `router_isis.is_type`  
**Valid Values**: `level-1`, `level-1-2`, `level-2`  
---

## K

### key_type

**Type**: String  
**Path**: `router_isis.authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

## L

### level

**Type**: String  
**Path**: `router_isis.address_family_ipv4.fast_reroute_ti_lfa.level`  
**Valid Values**: `level-1`, `level-2`  
---

### level

**Type**: String  
**Path**: `router_isis.address_family_ipv6.fast_reroute_ti_lfa.level`  
**Valid Values**: `level-1`, `level-2`  

Optional, default is to protect all levels.

---

## M

### mode

**Type**: String  
**Path**: `router_isis.authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.address_family_ipv4.fast_reroute_ti_lfa.mode`  
**Valid Values**: `link-protection`, `node-protection`  
---

### mode

**Type**: String  
**Path**: `router_isis.address_family_ipv6.fast_reroute_ti_lfa.mode`  
**Valid Values**: `link-protection`, `node-protection`  
---

## O

### ospf_route_type

**Type**: String  
**Path**: `router_isis.redistribute_routes.[].ospf_route_type`  
**Valid Values**: `external`, `internal`, `nssa-external`  

ospf_route_type is required with source_protocols 'ospf' and 'ospfv3'.

---

## S

### source_protocol

**Type**: String  
**Path**: `router_isis.redistribute_routes.[].source_protocol`  
**Valid Values**: `bgp`, `connected`, `isis`, `ospf`, `ospfv3`, `static`  
---
