# host2

## Table of Contents

- [Interfaces](#interfaces)
  - [VXLAN Interface](#vxlan-interface)

## Interfaces

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |
| Qos dscp propagation encapsulation | Disabled |
| Qos ECN propagation | Disabled |
| Qos map dscp to traffic-class decapsulation | Disabled |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   no vxlan qos ecn propagation
   no vxlan qos dscp propagation encapsulation
   no vxlan qos map dscp to traffic-class decapsulation
```
