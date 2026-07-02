<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv4_standard_acls</samp>](## "ipv4_standard_acls") | List, items: Dictionary |  |  |  | IPv4 standard access-lists catalog.<br>These access-lists will only be configured on devices where they are in use. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv4_standard_acls.[].name") | String | Required, Unique |  |  | Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv4_standard_acls.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ipv4_standard_acls.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv4_standard_acls.[].entries.[].sequence") | Integer |  |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv4_standard_acls.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | Action as string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ipv4_standard_acls.[].entries.[].remark") | String |  |  |  | Specify a comment. If remark is specified other keys of the entry are ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ipv4_standard_acls.[].entries.[].source") | String |  |  |  | Required for non-remark entries.<br>The value can be:<br>1. A single source address.<br>2. Source address with mask. e.g. '10.0.0.1/8'.<br>3. 'any' source address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ipv4_standard_acls.[].entries.[].vlan") | Integer |  |  |  | Match packets by VLAN value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ipv4_standard_acls.[].entries.[].vlan_mask") | String |  |  |  | VLAN mask. Range "0x000"-"0xFFF". Required when `vlan` is defined.<br>To ensure that a value like 0x001 is treated strictly as a string<br>and not converted to a decimal (like 1), use single or double quotes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "ipv4_standard_acls.[].entries.[].inner_vlan") | Integer |  |  |  | Match packets by inner VLAN value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_mask</samp>](## "ipv4_standard_acls.[].entries.[].inner_vlan_mask") | String |  |  |  | Inner VLAN mask. Range 0x000-0xFFF. Required when `inner_vlan` is defined.<br>To ensure that a value like 0x001 is treated strictly as a string<br>and not converted to a decimal (like 1), use single or double quotes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ipv4_standard_acls.[].entries.[].log") | Boolean |  |  |  | Enable logging when a packet matches the ACL rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mirror_session</samp>](## "ipv4_standard_acls.[].entries.[].mirror_session") | String |  |  |  | Mirror session to mirror matches against this rule. |

=== "YAML"

    ```yaml
    # IPv4 standard access-lists catalog.
    # These access-lists will only be configured on devices where they are in use.
    ipv4_standard_acls:

        # Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>
        entries:

            # Sequence ID.
          - sequence: <int>

            # Action as string.
            action: <str; "permit" | "deny">

            # Specify a comment. If remark is specified other keys of the entry are ignored.
            remark: <str>

            # Required for non-remark entries.
            # The value can be:
            # 1. A single source address.
            # 2. Source address with mask. e.g. '10.0.0.1/8'.
            # 3. 'any' source address.
            source: <str>

            # Match packets by VLAN value.
            vlan: <int>

            # VLAN mask. Range "0x000"-"0xFFF". Required when `vlan` is defined.
            # To ensure that a value like 0x001 is treated strictly as a string
            # and not converted to a decimal (like 1), use single or double quotes.
            vlan_mask: <str>

            # Match packets by inner VLAN value.
            inner_vlan: <int>

            # Inner VLAN mask. Range 0x000-0xFFF. Required when `inner_vlan` is defined.
            # To ensure that a value like 0x001 is treated strictly as a string
            # and not converted to a decimal (like 1), use single or double quotes.
            inner_vlan_mask: <str>

            # Enable logging when a packet matches the ACL rule.
            log: <bool>

            # Mirror session to mirror matches against this rule.
            mirror_session: <str>
    ```
