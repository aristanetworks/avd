# host1

## Table of Contents

- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking)
- [Filters](#filters)
  - [Community-lists](#community-lists)

## Monitoring

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 | Encapsulations |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------- |
| default | default | disabled | disabled | - |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | - | - | - | 5 |  | - |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T1 | T1-E1 | 42.42.42.42 | - | No local interface |
| T1 | T1-E2 | - | - | No local interface |
| T1 | T1-E3 | 10.10.10.10 | 777 | No local interface |
| T1 | T1-E4 | this.is.my.awesome.collector.dns.name | 888 | No local interface |
| T1 | T1-E5 | dead:beef::cafe | - | No local interface |

#### Flow Tracking Hardware

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | - | - | 5 |  |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T1 | T1-E1 | 42.42.42.42 | - | No local interface |
| T1 | T1-E2 | - | - | No local interface |
| T1 | T1-E3 | 10.10.10.10 | 777 | No local interface |
| T1 | T1-E4 | this.is.my.awesome.collector.dns.name | 888 | No local interface |
| T1 | T1-E5 | dead:beef::cafe | - | No local interface |

#### Flow Tracking Device Configuration

```eos
!
flow tracking hardware
   tracker T1
      exporter T1-E1
         collector 42.42.42.42
      !
      exporter T1-E2
      !
      exporter T1-E3
         collector 10.10.10.10 port 777
      !
      exporter T1-E4
         collector this.is.my.awesome.collector.dns.name port 888
      !
      exporter T1-E5
         collector dead:beef::cafe
!
flow tracking sampled
   tracker T1
      exporter T1-E1
         collector 42.42.42.42
      !
      exporter T1-E2
      !
      exporter T1-E3
         collector 10.10.10.10 port 777
      !
      exporter T1-E4
         collector this.is.my.awesome.collector.dns.name port 888
      !
      exporter T1-E5
         collector dead:beef::cafe
```

## Filters

### Community-lists

#### Community-lists Summary

| Name | Action |
| -------- | ------ |
| TEST1 | permit 1000:1000 |
| TEST2 | permit 2000:3000 |

#### Community-lists Device Configuration

```eos
!
ip community-list TEST1 permit 1000:1000
ip community-list TEST2 permit 2000:3000
```
