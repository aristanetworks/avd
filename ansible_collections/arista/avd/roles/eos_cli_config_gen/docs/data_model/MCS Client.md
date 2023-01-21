---
search:
  boost: 2
---

# MCS Client
## MCS Client

=== "Table"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mcs_client</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;cvx_secondary</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;server_hosts</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IP or hostname |

=== "YAML"

    ```yaml
    mcs_client:
      shutdown: <bool>
      cvx_secondary:
        name: <str>
        shutdown: <bool>
        server_hosts:
          - <str>
    ```
