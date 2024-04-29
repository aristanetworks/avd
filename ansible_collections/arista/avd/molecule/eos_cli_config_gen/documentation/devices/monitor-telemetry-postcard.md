# monitor-telemetry-postcard

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Monitor Telemetry Postcard Configuration](#monitor-telemetry-postcard-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

## Monitoring

### Monitor Telemetry Postcard Configuration

```eos
!
monitor telemetry postcard policy
   no disabled
   ingress collection gre source 10.3.3.3 destination 10.3.3.4 version 2
   ingress sample rate 16384
   ingress sample tcp-udp-checksum 65000
   sample policy samplepo1
      match rule1 ipv4
         destination prefix 10.3.3.0/24
         source prefix 3.4.5.0/24
         protocol tcp destination port www
         protocol tcp destination port 78-80
         protocol tcp destination port 77
      match rule2 ipv6
         destination prefix 4::0/128
         source prefix 5::0/128
         protocol udp destination port ssh
         protocol udp destination port 748-800
         protocol udp destination port 747
   sample policy samplepo2
      match rule1 ipv4
         destination prefix 10.3.3.0/24
         source prefix 3.4.5.0/24
         protocol udp destination port www
         protocol udp destination port 88
         protocol udp source port www
         protocol udp source port 78-80
         protocol udp source port 77
   profile profile1
      ingress sample policy ingresspo1
   profile profile2
      ingress sample policy ingresspo1
```
