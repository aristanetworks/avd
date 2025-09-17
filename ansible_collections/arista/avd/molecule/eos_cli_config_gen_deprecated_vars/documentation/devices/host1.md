# host1

## Table of Contents

- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking)
- [Interfaces](#interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Static Routes](#static-routes)
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [Router BGP](#router-bgp)
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

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | - | default | - | - |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  default  |  -  |  -  |  -  |  -  |  -  |

##### VRRP Details

| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IPs | IPv4 VRRP Version | IPv6 Virtual IPs | Peer Authentication Mode |
| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | ---------------- | ----------------- | ---------------- | ------------------------ |
| Vlan10 | 2 | - | - | Enabled | - | - |  | 2 | 2, 0, 0, 1, :, d, b, 8, :, :, 2 | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   vrrp 2 ipv6 2001:db8::2
```

## Routing

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| default | 1.1.2.0/24 | 10.1.1.1 | vlan1001 | 200 | 666 | RT-TO-FAKE-DMZ | - |

#### Static Routes Device Configuration

```eos
!
ip route 1.1.2.0/24 Vlan1001 10.1.1.1 200 tag 666 name RT-TO-FAKE-DMZ
```

### IPv6 Static Routes

#### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| TENANT_A_PROJECT01 | 2a01:cb04:4e6:a300::/64 | 2a01:cb04:4e6:100::1 | vlan1001 | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ipv6 route vrf TENANT_A_PROJECT01 2a01:cb04:4e6:a300::/64 Vlan1001 2a01:cb04:4e6:100::1
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| Tenant_A | - | ospf<br>ospfv3<br>ospfv3<br>connected | - |
| TENANT_A_PROJECT01 | - | connected<br>static<br>isis<br>bgp | - |
| TENANT_A_PROJECT02 | - | connected<br>isis | - |
| VRF03 | - | dynamic | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
   redistribute connected rcf Router_BGP_Connected()
   redistribute ospf include leaked
   redistribute ospf match internal
   redistribute ospf match external
   redistribute ospf match nssa-external 1 include leaked route-map RM-REDISTRIBUTE-OSPF-NSSA-1
   redistribute static rcf Router_BGP_Static()
   !
   address-family ipv4
      redistribute bgp leaked
      redistribute connected include leaked rcf Address_Family_IPV4_Connected()
      redistribute dynamic route-map Address_Family_IPV4_Dynamic_RM
      redistribute ospf match internal include leaked
      redistribute ospf match external include leaked route-map RM-REDISTRIBUTE-OSPF-EXTERNAL
      redistribute ospf match nssa-external
      redistribute static rcf Address_Family_IPV4_Static()
   !
   address-family ipv4 multicast
      redistribute attached-host
      redistribute connected
      redistribute isis include leaked rcf Router_BGP_Isis()
      redistribute ospf match external
      redistribute ospf match internal
      redistribute ospf match nssa-external 2
      redistribute ospfv3 match external
      redistribute static route-map VRF_AFIPV4MULTI_RM_STATIC
   !
   address-family ipv6
      redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
      redistribute connected rcf Address_Family_IPV6_Connected()
      redistribute ospfv3 match external include leaked
      redistribute ospfv3 match internal include leaked route-map RM-REDISTRIBUTE-OSPF-INTERNAL
      redistribute ospfv3 match nssa-external 1
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   !
   address-family ipv6 multicast
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal
      redistribute ospfv3 match external
      redistribute ospfv3 match nssa-external 2
   !
   vrf Tenant_A
      redistribute connected
      redistribute ospf match external include leaked
      redistribute ospfv3 match internal
      redistribute ospfv3 match nssa-external
   !
   vrf TENANT_A_PROJECT01
      redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
      redistribute connected
      redistribute isis route-map Router_BGP_Isis
      redistribute static rcf Router_BGP_Static()
      !
      address-family ipv4
         redistribute connected rcf VRF_AFIPV4_RCF_CONNECTED()
         redistribute ospf match external
         redistribute ospf match nssa-external 1
         redistribute ospfv3 match internal
         redistribute static route-map VRF_AFIPV4_RM_STATIC
   !
   vrf TENANT_A_PROJECT02
      redistribute connected
      redistribute isis
      !
      address-family ipv6
         redistribute connected rcf VRF_AFIPV6_RCF_CONNECTED()
         redistribute isis include leaked
         redistribute ospfv3 match external
         redistribute ospfv3 match internal include leaked
         redistribute ospfv3 match nssa-external
         redistribute static route-map VRF_AFIPV6_RM_STATIC
   !
   vrf VRF03
      redistribute dynamic rcf VRF_RCF_DYNAMIC()
      !
      address-family ipv4 multicast
         redistribute connected
         redistribute ospf match internal
         redistribute ospf match nssa-external 2
         redistribute ospfv3 match external
         redistribute static route-map VRF_AFIPV4MULTI_RM_STATIC
      !
      address-family ipv6 multicast
         redistribute connected
         redistribute ospf match external
         redistribute ospf match nssa-external
         redistribute ospfv3 match internal
         redistribute static route-map VRF_AFIPV6MULTI_RM_STATIC
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
