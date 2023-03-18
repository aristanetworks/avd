# management-ssh
# Table of Contents

- [Management](#management)
  - [Management SSH](#management-ssh)

# Management

## Management SSH


### SSH timeout and management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| default | Enabled |

### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| - | - |

### Ciphers and algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

### VRFs

| VRF | Status |
| --- | ------ |
| mgt | Enabled |

### Management SSH Configuration

```eos
!
management ssh
   !
   vrf mgt
      no shutdown
```
