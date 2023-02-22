# address-locking
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Address Locking](#address-locking)
  - [Address Locking Summary](#address-locking-summary)
  - [DHCP Servers](#dhcp-servers)
  - [Leases](#leases)
  - [Address Locking Configuration](#address-locking-configuration)

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
| Management1 | oob_management | oob | MGMT | - | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Address Locking

## Address Locking Summary

| Settings | Value |
| -------- | ----- |
| Disable IP locking on configured ports | True |
| Local Interface | Loopback0 |
| Disable deauthorizing locked addresses upon MAC aging out | True |
| Disable enforcement for locked ipv4 addresses | True |
| Disable enforcement for locked ipv6 addresses | True |

## DHCP Servers

| Server IP |
| --------- |
| 1.1.1.1 |
| 4.4.4.4 |

## Leases

| Lease IP Address | Lease MAC Address |
| ---------------- | ----------------- |
| 2.2.2.2 | dead.beef.cafe |
| 3.3.3.3 | de:af:be:ef:ca:fe |


## Address Locking Configuration

```eos
!
address locking
   disabled
   local-interface Loopback0
   dhcp server ipv4 1.1.1.1
   dhcp server ipv4 4.4.4.4
   lease 2.2.2.2 mac dead.beef.cafe
   lease 3.3.3.3 mac de:af:be:ef:ca:fe
   locked-address expiration mac disabled
   locked-address ipv4 enforcement disabled
   locked-address ipv6 enforcement disabled
```
