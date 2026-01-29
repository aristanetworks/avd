# Glossary

## Table of Contents

- [L](#l)
- [N](#n)
- [T](#t)

## L

### l2vlan_profiles

**Type**: List, items: Dictionary  
**Path**: `l2vlan_profiles`  

Profiles to inherit common settings for l2vlans defined under the network_services key.

---

## N

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

## T

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].l2vlans.[].private_vlan.type`  
**Valid Values**: `community`, `isolated`  
---

### type

**Type**: String  
**Path**: `l2vlan_profiles.[].private_vlan.type`  
**Valid Values**: `community`, `isolated`  
---
