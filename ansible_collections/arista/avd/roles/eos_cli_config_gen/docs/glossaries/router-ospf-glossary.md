# Glossary

## Table of Contents

- [M](#m)
- [R](#r)
- [T](#t)

## M

### metric_type

**Type**: Integer  
**Path**: `router_ospf.process_ids.[].default_information_originate.metric_type`  
**Valid Values**: `1`, `2`  

OSPF metric type for default route.

---

### metric_type

**Type**: Integer  
**Path**: `router_ospf.process_ids.[].areas.[].default_information_originate.metric_type`  
**Valid Values**: `1`, `2`  

OSPF metric type for default route.

---

## R

### Router OSPF Configuration

**Type**: Dictionary  
**Path**: `router_ospf`  
---

## T

### type

**Type**: String  
**Path**: `router_ospf.process_ids.[].areas.[].type`  
**Default**: `normal`  
**Valid Values**: `normal`, `stub`, `nssa`  
---
