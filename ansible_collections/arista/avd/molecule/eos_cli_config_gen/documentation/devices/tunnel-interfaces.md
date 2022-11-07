# tunnel-interfaces
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
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
| Management1 | oob_management | oob | MGMT | - | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

## Tunnel Interfaces

### Tunnel Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Tunnel1 | test ipv4 only | Tunnel-VRF | 1500 | False |
| Tunnel2 | test ipv6 only | default | - | True |
| Tunnel3 | test dual stack | default | 1500 | - |
| Tunnel4 | test no tcp_mss | default | 1500 | - |

#### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | Source Interface | Destination | PMTU-Discovery | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ---------------- | ------------| -------------- | ------ | ------- |
| Tunnel1 | Tunnel-VRF | 42.42.42.42/24 | 666 | ingress | Ethernnet42 | 6.6.6.6 | True | test-in | test-out |
| Tunnel3 | default | 64.64.64.64/24 | 666 | - | Ethernnet42 | 1.1.1.1 | - | - | - |
| Tunnel4 | default | 64.64.64.64/24 | - | - | Ethernnet42 | 1.1.1.1 | - | - | - |

#### IPv6

| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | Source Interface | Destination | PMTU-Discovery | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ------- | ----------------- | ---------------- | ------------| -------------- | ----------- | ------------ |
| Tunnel2 | default | cafe::1/64 | 666 | egress | Ethernnet42 | dead:beef::1 | False | test-in | test-out |
| Tunnel3 | default | beef::64/64 | 666 | - | Ethernnet42 | 1.1.1.1 | - | - | - |
| Tunnel4 | default | beef::64/64 | - | - | Ethernnet42 | 1.1.1.1 | - | - | - |

### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel1
   description test ipv4 only
   no shutdown
   mtu 1500
   vrf Tunnel-VRF
   ip address 42.42.42.42/24
   ip access-group test-in in
   ip access-group test-out out
   tcp mss ceiling ipv4 666 ingress
   tunnel source interface Ethernnet42
   tunnel destination 6.6.6.6
   tunnel path-mtu-discovery
   comment
   Comment created from eos_cli under tunnel_interfaces.Tunnel1
   EOF

!
interface Tunnel2
   description test ipv6 only
   shutdown
   ipv6 enable
   ipv6 address cafe::1/64
   ipv6 access-group test-in in
   ipv6 access-group test-out out
   tcp mss ceiling ipv6 666 egress
   tunnel source interface Ethernnet42
   tunnel destination dead:beef::1
!
interface Tunnel3
   description test dual stack
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tcp mss ceiling ipv4 666 ipv6 666
   tunnel source interface Ethernnet42
   tunnel destination 1.1.1.1
!
interface Tunnel4
   description test no tcp_mss
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tunnel source interface Ethernnet42
   tunnel destination 1.1.1.1
```

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

# Multicast

# Filters

# ACL

# Quality Of Service
