# dhcp-server

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [DHCP Server](#dhcp-server)
  - [DHCP Servers Summary](#dhcp-servers-summary)
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

| DHCP Server Enabled | VRF |
| ------------------- | --- |
| True | - |
| True | TEST |

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
      name TEST1
      dns server 10.1.1.12 10.1.1.13
      lease time 0 days 0 hours 10 minutes
      default-gateway 10.0.0.1
   !
   vendor-option ipv4 NTP
      sub-option 1 type string data "doge"
      sub-option 42 type ipv4-address data 10.1.1.1
```
