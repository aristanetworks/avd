<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_nat</samp>](## "ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;kernel_buffer_size</samp>](## "ip_nat.kernel_buffer_size") | Integer |  |  | Min: 1<br>Max: 64 | Buffer size in MB |
    | [<samp>&nbsp;&nbsp;pools</samp>](## "ip_nat.pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_nat.pools.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "ip_nat.pools.[].prefix_length") | Integer | Required |  | Min: 16<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ranges</samp>](## "ip_nat.pools.[].ranges") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- first_ip</samp>](## "ip_nat.pools.[].ranges.[].first_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_ip</samp>](## "ip_nat.pools.[].ranges.[].last_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;first_port</samp>](## "ip_nat.pools.[].ranges.[].first_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_port</samp>](## "ip_nat.pools.[].ranges.[].last_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;utilization_log_threshold</samp>](## "ip_nat.pools.[].utilization_log_threshold") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;synchronization</samp>](## "ip_nat.synchronization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "ip_nat.synchronization.description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;expiry_interval</samp>](## "ip_nat.synchronization.expiry_interval") | Integer |  |  | Min: 60<br>Max: 3600 | in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ip_nat.synchronization.local_interface") | String |  |  |  | EOS interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_address</samp>](## "ip_nat.synchronization.peer_address") | String |  |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_range</samp>](## "ip_nat.synchronization.port_range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;first_port</samp>](## "ip_nat.synchronization.port_range.first_port") | Integer |  |  | Min: 1024<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_port</samp>](## "ip_nat.synchronization.port_range.last_port") | Integer |  |  | Min: 1024<br>Max: 65535 | >= first_port |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;split_disabled</samp>](## "ip_nat.synchronization.port_range.split_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ip_nat.synchronization.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;translation</samp>](## "ip_nat.translation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_selection</samp>](## "ip_nat.translation.address_selection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any</samp>](## "ip_nat.translation.address_selection.any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_field_source_ip</samp>](## "ip_nat.translation.address_selection.hash_field_source_ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "ip_nat.translation.counters") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low_mark</samp>](## "ip_nat.translation.low_mark") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;percentage</samp>](## "ip_nat.translation.low_mark.percentage") | Integer |  |  | Min: 1<br>Max: 99 | Used to render 'ip nat translation low-mark <percentage>' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_percentage</samp>](## "ip_nat.translation.low_mark.host_percentage") | Integer |  |  | Min: 1<br>Max: 99 | Used to render 'ip nat translation low-mark <host_percentage> host' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_entries</samp>](## "ip_nat.translation.max_entries") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ip_nat.translation.max_entries.limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_limit</samp>](## "ip_nat.translation.max_entries.host_limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_limits</samp>](## "ip_nat.translation.max_entries.ip_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip</samp>](## "ip_nat.translation.max_entries.ip_limits.[].ip") | String | Required, Unique |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ip_nat.translation.max_entries.ip_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeouts</samp>](## "ip_nat.translation.timeouts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- protocol</samp>](## "ip_nat.translation.timeouts.[].protocol") | String | Required, Unique |  | Valid Values:<br>- tcp<br>- udp |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ip_nat.translation.timeouts.[].timeout") | Integer | Required |  | Min: 0<br>Max: 4294967295 | in seconds |

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
      synchronization:
        description: <str>
        expiry_interval: <int>
        local_interface: <str>
        peer_address: <str>
        port_range:
          first_port: <int>
          last_port: <int>
          split_disabled: <bool>
        shutdown: <bool>
      translation:
        address_selection:
          any: <bool>
          hash_field_source_ip: <bool>
        counters: <bool>
        low_mark:
          percentage: <int>
          host_percentage: <int>
        max_entries:
          limit: <int>
          host_limit: <int>
          ip_limits:
            - ip: <str>
              limit: <int>
        timeouts:
          - protocol: <str>
            timeout: <int>
    ```
