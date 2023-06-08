=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  | BFD Multihop tuning. |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | `300` | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | `300` | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | `3` | Min: 3<br>Max: 50 |  |

=== "YAML"

    ```yaml
    bfd_multihop:
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    ```
