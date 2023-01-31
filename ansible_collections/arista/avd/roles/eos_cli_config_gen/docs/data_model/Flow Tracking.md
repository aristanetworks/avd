---
search:
  boost: 2
---

# Flow Tracking

## Flow Trackings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>flow_trackings</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- type</samp> | String | Required, Unique |  | Valid Values:<br>- sampled | Flow Tracking Type - only 'sampled' supported for now |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp> | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Tracker Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp> | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp> | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Boolean |  |  |  | Export MPLS forwarding information |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Exporter Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp> | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp> | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | String |  |  |  | Local Source Interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp> | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    flow_trackings:
      - type: <str>
        sample: <int>
        trackers:
          - name: <str>
            record_export:
              on_inactive_timeout: <int>
              on_interval: <int>
              mpls: <bool>
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
