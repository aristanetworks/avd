# Multicast

## IP IGMP Snooping

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_igmp_snooping</samp>](## "ip_igmp_snooping") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;globally_enabled</samp>](## "ip_igmp_snooping.globally_enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;robustness_variable</samp>](## "ip_igmp_snooping.robustness_variable") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;restart_query_interval</samp>](## "ip_igmp_snooping.restart_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;interface_restart_query</samp>](## "ip_igmp_snooping.interface_restart_query") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.proxy") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;vlans</samp>](## "ip_igmp_snooping.vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "ip_igmp_snooping.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.vlans.[].querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.vlans.[].querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.vlans.[].querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.vlans.[].querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_groups</samp>](## "ip_igmp_snooping.vlans.[].max_groups") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.vlans.[].fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.vlans.[].proxy") | Boolean |  |  |  | Global proxy settings should be enabled before enabling per-vlan |

### YAML

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_multicast</samp>](## "router_multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_multicast.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "router_multicast.ipv4.counters") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_period_decay</samp>](## "router_multicast.ipv4.counters.rate_period_decay") | Integer |  |  | Min: 0<br>Max: 600 | Rate in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.ipv4.routing") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multipath</samp>](## "router_multicast.ipv4.multipath") | String |  |  | Valid Values:<br>- none<br>- deterministic<br>- deterministic color<br>- deterministic router-id |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;software_forwarding</samp>](## "router_multicast.ipv4.software_forwarding") | String |  |  | Valid Values:<br>- kernel<br>- sfe |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rpf</samp>](## "router_multicast.ipv4.rpf") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_multicast.ipv4.rpf.routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_multicast.ipv4.rpf.routes.[].source_prefix") | String | Required |  |  | Source address A.B.C.D or Source prefix A.B.C.D/E |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nexthop</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].nexthop") | String | Required |  |  | Next-hop IP address or interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for this route |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_multicast.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_multicast.vrfs.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_multicast.vrfs.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.vrfs.[].ipv4.routing") | Boolean |  |  |  |  |

### YAML

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_pim_sparse_mode</samp>](## "router_pim_sparse_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssm_range</samp>](## "router_pim_sparse_mode.ipv4.ssm_range") | String |  |  |  | IPv4 Prefix associated with SSM |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].address") | String | Required, Unique |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;anycast_rps</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].address") | String | Required, Unique |  |  | Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_anycast_rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].address") | String | Required, Unique |  |  | Other Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register_count</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].register_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_pim_sparse_mode.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_pim_sparse_mode.vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].address") | String | Required |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |

### YAML

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
