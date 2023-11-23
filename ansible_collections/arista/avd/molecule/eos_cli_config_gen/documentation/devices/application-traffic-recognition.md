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
| aim | file-transfer |
| apple_update | software-update |

##### Category category1

###### Applications

| Application Name | Service |
| ---------------- | ------- |
| aim | chat |
| aim | audio-video |
| anydesk | - |

#### Field Sets

##### l4 Port Sets

###### l4 Port Set src_port_set1

| Ports |
| ----- |
| 2400-2500 |
| 2900-3000 |

###### l4 Port Set dest_port_set1

| Ports |
| ----- |
| 2300-2350 |

##### Ipv4 Prefix Sets

###### Ipv4 Prefix Set src_prefix_set1

| Prefixes |
| -------- |
| 1.2.3.0/24 |
| 1.2.5.0/24 |

###### Ipv4 Prefix Set dest_prefix_set1

| Prefixes |
| -------- |
| 2.3.4.0/24 |

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

#### Application Profile Details

##### Application Profile Name app_profile_1

##### Applications and Services under Application Profile

| Setting | Application | Service |
| ------- | ----------- | ------- |
| application | user_defined_app1 | - |
| application | aim | chat |
| application | aim | audio-video |

##### Category and Services under Application Profile

| Setting | Category | Service |
| ------- | -------- | ------- |
| category | best-effort | - |
| category | category1 | audio-video |

##### Underlying transports for application

| Transport name |
| -------------- |
| http |
| udp |

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
   category best-effort
      application aim service file-transfer
      application apple_update service software-update
   !
   category category1
      application aim service chat
      application aim service audio-video
      application anydesk
   !
   application-profile app_profile_1
      application user_defined_app1
      application aim service chat
      application aim service audio-video
      application http transport
      application udp transport
      category best-effort
      category category1 service audio-video
   !
   field-set l4-port src_port_set1
      2400-2500, 2900-3000
   !
   field-set l4-port dest_port_set1
      2300-2350
   !
   field-set ipv4 prefix src_prefix_set1
      1.2.3.0/24 1.2.5.0/24
   !
   field-set ipv4 prefix dest_prefix_set1
      2.3.4.0/24
```
