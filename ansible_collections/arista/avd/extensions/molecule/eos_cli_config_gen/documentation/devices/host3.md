# host3

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA RX Accept | ND RA Disabled | Managed Config Flag |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | --------------- | -------------- | ------------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 2.2.2.55 | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp server 2.2.2.55
ntp serve all
ntp serve all vrf 1
ntp serve all vrf BLUE
ntp serve all vrf PINK
ntp serve all vrf RED
ntp serve all vrf default
ntp serve ip access-group test_ACL vrf 1 in
ntp serve ip access-group test_ACL vrf BLUE in
ntp serve ip access-group test_ACL vrf RED in
ntp serve ip access-group test_ACL in
ntp serve ipv6 access-group test_ACL_v6 vrf 1 in
ntp serve ipv6 access-group test_ACL_v6 vrf PINK in
ntp serve ipv6 access-group test_ACL_v6 vrf RED in
ntp serve ipv6 access-group test_ACL_v6 in
```

### PTP

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward V1 | Forward Unicast | Free Running Enabled |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | ---------- | --------------- | -------------------- |
| - | - | - | - | - | - | - | - | - | False |

#### PTP Device Configuration

```eos
!
no ptp free-running
```

### Management SSH

#### VRFs

| VRF | Enabled | IPv4 ACL | IPv6 ACL |
| --- | ------- | -------- | -------- |
| mgt | - | - | - |
| default | True | - | - |

#### Other SSH Settings

| Idle Timeout | Connection Limit | Max from a single Host | Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
| ------------ | ---------------- | ---------------------- | ------- | -------------------- | -------------- | ------------------------- |
| default | - | - | default | default | default | default |

#### Management SSH Device Configuration

```eos
!
management ssh
   !
   vrf mgt
```

## CVX

CVX is enabled

### CVX Services

| Service | Enabled | Settings |
| ------- | ------- | -------- |
| MCS | - | Redis Password Set |
| VXLAN | - | VTEP MAC learning: control-plane |

### CVX Device Configuration

```eos
!
cvx
   no shutdown
   !
   service mcs
      redis password 7 <removed>
   !
   service vxlan
      vtep mac-learning control-plane
```

## Authentication

### AAA Accounting

#### AAA Accounting Summary

| Type | Commands | Record type | Groups | Logging |
| ---- | -------- | ----------- | ------ | ------- |
| Commands - Console | all | none | - | - |
| Commands - Console | 0 | none | - | - |
| Commands - Default | all | none | - | - |
| Commands - Default | 0 | none | - | - |

#### AAA Accounting Device Configuration

```eos
aaa accounting commands all console none
aaa accounting commands 0 console none
aaa accounting commands all default none
aaa accounting commands 0 default none
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | apiserver.arista.io:443 | mgt | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=apiserver.arista.io:443 -cvauth=token-secure,/tmp/cv-onboarding-token -cvvrf=mgt -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| ---- | ----- |
| Synchronous | critical |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |
| RFC5424 | False |

| VRF | Source Interface |
| --- | ---------------- |
| - | Ethernet1 |
| check_source_interface_table_created | Ethernet1 |

| VRF | Hosts | Ports | Protocol | SSL-profile |
| --- | ----- | ----- | -------- | ----------- |
| check_source_interface_table_created | 1.2.3.4 | Default | UDP | - |
| check_source_interface_table_created | 2001:db8::1:2:3:4 | Default | UDP | - |

#### Logging Servers and Features Device Configuration

```eos
!
logging synchronous level critical
logging vrf check_source_interface_table_created host 1.2.3.4
logging vrf check_source_interface_table_created host 2001:db8::1:2:3:4
logging format timestamp traditional year timezone
logging local-interface Ethernet1
logging vrf check_source_interface_table_created source-interface Ethernet1
```

### MCS Client Summary

MCS client is shutdown

| Secondary CVX cluster | Server Hosts | Enabled |
| --------------------- | ------------ | ------- |
| default | - | - |

#### MCS Client Device Configuration

```eos
!
mcs client
   shutdown
   !
   cvx secondary default
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |
| 100-200 | 8192 |

#### MST Configuration

| Variable | Value |
| -------- | -------- |
| Name | test |
| Revision | 5 |
| Instance 2 | VLAN(s) 15,16,17,18 |
| Instance 3 | VLAN(s) 15 |
| Instance 4 | VLAN(s) 200-300 |

#### Global Spanning-Tree Settings

- MST PSVT Border is enabled.

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst pvst border
spanning-tree mst 0 priority 4096
spanning-tree mst 100-200 priority 8192
!
spanning-tree mst configuration
   name test
   revision 5
   instance 2 vlan 15,16,17,18
   instance 3 vlan 15
   instance 4 vlan 200-300
```

## Routing

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| SPF Interval | 250 seconds |
| SPF Interval Wait Time | 30 milliseconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   set-overload-bit on-startup 55
   spf-interval 250 30
   authentication mode shared-secret profile test1 algorithm md5 rx-disabled
   authentication key 0 password
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101.0001 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| maximum-paths 2 ecmp 2 |
| graceful-restart-helper long-lived |
| bgp additional-paths send limit 5 |

#### Router BGP EVPN Address Family

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |

#### Router BGP Path-Selection Address Family

#### Router BGP Device Configuration

```eos
!
router bgp 65101.0001
   router-id 192.168.255.3
   graceful-restart-helper long-lived
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   graceful-restart restart-time 300
   maximum-paths 2 ecmp 2
   bgp additional-paths send limit 5
   redistribute ospf include leaked route-map RM-OSPF-TO-BGP
   redistribute static
   !
   address-family evpn
      bgp additional-paths send ecmp limit 10
   !
   address-family ipv4
      bgp additional-paths send limit 10
   !
   address-family ipv4 labeled-unicast
      no bgp additional-paths send
   !
   address-family ipv4 multicast
      redistribute attached-host
      redistribute connected
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal
      redistribute ospfv3 match internal
      redistribute ospfv3 match external
      redistribute ospfv3 match nssa-external 2
      redistribute ospf match external
      redistribute ospf match nssa-external 2
   !
   address-family ipv6
      no bgp additional-paths send
      redistribute ospfv3 include leaked route-map RM-REDISTRIBUTE-OSPFV3
      redistribute ospfv3 match external include leaked route-map RM-REDISTRIBUTE-OSPFV3-EXTERNAL
   !
   address-family path-selection
      bgp additional-paths send limit 20
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | False |
| LDP Router ID | 192.168.1.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | - |

### MPLS RSVP

#### MPLS RSVP Summary

| Setting | Value |
| ------- | ----- |

### MPLS Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 192.168.1.2
   interface disabled default
!
mpls rsvp
```

## Multicast

### Router Multicast

#### IP Router Multicast Summary

- Multipathing operates via ECMP.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      multipath deterministic
```

## IPv6 DHCP Relay

### IPv6 DHCP Relay Summary

DhcpRelay Agent is in always-on mode.

Forwarding requests with additional IPv6 addresses in the "giaddr" field is allowed.

Add Option 79 - Link Layer Address Option.

Add RemoteID option 37 in format MAC address, hostname and interface name.

### IPv6 DHCP Relay Device Configuration

```eos
!
ipv6 dhcp relay always-on
ipv6 dhcp relay all-subnets default
ipv6 dhcp relay option link-layer address
ipv6 dhcp relay option remote-id format %m:%h:%p
```

## Errdisable

### Errdisable Summary

Errdisable recovery timer interval: 300 seconds

```eos
!
errdisable recovery interval 300
```

### Traffic Policies information

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
```
