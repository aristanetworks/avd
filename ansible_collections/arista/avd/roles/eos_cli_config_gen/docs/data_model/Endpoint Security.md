---
search:
  boost: 2
---

# Endpoint Security
## Global 802.1x Authentication

=== "Global 802.1x Authentication"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>dot1x</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;system_auth_control</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;protocol_lldp_bypass</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;dynamic_authorization</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    dot1x:
      system_auth_control: <bool>
      protocol_lldp_bypass: <bool>
      dynamic_authorization: <bool>
    ```
