---
search:
  boost: 2
---

# Filters
## As Path

=== "As Path"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>as_path</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;regex_mode</samp> | String |  |  | Valid Values:<br>- asn<br>- string |  |
    | <samp>&nbsp;&nbsp;access_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Access List Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp> | String |  |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp> | String |  |  |  | Regex To Match |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin</samp> | String |  | any | Valid Values:<br>- any<br>- egp<br>- igp<br>- incomplete |  |

=== "YAML"

    ```yaml
    as_path:
      regex_mode: <str>
      access_lists:
        - name: <str>
          entries:
            - type: <str>
              match: <str>
              origin: <str>
    ```
## Community Lists (legacy model)

=== "Community Lists (legacy model)"

    AVD supports 2 different data models for community lists:

    - The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
    - The improved `ip_community_lists` data model.

    Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
    Community list names must be unique.

    The legacy data model supports simplified community list definition that only allows a single action to be defined as string:


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>community_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Community-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

=== "YAML"

    ```yaml
    community_lists:
      - name: <str>
        action: <str>
    ```
## Dynamic Prefix Lists

=== "Dynamic Prefix Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>dynamic_prefix_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Dynamic prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | String |  |  |  | Prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | String |  |  |  | Prefix-list name |

=== "YAML"

    ```yaml
    dynamic_prefix_lists:
      - name: <str>
        match_map: <str>
        prefix_list:
          ipv4: <str>
          ipv6: <str>
    ```
## IP Community Lists

=== "IP Community Lists"

    AVD supports 2 different data models for community lists:

    - The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
    - The improved `ip_community_lists` data model.

    Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
    Community list names must be unique.

    The improved data model has a better design documented below:

    communities and regexp MUST not be configured together in the same entry
    possible community strings are (case insensitive):
     - GSHUT
     - internet
     - local-as
     - no-advertise
     - no-export
     - <1-4294967040>
     - aa:nn


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_community_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | IP Community-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- action</samp> | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp> | List, items: String |  |  |  | If defined, a standard community-list will be configured |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp> | String |  |  |  | Regular Expression<br>If defined, a regex community-list will be configured |

=== "YAML"

    ```yaml
    ip_community_lists:
      - name: <str>
        entries:
          - action: <str>
            communities:
              - <str>
            regexp: <str>
    ```
## IP Extended Community Lists

=== "IP Extended Community Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_extcommunity_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Community-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp> | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extcommunities</samp> | String | Required |  |  | Communities as string<br>Example: "65000:65000" |

=== "YAML"

    ```yaml
    ip_extcommunity_lists:
      - name: <str>
        entries:
          - type: <str>
            extcommunities: <str>
    ```
## IP Extended Community Lists RegExp

=== "IP Extended Community Lists RegExp"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_extcommunity_lists_regexp</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Community-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp> | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp> | String | Required |  |  | Regular Expression |

=== "YAML"

    ```yaml
    ip_extcommunity_lists_regexp:
      - name: <str>
        entries:
          - type: <str>
            regexp: <str>
    ```
## IPv6 Prefix Lists

=== "IPv6 Prefix Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ipv6_prefix_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Prefix-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "permit 1b11:3a00:22b0:0082::/64 eq 128" |

=== "YAML"

    ```yaml
    ipv6_prefix_lists:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
## Match Lists

=== "Match Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>match_list_input</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;string</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Match-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_regex</samp> | String | Required |  |  | Regular Expression |

=== "YAML"

    ```yaml
    match_list_input:
      string:
        - name: <str>
          sequence_numbers:
            - sequence: <int>
              match_regex: <str>
    ```
## Peer Filters

=== "Peer Filters"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>peer_filters</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-filter Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp> | String | Required |  |  | Match as string<br>Example: "as-range 1-100 result accept" |

=== "YAML"

    ```yaml
    peer_filters:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            match: <str>
    ```
## Prefix Lists

=== "Prefix Lists"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>prefix_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Prefix-list Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String | Required |  |  | Action as string<br>Example: "permit 10.255.0.0/27 eq 32" |

=== "YAML"

    ```yaml
    prefix_lists:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
## Route Maps

=== "Route Maps"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>route_maps</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Route-map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer | Required, Unique |  |  | Sequence ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp> | List, items: String |  |  |  | List of "match" statements |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Match as string<br>Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp> | List, items: String |  |  |  | List of "set" statements |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Set as string<br>Example: "origin incomplete"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_route_map</samp> | String |  |  |  | Name of Sub-Route-map |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    route_maps:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            type: <str>
            description: <str>
            match:
              - <str>
            set:
              - <str>
            sub_route_map: <str>
            continue:
              enabled: <bool>
              sequence_number: <int>
    ```
