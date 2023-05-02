---
search:
  boost: 2
---

# Quality of Service

## QOS Class-maps

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>class_maps</samp>](## "class_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "class_maps.pbr") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.pbr.[].name") | String | Required, Unique |  |  | Class-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.pbr.[].ip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.pbr.[].ip.access_group") | String |  |  |  | Standard Access-List Name |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "class_maps.qos") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.qos.[].name") | String | Required, Unique |  |  | Class-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "class_maps.qos.[].vlan") | Integer |  |  |  | VLAN value(s) or range(s) of VLAN values |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "class_maps.qos.[].cos") | Integer |  |  |  | CoS value(s) or range(s) of CoS values |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.qos.[].ip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ip.access_group") | String |  |  |  | IPv4 Access-List Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "class_maps.qos.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ipv6.access_group") | String |  |  |  | IPv6 Access-List Name |

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
    | [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  |  |

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
    | [<samp>qos</samp>](## "qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;map</samp>](## "qos.map") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos.map.cos") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.cos.[].&lt;str&gt;") | String |  |  |  | Example: "0 1 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos.map.dscp") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.dscp.[].&lt;str&gt;") | String |  |  |  | Example: "8 9 10 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "qos.map.traffic_class") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.traffic_class.[].&lt;str&gt;") | String |  |  |  | Example: "1 to dscp 32"<br> |
    | [<samp>&nbsp;&nbsp;rewrite_dscp</samp>](## "qos.rewrite_dscp") | Boolean |  |  |  |  |

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
    | [<samp>qos_profiles</samp>](## "qos_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "qos_profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "qos_profiles.[].trust") | String |  |  | Valid Values:<br>- cos<br>- dscp<br>- disabled |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos_profiles.[].cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos_profiles.[].dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "qos_profiles.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "qos_profiles.[].service_policy.type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_input</samp>](## "qos_profiles.[].service_policy.type.qos_input") | String |  |  |  | Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "qos_profiles.[].tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "qos_profiles.[].tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Turn on random-detect ecn count<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.units") | String |  |  | Valid Values:<br>- segments<br>- bytes<br>- kbytes<br>- mbytes |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.min") | Integer |  |  |  | Set the random-detect ecn minimum-threshold<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.max") | Integer |  |  |  | Set the random-detect ecn maximum-threshold<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  |  | Set the random-detect ecn max-mark-probability<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  |  | Set the random-detect ecn weight<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "qos_profiles.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | UC TX queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].uc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].uc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].uc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Turn on random-detect ecn count<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- segments<br>- bytes<br>- kbytes<br>- mbytes | Indicate whether values are in kbytes or segments<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.min") | Integer |  |  |  | Set the random-detect ecn minimum-threshold<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.max") | Integer |  |  |  | Set the random-detect ecn maximum-threshold<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  |  | Set the random-detect ecn max-mark-probability<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  |  | Set the random-detect ecn weight<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mc_tx_queues</samp>](## "qos_profiles.[].mc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].mc_tx_queues.[].id") | Integer | Required, Unique |  |  | MC TX queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].mc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].mc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].mc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps" |

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
            random_detect:
              ecn:
                count: <bool>
                threshold:
                  units: <str>
                  min: <int>
                  max: <int>
                  max_probability: <int>
                  weight: <int>
        uc_tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
            random_detect:
              ecn:
                count: <bool>
                threshold:
                  units: <str>
                  min: <int>
                  max: <int>
                  max_probability: <int>
                  weight: <int>
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
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean |  |  |  | "enabled: true" will be required in AVD4.0.<br>In AVD3.x default is true as long as queue_monitor_length is defined and not None<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | should only be used for platforms supporting the "queue-monitor length notifying" CLI |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |

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
    | [<samp>queue_monitor_streaming</samp>](## "queue_monitor_streaming") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "queue_monitor_streaming.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ip_access_group</samp>](## "queue_monitor_streaming.ip_access_group") | String |  |  |  | Name of IP ACL |
    | [<samp>&nbsp;&nbsp;ipv6_access_group</samp>](## "queue_monitor_streaming.ipv6_access_group") | String |  |  |  | Name of IPv6 ACL |
    | [<samp>&nbsp;&nbsp;max_connections</samp>](## "queue_monitor_streaming.max_connections") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "queue_monitor_streaming.vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    queue_monitor_streaming:
      enable: <bool>
      ip_access_group: <str>
      ipv6_access_group: <str>
      max_connections: <int>
      vrf: <str>
    ```
