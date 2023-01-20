---
search:
  boost: 2
---

# Multicast

## IP IGMP Snooping

=== "IP IGMP Snooping"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_igmp_snooping</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;globally_enabled</samp> | Boolean |  | True |  |  |
    | <samp>&nbsp;&nbsp;robustness_variable</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;restart_query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;interface_restart_query</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;fast_leave</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;querier</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp> | String |  |  |  | IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;proxy</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;vlans</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;querier</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp> | String |  |  |  | IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_groups</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxy</samp> | Boolean |  |  |  | Global proxy settings should be enabled before enabling per-vlan |

=== "YAML"

    ```yaml
    ip_igmp_snooping:
      globally_enabled: <bool>
      robustness_variable: <int>
      restart_query_interval: <int>
      interface_restart_query: <int>
      fast_leave: <bool>
      querier:
        enabled: <bool>
        address: <str>
        query_interval: <int>
        max_response_time: <int>
        last_member_query_interval: <int>
        last_member_query_count: <int>
        startup_query_interval: <int>
        startup_query_count: <int>
        version: <int>
      proxy: <bool>
      vlans:
        - id: <int>
          enabled: <bool>
          querier:
            enabled: <bool>
            address: <str>
            query_interval: <int>
            max_response_time: <int>
            last_member_query_interval: <int>
            last_member_query_count: <int>
            startup_query_interval: <int>
            startup_query_count: <int>
            version: <int>
          max_groups: <int>
          fast_leave: <bool>
          proxy: <bool>
    ```

## Router Multicast

=== "Router Multicast"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_multicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_period_decay</samp> | Integer |  |  | Min: 0<br>Max: 600 | Rate in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;routing</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;multipath</samp> | String |  |  | Valid Values:<br>- none<br>- deterministic<br>- deterministic color<br>- deterministic router-id |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;software_forwarding</samp> | String |  |  | Valid Values:<br>- kernel<br>- sfe |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;rpf</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp> | String | Required |  |  | Source address A.B.C.D or Source prefix A.B.C.D/E |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp> | List, items: Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nexthop</samp> | String | Required |  |  | Next-hop IP address or interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp> | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for this route |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_multicast:
      ipv4:
        counters:
          rate_period_decay: <int>
        routing: <bool>
        multipath: <str>
        software_forwarding: <str>
        rpf:
          routes:
            - source_prefix: <str>
              destinations:
                - nexthop: <str>
                  distance: <int>
      vrfs:
        - name: <str>
          ipv4:
            routing: <bool>
    ```

## Router PIM Sparse Mode

=== "Router PIM Sparse Mode"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_pim_sparse_mode</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Boolean |  |  |  | Enable/Disable BFD |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ssm_range</samp> | String |  |  |  | IPv4 Prefix associated with SSM |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp> | String | Required, Unique |  |  | RP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp> | Integer |  |  | Min: 0<br>Max: 32 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;anycast_rps</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp> | String | Required, Unique |  |  | Anycast RP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_anycast_rp_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp> | String | Required, Unique |  |  | Other Anycast RP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register_count</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Boolean |  |  |  | Enable/Disable BFD |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp> | String | Required |  |  | RP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp> | Integer |  |  | Min: 0<br>Max: 32 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_pim_sparse_mode:
      ipv4:
        bfd: <bool>
        ssm_range: <str>
        rp_addresses:
          - address: <str>
            groups:
              - <str>
            access_lists:
              - <str>
            priority: <int>
            hashmask: <int>
            override: <bool>
        anycast_rps:
          - address: <str>
            other_anycast_rp_addresses:
              - address: <str>
                register_count: <int>
      vrfs:
        - name: <str>
          ipv4:
            bfd: <bool>
            rp_addresses:
              - address: <str>
                groups:
                  - <str>
                access_lists:
                  - <str>
                priority: <int>
                hashmask: <int>
                override: <bool>
    ```
