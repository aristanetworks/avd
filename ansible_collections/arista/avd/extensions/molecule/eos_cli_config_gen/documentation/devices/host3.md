# host3

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

### NTP

#### NTP Summary

##### NTP Servers

| Server | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Source Address | Key |
| ------ | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | -------------- | --- |
| 2.2.2.55 | - | - | - | - | - | - | - | - | - |

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
| PROD | True | - | - |
| default | False | - | - |

#### Other SSH Settings

| Idle Timeout | Connection Limit | Max from a single Host | Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
| ------------ | ---------------- | ---------------------- | ------- | -------------------- | -------------- | ------------------------- |
| default | - | - | default | default | default | default |

#### Management SSH Device Configuration

```eos
!
management ssh
   !
   vrf PROD
      no shutdown
   !
   vrf mgt
```

### Management Accounts

#### Password Policy

No specific password policy is set for management accounts.

#### Management Accounts Device Configuration

```eos
!
management accounts
```

## CVX

CVX is enabled

### CVX Services

| Service | Enabled | Settings |
| ------- | ------- | -------- |
| MCS | - | Redis Password Set |
| OpenStack | True | - |
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
   service openstack
      ip access-group ACL-OS
      ipv6 access-group ACL-V6-IN
      no shutdown
      network type-driver vlan default
   !
   service vxlan
      vtep mac-learning control-plane
```

## Authentication

### AAA Accounting

#### AAA Accounting Summary

| Type | Commands | Record type | Groups | Logging |
| ---- | -------- | ----------- | ------ | ------- |
| Exec - Console | - | start-stop | - | True |
| Commands - Console | all | none | - | - |
| Commands - Console | 0 | none | - | - |
| Commands - Console | 1 | start-stop | - | True |
| System - Default | - | start-stop | - | True |
| Commands - Default | all | none | - | - |
| Commands - Default | 0 | none | - | - |

#### AAA Accounting Device Configuration

```eos
aaa accounting exec console start-stop logging
aaa accounting commands all console none
aaa accounting commands 0 console none
aaa accounting commands 1 console start-stop logging
aaa accounting system default start-stop logging
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

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| default | - | 192.0.2.10 | 6343 |
| default | 192.0.2.3 | - | - |

sFlow is disabled.

#### SFlow Device Configuration

```eos
!
sflow destination 192.0.2.10
sflow source 192.0.2.3
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

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 702 | 10.255.0.3 | disabled | - | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Segment Routing

| Process ID | Adjacency Segment Allocation | Shutdown |
| ---------- | ---------------------------- | -------- |
| 702 | none | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 702
   router-id 10.255.0.3
   segment-routing mpls
      adjacency-segment allocation none
```

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
| 65003 | 192.0.2.3 |

| BGP Tuning |
| ---------- |
| bgp additional-paths send ecmp |

#### Router BGP Device Configuration

```eos
!
router bgp 65003
   router-id 192.0.2.3
   bgp additional-paths send ecmp
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

## Group-Based Multi-domain Segmentation Services (MSS-Group)

MSS-G is disabled.

### Router MSS-G Device Configuration

```eos
!
router segment-security
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

| Cause | Detection Enabled | Recovery Enabled | Recovery Interval (seconds) |
| ----- | ----------------- | ---------------- | --------------------------- |
| acl | - | False | - |
| arp-inspection | - | True | - |
| bpduguard | - | False | - |
| dot1x | - | False | 500 |
| dot1x-coa | - | False | - |
| dot1x-phone-classification | - | False | - |
| dot1x-session-replace | - | False | - |
| error-correction-encoding | - | False | - |
| fabric-capacity-low | - | False | - |
| hardware-speed-group | - | False | - |
| hitless-reload-down | - | True | - |
| interface-speed | - | False | - |
| internal-error | - | False | - |
| lacp-rate-limit | - | False | - |
| link-flap | - | False | - |
| no-internal-vlan | - | True | - |
| port-breakout | - | False | - |
| portchannelguard | - | False | 600 |
| portsec | - | False | - |
| speed-misconfigured | - | False | - |
| storm-control | - | False | - |
| stuck-queue | - | False | - |
| switchcard-unreachable | - | False | - |
| tap-port-init | - | False | - |
| tapagg | - | True | - |
| tpid | - | False | - |
| transceiver-adapter | - | False | - |
| uplink-failure-detection | - | False | - |
| xcvr-misconfigured | - | False | - |
| xcvr-overheat | - | False | - |
| xcvr-power-unsupported | - | False | - |
| xcvr-unsupported | - | False | - |

```eos
!
no errdisable recovery cause acl
errdisable recovery cause arp-inspection
no errdisable recovery cause bpduguard
no errdisable recovery cause dot1x
no errdisable recovery cause dot1x-coa
no errdisable recovery cause dot1x-phone-classification
no errdisable recovery cause dot1x-session-replace
no errdisable recovery cause error-correction-encoding
no errdisable recovery cause fabric-capacity-low
no errdisable recovery cause hardware-speed-group
errdisable recovery cause hitless-reload-down
no errdisable recovery cause interface-speed
no errdisable recovery cause internal-error
no errdisable recovery cause lacp-rate-limit
no errdisable recovery cause link-flap
errdisable recovery cause no-internal-vlan
no errdisable recovery cause port-breakout
no errdisable recovery cause portchannelguard
no errdisable recovery cause portsec
no errdisable recovery cause speed-misconfigured
no errdisable recovery cause storm-control
no errdisable recovery cause stuck-queue
no errdisable recovery cause switchcard-unreachable
no errdisable recovery cause tap-port-init
errdisable recovery cause tapagg
no errdisable recovery cause tpid
no errdisable recovery cause transceiver-adapter
no errdisable recovery cause uplink-failure-detection
no errdisable recovery cause xcvr-misconfigured
no errdisable recovery cause xcvr-overheat
no errdisable recovery cause xcvr-power-unsupported
no errdisable recovery cause xcvr-unsupported
errdisable recovery cause dot1x interval 500
errdisable recovery cause portchannelguard interval 600
errdisable recovery interval 300
```

### Traffic Policies information

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
```

### Priority Flow Control

#### Global Settings

##### Priority Flow Control Watchdog Settings

| Action | Timeout | Recovery | Polling | Override Action Drop |
| ------ | ------- | -------- | ------- |
| errdisable | - | - | - | True |

```eos
!
priority-flow-control pause watchdog override action drop
```

## STUN

### STUN Server

| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |
| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |
| Ethernet2 | - | - | - | 3478 |

### STUN Device Configuration

```eos
!
stun
   server
      local-interface Ethernet2
```

## Schedule

### Schedule Config

| Max Concurrent Jobs | Prepend Hostname Logfile |
| ------------------- | ------------------------ |
| 3 | - |

### Schedule Jobs Summary

| Name | Period | Command | Max Log Files | Timeout | Logging Verbose | Log Location | Max Total Size |
| ---- | ------ | ------- | ------------- | ------- | --------------- | ------------ | -------------- |
| at_interval_nodate | at 10:00:00 interval 60 minutes | show clock | 1 | - | - | - | - |

### Schedule Device Configuration

```eos
schedule config max-concurrent-jobs 3
schedule at_interval_nodate at 10:00:00 interval 60 max-log-files 1 command show clock
```
