<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>switchport</samp>](## "switchport") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ethernet_llc_validation</samp>](## "switchport.ethernet_llc_validation") | Boolean |  |  |  | Enable Ethernet LLC header validation. |
    | [<samp>&nbsp;&nbsp;vlan_tag_validation</samp>](## "switchport.vlan_tag_validation") | Boolean |  |  |  | Enable VLAN tag validation. |

=== "YAML"

    ```yaml
    switchport:

      # Enable Ethernet LLC header validation.
      ethernet_llc_validation: <bool>

      # Enable VLAN tag validation.
      vlan_tag_validation: <bool>
    ```
