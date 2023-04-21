# ip-nat

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP NAT](#ip-nat)
  - [NAT Pools](#nat-pools)
  - [NAT Synchronization](#nat-synchronization)
  - [NAT Translation Settings](#nat-translation-settings)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## IP NAT

| Settings | Value |
| -------- | ----- |
| Kernel Buffer Size | 64 MB |

### NAT Pools

#### Pool: prefix_16

| Settings | Value |
| -------- | ----- |
| Pool Prefix Length | 16 |
| Pool Utilization Threshold | 1 % (action: log) |

##### Pool Ranges

| First IP Address  | Last IP Address | First Port | Last Port |
| ----------------- | --------------- | ---------- | --------- |
| 10.0.0.1 | 10.0.255.254 | n.a. | n.a. |
| 10.1.0.0 | 10.1.255.255 | 1024 | 65535 |

#### Pool: prefix_32

| Settings | Value |
| -------- | ----- |
| Pool Prefix Length | 32 |

##### Pool Ranges

| First IP Address  | Last IP Address | First Port | Last Port |
| ----------------- | --------------- | ---------- | --------- |
| 10.2.0.1 | 10.2.0.1 | n.a. | n.a. |

#### Pool: prefix_24

| Settings | Value |
| -------- | ----- |
| Pool Prefix Length | 24 |
| Pool Utilization Threshold | 100 % (action: log) |

##### Pool Ranges

| First IP Address  | Last IP Address | First Port | Last Port |
| ----------------- | --------------- | ---------- | --------- |
| 10.3.0.1 | 10.3.0.254 | n.a. | n.a. |
| 10.3.1.0 | 10.3.1.255 | 1024 | 65535 |

### NAT Synchronization

| Settings | Value |
| -------- | ----- |
| State | Disabled !
| Expiry Interval | 60 Seconds |
| Interface | Ethernet1 |
| Peer IP Address | 1.1.1.1 |
| Port Range | 1024 - 65535 |
| Port Range Split | Disabled |

### NAT Translation Settings

| Settings | Value |
| -------- | ----- |
| Address Selection | Any |
| Address Selection | Hash Source IP Field |
| Counters | Enabled |
| Global Connection Limit | max. 100000 Connections |
| per Host Connection Limit | max. 1000 Connections |
| IP Host 10.0.0.1 Connection Limit | max. 100 Connections |
| IP Host 10.0.0.2 Connection Limit | max. 200 Connections |
| Global Connection Limit Low Mark | 50 % |
| per Host Connection Limit Low Mark | 50 % |
| UDP Connection Timeout | 3600 Seconds |
| TCP Connection Timeout | 7200 Seconds |

### IP NAT Device Configuration

```eos
!
ip nat translation address selection any
ip nat translation address selection hash field source-ip
ip nat translation udp-timeout 3600
ip nat translation tcp-timeout 7200
ip nat translation max-entries 100000
ip nat translation low-mark 50
ip nat translation max-entries 1000 host
ip nat translation low-mark 50 host
ip nat translation max-entries 100 10.0.0.1
ip nat translation max-entries 200 10.0.0.2
ip nat kernel buffer size 64
ip nat pool prefix_16 prefix-length 16
   range 10.0.0.1 10.0.255.254
   range 10.1.0.0 10.1.255.255 1024 65535
   utilization threshold 1 action log
ip nat pool prefix_32 prefix-length 32
   range 10.2.0.1 10.2.0.1
ip nat pool prefix_24 prefix-length 24
   range 10.3.0.1 10.3.0.254
   range 10.3.1.0 10.3.1.255 1024 65535
   utilization threshold 100 action log
ip nat synchronization
   description test sync config
   expiry-interval 60
   shutdown
   peer-address 1.1.1.1
   local-interface Ethernet1
   port-range 1024 65535
   port-range split disabled
```
