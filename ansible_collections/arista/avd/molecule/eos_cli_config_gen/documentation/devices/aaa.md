# aaa
# Table of Contents
<!-- toc -->

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [TACACS Servers](#tacacs-servers)
  - [RADIUS Servers](#radius-servers)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| ansible | 15 | network-admin |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username ansible privilege 15 role network-admin secret sha512 $6$.I7/ZR/zlLIUv8fr$vR/JvLTbq5amMt6Y1SE4CKlPDv/AzJYlFYHkUZ17BDovm0Oi4aLdBULe1EmZ0Y9xKjVLMKpxCSKmlrAioDxbQ0
username cvpadmin privilege 15 role network-admin secret sha512 $6$.I7/ZR/zlLIUv8fr$vR/JvLTbq5amMt6Y1SE4CKlPDv/AzJYlFYHkUZ17BDovm0Oi4aLdBULe1EmZ0Y9xKjVLMKpxCSKmlrAioDxbQ0
```

## TACACS Servers

### TACACS Servers

| VRF | TACACS Servers |
| --- | ---------------|
|  mgt | 10.10.10.157 |
|  default | 10.10.10.249 |
|  default | 10.10.10.158 |

### TACACS Servers Device Configuration

```eos
!
tacacs-server host 10.10.10.157 vrf mgt key 7 071B245F5A
tacacs-server host 10.10.10.158 key 7 071B245F5A
tacacs-server host 10.10.10.249 key 7 071B245F5A
```

## RADIUS Servers

### RADIUS Servers

| VRF | RADIUS Servers |
| --- | ---------------|
|  mgt | 10.10.10.157 |
|  default | 10.10.10.249 |
|  default | 10.10.10.158 |

### RADIUS Servers Device Configuration

```eos
!
radius-server host 10.10.10.157 vrf mgt key 7 071B245F5A
radius-server host 10.10.10.249 key 7 071B245F5A
radius-server host 10.10.10.158 vrf default key 7 071B245F5A
```

## AAA Server Groups

### AAA Server Groups Summary

| Server Group Name | Type  | VRF | IP address |
| ------------------| ----- | --- | ---------- |
| TACACS | tacacs+ |  mgt | 10.10.10.157 |
| TACACS | tacacs+ |  default | 10.10.10.249 |

### AAA Server Groups Device Configuration

```eos
!
aaa group server tacacs+ TACACS
   server 10.10.10.157 vrf mgt
   server 10.10.10.249
```

## AAA Authentication

### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | group TACACS local |
| Login | serial-console | local |

AAA Authentication on-failure log has been enabled

AAA Authentication on-success log has been enabled

Policy local allow-nopassword-remote-login has been enabled.

### AAA Authentication Device Configuration

```eos
!
aaa authentication login default group TACACS local
aaa authentication login serial-console local
aaa authentication enable default group TACACS local
aaa authentication dot1x default DOT1X default group
aaa authentication policy on-failure log
aaa authentication policy on-success log
aaa authentication policy local allow-nopassword-remote-login
!
```

## AAA Authorization

### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | group CUST local |

Authorization for configuration commands is enabled.

Authorization for serial console is enabled.

### AAA Authorization Device Configuration

```eos
!
aaa authorization exec default group CUST local
aaa authorization serial-console
aaa authorization commands all default group aaaAuth
!
```

## AAA Accounting

### AAA Accounting Summary

| Type | Sub-type | Record | Accounting Stores | Logging |
| ---- | -------- | ------ |------------------ | ------- |
| Exec | - | start-stop | TACACS | - |
| Commands | all | start-stop | TACACS  | True  |
| Commands | 0 | start-stop |  -  | True  |

### AAA Accounting Device Configuration

```eos
!
aaa accounting exec default start-stop group TACACS
aaa accounting commands all default start-stop group TACACS logging
aaa accounting commands 0 default start-stop logging
```

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false|
### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

*No device configuration required - default values

# Multicast

# Filters

# ACL
