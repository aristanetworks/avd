# Glossary

## Table of Contents

- [E](#e)
- [Q](#q)

## E

### ecn

**Type**: String  
**Path**: `class_maps.qos.[].ecn`  
**Valid Values**: `ce`, `ect`, `ect-ce`, `non-ect`  

Match packets based on the ECN value.
Accepted values:
  - non-ect (matches 00).
  - ect (matches 01 an 10).
  - ce (matches 11).
  - ect-ce (matches 01, 10 and 11).

---

## Q

### QOS Class-maps

**Type**: Dictionary  
**Path**: `class_maps`  
---
