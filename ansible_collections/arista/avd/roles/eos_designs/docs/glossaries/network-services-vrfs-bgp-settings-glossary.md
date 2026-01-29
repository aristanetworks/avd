# Glossary

## Table of Contents

- [A](#a)
- [H](#h)
- [N](#n)
- [P](#p)

## A

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

## H

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

## N

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

## P

### password_type

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---
