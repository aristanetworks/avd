<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_access_lists</samp>](## "ip_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ip_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_access_lists.[].entries") | List, items: Dictionary |  |  |  | ACL Entries |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ip_access_lists.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ip_access_lists.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in acl entry will be ignored.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny | ACL action.<br>Required for standard entry.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_access_lists.[].entries.[].protocol") | String |  |  |  | ip, tcp, udp, icmp or other protocol name or number.<br>Required for standard entry.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ip_access_lists.[].entries.[].source") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ip_access_lists.[].entries.[].source_ports_match") | String |  | `eq` | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ip_access_lists.[].entries.[].source_ports") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].source_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP source port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ip_access_lists.[].entries.[].destination") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ip_access_lists.[].entries.[].destination_ports_match") | String |  | `eq` | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ip_access_lists.[].entries.[].destination_ports") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].destination_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP destination port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ip_access_lists.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].tcp_flags.[].&lt;str&gt;") | String |  |  |  | TCP Flag Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp>](## "ip_access_lists.[].entries.[].fragments") | Boolean |  |  |  | Match non-head fragment packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ip_access_lists.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "ip_access_lists.[].entries.[].ttl") | Integer |  |  | Min: 0<br>Max: 254 | TTL value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp>](## "ip_access_lists.[].entries.[].ttl_match") | String |  | `eq` | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ip_access_lists.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ip_access_lists.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ip_access_lists.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ip_access_lists.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ip_access_lists.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ip_access_lists.[].entries.[].vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp>](## "ip_access_lists.[].entries.[].vlan_inner") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ip_access_lists.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |

=== "YAML"

    ```yaml
    ip_access_lists:
      - name: <str>
        counters_per_entry: <bool>
        entries:
          - sequence: <int>
            remark: <str>
            action: <str>
            protocol: <str>
            source: <str>
            source_ports_match: <str>
            source_ports:
              - <str>
            destination: <str>
            destination_ports_match: <str>
            destination_ports:
              - <str>
            tcp_flags:
              - <str>
            fragments: <bool>
            log: <bool>
            ttl: <int>
            ttl_match: <str>
            icmp_type: <str>
            icmp_code: <str>
            nexthop_group: <str>
            tracked: <bool>
            dscp: <str>
            vlan_number: <int>
            vlan_inner: <bool>
            vlan_mask: <str>
    ```
