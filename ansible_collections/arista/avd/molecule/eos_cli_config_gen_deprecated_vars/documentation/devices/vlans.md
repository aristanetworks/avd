# vlans
# Table of Contents

- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | PR01-DMZ | - |
| 111 | PRIVATE_VLAN_COMMUNITY | - |

### Private VLANs

| Primary Vlan ID | Secondary VLAN ID | Private Vlan Type |
| --------------- | ----------------- | ----------------- |
| community | 111 | 110 |

## VLANs Device Configuration

```eos
!
vlan 110
   name PR01-DMZ
!
vlan 111
   name PRIVATE_VLAN_COMMUNITY
   private-vlan community primary vlan 110
```
