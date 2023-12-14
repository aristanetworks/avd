# flow-tracking

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking)
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

## Monitoring

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 |
| ----------- | ------------------- | ------------------------- | ------------------------- |
| 666 | 2 | enabled | disabled |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | 3666 | 5666 | True | 0 |  | - |
| T2 | - | - | False | 1 | Ethernet40 | 614400 |
| T3 | - | - | - | 4 | Ethernet41<br>Ethernet42<br>Port-Channel42 | 100000 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Hardware

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | 3666 | 5666 | 0 |  |
| T2 | - | - | 1 | Ethernet40 |
| T3 | - | - | 4 | Ethernet41<br>Port-Channel42 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Device Configuration

```eos
!
flow tracking sampled
   sample 666
   hardware offload ipv4
   hardware offload threshold minimum 2 samples
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
      record export mpls
   tracker T2
      exporter T2-E1
         collector 42.42.42.42
      flow table size 614400 entries
   tracker T3
      exporter T3-E1
      exporter T3-E2
         collector 10.10.10.10 port 777
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      exporter T3-E4
         collector dead:beef::cafe
      flow table size 100000 entries
   no shutdown
!
flow tracking hardware
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
   tracker T2
      exporter T2-E1
         collector 42.42.42.42
   tracker T3
      exporter T3-E1
      exporter T3-E2
         collector 10.10.10.10 port 777
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      exporter T3-E4
         collector dead:beef::cafe
   no shutdown
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet40 |  - | access | - | - | - | - |
| Ethernet41 |  - | access | - | - | - | - |
| Ethernet42 |  - | access | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet40
   switchport
   flow tracker hardware T2
   flow tracker sampled T2
!
interface Ethernet41
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
!
interface Ethernet42
   switchport
   flow tracker sampled T3
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel42 | - | switched | access | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel42
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
```
