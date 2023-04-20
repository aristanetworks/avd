---
search:
  boost: 2
---

# IP NAT.md

## IP Nat

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_nat</samp>](## "ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;kernel_buffer_size</samp>](## "ip_nat.kernel_buffer_size") | Integer |  |  | Min: 1<br>Max: 64 |  |
    | [<samp>&nbsp;&nbsp;pools</samp>](## "ip_nat.pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_nat.pools.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "ip_nat.pools.[].prefix_length") | Integer | Required |  | Min: 16<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ranges</samp>](## "ip_nat.pools.[].ranges") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- first_ip</samp>](## "ip_nat.pools.[].ranges.[].first_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_ip</samp>](## "ip_nat.pools.[].ranges.[].last_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;first_port</samp>](## "ip_nat.pools.[].ranges.[].first_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_port</samp>](## "ip_nat.pools.[].ranges.[].last_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;utilization_log_threshold</samp>](## "ip_nat.pools.[].utilization_log_threshold") | Integer |  |  | Min: 1<br>Max: 100 |  |

=== "YAML"

    ```yaml
    ip_nat:
      kernel_buffer_size: <int>
      pools:
        - name: <str>
          prefix_length: <int>
          ranges:
            - first_ip: <str>
              last_ip: <str>
              first_port: <int>
              last_port: <int>
          utilization_log_threshold: <int>
    ```
