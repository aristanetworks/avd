---
search:
  boost: 2
---

# Quality of Service
## QOS Class-maps



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>class_maps</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;pbr</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Class-Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | String |  |  |  | Standard Access-List Name |
    | <samp>&nbsp;&nbsp;qos</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Class-Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  |  | VLAN value(s) or range(s) of VLAN values |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  |  | CoS value(s) or range(s) of CoS values |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | String |  |  |  | IPv4 Access-List Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | String |  |  |  | IPv6 Access-List Name |

=== "YAML"

    ```yaml
    class_maps:
      pbr:
        - name: <str>
          ip:
            access_group: <str>
      qos:
        - name: <str>
          vlan: <int>
          cos: <int>
          ip:
            access_group: <str>
          ipv6:
            access_group: <str>
    ```
## Policy Maps



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>policy_maps</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;pbr</samp> | List, items: Dictionary |  |  |  | PBR Policy-Maps |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Policy-Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Class Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp> | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp> | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4 or IPv6 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;qos</samp> | List, items: Dictionary |  |  |  | QOS Policy-Maps |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Policy-Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Class Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    policy_maps:
      pbr:
        - name: <str>
          classes:
            - name: <str>
              index: <int>
              drop: <bool>
              set:
                nexthop:
                  ip_address: <str>
                  recursive: <bool>
      qos:
        - name: <str>
          classes:
            - name: <str>
              set:
                cos: <int>
                dscp: <str>
                traffic_class: <int>
                drop_precedence: <int>
    ```
## QOS



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>qos</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;map</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Example: "0 1 to traffic-class 1"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Example: "8 9 10 to traffic-class 1"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Example: "1 to dscp 32"<br> |
    | <samp>&nbsp;&nbsp;rewrite_dscp</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    qos:
      map:
        cos:
          - <str>
        dscp:
          - <str>
        traffic_class:
          - <str>
      rewrite_dscp: <bool>
    ```
## QOS Profiles



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>qos_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Profile-Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trust</samp> | String |  |  | Valid Values:<br>- cos<br>- dscp<br>- disabled |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_input</samp> | String |  |  |  | Policy-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | TX-Queue ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | UC TX queue ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mc_tx_queues</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | MC TX queue ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps" |

=== "YAML"

    ```yaml
    qos_profiles:
      - name: <str>
        trust: <str>
        cos: <int>
        dscp: <int>
        shape:
          rate: <str>
        service_policy:
          type:
            qos_input: <str>
        tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
        uc_tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
        mc_tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
    ```
## Queue Monitor Length



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>queue_monitor_length</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  | "enabled: true" will be required in AVD4.0.<br>In AVD3.x default is true as long as queue_monitor_length is defined and not None<br> |
    | <samp>&nbsp;&nbsp;log</samp> | Integer |  |  |  | Logging interval in seconds |
    | <samp>&nbsp;&nbsp;notifying</samp> | Boolean |  |  |  | should only be used for platforms supporting the "queue-monitor length notifying" CLI |
    | <samp>&nbsp;&nbsp;cpu</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp> | Integer | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    queue_monitor_length:
      enabled: <bool>
      log: <int>
      notifying: <bool>
      cpu:
        thresholds:
          high: <int>
          low: <int>
    ```
## Queue Monitor Streaming



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>queue_monitor_streaming</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;ip_access_group</samp> | String |  |  |  | Name of IP ACL |
    | <samp>&nbsp;&nbsp;ipv6_access_group</samp> | String |  |  |  | Name of IPv6 ACL |
    | <samp>&nbsp;&nbsp;max_connections</samp> | Integer |  |  | Min: 1<br>Max: 100 |  |
    | <samp>&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    queue_monitor_streaming:
      enable: <bool>
      ip_access_group: <str>
      ipv6_access_group: <str>
      max_connections: <int>
      vrf: <str>
    ```
