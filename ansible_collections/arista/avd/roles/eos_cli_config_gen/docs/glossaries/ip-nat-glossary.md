# Glossary

## Table of Contents

- [D](#d)
- [N](#n)
- [P](#p)
- [T](#t)

## D

### direction

**Type**: String  
**Path**: `ip_nat.profiles.[].destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `ip_nat.profiles.[].source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

## N

### nat_type

**Type**: String  
**Path**: `ip_nat.profiles.[].source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

## P

### protocol

**Type**: String  
**Path**: `ip_nat.profiles.[].destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `ip_nat.profiles.[].source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `ip_nat.translation.timeouts.[].protocol`  
**Valid Values**: `tcp`, `udp`  
---

## T

### type

**Type**: String  
**Path**: `ip_nat.pools.[].type`  
**Default**: `ip-port`  
**Valid Values**: `ip-port`, `port-only`  
---
