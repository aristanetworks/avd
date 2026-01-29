# Glossary

## Table of Contents

- [D](#d)
- [E](#e)
- [G](#g)
- [M](#m)
- [P](#p)
- [T](#t)

## D

### delimiter

**Type**: String  
**Path**: `dot1x.radius_av_pair_username_format.delimiter`  
**Valid Values**: `colon`, `hyphen`, `none`, `period`  

Delimiter to use in MAC address string.

---

## E

### eap_method

**Type**: String  
**Path**: `dot1x.supplicant.profiles.[].eap_method`  
**Valid Values**: `fast`, `tls`  

Extensible Authentication Protocol method:
  - EAP Flexible Authentication via Secure Tunneling.
  - EAP with Transport Layer Security.

---

### eap_response

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send.

---

## G

### Global 802.1x Authentication

**Type**: Dictionary  
**Path**: `dot1x`  
---

## M

### mac_string_case

**Type**: String  
**Path**: `dot1x.radius_av_pair_username_format.mac_string_case`  
**Valid Values**: `lowercase`, `uppercase`  

MAC address string in lowercase/uppercase.

---

## P

### passphrase_type

**Type**: String  
**Path**: `dot1x.supplicant.profiles.[].passphrase_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

## T

### time_duration_unit

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---
