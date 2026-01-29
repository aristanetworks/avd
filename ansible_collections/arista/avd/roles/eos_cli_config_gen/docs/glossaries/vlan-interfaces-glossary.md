# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [H](#h)
- [I](#i)
- [K](#k)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [V](#v)

## A

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

## D

### direction

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

## H

### hash_algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

## I

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `vlan_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

## K

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_message_digest_keys.[].key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].vrrp_ids.[].peer_authentication.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Authentication key type.

---

## M

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].vrrp_ids.[].peer_authentication.mode`  
**Valid Values**: `text`, `ietf-md5`  

Authentication mode.

---

## N

### nat_type

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

## O

### ospf_authentication

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication_key_type

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

## P

### protocol

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

## V

### version

**Type**: Integer  
**Path**: `vlan_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---
