<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_peer_filters_catalog</samp>](## "bgp_peer_filters_catalog") | List, items: Dictionary |  |  |  | BGP peer filter catalog.<br>Note: Entries defined in `bgp_peer_filters_catalog` are only rendered in the configuration when<br>they are explicitly referenced in listen ranges. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "bgp_peer_filters_catalog.[].name") | String | Required, Unique |  |  | Peer-filter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "bgp_peer_filters_catalog.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "bgp_peer_filters_catalog.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "bgp_peer_filters_catalog.[].sequence_numbers.[].match") | String | Required |  |  | Match as string.<br>Example: "as-range 1-100 result accept"<br> |

=== "YAML"

    ```yaml
    # BGP peer filter catalog.
    # Note: Entries defined in `bgp_peer_filters_catalog` are only rendered in the configuration when
    # they are explicitly referenced in listen ranges.
    bgp_peer_filters_catalog:

        # Peer-filter Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Match as string.
            # Example: "as-range 1-100 result accept"
            match: <str; required>
    ```
