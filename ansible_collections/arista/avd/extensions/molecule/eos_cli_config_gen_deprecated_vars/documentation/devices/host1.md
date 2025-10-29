# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)

## Management

### IP Name Server Groups

#### IP Name Server Groups Summary

##### mynameserver1

###### Name Server

| IP Address | VRF | Priority |
| ---------- | --- | -------- |
| 1.1.1.1 | default | 1 |
| 2.2.2.4 | vrf1 | 4 |
| 8.8.8.8 | vrf1 | - |

#### IP Name Server Groups Device Configuration

```eos
!
ip name-server group mynameserver1
   name-server vrf vrf1 8.8.8.8
   name-server vrf default 1.1.1.1 priority 1
   name-server vrf vrf1 2.2.2.4 priority 4
```
