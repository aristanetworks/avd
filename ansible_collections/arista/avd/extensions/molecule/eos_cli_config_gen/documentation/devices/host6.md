# host6

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Monitor Layer 1 Logging](#monitor-layer-1-logging)
  - [Monitor Layer 1 Device Configuration](#monitor-layer-1-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BGP](#router-bgp)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- | --- | --------- | -------- | -------------------- | ------------ |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-1 | - | - | 1 |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-2 | - | - | 2c |

#### SNMP Device Configuration

```eos
!
snmp-server host 10.6.75.121 vrf MGMT version 1 SNMP-COMMUNITY-1
snmp-server host 10.6.75.121 vrf MGMT version 2c SNMP-COMMUNITY-2
```

## Monitor Layer 1 Logging

| Layer 1 Event | Logging |
| ------------- | ------- |
| MAC fault | True |

### Monitor Layer 1 Device Configuration

```eos
!
monitor layer1
   logging mac fault
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | Test portfast edge keyword | - | - | - | - | - |
| Ethernet2 | Test portfast network keyword | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description Test portfast edge keyword
   switchport
   spanning-tree portfast edge
!
interface Ethernet2
   description Test portfast network keyword
   switchport
   spanning-tree portfast network
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | Test portfast edge keyword | - | - | - | - | - | - | - | - |
| Port-Channel2 | Test portfast network keyword | - | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description Test portfast edge keyword
   switchport
   spanning-tree portfast edge
!
interface Port-Channel2
   description Test portfast network keyword
   switchport
   spanning-tree portfast network
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | False |
| TENANT_A | True |
| TENANT_B | True (ipv6 interfaces) |
| TENANT_C | - |

#### IP Routing Device Configuration

```eos
!
no ip routing vrf MGMT
ip routing vrf TENANT_A
ip routing ipv6 interfaces vrf TENANT_B
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| TENANT_A | false |
| TENANT_B | false |
| TENANT_C | true |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing vrf TENANT_C
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65006 | - |

| BGP Tuning |
| ---------- |
| bgp additional-paths send limit 6 |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |

#### Router BGP Path-Selection Address Family

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| TENANT_B | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65006
   bgp additional-paths send limit 6
   redistribute ospf include leaked route-map RM-BGP-OSPF
   !
   address-family ipv4
      bgp additional-paths send limit 4
   !
   address-family ipv4 labeled-unicast
      no bgp additional-paths send
   !
   address-family ipv6
      no bgp additional-paths send
      redistribute ospfv3 match external route-map RM-BGP-OSPFV3-EXTERNAL
   !
   address-family path-selection
      bgp additional-paths send limit 5
   !
   vrf TENANT_B
      !
      address-family ipv6
         bgp additional-paths install ecmp-primary
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | - |
| LDP Enabled | False |
| LDP Router ID | - |
| LDP Interface Disabled Default | - |
| LDP Transport-Address Interface | - |

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| TENANT_A | enabled |
| TENANT_B | enabled (ipv6 interface) |
| TENANT_C | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TENANT_A
!
vrf instance TENANT_B
!
vrf instance TENANT_C
```
