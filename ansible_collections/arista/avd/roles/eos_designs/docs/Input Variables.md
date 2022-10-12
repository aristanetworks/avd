!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## BFD Multihop tunning

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  | BFD Multihop tunning |
| [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 |  |  |

### YAML

```yaml
bfd_multihop:
  interval: <int>
  min_rx: <int>
  multiplier: <int>
```
