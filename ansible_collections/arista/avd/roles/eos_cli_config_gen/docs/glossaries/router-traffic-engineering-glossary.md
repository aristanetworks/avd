# Glossary

## Table of Contents

- [E](#e)
- [M](#m)

## E

### explicit_null

**Type**: String  
**Path**: `router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].explicit_null`  
**Valid Values**: `ipv4`, `ipv6`, `ipv4 ipv6`, `none`  
---

## M

### metric

**Type**: String  
**Path**: `router_traffic_engineering.flex_algos.[].metric`  
**Valid Values**: `0`, `1`, `2`, `igp-metric`, `min-delay`, `te-metric`  

Metric can be specified as an integer or named type, 0 = igp-metric, 1 = min-delay, 2 = te-metric. Device CLI will show the name regardless.

---
