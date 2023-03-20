# tunnel-interfaces
# Table of Contents

- [Interfaces](#interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)

# Interfaces

## Tunnel Interfaces

### Tunnel Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown | Source Interface | Destination | PMTU-Discovery |
| --------- | ----------- | --- | --- | -------- | ---------------- | ----------- | -------------- |
| Tunnel3 | test dual stack | default | 1500 | - | Ethernet42 | 1.1.1.1 | - |
| Tunnel4 | test no tcp_mss | default | 1500 | - | Ethernet42 | 1.1.1.1 | - |

#### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |
| Tunnel3 | default | 64.64.64.64/24 | - | - | - | - |
| Tunnel4 | default | 64.64.64.64/24 | - | - | - | - |

#### IPv6

| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ------- | ----------------- | ----------- | ------------ |
| Tunnel3 | default | beef::64/64 | - | - | - | - |
| Tunnel4 | default | beef::64/64 | - | - | - | - |

### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel3
   description test dual stack
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
!
interface Tunnel4
   description test no tcp_mss
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
```
