# Glossary

## Table of Contents

- [H](#h)
- [K](#k)
- [N](#n)
- [T](#t)

## H

### hash_algorithm

**Type**: String  
**Path**: `ntp_settings.authentication_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`  
---

## K

### key_type

**Type**: String  
**Path**: `ntp_settings.authentication_keys.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Key type of the `key`.
Does not have any influence on `cleartext_key`.

---

## N

### ntp_settings

**Type**: Dictionary  
**Path**: `ntp_settings`  

NTP settings

---

## T

### timezone

**Type**: String  
**Path**: `timezone`  

Clock timezone like "CET" or "US/Pacific".

---
