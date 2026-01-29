# Glossary

## Table of Contents

- [D](#d)
- [L](#l)
- [M](#m)
- [P](#p)
- [R](#r)
- [T](#t)

## D

### dscp

**Type**: String  
**Path**: `mpls.tunnel.termination.model.dscp`  
**Valid Values**: `pipe`, `uniform`  

The DSCP model `uniform` is supported only on specific hardware platforms.

---

### dscp

**Type**: String  
**Path**: `mpls.tunnel.termination.php_model.dscp`  
**Valid Values**: `pipe`, `uniform`  

The DSCP model `uniform` is supported only on specific hardware platforms.

---

## L

### label_local_termination

**Type**: String  
**Path**: `mpls.rsvp.label_local_termination`  
**Valid Values**: `implicit-null`, `explicit-null`  

Local termination label to be advertised.

---

## M

### method

**Type**: String  
**Path**: `mpls.rsvp.refresh.method`  
**Valid Values**: `bundled`, `explicit`  

Neighbor refresh mechanism.
bundled: Refresh states using message identifier lists.
explicit: Send each message individually.

---

### mode

**Type**: String  
**Path**: `mpls.rsvp.fast_reroute.mode`  
**Valid Values**: `link-protection`, `node-protection`, `none`  

Fast reroute mode.
link-protection: Protect against failure of the next link.
node-protection: Protect against failure of the next node.
none: Disable fast reroute.

---

## P

### password_type

**Type**: String  
**Path**: `mpls.rsvp.authentication.password_indexes.[].password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  

Authentication password type.

---

### preemption

**Type**: String  
**Path**: `mpls.rsvp.preemption_method.preemption`  
**Valid Values**: `hard`, `soft`  
---

## R

### reversion

**Type**: String  
**Path**: `mpls.rsvp.fast_reroute.reversion`  
**Valid Values**: `global`, `local`  

Reversion behavior.
Global revertive repair.
Local revertive repair.

---

## T

### ttl

**Type**: String  
**Path**: `mpls.tunnel.termination.model.ttl`  
**Valid Values**: `pipe`, `uniform`  
---

### ttl

**Type**: String  
**Path**: `mpls.tunnel.termination.php_model.ttl`  
**Valid Values**: `pipe`, `uniform`  
---

### type

**Type**: String  
**Path**: `mpls.rsvp.authentication.type`  
**Valid Values**: `md5`, `none`  

Authentication mechanism.

---

### type

**Type**: String  
**Path**: `mpls.rsvp.neighbors.[].authentication.type`  
**Valid Values**: `md5`, `none`  

Authentication mechanism.

---
