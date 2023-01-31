---
search:
  boost: 2
---

# DHCP Relay

## DHCP Relay

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>dhcp_relay</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;servers</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Server IP or Hostname |
    | <samp>&nbsp;&nbsp;tunnel_requests_disabled</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    dhcp_relay:
      servers:
        - <str>
      tunnel_requests_disabled: <bool>
    ```
