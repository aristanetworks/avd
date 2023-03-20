# ipv6-prefix-lists
# Table of Contents

- [Filters](#filters)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)

# Filters

## IPv6 Prefix-lists

### IPv6 Prefix-lists Summary

#### PL-IPV6-LOOPBACKS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1b11:3a00:22b0:0082::/64 eq 128 |

### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-IPV6-LOOPBACKS
   seq 10 permit 1b11:3a00:22b0:0082::/64 eq 128
```
