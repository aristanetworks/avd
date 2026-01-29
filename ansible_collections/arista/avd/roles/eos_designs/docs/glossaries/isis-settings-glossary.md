# Glossary

## Table of Contents

- [I](#i)
- [P](#p)
- [U](#u)

## I

### ISIS Default IS System-ID format

**Type**: String  
**Path**: `isis_system_id_format`  
**Default**: `underlay_loopback`  
**Valid Values**: `node_id`, `underlay_loopback`  

Configures source for the system-id within the ISIS net id.
If this key is set to `node_id`, the fields `id` and `isis_system_id_prefix` configured under the node attributes are used to generate the system-id.
If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id.

---

### ISIS Default IS Type

**Type**: String  
**Path**: `isis_default_is_type`  
**Default**: `level-2`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  
---

### isis_default_circuit_type

**Type**: String  
**Path**: `isis_default_circuit_type`  
**Default**: `level-2`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.


---

### isis_default_metric

**Type**: Integer  
**Path**: `isis_default_metric`  
**Default**: `50`  

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.


---

### isis_maximum_paths

**Type**: Integer  
**Path**: `isis_maximum_paths`  
**Default**: `4`  

Number of path to configure in ECMP for ISIS.

---

## P

### protection

**Type**: String  
**Path**: `isis_ti_lfa.protection`  
**Valid Values**: `link`, `node`  
---

## U

### underlay_isis_authentication_cleartext_key

**Type**: String  
**Path**: `underlay_isis_authentication_cleartext_key`  

Cleartext password.
Encrypted to Type 7 by AVD.
To protect the password at rest it is strongly recommended to make use of a vault or similar.

---

### underlay_isis_authentication_key

**Type**: String  
**Path**: `underlay_isis_authentication_key`  

Type-7 encrypted password.
Takes precedence over `underlay_isis_authentication_cleartext_key`.
To protect the password at rest it is strongly recommended to make use of a vault or similar.

---

### underlay_isis_authentication_mode

**Type**: String  
**Path**: `underlay_isis_authentication_mode`  
**Valid Values**: `md5`, `text`  

Underlay ISIS authentication mode.

---

### underlay_isis_bfd

**Type**: Boolean  
**Path**: `underlay_isis_bfd`  
**Default**: `False`  

Enable BFD for ISIS on all underlay links.

---

### underlay_isis_instance_name

**Type**: String  
**Path**: `underlay_isis_instance_name`  

Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls.

---
