<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | `l3ls-evpn` | Valid Values:<br>- <code>l3ls-evpn</code><br>- <code>mpls</code><br>- <code>l2ls</code> | By setting the design.type variable, the default node-types and templates described in these documents will be used.<br> |

=== "YAML"

    ```yaml
    design:

      # By setting the design.type variable, the default node-types and templates described in these documents will be used.
      type: <str; "l3ls-evpn" | "mpls" | "l2ls"; default="l3ls-evpn">
    ```
