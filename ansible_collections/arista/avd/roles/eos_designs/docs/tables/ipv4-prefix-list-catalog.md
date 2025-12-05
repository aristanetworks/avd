<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv4_prefix_list_catalog</samp>](## "ipv4_prefix_list_catalog") | List, items: Dictionary |  |  |  | IPv4 prefix-list catalog.<br>Note: Entries defined in `ipv4_prefix_list_catalog` are only rendered in the configuration when<br>they are explicitly referenced in one of the following node config keys:<br>- `l3_interfaces.[].bgp.ipv4_prefix_list_in`<br>- `l3_interfaces.[].bgp.ipv4_prefix_list_out`<br>- `l3_port_channels.[].bgp.ipv4_prefix_list_in`<br>- `l3_port_channels.[].bgp.ipv4_prefix_list_out`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv4_prefix_list_catalog.[].name") | String | Required, Unique |  |  | Prefix-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "permit 10.255.0.0/27 eq 32" |

=== "YAML"

    ```yaml
    # IPv4 prefix-list catalog.
    # Note: Entries defined in `ipv4_prefix_list_catalog` are only rendered in the configuration when
    # they are explicitly referenced in one of the following node config keys:
    # - `l3_interfaces.[].bgp.ipv4_prefix_list_in`
    # - `l3_interfaces.[].bgp.ipv4_prefix_list_out`
    # - `l3_port_channels.[].bgp.ipv4_prefix_list_in`
    # - `l3_port_channels.[].bgp.ipv4_prefix_list_out`.
    ipv4_prefix_list_catalog:

        # Prefix-list Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "permit 10.255.0.0/27 eq 32"
            action: <str; required>
    ```
