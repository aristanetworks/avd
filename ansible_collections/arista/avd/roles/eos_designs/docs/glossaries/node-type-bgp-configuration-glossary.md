# Glossary

## Table of Contents

- [D](#d)
- [E](#e)
- [N](#n)

## D

### device_profiles

**Type**: List, items: Dictionary  
**Path**: `device_profiles`  

PREVIEW - This datamodel is still under development and may change or get removed at any time.

---

### devices

**Type**: List, items: Dictionary  
**Path**: `devices`  

PREVIEW - This datamodel is still under development and may change or get removed at any time.

---

## E

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `device_profiles.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `devices.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

## N

### Node Types

**Type**: Dictionary  
**Path**: `<node_type_keys.key>`  
---
