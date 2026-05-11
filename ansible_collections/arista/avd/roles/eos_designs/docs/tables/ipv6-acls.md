<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_acls</samp>](## "ipv6_acls") | List, items: Dictionary |  |  |  | IPv6 extended access-lists supporting substitution on certain fields.<br>These access-lists can be referenced under network services `svis` using `ipv6_acl_in` / `ipv6_acl_out`, and will only be configured on devices where they are in use.<br><br>The substitution is useful when assigning the same access-list on multiple interfaces where certain fields require unique values.<br>When using substitution, the interface name will be appended to the ACL name.<br><br>The "interface_ip" substitution field is resolved from `ipv6_address` set on the SVI.<br>If `ipv6_address` is not set, the first entry of `ipv6_address_virtuals` is used as a fallback.<br>If neither is set, the substitution will fail with an error. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv6_acls.[].name") | String | Required, Unique |  |  | Access-list name.<br>When using substitution for any fields, the interface name will be appended to the ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ipv6_acls.[].entries") | List, items: Dictionary | Required |  |  | ACL Entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "ipv6_acls.[].entries.[].source") | String |  |  |  | This field supports substitution of the field "interface_ip" for SVIs.<br>Alternatively it can be set with a static value of "any", "<ipv6>/<mask>" or "<ipv6>".<br>"<ipv6>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ipv6_acls.[].entries.[].destination") | String |  |  |  | This field supports substitution of the field "interface_ip" for SVIs.<br>Alternatively it can be set with a static value of "any", "<ipv6>/<mask>" or "<ipv6>".<br>"<ipv6>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ipv6_acls.[].entries.[].protocol") | String |  |  |  | "ipv6", "tcp", "udp", "icmpv6" or other protocol name or number.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_limit</samp>](## "ipv6_acls.[].entries.[].hop_limit") | Integer |  |  | Min: 0 | Match Hop Limit value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_limit_match</samp>](## "ipv6_acls.[].entries.[].hop_limit_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_mask</samp>](## "ipv6_acls.[].entries.[].dscp_mask") | String |  |  |  | DSCP mask ranges from 0x00 to 0x3F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence</samp>](## "ipv6_acls.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ipv6_acls.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in the ACL entry will be ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_acls.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | ACL action.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ipv6_acls.[].entries.[].source_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ipv6_acls.[].entries.[].source_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_acls.[].entries.[].source_ports.[]") | String |  |  |  | TCP/UDP source port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ipv6_acls.[].entries.[].destination_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ipv6_acls.[].entries.[].destination_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_acls.[].entries.[].destination_ports.[]") | String |  |  |  | TCP/UDP destination port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ipv6_acls.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_acls.[].entries.[].tcp_flags.[]") | String |  |  |  | TCP Flag Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ipv6_acls.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ipv6_acls.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ipv6_acls.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ipv6_acls.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ipv6_acls.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ipv6_acls.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ipv6_acls.[].entries.[].vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ipv6_acls.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_number</samp>](## "ipv6_acls.[].entries.[].inner_vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_mask</samp>](## "ipv6_acls.[].entries.[].inner_vlan_mask") | String |  |  |  | 0x000-0xFFF inner VLAN mask. This field is required when `inner_vlan_number` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_acls.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_acls.[].sequence_numbers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv6_acls.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_acls.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "deny ipv6 any any"<br> |

=== "YAML"

    ```yaml
    # IPv6 extended access-lists supporting substitution on certain fields.
    # These access-lists can be referenced under network services `svis` using `ipv6_acl_in` / `ipv6_acl_out`, and will only be configured on devices where they are in use.
    #
    # The substitution is useful when assigning the same access-list on multiple interfaces where certain fields require unique values.
    # When using substitution, the interface name will be appended to the ACL name.
    #
    # The "interface_ip" substitution field is resolved from `ipv6_address` set on the SVI.
    # If `ipv6_address` is not set, the first entry of `ipv6_address_virtuals` is used as a fallback.
    # If neither is set, the substitution will fail with an error.
    ipv6_acls:

        # Access-list name.
        # When using substitution for any fields, the interface name will be appended to the ACL name.
      - name: <str; required; unique>

        # ACL Entries.
        entries: # required

            # This field supports substitution of the field "interface_ip" for SVIs.
            # Alternatively it can be set with a static value of "any", "<ipv6>/<mask>" or "<ipv6>".
            # "<ipv6>" without a mask means host.
            # Required except for remarks.
          - source: <str>

            # This field supports substitution of the field "interface_ip" for SVIs.
            # Alternatively it can be set with a static value of "any", "<ipv6>/<mask>" or "<ipv6>".
            # "<ipv6>" without a mask means host.
            # Required except for remarks.
            destination: <str>

            # "ipv6", "tcp", "udp", "icmpv6" or other protocol name or number.
            # Required except for remarks.
            protocol: <str>

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
        counters_per_entry: <bool>
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        sequence_numbers:

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "deny ipv6 any any"
            action: <str; required>
    ```
