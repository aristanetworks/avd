# ip-client-source-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)

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
#### IP Client Source Interfaces


#### IP FTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


#### IP HTTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback0 |
| MGMT | Management0 |
| default | Ethernet10 |


#### IP SSH Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


#### IP Telnet Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


#### IP TFTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |


#### IP Client Source Interfaces Configuration

```eos
!
ip ftp client source-interface Loopback0 vrf default
ip ftp client source-interface Management0 vrf MGMT
ip ftp client source-interface Ethernet10
ip http client local-interface Loopback0 vrf default
ip http client local-interface Management0 vrf MGMT
ip http client local-interface Ethernet10
ip ssh client source-interface Ethernet10
ip ssh client source-interface Loopback0 vrf default
ip ssh client source-interface Management0 vrf MGMT
ip telnet client source-interface Loopback0 vrf default
ip telnet client source-interface Management0 vrf MGMT
ip telnet client source-interface Ethernet10
ip tftp client source-interface Loopback0 vrf default
ip tftp client source-interface Management0 vrf MGMT
ip tftp client source-interface Ethernet10
 ```

