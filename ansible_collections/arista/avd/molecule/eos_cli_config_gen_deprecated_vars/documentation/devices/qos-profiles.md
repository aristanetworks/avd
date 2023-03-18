# qos-profiles
# Table of Contents

- [Quality Of Service](#quality-of-service)
  - [QOS Profiles](#qos-profiles)

# Quality Of Service

## QOS Profiles

### QOS Profiles Summary


QOS Profile: **test**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | 46 | dscp | 80 percent | - |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate |
| -------- | ---- | --------- | -------- | ---------- |
| 1 | All | 50 | no priority | - |
| 2 | Unicast | 50 | no priority | - |
| 3 | Multicast | 50 | no priority | - |

### QOS Profile Device Configuration

```eos
!
qos profile test
   qos trust dscp
   qos dscp 46
   shape rate 80 percent
   !
   tx-queue 1
      bandwidth percent 50
      no priority
   !
   uc-tx-queue 2
      bandwidth percent 50
      no priority
   !
   mc-tx-queue 3
      bandwidth percent 50
      no priority
```
