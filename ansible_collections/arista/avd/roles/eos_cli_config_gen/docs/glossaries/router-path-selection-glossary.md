# Glossary

## Table of Contents

- [D](#d)
- [F](#f)
- [P](#p)
- [R](#r)

## D

### direction

**Type**: String  
**Path**: `router_path_selection.tcp_mss_ceiling.direction`  
**Default**: `ingress`  
**Valid Values**: `ingress`  

Enforce on packets through DPS tunnel for a specific direction.
Only 'ingress' direction is supported.

---

## F

### flow_assignment

**Type**: String  
**Path**: `router_path_selection.path_groups.[].flow_assignment`  
**Valid Values**: `lan`  

Flow assignment `lan` can not be configured in a path group with dynamic peers.

---

## P

### peer_dynamic_source

**Type**: String  
**Path**: `router_path_selection.peer_dynamic_source`  
**Valid Values**: `stun`  

Source of dynamic peer discovery.

---

## R

### router_path_selection

**Type**: Dictionary  
**Path**: `router_path_selection`  

Dynamic path selection configuration.

---
