# match-list-input
# Table of Contents

- [Filters](#filters)
  - [Match-lists](#match-lists)

# Filters

## Match-lists

### Match-list Input String Summary

#### molecule

| Sequence | Match Regex |
| -------- | ------ |
| 10 | ^.*MOLECULE.*$ |
| 20 | ^.*TESTING.*$ |


### Match-lists Device Configuration

```eos
!
match-list input string molecule
   10 match regex ^.*MOLECULE.*$
   20 match regex ^.*TESTING.*$
```
