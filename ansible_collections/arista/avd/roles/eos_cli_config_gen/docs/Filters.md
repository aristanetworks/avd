# Filters

## As Path

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>as_path</samp>](## "as_path") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;regex_mode</samp>](## "as_path.regex_mode") | String |  |  | Valid Values:<br>- asn<br>- string |  |
| [<samp>&nbsp;&nbsp;access_lists</samp>](## "as_path.access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "as_path.access_lists.[].name") | String |  |  |  | Access List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "as_path.access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "as_path.access_lists.[].entries.[].type") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "as_path.access_lists.[].entries.[].match") | String |  |  |  | Regex To Match |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin</samp>](## "as_path.access_lists.[].entries.[].origin") | String |  | any | Valid Values:<br>- any<br>- egp<br>- igp<br>- incomplete |  |

### YAML

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

### Description

AVD supports 2 different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The legacy data model supports simplified community list definition that only allows a single action to be defined as string:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>community_lists</samp>](## "community_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

### YAML

```yaml
community_lists:
  - name: <str>
    action: <str>
```

## Dynamic Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dynamic_prefix_lists</samp>](## "dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "dynamic_prefix_lists.[].match_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "dynamic_prefix_lists.[].prefix_list") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv4") | String |  |  |  | Prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv6") | String |  |  |  | Prefix-list name |

### YAML

```yaml
dynamic_prefix_lists:
  - name: <str>
    match_map: <str>
    prefix_list:
      ipv4: <str>
      ipv6: <str>
```

## IP Community Lists

### Description

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_community_lists.[].name") | String | Required, Unique |  |  | IP Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_community_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- action</samp>](## "ip_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "ip_community_lists.[].entries.[].communities") | List, items: String |  |  |  | If defined, a standard community-list will be configured |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_community_lists.[].entries.[].communities.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression<br>If defined, a regex community-list will be configured |

### YAML

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists</samp>](## "ip_extcommunity_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extcommunities</samp>](## "ip_extcommunity_lists.[].entries.[].extcommunities") | String | Required |  |  | Communities as string<br>Example: "65000:65000" |

### YAML

```yaml
ip_extcommunity_lists:
  - name: <str>
    entries:
      - type: <str>
        extcommunities: <str>
```

## IP Extended Community Lists RegExp

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists_regexp</samp>](## "ip_extcommunity_lists_regexp") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists_regexp.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists_regexp.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].regexp") | String | Required |  |  | Regular Expression |

### YAML

```yaml
ip_extcommunity_lists_regexp:
  - name: <str>
    entries:
      - type: <str>
        regexp: <str>
```

## IPv6 Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_prefix_lists</samp>](## "ipv6_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 1b11:3a00:22b0:0082::/64 eq 128" |

### YAML

```yaml
ipv6_prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Match Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>match_list_input</samp>](## "match_list_input") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;string</samp>](## "match_list_input.string") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "match_list_input.string.[].name") | String | Required, Unique |  |  | Match-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "match_list_input.string.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "match_list_input.string.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_regex</samp>](## "match_list_input.string.[].sequence_numbers.[].match_regex") | String | Required |  |  | Regular Expression |

### YAML

```yaml
match_list_input:
  string:
    - name: <str>
      sequence_numbers:
        - sequence: <int>
          match_regex: <str>
```

## Peer Filters

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>peer_filters</samp>](## "peer_filters") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "peer_filters.[].name") | String | Required, Unique |  |  | Peer-filter Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "peer_filters.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "peer_filters.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "peer_filters.[].sequence_numbers.[].match") | String | Required |  |  | Match as string<br>Example: "as-range 1-100 result accept" |

### YAML

```yaml
peer_filters:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        match: <str>
```

## Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>prefix_lists</samp>](## "prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 10.255.0.0/27 eq 32" |

### YAML

```yaml
prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Route Maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>route_maps</samp>](## "route_maps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "route_maps.[].name") | String | Required, Unique |  |  | Route-map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "route_maps.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "route_maps.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "route_maps.[].sequence_numbers.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "route_maps.[].sequence_numbers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "route_maps.[].sequence_numbers.[].match") | List, items: String |  |  |  | List of "match" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].match.[].&lt;str&gt;") | String |  |  |  | Match as string<br>Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "route_maps.[].sequence_numbers.[].set") | List, items: String |  |  |  | List of "set" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].set.[].&lt;str&gt;") | String |  |  |  | Set as string<br>Example: "origin incomplete"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_route_map</samp>](## "route_maps.[].sequence_numbers.[].sub_route_map") | String |  |  |  | Name of Sub-Route-map |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</samp>](## "route_maps.[].sequence_numbers.[].continue") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "route_maps.[].sequence_numbers.[].continue.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number</samp>](## "route_maps.[].sequence_numbers.[].continue.sequence_number") | Integer |  |  |  |  |

### YAML

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
