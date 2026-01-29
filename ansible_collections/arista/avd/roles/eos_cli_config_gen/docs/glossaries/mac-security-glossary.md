# Glossary

## Table of Contents

- [A](#a)
- [C](#c)
- [M](#m)

## A

### action

**Type**: String  
**Path**: `mac_security.profiles.[].traffic_unprotected.action`  
**Valid Values**: `allow`, `drop`  

Allow/drop the transmit/receive of unprotected traffic.

---

## C

### cipher

**Type**: String  
**Path**: `mac_security.profiles.[].cipher`  
**Valid Values**: `aes128-gcm`, `aes128-gcm-xpn`, `aes256-gcm`, `aes256-gcm-xpn`  
---

## M

### MAC Security (MACsec)

**Type**: Dictionary  
**Path**: `mac_security`  
---

### mode

**Type**: String  
**Path**: `mac_security.profiles.[].l2_protocols.ethernet_flow_control.mode`  
**Valid Values**: `encrypt`, `bypass`  
---

### mode

**Type**: String  
**Path**: `mac_security.profiles.[].l2_protocols.lldp.mode`  
**Valid Values**: `bypass`, `bypass unauthorized`  
---
