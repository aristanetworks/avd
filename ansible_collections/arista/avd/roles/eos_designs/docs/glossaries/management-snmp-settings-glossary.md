# Glossary

## Table of Contents

- [A](#a)
- [C](#c)
- [P](#p)
- [S](#s)
- [V](#v)

## A

### access

**Type**: String  
**Path**: `snmp_settings.communities.[].access`  
**Valid Values**: `ro`, `rw`  
---

### auth

**Type**: String  
**Path**: `snmp_settings.users.[].auth`  
**Valid Values**: `md5`, `sha`, `sha256`, `sha384`, `sha512`  
---

### authentication

**Type**: String  
**Path**: `snmp_settings.groups.[].authentication`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### authentication_level

**Type**: String  
**Path**: `snmp_settings.hosts.[].users.[].authentication_level`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

## C

### compute_local_engineid_source

**Type**: String  
**Path**: `snmp_settings.compute_local_engineid_source`  
**Default**: `rfc3411_type5`  
**Valid Values**: `rfc3411_type5`, `rfc3411_type3`, `system_mac`, `hostname_and_ip`  

`compute_local_engineid_source` supports:
- `rfc3411_type5` use the value of `local_engineid_ip` to find the mgmt ip and calculate an RFC3411 compliant Engine ID based on 8000757105 + sha1(hostname + local_engineid_ip)
- `rfc3411_type3` generate an RFC3411 type 3 compliant Engine ID.
  To use this, `system_mac_address` MUST be set for the device.
  The formula is 8000757103 + system_mac_address.
- `system_mac` generate the Engine ID similar to the default EOS behavior.
  To use this, `system_mac_address` MUST be set for the device.
  The formula is f5717f + system_mac_address + 00.
- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1 the string generated via the concatenation of the hostname plus the out-of-band management IP.
    sha1(hostname + mgmt_ip)
  `local_engineid_ip` does not have any effect when using `compute_local_engineid_source: hostname_and_ip`.
  Note that this is a legacy method kept for backward compatibility; it does not follow RFC 3411 and does not properly support in-band management.

---

## P

### priv

**Type**: String  
**Path**: `snmp_settings.users.[].priv`  
**Valid Values**: `des`, `aes`, `aes192`, `aes256`  
---

## S

### snmp_settings

**Type**: Dictionary  
**Path**: `snmp_settings`  

SNMP settings.
Configuration of remote SNMP engine IDs are currently only possible using `structured_config`.

---

## V

### version

**Type**: String  
**Path**: `snmp_settings.users.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_settings.hosts.[].version`  
**Valid Values**: `1`, `2c`, `3`  
---

### version

**Type**: String  
**Path**: `snmp_settings.groups.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---
