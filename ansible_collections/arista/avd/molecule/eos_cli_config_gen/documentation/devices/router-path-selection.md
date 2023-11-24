# router-path-selection

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Router Path-selection](#router-path-selection)

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

### Router Path-selection

#### Router Path-selection Summary

| Setting | Value |
| ------  | ----- |
| Dynamic peers source | STUN |

#### Path Groups

##### Path Group PG-1

| Setting | Value |
| ------  | ----- |
| Path Group ID | 666 |

###### Dynamic peers settings

| Setting | Value |
| ------  | ----- |
| IP Local | True |
| IPSec | True |

###### Static peers

| Router IP | Name | IPv4 address(es) |
| --------- | ---- | ---------------- |
| 172.16.1.42 | - | - |
| 172.16.2.42 | - | 192.168.2.42 |
| 172.16.42.42 | TEST-STATIC-PEER-WITH-NAME | 192.168.42.42<br>192.168.1.42 |

##### Path Group PG-2

| Setting | Value |
| ------  | ----- |
| Path Group ID | 42 |
| IPSec profile | IPSEC-P-1 |
| Flow assignment | LAN |

###### Local Interfaces

| Interface name | Public address | STUN server profile(s) |
| -------------- | -------------- | ---------------------- |
| Ethernet1/1 | - |  |
| Ethernet1/1/3 | - |  |
| Ethernet2 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| Ethernet2/4.666 | - |  |
| Ethernet3 | - | STUN-P-1 |
| Ethernet4.666 | - |  |

###### Local IPs

| IP address | Public address | STUN server profile(s) |
| ---------- | -------------- | ---------------------- |
| 192.168.1.100 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| 192.168.100.1 | - | STUN-P-1 |

###### Dynamic peers settings

| Setting | Value |
| ------  | ----- |
| IP Local | - |
| IPSec | False |

##### Path Group PG-3

| Setting | Value |
| ------  | ----- |
| Path Group ID | 888 |

##### Path Group PG-4

| Setting | Value |
| ------  | ----- |
| Path Group ID | - |

#### Load-balance policies

| Policy Name | Jitter (ms) | Latency (ms) | Loss Rate (%) | Path Groups (priority) | Lowest Hop Count |
| ----------- | ----------- | ------------ | ------------- | ---------------------- | ---------------- |
| LB-P-1 | - | - | 17 | PG-5 (1)<br>PG-2 (42)<br>PG-4 (42)<br>PG-3 (666) | True |
| LB-P-2 | 666 | 42 | 42.42 | PG-1 (1)<br>PG-3 (1) | False |

#### DPS policies

##### DPS policy DPS-P-1

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-1 |
| 42 | AP-3 | LB-P-1 |

##### DPS policy DPS-P-2

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-2 |

##### DPS policy DPS-P-3

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| 42 | AP-2 | - |
| 66 | AP-1 | LB-P-1 |

#### VRFs configuration

| VRF name | DPS policy |
| -------- | ---------- |
| VRF-1 | DPS-P-1 |
| VRF-2 | DPS-P-2 |
| VRF-3 | - |

#### Router Path-selection Device Configuration

```eos
!
router path-selection
   peer dynamic source stun
   !
   path-group PG-1 id 666
      !
      peer dynamic
         ip local
         ipsec
      !
      peer static router-ip 172.16.1.42
      !
      peer static router-ip 172.16.2.42
         ipv4 address 192.168.2.42
      !
      peer static router-ip 172.16.42.42
         name TEST-STATIC-PEER-WITH-NAME
         ipv4 address 192.168.42.42
         ipv4 address 192.168.1.42
   !
   path-group PG-2 id 42
      ipsec profile IPSEC-P-1
      flow assignment lan
      !
      local interface Ethernet1/1
      !
      local interface Ethernet1/1/3
      !
      local interface Ethernet2 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local interface Ethernet2/4.666
      !
      local interface Ethernet3
         stun server-profile STUN-P-1
      !
      local interface Ethernet4.666
      !
      local ip 192.168.1.100 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local ip 192.168.100.1
         stun server-profile STUN-P-1
      !
      peer dynamic
         ipsec disabled
   !
   path-group PG-3 id 888
   !
   path-group PG-4
   !
   load-balance policy LB-P-1
      hop count lowest
      loss-rate 17
      path-group PG-5
      path-group PG-2 priority 42
      path-group PG-4 priority 42
      path-group PG-3 priority 666
   !
   load-balance policy LB-P-2
      jitter 666
      latency 42
      loss-rate 42.42
      path-group PG-1 priority 1
      path-group PG-3
   !
   policy DPS-P-1
      default-match
         load-balance LB-P-1
      42 application-profile AP-3
         load-balance LB-P-1
   !
   policy DPS-P-2
      default-match
         load-balance LB-P-2
   !
   policy DPS-P-3
      42 application-profile AP-2
      66 application-profile AP-1
         load-balance LB-P-1
   !
   vrf VRF-1
      path-selection-policy DPS-P-1
   !
   vrf VRF-2
      path-selection-policy DPS-P-2
   !
   vrf VRF-3
```
