# radius-servers
# Table of Contents

- [Authentication](#authentication)
  - [RADIUS Server](#radius-server)

# Authentication

## RADIUS Server

### RADIUS Server Hosts

| VRF | RADIUS Servers | Timeout | Retransmit |
| --- | -------------- | ------- | ---------- |
| mgt | 10.10.10.157 | - | - |
| default | 10.10.10.158 | - | - |
| default | 10.10.10.249 | - | - |

### RADIUS Server Device Configuration

```eos
!
radius-server host 10.10.10.157 vrf mgt key 7 071B245F5A
radius-server host 10.10.10.249 key 7 071B245F5A
radius-server host 10.10.10.158 vrf default key 7 071B245F5A
```
