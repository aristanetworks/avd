<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>flow_tracking</samp>](## "flow_tracking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sampled</samp>](## "flow_tracking.sampled") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_tracking.sampled.sample") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_offload</samp>](## "flow_tracking.sampled.hardware_offload") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "flow_tracking.sampled.hardware_offload.ipv4") | Boolean |  |  |  | Configure hardware offload for IPv4 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "flow_tracking.sampled.hardware_offload.ipv6") | Boolean |  |  |  | Configure hardware offload for IPv6 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold_minimum</samp>](## "flow_tracking.sampled.hardware_offload.threshold_minimum") | Integer |  |  | Min: 1<br>Max: 4294967295 | Minimum number of samples. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.sampled.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- table_size</samp>](## "flow_tracking.sampled.trackers.[].table_size") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in flow table.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.sampled.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.sampled.trackers.[].record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "flow_tracking.sampled.trackers.[].name") | String | Required, Unique |  |  | Tracker Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.sampled.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.sampled.shutdown") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;hardware</samp>](## "flow_tracking.hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.hardware.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "flow_tracking.hardware.trackers.[].name") | String | Required, Unique |  |  | Tracker Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.hardware.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.hardware.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.hardware.shutdown") | Boolean |  | `False` |  |  |

=== "YAML"

    ```yaml
    flow_tracking:
      sampled:
        sample: <int>
        hardware_offload:
          ipv4: <bool>
          ipv6: <bool>
          threshold_minimum: <int>
        trackers:
          - table_size: <int>
            record_export:
              mpls: <bool>
              on_inactive_timeout: <int>
              on_interval: <int>
            name: <str>
            exporters:
              - name: <str>
                collector:
                  host: <str>
                  port: <int>
                format:
                  ipfix_version: <int>
                local_interface: <str>
                template_interval: <int>
        shutdown: <bool>
      hardware:
        trackers:
          - name: <str>
            record_export:
              on_inactive_timeout: <int>
              on_interval: <int>
            exporters:
              - name: <str>
                collector:
                  host: <str>
                  port: <int>
                format:
                  ipfix_version: <int>
                local_interface: <str>
                template_interval: <int>
        shutdown: <bool>
    ```
