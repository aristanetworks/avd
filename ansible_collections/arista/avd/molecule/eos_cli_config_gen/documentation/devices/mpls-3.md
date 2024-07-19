# mpls-3

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | False |
| LDP Router ID | 192.168.1.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | - |
| ICMP Fragmentation-Needed Tunneling Enabled | - |
| ICMP TTL-Exceeded Tunneling Enabled | - |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   interface disabled default
   router-id 192.168.1.2
```
