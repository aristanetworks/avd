# logging
# Table of Contents

- [Monitoring](#monitoring)
  - [Logging](#logging)

# Monitoring

## Logging

### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |

| VRF | Source Interface |
| --- | ---------------- |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |

### Logging Servers and Features Device Configuration

```eos
!
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf mgt source-interface Management0
logging policy match match-list molecule discard
```
