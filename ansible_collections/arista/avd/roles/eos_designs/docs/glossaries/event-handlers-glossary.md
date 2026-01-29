# Glossary

## Table of Contents

- [A](#a)
- [E](#e)
- [O](#o)
- [S](#s)
- [T](#t)

## A

### action

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.action`  
**Valid Values**: `after`, `before`, `all`, `begin`, `end`  

Action for maintenance operation.

---

## E

### event_handlers

**Type**: List, items: Dictionary  
**Path**: `event_handlers`  

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.


---

## O

### operation

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.operation`  
**Valid Values**: `enter`, `exit`  
---

## S

### stage

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.stage`  
**Valid Values**: `bgp`, `linkdown`, `mlag`, `ratemon`  

Action is triggered after/before specified stage.

---

## T

### trigger

**Type**: String  
**Path**: `event_handlers.[].trigger`  
**Valid Values**: `on-boot`, `on-counters`, `on-intf`, `on-logging`, `on-maintenance`, `on-startup-config`, `vm-tracer vm`  

Configure event trigger condition.


---
