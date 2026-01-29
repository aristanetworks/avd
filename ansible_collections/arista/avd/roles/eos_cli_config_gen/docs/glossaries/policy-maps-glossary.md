# Glossary

## Table of Contents

- [H](#h)
- [R](#r)
- [T](#t)

## H

### higher_rate_burst_size_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.higher_rate_burst_size_unit`  
**Default**: `bytes`  
**Valid Values**: `bytes`, `kbytes`, `mbytes`, `packets`  
---

### higher_rate_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.higher_rate_unit`  
**Default**: `bps`  
**Valid Values**: `bps`, `kbps`, `mbps`, `pps`  
---

## R

### rate_burst_size_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.rate_burst_size_unit`  
**Default**: `bytes`  
**Valid Values**: `bytes`, `kbytes`, `mbytes`, `packets`  
---

### rate_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.rate_unit`  
**Default**: `bps`  
**Valid Values**: `bps`, `kbps`, `mbps`, `pps`  
---

### rate_unit

**Type**: String  
**Path**: `policy_maps.copp_system_policy.classes.[].rate_unit`  
**Valid Values**: `pps`, `kbps`  

The `rate_unit` must be defined for `shape` and `bandwidth`.

---

## T

### type

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.action.type`  
**Valid Values**: `dscp`, `drop-precedence`  

Set action for policed traffic.

---
