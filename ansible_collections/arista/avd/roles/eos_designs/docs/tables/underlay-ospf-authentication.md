<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_authentication</samp>](## "underlay_ospf_authentication") | String |  |  | Valid Values:<br>- <code>simple</code><br>- <code>message-digest</code> |  |

=== "YAML"

    ```yaml
    underlay_ospf_authentication: <str; "simple" | "message-digest">
    ```
