<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | `0.0.0.0` | Format: ipv4 |  |
    | [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | `False` |  |  |
    | [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | `12000` |  |  |
    | [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | `100` |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_area: <str; default="0.0.0.0">
    underlay_ospf_bfd_enable: <bool; default=False>
    underlay_ospf_max_lsa: <int; default=12000>
    underlay_ospf_process_id: <int; default=100>
    ```
