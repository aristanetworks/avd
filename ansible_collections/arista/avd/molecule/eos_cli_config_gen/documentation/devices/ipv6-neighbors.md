# ipv6-neighbors

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IPv6 Neighbors](#ipv6-neighbors-1)
  - [IPv6 Static Neighbors](#ipv6-static-neighbors)

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

## IPv6 Neighbors

IPv6 neighbor cache is enabled.
Refresh delay to restore the IPv6 neighbor cache after reboot: 1000 seconds

### IPv6 Static Neighbors

#### IPv6 Static Neighbors Summary

| VRF | IPv6 address | Exit interface | Hardware Address |
| --- | ------------ | -------------- | ---------------- |
| MGMT | 11:22:33:44:55:66:77:88 | Ethernet1 | 11.22.33 |
| - | ::ffff:192.1.56.10 | Loopback99 | aaaf.1234.bcbf |

#### IPv6 Neighbor Configuration

```eos
!
ipv6 neighbor cache persistent
ipv6 neighbor persistent refresh-delay 1000
ipv6 neighbor vrf MGMT 11:22:33:44:55:66:77:88 Ethernet1 11.22.33
ipv6 neighbor ::ffff:192.1.56.10 Loopback99 aaaf.1234.bcbf
```
