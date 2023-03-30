# l2-protocol-forwarding

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [L2 Protocol Forwarding](#l2-protocol-forwarding)
  - [Forwarding Profiles Summary](#forwarding-profiles-summary)
  - [L2 Protocol Forwarding Configuration](#l2-protocol-forwarding-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

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

## L2 Protocol Forwarding

### Forwarding Profiles Summary

| Profile | BFD Per-link RFC-7130 | E-LMI | ISIS | LACP | LLDP | MACSEC | Pause | STP |
| ------- | --------------------- | ----- | ---- | ---- | ---- | ------ | ----- | --- |
| TEST1 | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward | forward,tagged forward,untagged forward |
| TEST2 | tagged forward | forward | untagged forward | forward,untagged forward | tagged forward | tagged forward | untagged forward | tagged forward,untagged forward |

### L2 Protocol Forwarding Configuration

```eos
!
l2-protocol
   forwarding profile TEST1
      bfd per-link rfc-7130 forward
      bfd per-link rfc-7130 tagged forward
      bfd per-link rfc-7130 untagged forward
      e-lmi forward
      e-lmi tagged forward
      e-lmi untagged forward
      isis forward
      isis tagged forward
      isis untagged forward
      lacp forward
      lacp tagged forward
      lacp untagged forward
      lldp forward
      lldp tagged forward
      lldp untagged forward
      macsec forward
      macsec tagged forward
      macsec untagged forward
      pause forward
      pause tagged forward
      pause untagged forward
      stp forward
      stp tagged forward
      stp untagged forward
   forwarding profile TEST2
      bfd per-link rfc-7130 tagged forward
      e-lmi forward
      isis untagged forward
      lacp forward
      lacp untagged forward
      lldp tagged forward
      macsec tagged forward
      pause untagged forward
      stp tagged forward
      stp untagged forward
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 |  L2PF test | access | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2PF test
   switchport
   l2-protocol forwarding profile TEST1
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2PF test | switched | access | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2PF test
   switchport
   l2-protocol forwarding profile TEST2
```
