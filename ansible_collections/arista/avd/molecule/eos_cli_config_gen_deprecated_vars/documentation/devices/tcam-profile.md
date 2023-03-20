# tcam-profile
# Table of Contents

- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Custom TCAM profiles](#custom-tcam-profiles)
  - [Hardware TCAM configuration](#hardware-tcam-configuration)

# Hardware TCAM Profile

TCAM profile __`traffic_policy`__ is active

## Custom TCAM profiles

Following TCAM profiles are configured on device:

- Profile Name: `traffic_policy`

## Hardware TCAM configuration

```eos
!
hardware tcam
   profile traffic_policy
! EOS_CLI inserted directly

   !
   system profile traffic_policy
```
