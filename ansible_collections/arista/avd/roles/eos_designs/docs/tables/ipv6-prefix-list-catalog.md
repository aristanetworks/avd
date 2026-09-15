<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_prefix_list_catalog</samp>](## "ipv6_prefix_list_catalog") | List, items: Dictionary |  |  |  | IPv6 prefix-list catalog.<br>Entries are only rendered when explicitly referenced by `ipv6_prefix_list_in` or<br>`ipv6_prefix_list_out` under BGP on an L3 interface or L3 Port-Channel. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv6_prefix_list_catalog.[].name") | String | Required, Unique |  |  | Prefix-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_prefix_list_catalog.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv6_prefix_list_catalog.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_prefix_list_catalog.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "permit 2001:db8::/32 le 128" |

=== "YAML"

    ```yaml
    # IPv6 prefix-list catalog.
    # Entries are only rendered when explicitly referenced by `ipv6_prefix_list_in` or
    # `ipv6_prefix_list_out` under BGP on an L3 interface or L3 Port-Channel.
    ipv6_prefix_list_catalog:

        # Prefix-list Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "permit 2001:db8::/32 le 128"
            action: <str; required>
    ```
