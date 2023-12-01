# logging

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Logging](#logging)

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

## Monitoring

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | errors |
| Buffer | warnings |
| Trap | disabled |
| Synchronous | critical |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |
| RFC5424 | True |

| VRF | Source Interface |
| --- | ---------------- |
| default | Loopback0 |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| default | 20.20.20.7 | Default | UDP |
| default | 50.50.50.7 | 100, 200 | TCP |
| default | 60.60.60.7 | 100, 200 | UDP |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |
| vrf_with_no_source_interface | 1.2.3.4 | Default | UDP |

#### Logging Servers and Features Device Configuration

```eos
!
logging buffered 1000000 warnings
no logging trap
logging console errors
logging event storm-control discards global
logging event storm-control discards interval 10
logging synchronous level critical
logging host 20.20.20.7
logging host 50.50.50.7 100 200 protocol tcp
logging host 60.60.60.7 100 200
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf vrf_with_no_source_interface host 1.2.3.4
logging format timestamp traditional year timezone
logging format rfc5424
logging source-interface Loopback0
logging vrf mgt source-interface Management0
```
