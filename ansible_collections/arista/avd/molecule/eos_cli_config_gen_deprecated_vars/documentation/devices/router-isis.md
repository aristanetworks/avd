# router-isis
# Table of Contents

- [Routing](#routing)
  - [Router ISIS](#router-isis)

# Routing

## Router ISIS

### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Address Family | ipv4 unicast, ipv6 unicast |

### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   !
   address-family ipv4 unicast
      maximum-paths 2
      fast-reroute ti-lfa mode link-protection
   address-family ipv6 unicast
      maximum-paths 2
      fast-reroute ti-lfa mode link-protection
   !
```
