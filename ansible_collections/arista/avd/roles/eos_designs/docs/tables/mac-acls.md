<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_acls</samp>](## "mac_acls") | List, items: Dictionary |  |  |  | MAC access-lists.<br>These can be referenced under `network_ports/connected_endpoints`<br>and only configured when it is in use. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "mac_acls.[].name") | String | Required, Unique |  |  | Access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_acls.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "mac_acls.[].entries.[].sequence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_acls.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "mac_acls.[].entries.[].source") | String |  |  |  | Source mac-address.<br>This can be `any` or a MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_wildcard</samp>](## "mac_acls.[].entries.[].source_wildcard") | String |  |  |  | Wildcard bits for source MAC address.<br>Required when `source` is not `any`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "mac_acls.[].entries.[].destination") | String |  |  |  | Destination MAC address.<br>This can be `any` or a MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_wildcard</samp>](## "mac_acls.[].entries.[].destination_wildcard") | String |  |  |  | Wildcard bits for destination MAC address.<br>Required when `destination` is not `any`. |

=== "YAML"

    ```yaml
    # MAC access-lists.
    # These can be referenced under `network_ports/connected_endpoints`
    # and only configured when it is in use.
    mac_acls:

        # Access-list name.
      - name: <str; required; unique>
        entries:
          - sequence: <int>
            action: <str; "permit" | "deny">

            # Source mac-address.
            # This can be `any` or a MAC address.
            source: <str>

            # Wildcard bits for source MAC address.
            # Required when `source` is not `any`.
            source_wildcard: <str>

            # Destination MAC address.
            # This can be `any` or a MAC address.
            destination: <str>

            # Wildcard bits for destination MAC address.
            # Required when `destination` is not `any`.
            destination_wildcard: <str>
    ```
