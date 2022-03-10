# dhcp-relay
# Table of Contents

- [dhcp-relay](#dhcp-relay)
- [Table of Contents](#table-of-contents)
- [Management](#management)
  - [Management Interfaces](#management-interfaces)
    - [Management Interfaces Summary](#management-interfaces-summary)
      - [IPv4](#ipv4)
      - [IPv6](#ipv6)
    - [Management Interfaces Device Configuration](#management-interfaces-device-configuration)
- [Authentication](#authentication)
- [DHCP Relay](#dhcp-relay-1)
  - [DHCP Relay Summary](#dhcp-relay-summary)
  - [DHCP Relay Configuration](#dhcp-relay-configuration)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
    - [IP Routing Summary](#ip-routing-summary)
    - [IP Routing Device Configuration](#ip-routing-device-configuration)
  - [IPv6 Routing](#ipv6-routing)
    - [IPv6 Routing Summary](#ipv6-routing-summary)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [Quality Of Service](#quality-of-service)

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

# DHCP Relay

## DHCP Relay Summary

- DHCP Relay is disabled for tunnelled requests

| DHCP Relay Servers |
| ------------------ |
| dhcp-relay-server1 |
| dhcp-relay-server2 |

## DHCP Relay Configuration

```eos
!
dhcp relay
   server dhcp-relay-server1
   server dhcp-relay-server2
   tunnel requests disabled
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
| default | false |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

# Multicast

# Filters

# ACL

# Quality Of Service
