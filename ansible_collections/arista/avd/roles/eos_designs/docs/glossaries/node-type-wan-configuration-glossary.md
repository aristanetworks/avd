# Glossary

## Table of Contents

- [C](#c)
- [D](#d)
- [N](#n)
- [W](#w)

## C

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `device_profiles.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `devices.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

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

## N

### Node Types

**Type**: Dictionary  
**Path**: `<node_type_keys.key>`  
---

## W

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `device_profiles.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `devices.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---
