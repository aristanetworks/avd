# Glossary

## Table of Contents

- [A](#a)
- [S](#s)
- [V](#v)

## A

### access

**Type**: String  
**Path**: `snmp_server.communities.[].access`  
**Valid Values**: `ro`, `rw`  
---

### authentication

**Type**: String  
**Path**: `snmp_server.groups.[].authentication`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### authentication_level

**Type**: String  
**Path**: `snmp_server.hosts.[].users.[].authentication_level`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

## S

### snmp_server

**Type**: Dictionary  
**Path**: `snmp_server`  

SNMP settings.

---

## V

### version

**Type**: String  
**Path**: `snmp_server.groups.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_server.users.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_server.hosts.[].version`  
**Valid Values**: `1`, `2c`, `3`  
---
