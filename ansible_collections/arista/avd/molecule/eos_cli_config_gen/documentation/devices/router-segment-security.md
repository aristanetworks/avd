# router-segment-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)

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

#### Group-Based Multi-domain Segmentation Services (MSS-Group)

- MSS-G is enabled.

##### Segmentation Policies

###### POLICY-TEST1

| Sequence Number | Application Name | Action | Next-Hop |
| --------------- | ---------------- | ------ | -------- |
| 10 | APP-TEST-1 | forward | - |
| 20 | APP-TEST-2 | drop | - |

##### Segment Definitions

###### VRF default Segmentation

####### Segment SEGMENT-TEST1 Definitions

| Match-List Name | Address Family | Covered |
| ------------ | -------------- | ------- |
| MATCH-LIST1 | ipv4 | False |
| MATCH-LIST10 | ipv4 | False |
| MATCH-LIST11 | ipv6 | False |

####### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST21 | POLICY-TEST1 |
| MATCH-LIST30 | policy-drop-all |

###### VRF SECURE Segmentation

####### Segment SEGMENT-TEST1 Definitions

| Match-List Name | Address Family | Covered |
| ------------ | -------------- | ------- |
| MATCH-LIST1 | ipv4 | False |
| MATCH-LIST10 | ipv4 | False |

####### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST30 | policy-drop-all |

##### Router MSS-G Device Configuration

```eos
!
router segment-security
   no shutdown
   !
   policy POLICY-TEST1
      10 application APP-TEST-1 action forward stateless
      20 application APP-TEST-2 action drop stateless
   !
   vrf default
      segment SEGMENT-TEST1
         definition
            match prefix-ipv4 MATCH-LIST1
            match prefix-ipv4 MATCH-LIST10
            match prefix-ipv6 MATCH-LIST11
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST21 policy POLICY-TEST1
            from MATCH-LIST30 policy policy-drop-all
   vrf SECURE
      segment SEGMENT-TEST1
         definition
            match prefix-ipv4 MATCH-LIST1
            match prefix-ipv4 MATCH-LIST10
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST30 policy policy-drop-all
```
