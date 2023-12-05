# router-bgp-link-state

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

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

## Routing

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

#### Router BGP Peer Groups

##### PG-1

| Settings | Value |
| -------- | ----- |
| Remote AS | 65001 |

##### PG-2

| Settings | Value |
| -------- | ----- |
| Remote AS | 65001 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.255.1 | - | default | - | - | - | - | - | - | - | - |
| 192.168.255.2 | - | default | - | - | - | - | - | - | - | - |

#### Router BGP Link-State Address Family

##### Link-State Neighbors

| Neighbor | Activate | Missing policy In action | Missing policy Out action |
| -------- | -------- | ------------------------ | ------------------------- |
| 192.168.255.1 | True | deny | deny |
| 192.168.255.2 | True | - | - |

##### Link-State Peer Groups

| Peer Group | Activate | Missing policy In action | Missing policy Out action |
| ---------- | -------- | ------------------------ | ------------------------- |
| PG-1 | True | deny-in-out | permit |
| PG-2 | False | - | - |

##### Link-State Path Selection Configuration

| Settings | Value |
| -------- | ----- |
| Role(s) | producer<br>consumer<br>propagator |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   neighbor PG-1 peer group
   neighbor PG-1 remote-as 65001
   neighbor PG-2 peer group
   neighbor PG-2 remote-as 65001
   !
   address-family link-state
      bgp missing-policy direction in action permit
      bgp missing-policy direction out action deny
      neighbor PG-1 activate
      neighbor PG-1 missing-policy direction in action deny-in-out
      neighbor PG-1 missing-policy direction out action permit
      no neighbor PG-2 activate
      neighbor 192.168.255.1 activate
      neighbor 192.168.255.1 missing-policy direction in action deny
      neighbor 192.168.255.1 missing-policy direction out action deny
      neighbor 192.168.255.2 activate
      path-selection
      path-selection role consumer propagator
```
