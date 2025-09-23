# host1

## Table of Contents

- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking)
- [Interfaces](#interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Filters](#filters)
  - [Community-lists](#community-lists)

## Monitoring

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 | Encapsulations |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------- |
| default | default | disabled | disabled | - |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | - | - | - | 5 |  | - |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T1 | T1-E1 | 42.42.42.42 | - | No local interface |
| T1 | T1-E2 | - | - | No local interface |
| T1 | T1-E3 | 10.10.10.10 | 777 | No local interface |
| T1 | T1-E4 | this.is.my.awesome.collector.dns.name | 888 | No local interface |
| T1 | T1-E5 | dead:beef::cafe | - | No local interface |

#### Flow Tracking Hardware

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | - | - | 5 |  |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T1 | T1-E1 | 42.42.42.42 | - | No local interface |
| T1 | T1-E2 | - | - | No local interface |
| T1 | T1-E3 | 10.10.10.10 | 777 | No local interface |
| T1 | T1-E4 | this.is.my.awesome.collector.dns.name | 888 | No local interface |
| T1 | T1-E5 | dead:beef::cafe | - | No local interface |

#### Flow Tracking Device Configuration

```eos
!
flow tracking hardware
   tracker T1
      exporter T1-E1
         collector 42.42.42.42
      !
      exporter T1-E2
      !
      exporter T1-E3
         collector 10.10.10.10 port 777
      !
      exporter T1-E4
         collector this.is.my.awesome.collector.dns.name port 888
      !
      exporter T1-E5
         collector dead:beef::cafe
!
flow tracking sampled
   tracker T1
      exporter T1-E1
         collector 42.42.42.42
      !
      exporter T1-E2
      !
      exporter T1-E3
         collector 10.10.10.10 port 777
      !
      exporter T1-E4
         collector this.is.my.awesome.collector.dns.name port 888
      !
      exporter T1-E5
         collector dead:beef::cafe
```

## Interfaces

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel2 | Test_mode_and_vlans | access | 100 | - | - | - | - | - | - |
| Port-Channel3 | Test_trunk_groups_and_native_vlan | trunk | 110 | 10 | group1, group2 | - | - | - | - |
| Port-Channel4 | Test_native_vlan_tag_and_phone | trunk phone | - | tag | - | - | - | - | - |
| Port-Channel5 | Test_vlan_translations | - | - | - | - | - | - | - | - |

##### Encapsulation Dot1q

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Port-Channel6 | Test_encapsulation_dot1q_vlan | - | 20 | - |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- | ------------ | ---------------------- | ---------------------- |
| Port-Channel7 | Test_encapsulation_vlan1 | - | dot1q | - | 10 | - | - | dot1q | - | 20 | - | - |
| Port-Channel8 | Test_encapsulation_vlan2 | - | dot1q | - | - | 10 | 12 | client | - | - | - | - |
| Port-Channel9 | Test_encapsulation_vlan3 | - | unmatched | - | - | - | - | - | - | - | - | - |
| Port-Channel10 | Test_encapsulation_vlan4 | 100 | dot1q | - | - | 10 | 12 | dot1q | - | - | 20 | 22 |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Port-Channel5 | 2,3,4 | True |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Port-Channel5 | in | 23 | 50 | - | - | - | - |
| Port-Channel5 | out | 25 | 49 | - | - | - | - |
| Port-Channel5 | both | 34 | 60 | - | - | - | - |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Port-Channel3 | ISIS_TEST | - | - | - | - | - | md5 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   description Test_mode_and_vlans
   switchport access vlan 100
   switchport
!
interface Port-Channel3
   description Test_trunk_groups_and_native_vlan
   switchport trunk native vlan 10
   switchport trunk allowed vlan 110
   switchport mode trunk
   switchport trunk group group1
   switchport trunk group group2
   switchport
   isis enable ISIS_TEST
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Port-Channel4
   description Test_native_vlan_tag_and_phone
   switchport trunk native vlan tag
   switchport phone vlan 20
   switchport phone trunk tagged
   switchport mode trunk phone
   switchport
!
interface Port-Channel5
   description Test_vlan_translations
   switchport
   switchport vlan translation in 23 50
   switchport vlan translation out 25 49
   switchport vlan translation 34 60
   switchport trunk private-vlan secondary
   switchport pvlan mapping 2,3,4
!
interface Port-Channel6
   description Test_encapsulation_dot1q_vlan
   encapsulation dot1q vlan 20
!
interface Port-Channel7
   description Test_encapsulation_vlan1
   !
   encapsulation vlan
      client dot1q 10 network dot1q 20
!
interface Port-Channel8
   description Test_encapsulation_vlan2
   !
   encapsulation vlan
      client dot1q outer 10 inner 12
!
interface Port-Channel9
   description Test_encapsulation_vlan3
   !
   encapsulation vlan
      client unmatched
!
interface Port-Channel10
   description Test_encapsulation_vlan4
   vlan id 100
   !
   encapsulation vlan
      client dot1q outer 10 inner 12 network dot1q outer 20 inner 22
```

## Filters

### Community-lists

#### Community-lists Summary

| Name | Action |
| -------- | ------ |
| TEST1 | permit 1000:1000 |
| TEST2 | permit 2000:3000 |

#### Community-lists Device Configuration

```eos
!
ip community-list TEST1 permit 1000:1000
ip community-list TEST2 permit 2000:3000
```
