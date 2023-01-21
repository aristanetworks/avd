---
search:
  boost: 2
---

# ACLs
## IP Extended Access-Lists (legacy model)

=== "IP Extended Access-Lists (legacy model)"

    AVD currently supports 2 different data models for extended ACLs:

    - The legacy `access_lists` data model, for compatibility with existing deployments
    - The improved `ip_access_lists` data model, for access to more EOS features

    Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
    Access list names must be unique.

    The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

=== "YAML"

    ```yaml
    access_lists:
      - name: <str>
        counters_per_entry: <bool>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
## IP Extended Access-Lists (improved model)

=== "IP Extended Access-Lists (improved model)"

    AVD currently supports 2 different data models for extended ACLs:

    - The legacy `access_lists` data model, for compatibility with existing deployments
    - The improved `ip_access_lists` data model, for access to more EOS features

    Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
    Access list names must be unique.

    The improved data model has a more sophisticated design documented below:


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary |  |  |  | ACL Entries |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer |  |  |  | ACL entry sequence number.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp> | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in acl entry will be ignored.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  | Valid Values:<br>- permit<br>- deny | ACL action.<br>Required for standard entry.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp> | String |  |  |  | ip, tcp, udp, icmp or other protocol name or number.<br>Required for standard entry.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp> | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp> | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | TCP/UDP source port name or number. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp> | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp> | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | TCP/UDP destination port name or number. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | TCP Flag Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp> | Boolean |  |  |  | Match non-head fragment packets. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp> | Boolean |  |  |  | Log matches against this rule. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp> | Integer |  |  | Min: 0<br>Max: 254 | TTL value |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp> | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp> | String |  |  |  | Message type name/number for ICMP packets. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp> | String |  |  |  | Message code for ICMP packets. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp> | String |  |  |  | nexthop-group name. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp> | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | String |  |  |  | DSCP value or name. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp> | Boolean |  | False |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp> | String |  |  |  | 0x000-0xFFF VLAN mask. |

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
## IP Access Lists Max Entries

=== "IP Access Lists Max Entries"

    The `ip_access_lists` data model allows to limit the number of ACL entries that AVD is allowed to generate by defining `ip_access_lists_max_entries`.
    Only normal entries under `ip_access_lists` will be counted, remarks will be ignored.
    If the number is above the limit, the playbook will fail. This provides a simplified control over hardware utilization.
    The numbers must be based on the hardware tests and AVD does not provide any guidance. Note that other EOS features may use the same hardware resources and affect the supported scale.

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_access_lists_max_entries</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    ip_access_lists_max_entries: <int>
    ```
## IPv6 Extended Access-Lists

=== "IPv6 Extended Access-Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ipv6_access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | IPv6 Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

=== "YAML"

    ```yaml
    ipv6_access_lists:
      - name: <str>
        counters_per_entry: <bool>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
## IPv6 Standard Access Lists

=== "IPv6 Standard Access Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ipv6_standard_access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

=== "YAML"

    ```yaml
    ipv6_standard_access_lists:
      - name: <str>
        counters_per_entry: <bool>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
## MAC Access Lists

=== "MAC Access Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mac_access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | MAC Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    mac_access_lists:
      - name: <str>
        counters_per_entry: <bool>
        entries:
          - sequence: <int>
            action: <str>
    ```
## Standard Access Lists

=== "Standard Access Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>standard_access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Access-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

=== "YAML"

    ```yaml
    standard_access_lists:
      - name: <str>
        counters_per_entry: <bool>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
