<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_access_lists</samp>](## "ipv6_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv6_access_lists.[].name") | String | Required, Unique |  |  | IPv6 Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ipv6_access_lists.[].entries") | List, items: Dictionary |  |  |  | ACL Entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "ipv6_access_lists.[].entries.[].protocol") | String |  |  |  | "ipv6", "tcp", "udp", "icmpv6" or other protocol name or number.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ipv6_access_lists.[].entries.[].source") | String |  |  |  | "any", "<ipv6>/<mask>" or "<ipv6>".<br>"<ipv6>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ipv6_access_lists.[].entries.[].destination") | String |  |  |  | "any", "<ipv6>/<mask>" or "<ipv6>".<br>"<ipv6>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_limit</samp>](## "ipv6_access_lists.[].entries.[].hop_limit") | Integer |  |  | Min: 0 | Match Hop Limit value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_limit_match</samp>](## "ipv6_access_lists.[].entries.[].hop_limit_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_mask</samp>](## "ipv6_access_lists.[].entries.[].dscp_mask") | String |  |  |  | DSCP mask ranges from 0x00 to 0x3F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence</samp>](## "ipv6_access_lists.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ipv6_access_lists.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in the ACL entry will be ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | ACL action.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ipv6_access_lists.[].entries.[].source_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ipv6_access_lists.[].entries.[].source_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_access_lists.[].entries.[].source_ports.[]") | String |  |  |  | TCP/UDP source port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ipv6_access_lists.[].entries.[].destination_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ipv6_access_lists.[].entries.[].destination_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_access_lists.[].entries.[].destination_ports.[]") | String |  |  |  | TCP/UDP destination port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ipv6_access_lists.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_access_lists.[].entries.[].tcp_flags.[]") | String |  |  |  | TCP Flag Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ipv6_access_lists.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule.<br>Mutually exclusive with `copy_captive_portal`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ipv6_access_lists.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ipv6_access_lists.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ipv6_access_lists.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ipv6_access_lists.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ipv6_access_lists.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ipv6_access_lists.[].entries.[].vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ipv6_access_lists.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_number</samp>](## "ipv6_access_lists.[].entries.[].inner_vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_mask</samp>](## "ipv6_access_lists.[].entries.[].inner_vlan_mask") | String |  |  |  | 0x000-0xFFF inner VLAN mask. This field is required when `inner_vlan_number` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_access_lists.[].sequence_numbers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv6_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "deny ipv6 any any"<br> |

=== "YAML"

    ```yaml
    ipv6_access_lists:

        # IPv6 Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>

        # ACL Entries.
        entries:

            # "ipv6", "tcp", "udp", "icmpv6" or other protocol name or number.
            # Required except for remarks.
          - protocol: <str>

            # "any", "<ipv6>/<mask>" or "<ipv6>".
            # "<ipv6>" without a mask means host.
            # Required except for remarks.
            source: <str>

            # "any", "<ipv6>/<mask>" or "<ipv6>".
            # "<ipv6>" without a mask means host.
            # Required except for remarks.
            destination: <str>

            # Match Hop Limit value.
            hop_limit: <int; >=0>
            hop_limit_match: <str; "eq" | "gt" | "lt" | "neq"; default="eq">

            # DSCP mask ranges from 0x00 to 0x3F.
            dscp_mask: <str>

            # ACL entry sequence number.
            sequence: <int>

            # Comment up to 100 characters.
            # If remark is defined, other keys in the ACL entry will be ignored.
            remark: <str>

            # ACL action.
            # Required except for remarks.
            action: <str; "permit" | "deny">
            source_ports_match: <str; "eq" | "gt" | "lt" | "neq" | "range"; default="eq">
            source_ports: # >=1 items

                # TCP/UDP source port name or number.
              - <str>
            destination_ports_match: <str; "eq" | "gt" | "lt" | "neq" | "range"; default="eq">
            destination_ports: # >=1 items

                # TCP/UDP destination port name or number.
              - <str>
            tcp_flags:

                # TCP Flag Name.
              - <str>

            # Log matches against this rule.
            # Mutually exclusive with `copy_captive_portal`.
            log: <bool>

            # Message type name/number for ICMP packets.
            icmp_type: <str>

            # Message code for ICMP packets.
            icmp_code: <str>

            # nexthop-group name.
            nexthop_group: <str>

            # Match packets in existing ICMP/UDP/TCP connections.
            tracked: <bool>

            # DSCP value or name.
            dscp: <str>
            vlan_number: <int>

            # 0x000-0xFFF VLAN mask.
            vlan_mask: <str>
            inner_vlan_number: <int>

            # 0x000-0xFFF inner VLAN mask. This field is required when `inner_vlan_number` is set.
            inner_vlan_mask: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        sequence_numbers:

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "deny ipv6 any any"
            action: <str; required>
    ```
