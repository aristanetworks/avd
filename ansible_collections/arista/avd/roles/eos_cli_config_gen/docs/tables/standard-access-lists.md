<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>standard_access_lists</samp>](## "standard_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "standard_access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "standard_access_lists.[].entries.[].sequence") | Integer |  |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "standard_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | Action as string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "standard_access_lists.[].entries.[].remark") | String |  |  |  | Specify a comment. If remark is specified other keys of the entry are ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "standard_access_lists.[].entries.[].source") | String |  |  |  | The value can be:<br>1. A single source address.<br>2. Source address with mask. e.g. '10.0.0.1/8'.<br>3. 'any' source address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "standard_access_lists.[].entries.[].vlan") | Integer |  |  |  | Match packets by VLAN value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "standard_access_lists.[].entries.[].vlan_mask") | String |  |  |  | VLAN mask. Range "0x000"-"0xFFF". Required when `vlan` is defined.<br>To ensure that a value like 0x001 is treated strictly as a string<br>and not converted to a decimal (like 1), use single or double quotes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "standard_access_lists.[].entries.[].inner_vlan") | Integer |  |  |  | Match packets by inner VLAN value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_mask</samp>](## "standard_access_lists.[].entries.[].inner_vlan_mask") | String |  |  |  | Inner VLAN mask. Range 0x000-0xFFF. Required when `inner_vlan` is defined.<br>To ensure that a value like 0x001 is treated strictly as a string<br>and not converted to a decimal (like 1), use single or double quotes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "standard_access_lists.[].entries.[].log") | Boolean |  |  |  | Enable logging when a packet matches the ACL rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mirror_session</samp>](## "standard_access_lists.[].entries.[].mirror_session") | String |  |  |  | Mirror session to mirror matches against this rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "standard_access_lists.[].sequence_numbers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>entries</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "deny ip any any"<br> |

=== "YAML"

    ```yaml
    standard_access_lists:

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
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `entries` instead.
        sequence_numbers:

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "deny ip any any"
            action: <str; required>
    ```
