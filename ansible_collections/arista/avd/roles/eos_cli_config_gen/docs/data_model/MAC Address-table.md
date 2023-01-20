---
search:
  boost: 2
---

# MAC Address-table

## MAC Address Table

=== "MAC Address Table"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mac_address_table</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;aging_time</samp> | Integer |  |  |  | Aging time in seconds |
    | <samp>&nbsp;&nbsp;notification_host_flap</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp> | Integer |  |  | Min: 2<br>Max: 300 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp> | Integer |  |  | Min: 2<br>Max: 10 |  |

=== "YAML"

    ```yaml
    mac_address_table:
      aging_time: <int>
      notification_host_flap:
        logging: <bool>
        detection:
          window: <int>
          moves: <int>
    ```
