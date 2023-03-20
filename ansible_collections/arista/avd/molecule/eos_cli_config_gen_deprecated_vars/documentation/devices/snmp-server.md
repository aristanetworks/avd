# snmp-server
# Table of Contents

- [Monitoring](#monitoring)
  - [SNMP](#snmp)

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

### SNMP Local Interfaces

| Local Interface | VRF |
| --------------- | --- |
| Management1 | MGMT |
| Loopback0 | default |
| Loopback12 | Tenant_A_APP_Zone |

### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| SNMP-COMMUNITY-1 | ro | onur | - | - |
| SNMP-COMMUNITY-2 | rw | SNMP-MGMT | SNMP-MGMT | VW-READ |
| SNMP-COMMUNITY-3 | ro | - | - | - |

### SNMP Device Configuration

```eos
!
snmp-server vrf MGMT local-interface Management1
snmp-server local-interface Loopback0
snmp-server vrf Tenant_A_APP_Zone local-interface Loopback12
snmp-server community SNMP-COMMUNITY-1 ro onur
snmp-server community SNMP-COMMUNITY-2 view VW-READ rw ipv6 SNMP-MGMT SNMP-MGMT
snmp-server community SNMP-COMMUNITY-3 ro
```
