# Glossary

## Table of Contents

- [C](#c)
- [D](#d)
- [F](#f)
- [P](#p)

## C

### campus

**Type**: String  
**Path**: `campus`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus fabric.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

### campus_access_pod

**Type**: String  
**Path**: `campus_access_pod`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus access pod.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

### campus_pod

**Type**: String  
**Path**: `campus_pod`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus pod.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

## D

### dc_name

**Type**: String  
**Path**: `dc_name`  

DC Name is used in:
- Fabric Documentation (Optional, falls back to fabric_name)
- SNMP Location: `snmp_settings.location` (Optional)
- HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)


---

## F

### fabric_name

**Type**: String  
**Path**: `fabric_name`  

Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.

---

## P

### pod_name

**Type**: String  
**Path**: `pod_name`  

POD Name is used in:
- Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)
- SNMP Location: `snmp_settings.location` (Optional)
- VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)

Recommended to be common between Spines and Leafs within a POD (One l3ls topology).


---
