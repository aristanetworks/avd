---
search:
  boost: 2
---

# MPLS
## MPLS



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;ip</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;ldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp> | String |  |  |  | Interface Name |

=== "YAML"

    ```yaml
    mpls:
      ip: <bool>
      ldp:
        interface_disabled_default: <bool>
        router_id: <str>
        shutdown: <bool>
        transport_address_interface: <str>
    ```
