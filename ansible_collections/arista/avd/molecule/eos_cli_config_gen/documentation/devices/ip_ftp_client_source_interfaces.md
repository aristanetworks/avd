# ip_ftp_client_source_interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP FTP Client Source Interfaces](#ip-ftp-client-source-interfaces)
  - [IP HTTP Client Source Interfaces](#ip-http-client-source-interfaces)
  - [IP SSH Client Source Interfaces](#ip-ssh-client-source-interfaces)
  - [IP Telnet Client Source Interfaces](#ip-telnet-client-source-interfaces)
  - [IP TFTP Client Source Interfaces](#ip-tftp-client-source-interfaces)

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

### IP FTP Client Source Interfaces

#### IP FTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


### IP HTTP Client Source Interfaces

#### IP HTTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback0 |
| MGMT | Management0 |
| default | Ethernet10 |


### IP SSH Client Source Interfaces

#### IP SSH Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


### IP Telnet Client Source Interfaces

#### IP Telnet Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |



### IP TFTP Client Source Interfaces

#### IP TFTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |

