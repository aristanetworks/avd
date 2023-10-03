# ip-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Security](#ip-security)

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


### IP Security

##### IPSec profiles

| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode |
| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- |
| Profile-1 | IKE-1 | SA-1 | start | - | - | - | transport |
| Profile-2 | - | SA-2 | start | - | - | - | tunnel |

##### Key controller

| Profile name |
| ------------ |
| Profile-1 |

#### IP Security Configuration

```eos
ip security
   ike policy IKE-1
      local_id 192.168.100.1
   ike policy IKE-2
   sa policy SA-1
      esp encryption aes128
      pfs_dh_group 14
   sa policy SA-2
      esp encryption aes128
      pfs_dh_group 14
   sa policy SA-3
      esp encryption null
      pfs_dh_group 17
   profile Profile-1
      ike-policy IKE-1
      sa-policy SA-1
      connection start
      shared-key 7 12312312313213AA
      dpd 42 666 clear
      mode transport
   profile Profile-2
      sa-policy SA-2
      connection start
      shared-key 7 1231231231321AA
      mode tunnel
   key controller
      profile Profile-1
```
