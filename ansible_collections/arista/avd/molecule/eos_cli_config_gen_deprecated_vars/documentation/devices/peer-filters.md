# peer-filters
# Table of Contents

- [Filters](#filters)
  - [Peer Filters](#peer-filters)

# Filters

## Peer Filters

### Peer Filters Summary

#### PF1

| Sequence | Match |
| -------- | ----- |
| 10 | as-range 1-2 result reject |
| 20 | as-range 1-100 result accept |

#### PF2

| Sequence | Match |
| -------- | ----- |
| 30 | as-range 65000 result accept |

### Peer Filters Device Configuration

```eos
!
peer-filter PF1
   10 match as-range 1-2 result reject
   20 match as-range 1-100 result accept
!
peer-filter PF2
   30 match as-range 65000 result accept
```
