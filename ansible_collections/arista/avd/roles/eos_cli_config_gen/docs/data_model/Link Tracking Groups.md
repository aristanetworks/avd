---
search:
  boost: 2
---

# Link Tracking Groups
## Link Tracking Groups



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>link_tracking_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp> | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp> | Integer |  |  | Min: 0<br>Max: 3600 |  |

=== "YAML"

    ```yaml
    link_tracking_groups:
      - name: <str>
        links_minimum: <int>
        recovery_delay: <int>
    ```
