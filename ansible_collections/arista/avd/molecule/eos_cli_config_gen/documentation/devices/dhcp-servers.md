# dhcp-servers

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [DHCP Server](#dhcp-server)
  - [DHCP Servers Summary](#dhcp-servers-summary)
  - [DHCP Server Subnets](#dhcp-server-subnets)
  - [DHCP Server IPv4 Vendor Options](#dhcp-server-ipv4-vendor-options)
  - [DHCP Server Configuration](#dhcp-server-configuration)

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

## DHCP Server

### DHCP Servers Summary

| DHCP Server Enabled | VRF | IPv4 DNS Domain | IPv6 DNS Domain |
| ------------------- | --- | --------------- | --------------- |
| True | - | - | - |
| True | TEST | testv4.com | testv6.com |

### DHCP Server Subnets

| Subnet | VRF |
| ------ | --- |
| 2a00:2::/64 | - |
| 10.0.0.0/24 | TEST |
| 10.2.3.0/24 | - |

### DHCP Server IPv4 Vendor Options

| Vendor ID | Sub-option Number | Sub-option Type | Sub-option Data |
| --------- | ----------------- | --------------- | --------------- |
| NTP | 1 | string | test |
| NTP | 42 | ipv4-address | 10.1.1.1 |

### DHCP Server Configuration

```eos
!
dhcp server
   !
   subnet 2a00:2::/64
   !
   subnet 10.2.3.0/24
!
dhcp server vrf TEST
   dns domain name ipv4 testv4.com
   dns domain name ipv6 testv6.com
   !
   subnet 10.0.0.0/24
      !
      range 10.0.0.10 10.0.0.100
      !
      range 10.0.0.110 10.0.0.120
      name TEST1
      dns server 10.1.1.12 10.1.1.13
      lease time 0 days 0 hours 10 minutes
      default-gateway 10.0.0.1
   !
   vendor-option ipv4 NTP
      sub-option 1 type string data "test"
      sub-option 42 type ipv4-address data 10.1.1.1
```
