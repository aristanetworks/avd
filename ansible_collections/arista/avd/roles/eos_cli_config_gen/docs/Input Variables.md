!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## IP Extended Access-Lists (legacy model)

### Description

AVD currently supports 2 different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>access_lists</samp>](## "access_lists") | List, items: Dictionary |  |  |  | IP Extended Access-Lists (legacy model) |
| [<samp>&nbsp;&nbsp;- name</samp>](## "access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
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
| [<samp>community_lists</samp>](## "community_lists") | List, items: Dictionary |  |  |  | Community Lists (legacy model) |
| [<samp>&nbsp;&nbsp;- name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

### YAML

```yaml
community_lists:
  - name: <str>
    action: <str>
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
| [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  | IP Community Lists |
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

## Domain Lookup

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_domain_lookup</samp>](## "ip_domain_lookup") | Dictionary |  |  |  | Domain Lookup |
| [<samp>&nbsp;&nbsp;source_interfaces</samp>](## "ip_domain_lookup.source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_domain_lookup.source_interfaces.[].name") | String | Required, Unique |  |  | Source Interface<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_domain_lookup.source_interfaces.[].vrf") | String |  |  |  | VRF |

### YAML

```yaml
ip_domain_lookup:
  source_interfaces:
    - name: <str>
      vrf: <str>
```

## IP Extended Community Lists RegExp

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists_regexp</samp>](## "ip_extcommunity_lists_regexp") | List, items: Dictionary |  |  |  | IP Extended Community Lists RegExp |
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

## IPv6 Extended Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_access_lists</samp>](## "ipv6_access_lists") | List, items: Dictionary |  |  |  | IPv6 Extended Access-Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_access_lists.[].name") | String | Required, Unique |  |  | IPv6 Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

### YAML

```yaml
ipv6_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Match Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>match_list_input</samp>](## "match_list_input") | Dictionary |  |  |  | Match Lists |
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

## Standard Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>standard_access_lists</samp>](## "standard_access_lists") | List, items: Dictionary |  |  |  | Standard Access-Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "standard_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
standard_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Internal VLAN Order

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlan_internal_order</samp>](## "vlan_internal_order") | Dictionary |  |  |  | Internal VLAN Order |
| [<samp>&nbsp;&nbsp;allocation</samp>](## "vlan_internal_order.allocation") | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
| [<samp>&nbsp;&nbsp;range</samp>](## "vlan_internal_order.range") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "vlan_internal_order.range.beginning") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "vlan_internal_order.range.ending") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |

### YAML

```yaml
vlan_internal_order:
  allocation: <str>
  range:
    beginning: <int>
    ending: <int>
```
