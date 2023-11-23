# application-traffic-recognition

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Application Traffic Recognition](#application-traffic-recognition)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)

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

### Application Traffic Recognition

#### Categories

##### Category best-effort

###### Applications

| Application Name | Service |
| ---------------- | ------- |
| aimini | peer-to-peer |
| apple_update | software-update |

##### Category category1

###### Applications

| Application Name | Service |
| ---------------- | ------- |
| aim | audio-video |
| aim | chat |
| anydesk | - |

#### Field Sets

##### l4 Port Sets

###### l4 Port Set dest_port_set1

| Ports |
| ----- |
| 2300-2350 |

###### l4 Port Set dest_port_set2

| Ports |
| ----- |
| 3300-3350 |

###### l4 Port Set src_port_set1

| Ports |
| ----- |
| 2400-2500 |
| 2900-3000 |

###### l4 Port Set src_port_set2

| Ports |
| ----- |
| 5700-5800 |
| 6500-6600 |

##### Ipv4 Prefix Sets

###### Ipv4 Prefix Set dest_prefix_set1

| Prefixes |
| -------- |
| 2.3.4.0/24 |

###### Ipv4 Prefix Set dest_prefix_set2

| Prefixes |
| -------- |
| 4.4.4.0/24 |

###### Ipv4 Prefix Set src_prefix_set1

| Prefixes |
| -------- |
| 1.2.3.0/24 |
| 1.2.5.0/24 |

###### Ipv4 Prefix Set src_prefix_set2

| Prefixes |
| -------- |
| 2.2.2.0/24 |
| 3.3.3.0/24 |

#### Applications

##### Ipv4 Applications

| Setting | Application Name |
| ------- | ---------------- |
| application ipv4 | user_defined_app1 |

###### Source Prefix for the Application

| Setting | Prefix Set Name |
| ------- | --------------- |
| source prefix field-set | src_prefix_set1 |

###### Destination Prefix for the Application

| Setting | Prefix Set Name |
| ------- | --------------- |
| destination prefix field-set | src_prefix_set1 |

###### Protocol, Source Port and Destination Port Name

| Protocol Name | Source Port Set | Destination Port Set |
| ------------- | --------------- | -------------------- |
| udp | src_port_set1 | dest_port_set1 |
| Setting | Application Name |
| ------- | ---------------- |
| application ipv4 | user_defined_app2 |

###### Source Prefix for the Application

| Setting | Prefix Set Name |
| ------- | --------------- |
| source prefix field-set | src_prefix_set2 |

###### Destination Prefix for the Application

| Setting | Prefix Set Name |
| ------- | --------------- |
| destination prefix field-set | src_prefix_set2 |

###### Protocol, Source Port and Destination Port Name

| Protocol Name | Source Port Set | Destination Port Set |
| ------------- | --------------- | -------------------- |
| udp | src_port_set2 | dest_port_set2 |

#### Application Profile Details

##### Application Profile Name app_profile_1

##### Applications and Services under Application Profile

| Setting | Application | Service |
| ------- | ----------- | ------- |
| application | aim | audio-video |
| application | aim | chat |
| application | user_defined_app1 | - |

##### Category and Services under Application Profile

| Setting | Category | Service |
| ------- | -------- | ------- |
| category | category1 | audio-video |
| category | best-effort | - |

##### Underlying transports for application

| Transport name |
| -------------- |
| udp |
| http |

##### Application Profile Name app_profile_2

##### Applications and Services under Application Profile

| Setting | Application | Service |
| ------- | ----------- | ------- |
| application | aim | audio-video |
| application | user_defined_app2 | - |

##### Category and Services under Application Profile

| Setting | Category | Service |
| ------- | -------- | ------- |
| category | category1 | chat |

##### Underlying transports for application

| Transport name |
| -------------- |
| https |
| quic |

### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   !
   application ipv4 user_defined_app1
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol udp source port field-set src_port_set1 destination port field-set dest_port_set1
   !
   application ipv4 user_defined_app2
      source prefix field-set src_prefix_set2
      destination prefix field-set dest_prefix_set2
      protocol udp source port field-set src_port_set2 destination port field-set dest_port_set2
   !
   category best-effort
      application aimini service peer-to-peer
      application apple_update service software-update
   !
   category category1
      application aim service audio-video
      application aim service chat
      application anydesk
   !
   application-profile app_profile_1
      application aim service audio-video
      application aim service chat
      application user_defined_app1
      application http transport
      application udp transport
      category best-effort
      category category1 service audio-video
   !
   application-profile app_profile_2
      application aim service audio-video
      application user_defined_app2
      application https transport
      application quic transport
      category category1 service chat
   !
   field-set l4-port dest_port_set1
      2300-2350
   !
   field-set l4-port dest_port_set2
      3300-3350
   !
   field-set l4-port src_port_set1
      2400-2500, 2900-3000
   !
   field-set l4-port src_port_set2
      5700-5800, 6500-6600
   !
   field-set ipv4 prefix dest_prefix_set1
      2.3.4.0/24
   !
   field-set ipv4 prefix dest_prefix_set2
      4.4.4.0/24
   !
   field-set ipv4 prefix src_prefix_set1
      1.2.3.0/24 1.2.5.0/24
   !
   field-set ipv4 prefix src_prefix_set2
      2.2.2.0/24 3.3.3.0/24
```
