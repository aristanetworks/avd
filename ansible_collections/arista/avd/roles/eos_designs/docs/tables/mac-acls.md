<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_acls</samp>](## "mac_acls") | List, items: Dictionary |  |  |  | These MAC access-lists can be referenced under `network_ports/connected_endpoints` and only configured when it is in use. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "mac_acls.[].name") | String | Required, Unique |  |  | MAC Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "mac_acls.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_acls.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "mac_acls.[].entries.[].sequence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_acls.[].entries.[].action") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    # These MAC access-lists can be referenced under `network_ports/connected_endpoints` and only configured when it is in use.
    mac_acls:

        # MAC Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>
        entries:
          - sequence: <int>
            action: <str; required>
    ```
