# application-traffic-recognition

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Application Traffic Recognition](#application-traffic-recognition)

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
      !

### Application Traffic Recognition

#### Application Traffic Recognition Summary

##### Categories

###### Category best-effort

####### Application And Services

| Application Name | Service |
| -------- | -------- |
 | app1 | software-update |
 | app3 | software-update |

###### Category category1

####### Application And Services

| Application Name | Service |
| -------- | -------- |
 | app1 | chat |
 | app1 | audio-video |
 | app2 | - |

##### Port Range Sets

###### Port Set src_port_set1

| Port Ranges |
[ -------- ]
| 2400-2500 |
| 2900-3000 |

###### Port Set dest_port_set1

| Port Ranges |
[ -------- ]
| 2300-2350 |

##### Prefix Sets

###### Prefix Set src_prefix_set1

| Prefixes |
| -------- |
| 1.2.3.0/24 |

###### Prefix Set dest_prefix_set1

| Prefixes |
| -------- |
| 2.3.4.0/24 |

##### User Defined Ipv4 Applications

| Setting | Application Name |
| ------ | -------- |
| application ipv4 | user_defined_app1 |


###### Source Prefix for the Application

| Setting | Prefix Set Name |
| ------ | -------- |
| source prefix field-set | src_prefix_set1 |


###### Destination Prefix for the Application

| Setting | Prefix Set Name |
| ------ | -------- |
| destination prefix field-set | src_prefix_set1 |


###### Protocol, Source Port and Destination Port Name

| Protocol Name | Source Port Set | Destination Port Set |
| ------ | -------- | -------- |
| udp | src_port_set1 | dest_port_set1 |

##### Application Profile Details

###### Application Profile Name app_profile_1

###### Category, Applications and Services under Application Profile

| Setting | Application/Category Name | Service |
| ------ | -------- | -------- |
| application | user_defined_app1 | - |
| application | app1 | - |
| application | app1 | - |
| category | best-effort | - |
| category | category1 | audio-video |


###### Underlying transports for application

| transport name |
| ----- |
| http |
| udp |

#### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   category best-effort
      application app1 service software-update
      application app3 service software-update
   !
   category category1
      application app1 service chat
      application app1 service audio-video
      application app2
   !
   field-set l4-port src_port_set1
      2400-2500
      2900-3000
   !
   field-set l4-port dest_port_set1
      2300-2350
   !
   field-set ipv4 prefix src_prefix_set1
      1.2.3.0/24
   !
   field-set ipv4 prefix dest_prefix_set1
      2.3.4.0/24
   !
   application ipv4 user_defined_app1
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol udp source port field-set src_port_set1 destination port field-set dest_port_set1
   !
   application-profile app_profile_1
      application user_defined_app1
      application app1 service chat
      application app1 service audio-video
      application http transport
      application udp transport
      category best-effort
      category category1 service audio-video
   !
```
