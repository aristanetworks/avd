# interface-groups
# Table of Contents

- [Maintenance Mode](#maintenance-mode)
  - [Interface Groups](#interface-groups)

# Maintenance Mode

## Interface Groups

### Interface Groups Summary

| Interface Group | Interfaces | Interface maintenance profile | BGP maintenance profiles |
| --------------- | ---------- | ----------------------------- | ------------------------ |
| QSFP_Interface_Group | Ethernet1,5 | uplink-interfaces | Default |
| SFP_Interface_Group | Ethernet10-20<br>Ethernet30-48 | Default | Default |

### Interface Groups Configuration

```eos
!
group interface QSFP_Interface_Group
   interface Ethernet1,5
   maintenance profile interface uplink-interfaces
!
group interface SFP_Interface_Group
   interface Ethernet10-20
   interface Ethernet30-48
```
