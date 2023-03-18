# ip-domain-lookup
# Table of Contents

- [Management](#management)
  - [Domain Lookup](#domain-lookup)

# Management

## Domain Lookup

### DNS Domain Lookup Summary

| Source interface | vrf |
| ---------------- | --- |
| Loopback0 | - |
| Management0 | mgt |

### DNS Domain Lookup Device Configuration

```eos
ip domain lookup source-interface Loopback0
ip domain lookup vrf mgt source-interface Management0
```
