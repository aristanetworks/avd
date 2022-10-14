---
search:
  boost: 2
---

# Input Variables

## ISIS Advertise Passive Only

Additional underlay ISIS parameters

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool>
    ```

## ISIS Area ID

Required when "underlay_routing_protocol" == ISIS variants

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |

=== "YAML"

    ```yaml
    isis_area_id: <str>
    ```

## ISIS Default Circuit Type

Fabric vevel variables. These fabric level parameters can be used with core_interfaces running ISIS,
and may be overridden on link profile or link level.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

=== "YAML"

    ```yaml
    isis_default_circuit_type: <str>
    ```

## ISIS Default IS Type

Additional underlay ISIS parameters

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

=== "YAML"

    ```yaml
    isis_default_is_type: <str>
    ```

## ISIS Default Metric

Fabric level variables. These fabric level parameters can be used with core_interfaces running ISIS,
and may be overridden on link profile or link level.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  |  |

=== "YAML"

    ```yaml
    isis_default_metric: <int>
    ```

## ISIS TI LFA

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | 10000 |  | Local convergence delay in mpls |

=== "YAML"

    ```yaml
    isis_ti_lfa:
      enabled: <bool>
      protection: <str>
      local_convergence_delay: <int>
    ```
