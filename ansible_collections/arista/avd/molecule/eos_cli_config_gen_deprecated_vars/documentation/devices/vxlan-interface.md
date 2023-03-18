# vxlan-interface
# Table of Contents

- [Interfaces](#interfaces)
  - [VXLAN Interface](#vxlan-interface)

# Interfaces

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | 10111 | 10.1.1.10<br/>10.1.1.11 | - |
| 112 | - | - | 239.9.1.6 |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_OP_Zone | 10 | 232.0.0.10 |
| Tenant_A_WEB_Zone | 11 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vlan 110 multicast group 239.9.1.4
   vxlan vlan 112 multicast group 239.9.1.6
   vxlan vrf Tenant_A_OP_Zone multicast group 232.0.0.10
```
