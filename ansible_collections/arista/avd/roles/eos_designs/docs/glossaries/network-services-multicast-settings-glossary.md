# Glossary

## Table of Contents

- [L](#l)
- [N](#n)
- [S](#s)
- [V](#v)

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

## S

### svi_profiles

**Type**: List, items: Dictionary  
**Path**: `svi_profiles`  

Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
Keys are the same used under SVIs. Keys defined under SVIs take precedence.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config


---

## V

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `l2vlan_profiles.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `svi_profiles.[].nodes.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `svi_profiles.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---
