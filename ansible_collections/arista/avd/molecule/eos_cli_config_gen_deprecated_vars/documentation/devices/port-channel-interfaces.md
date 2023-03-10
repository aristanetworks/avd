# port-channel-interfaces
# Table of Contents

- [Interfaces](#interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

# Interfaces

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | SRV01_bond0 | switched | trunk | 2-3000 | - | - | - | - | - | 0000:0000:0404:0404:0303 |

#### Flexible Encapsulation Interfaces

| Interface | Description | Type | Vlan ID | Client Unmatched | Client Dot1q VLAN | Client Dot1q Outer Tag | Client Dot1q Inner Tag | Network Retain Client Encapsulation | Network Dot1q VLAN | Network Dot1q Outer Tag | Network Dot1q Inner Tag |
| --------- | ----------- | ---- | ------- | -----------------| ----------------- | ---------------------- | ---------------------- | ----------------------------------- | ------------------ | ----------------------- | ----------------------- |
| Port-Channel2.1000 | L2 Subinterface | l2dot1q | 1000 | False | 100 | - | - | True | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description SRV01_bond0
   switchport
   switchport trunk allowed vlan 2-3000
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0404:0404:0303
      route-target import 04:04:03:03:02:02
   lacp system-id 0303.0202.0101
!
interface Port-Channel2
   description Flexencap Port-Channel
   no switchport
!
interface Port-Channel2.1000
   description L2 Subinterface
   vlan id 1000
   encapsulation vlan
      client dot1q 100 network client
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
```
