# host1

## Table of Contents

- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking)
- [Interfaces](#interfaces)
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
