<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_session_default_encapsulation_gre</samp>](## "monitor_session_default_encapsulation_gre") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;payload</samp>](## "monitor_session_default_encapsulation_gre.payload") | String |  |  | Valid Values:<br>- <code>full-packet</code><br>- <code>inner-packet</code> | Mirroring GRE payload type configuration commands. |

=== "YAML"

    ```yaml
    monitor_session_default_encapsulation_gre:

      # Mirroring GRE payload type configuration commands.
      payload: <str; "full-packet" | "inner-packet">
    ```
