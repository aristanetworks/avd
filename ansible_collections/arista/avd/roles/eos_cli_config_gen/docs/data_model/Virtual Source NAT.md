---
search:
  boost: 2
---

# Virtual Source NAT
## Virtual Source Nat VRFs



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>virtual_source_nat_vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4 Address |

=== "YAML"

    ```yaml
    virtual_source_nat_vrfs:
      - name: <str>
        ip_address: <str>
    ```
