# host1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Server Groups](#ip-name-server-groups)
- [Authentication](#authentication)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | Test_ipv6_address | oob | default | 10.2.255.3/32 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA RX Accept | ND RA Disabled | ND Managed Config Flag |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | --------------- | -------------- | ---------------------- |
| Management1 | Test_ipv6_address | oob | default | 2002::CAFE/128 | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
```

### IP Name Server Groups

#### IP Name Server Groups Summary

##### mynameserver1

###### Name Server

| IP Address | VRF | Priority |
| ---------- | --- | -------- |
| 1.1.1.1 | default | 1 |
| 2.2.2.4 | vrf1 | 4 |
| 8.8.8.8 | vrf1 | - |

#### IP Name Server Groups Device Configuration

```eos
!
ip name-server group mynameserver1
   name-server vrf vrf1 8.8.8.8
   name-server vrf default 1.1.1.1 priority 1
   name-server vrf vrf1 2.2.2.4 priority 4
```

## Authentication

### IP TACACS Source Interfaces

#### IP TACACS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------------- |
| default | Loopback1 |
| TEST1 | Loopback3 |
| default | Loopback10 |

#### IP TACACS Source Interfaces Device Configuration

```eos
!
ip tacacs vrf default source-interface Loopback1
ip tacacs vrf TEST1 source-interface Loopback3
ip tacacs source-interface Loopback10
```

### IP RADIUS Source Interfaces

#### IP RADIUS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback1 |
| default | Loopback10 |
| MGMT | Management1 |

#### IP RADIUS Source Interfaces Device Configuration

```eos
!
ip radius vrf default source-interface Loopback1
!
ip radius source-interface Loopback10
!
ip radius vrf MGMT source-interface Management1
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1 | Test_ipv6_address | - | 10.2.255.3/32 | default | - | - | - | - |

*Inherited from Port-Channel Interface

##### IPv6

| Interface | Description | Channel Group | IPv6 Addresses | VRF | MTU | Shutdown | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ------------- | -------------- | --- | --- | -------- | -------------- | --------------- | ---------------------- | ----------- | ------------ |
| Ethernet1 | Test_ipv6_address | - | 2002::CAFE/128 | default | - | - | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel1 | Test_ipv6_address | - | 10.2.255.3/32 | default | - | - | - | - |

##### IPv6

| Interface | Description | MLAG ID | IPv6 Addresses | VRF | MTU | Shutdown | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ------- | -------------- | --- | --- | -------- | -------------- | --------------- | ---------------------- | ----------- | ------------ |
| Port-Channel1 | Test_ipv6_address | - | 2002::CAFE/128 | default | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback2 | Test_ipv6_address | default | 10.2.255.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Addresses |
| --------- | ----------- | --- | -------------- |
| Loopback2 | Test_ipv6_address | default | 2002::CAFE/128 |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback2
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
```

### Tunnel Interfaces

#### Tunnel Interfaces Summary

| Interface | Description | VRF | Underlay VRF | MTU | Shutdown | NAT Profile | Mode | Source | Destination | PMTU-Discovery | IPsec Profile |
| --------- | ----------- | --- | ------------ | --- | -------- | ----------- | ---- | ------ | ----------- | -------------- | ------------- |
| Tunnel1 | test ipv4 only | default | default | - | - | - | - | - | - | - | - |

##### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |
| Tunnel1 | default | 42.42.42.42/24 | - | - | - | - |

##### IPv6

| Interface | VRF | IPv6 Addresses | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out | ND RA RX Accept | ND RA Disabled | ND Managed Config Flag |
| --------- | --- | -------------- | ------- | ----------------- | ----------- | ------------ | --------------- | -------------- | ---------------------- |
| Tunnel1 | default | 2002::CAFE/128 | - | - | - | - | - | - | - |

#### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel1
   description test ipv4 only
   ip address 42.42.42.42/24
   ipv6 address 2002::CAFE/128
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| VLAN10 | Test_ipv6_address | default | - | - |
| VLAN20 | - | default | - | - |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| VLAN10 | default | 10.2.255.3/32 | - | - | - | - |
| VLAN20 | default | - | - | - | - | - |

##### IPv6

| Interface | VRF | IPv6 Addresses | IPv6 Virtual Addresses | Virtual Router Addresses | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | -------------- | ---------------------- | ------------------------ | -------------- | --------------- | ---------------------- | -------------------- | ----------- | ------------ |
| VLAN10 | default | 2002::CAFE/128 | - | - | - | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface VLAN10
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
!
interface VLAN20
   ipv6 nd cache expire 200
   ipv6 nd cache dynamic capacity 800
   ipv6 nd cache refresh always
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd other-config-flag
   ipv6 nd prefix 2001:db8:20::/64 infinite infinite no-autoconfig
```

## ACL

### Standard Access-lists

#### Standard Access-lists Summary

##### ACL-API

| Sequence | Action | Source | Remark | Log | Mirror Session |
| -------- | ------ | ------ | ------ | --- | -------------- |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible | - | - | - | - |
| 20 | permit host 10.10.10.10 | - | - | - | - |

#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard ACL-API
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 permit host 10.10.10.10
```
