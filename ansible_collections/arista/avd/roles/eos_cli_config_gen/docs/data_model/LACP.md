---
search:
  boost: 2
---

# LACP
## LACP

=== "LACP"

    Set Link Aggregation Control Protocol (LACP) parameters.

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>lacp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;port_id</samp> | Dictionary |  |  |  | LACP port-ID range configuration. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;begin</samp> | Integer |  |  |  | Minimum LACP port-ID range. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp> | Integer |  |  |  | Maximum LACP port-ID range. |
    | <samp>&nbsp;&nbsp;rate_limit</samp> | Dictionary |  |  |  | Set LACPDU rate limit options. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | Boolean |  |  |  | Enable LACPDU rate limiting by default on all ports. |
    | <samp>&nbsp;&nbsp;system_priority</samp> | Integer |  |  | Min: 0<br>Max: 65535 | Set local system LACP priority. |

=== "YAML"

    ```yaml
    lacp:
      port_id:
        range:
          begin: <int>
          end: <int>
      rate_limit:
        default: <bool>
      system_priority: <int>
    ```
