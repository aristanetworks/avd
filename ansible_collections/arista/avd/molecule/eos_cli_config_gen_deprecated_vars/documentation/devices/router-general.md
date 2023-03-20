# router-general
# Table of Contents

- [Routing](#routing)
  - [Router General](#router-general)

# Routing

## Router General

### VRF Route leaking

| VRF | Source VRF | Route Map Policy |
|-----|------------|------------------|
| BLUE-C2 | BLUE-C1 | RM-BLUE-LEAKING |

### Router General configuration

```eos
!
router general
   vrf BLUE-C2
      leak routes source-vrf BLUE-C1 subscribe-policy RM-BLUE-LEAKING
      exit
   !
   exit
```
