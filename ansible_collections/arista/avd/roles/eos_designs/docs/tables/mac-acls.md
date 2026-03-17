<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_acls</samp>](## "mac_acls") | List, items: Dictionary |  |  |  | These MAC access-lists can be referenced under `network_ports/connected_endpoints`<br>and only configured when it is in use. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "mac_acls.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_acls.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "mac_acls.[].entries.[].sequence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_acls.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "mac_acls.[].entries.[].source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_wildcard</samp>](## "mac_acls.[].entries.[].source_wildcard") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "mac_acls.[].entries.[].destination") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_wildcard</samp>](## "mac_acls.[].entries.[].destination_wildcard") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # These MAC access-lists can be referenced under `network_ports/connected_endpoints`
    # and only configured when it is in use.
    mac_acls:
      - name: <str; required; unique>
        entries:
          - sequence: <int>
            action: <str; "permit" | "deny">
            source: <str>
            source_wildcard: <str>
            destination: <str>
            destination_wildcard: <str>
    ```
