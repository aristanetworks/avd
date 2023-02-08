# router-multicast
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [Router Multicast](#router-multicast)

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

# Multicast

## Router Multicast

### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.
- Multipathing deterministically by selecting the same upstream router.
- Software forwarding by the Software Forwarding Engine (SFE)

### IP Router Multicast VRFs

| VRF Name | Multicast Routing |
| -------- | ----------------- |
| MCAST_VRF1 | enabled |
| MCAST_VRF2 | enabled |

### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
      multipath deterministic router-id
      software-forwarding sfe
   !
   vrf MCAST_VRF1
      ipv4
         routing
   !
   vrf MCAST_VRF2
      ipv4
         routing
```

