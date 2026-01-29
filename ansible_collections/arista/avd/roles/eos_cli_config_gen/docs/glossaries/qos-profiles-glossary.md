# Glossary

## Table of Contents

- [A](#a)
- [P](#p)
- [T](#t)
- [U](#u)

## A

### action

**Type**: String  
**Path**: `qos_profiles.[].priority_flow_control.watchdog.action`  
**Valid Values**: `drop`, `notify-only`  

Override the default error-disable action to either drop
traffic on the stuck queue or notify-only
without making any actions on the stuck queue.


---

## P

### priority

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

### priority

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

### priority

**Type**: String  
**Path**: `qos_profiles.[].mc_tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

## T

### trust

**Type**: String  
**Path**: `qos_profiles.[].trust`  
**Valid Values**: `cos`, `dscp`, `disabled`  
---

## U

### units

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`, `microseconds`  

Units to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].random_detect.drop.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `microseconds`, `milliseconds`  

Units to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`  

Unit to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `microseconds`, `milliseconds`  

Units to be used for the threshold values.

---
