# virtual-source-nat

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Virtual Source NAT](#virtual-source-nat-1)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

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

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IPv4 Address | Source NAT IPv6 Address |
| -------------- | ----------------------- | ----------------------- |
| TEST_01 | 1.1.1.1 | - |
| TEST_02 | 1.1.1.2 | - |
| TEST_03 | - | 2001:db8:85a3::8a2e:370:7334 |
| TEST_04 | 1.1.1.3 | 2001:db8:85a3::8a2e:370:7335 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf TEST_01 address 1.1.1.1
ip address virtual source-nat vrf TEST_02 address 1.1.1.2
ipv6 address virtual source-nat vrf TEST_03 address 2001:db8:85a3::8a2e:370:7334
ip address virtual source-nat vrf TEST_04 address 1.1.1.3
ipv6 address virtual source-nat vrf TEST_04 address 2001:db8:85a3::8a2e:370:7335
```
