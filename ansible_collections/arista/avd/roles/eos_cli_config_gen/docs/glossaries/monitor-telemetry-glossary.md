# Glossary

## Table of Contents

- [P](#p)
- [R](#r)
- [T](#t)
- [V](#v)

## P

### password_type

**Type**: String  
**Path**: `monitor_telemetry_influx.destinations.[].password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### protocol

**Type**: String  
**Path**: `monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].protocol`  
**Valid Values**: `tcp`, `udp`  
---

## R

### rate

**Type**: Integer  
**Path**: `monitor_telemetry_postcard_policy.ingress.sample.rate`  
**Valid Values**: `16384`, `32768`, `65536`  

Sampling rate. `rate` is preferred when both `rate` and `tcp_udp_checksum` are defined.

---

## T

### type

**Type**: String  
**Path**: `monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].type`  
**Valid Values**: `ipv4`, `ipv6`  

IP address version.

---

## V

### version

**Type**: Integer  
**Path**: `monitor_telemetry_postcard_policy.ingress.collection.version`  
**Valid Values**: `1`, `2`  

Postcard version.

---
