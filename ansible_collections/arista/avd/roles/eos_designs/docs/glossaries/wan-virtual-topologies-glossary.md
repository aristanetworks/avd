# Glossary

## Table of Contents

- [P](#p)
- [W](#w)

## P

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.control_plane_virtual_topology.metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.policies.[].application_virtual_topologies.[].metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.policies.[].default_virtual_topology.metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

## W

### wan_virtual_topologies

**Type**: Dictionary  
**Path**: `wan_virtual_topologies`  

Configure Virtual Topologies for CV Pathfinder and AutoVPN.
Auto create a control plane profile/policy/application and enforce it being first in the default VRF.

---
