# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)
- [Authentication](#authentication)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
- [Interfaces](#interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

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

## Authentication

### IP RADIUS Source Interfaces

#### IP RADIUS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback1 |
| default | Loopback10 |
| MGMT | Management1 |

#### IP SOURCE Source Interfaces Device Configuration

```eos
!
ip radius vrf default source-interface Loopback1
ip radius source-interface Loopback10
ip radius vrf MGMT source-interface Management1
```

## Interfaces

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
```
