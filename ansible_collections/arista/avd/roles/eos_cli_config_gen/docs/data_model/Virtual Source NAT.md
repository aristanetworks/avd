---
search:
  boost: 2
---

# Virtual Source NAT

## Virtual Source Nat VRFs

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>virtual_source_nat_vrfs</samp>](## "virtual_source_nat_vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "virtual_source_nat_vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "virtual_source_nat_vrfs.[].ip_address") | String |  |  |  | IPv4 Address |

=== "YAML"

    ```yaml
    virtual_source_nat_vrfs:
      - name: <str>
        ip_address: <str>
    ```
