# Glossary

## Table of Contents

- [C](#c)
- [D](#d)
- [T](#t)

## C

### cfm

**Type**: Dictionary  
**Path**: `cfm`  

Configure connectivity fault management (CFM).
CFM is a network protocol for monitoring and troubleshooting Ethernet networks.

---

## D

### direction

**Type**: String  
**Path**: `cfm.domains.[].associations.[].direction`  
**Valid Values**: `up`, `down`  

Local maintenance endpoint direction.

---

## T

### tx_interval

**Type**: String  
**Path**: `cfm.profiles.[].alarm_indication.tx_interval`  
**Valid Values**: `1 seconds`, `1 minutes`  

Transmission interval for AIS packets.

---

### tx_interval

**Type**: String  
**Path**: `cfm.profiles.[].continuity_check.tx_interval`  
**Valid Values**: `3.33 milliseconds`, `10 milliseconds`, `100 milliseconds`, `1 seconds`, `10 seconds`, `1 minutes`, `10 minutes`  

Set the transmission interval for continuity check messages (CCMs).

---
