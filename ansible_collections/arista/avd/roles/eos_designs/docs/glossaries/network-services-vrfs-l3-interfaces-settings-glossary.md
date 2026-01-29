# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [H](#h)
- [N](#n)
- [R](#r)
- [T](#t)

## A

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

## D

### direction

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

## H

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

## N

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

## R

### role

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

## T

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---
