# Glossary

## Table of Contents

- [A](#a)
- [H](#h)
- [N](#n)
- [S](#s)

## A

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  

Configure OSPF authentication for all interfaces under the VRF.
Can be overridden at the interface level under `l3_interfaces`, `l3_port_channels` or `svis`.

---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `svi_profiles.[].nodes.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `svi_profiles.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

## H

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `svi_profiles.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `svi_profiles.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
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
