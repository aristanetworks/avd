# ip_telnet_client_source_interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Telnet Client Source Interfaces](#ip-telnet-client-source-interfaces)

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

### IP Telnet Client Source Interfaces

#### IP Telnet Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |

#### IP Telnet Client Source Interfaces Device Configuration

```eos
!
ip telnet client source-interface Loopback0 vrf default
ip telnet client source-interface Management0 vrf MGMT
ip telnet client source-interface Ethernet10
```
