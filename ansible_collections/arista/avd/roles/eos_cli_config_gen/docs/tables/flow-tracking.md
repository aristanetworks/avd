<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>flow_tracking</samp>](## "flow_tracking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sampled</samp>](## "flow_tracking.sampled") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "flow_tracking.sampled.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_ipv6</samp>](## "flow_tracking.sampled.encapsulation.ipv4_ipv6") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.sampled.encapsulation.mpls") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_tracking.sampled.sample") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_offload</samp>](## "flow_tracking.sampled.hardware_offload") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "flow_tracking.sampled.hardware_offload.ipv4") | Boolean |  |  |  | Configure hardware offload for IPv4 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "flow_tracking.sampled.hardware_offload.ipv6") | Boolean |  |  |  | Configure hardware offload for IPv6 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold_minimum</samp>](## "flow_tracking.sampled.hardware_offload.threshold_minimum") | Integer |  |  | Min: 1<br>Max: 4294967295 | Minimum number of samples. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.sampled.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;table_size</samp>](## "flow_tracking.sampled.trackers.[].table_size") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in flow table.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.sampled.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.sampled.trackers.[].record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "flow_tracking.sampled.trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.sampled.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>collectors</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collectors</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collectors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collectors.[].host") | String | Required, Unique |  |  | Flow collector name.<br>The collector name can be an IPv4 address, IPv6 address and fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collectors.[].port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.sampled.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hardware</samp>](## "flow_tracking.hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;record</samp>](## "flow_tracking.hardware.record") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format_ipfix_standard_timestamps_counters</samp>](## "flow_tracking.hardware.record.format_ipfix_standard_timestamps_counters") | Boolean |  |  |  | Enable software export of IPFIX data records. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.hardware.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.hardware.trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.hardware.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.hardware.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>collectors</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collectors</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collectors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collectors.[].host") | String | Required, Unique |  |  | Flow collector name.<br>The collector name can be an IPv4 address, IPv6 address and fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collectors.[].port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.hardware.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mirror_on_drop</samp>](## "flow_tracking.mirror_on_drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "flow_tracking.mirror_on_drop.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_ipv6</samp>](## "flow_tracking.mirror_on_drop.encapsulation.ipv4_ipv6") | Boolean |  |  |  | Set IPv4 and IPv6 encapsulations.<br>Both IPv4 and IPv6 encapsulations must be set together. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.mirror_on_drop.encapsulation.mpls") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample_limit</samp>](## "flow_tracking.mirror_on_drop.sample_limit") | Integer |  |  | Min: 1<br>Max: 4294967295 | Limit the number of packets sampled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.mirror_on_drop.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.mirror_on_drop.trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.mirror_on_drop.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.mirror_on_drop.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.mirror_on_drop.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collectors</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].collectors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].collectors.[].host") | String | Required, Unique |  |  | Flow collector name.<br>The collector name can be an IPv4 address, IPv6 address, fully qualified domain name or `"sflow"`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].collectors.[].port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].format") | String |  |  | Valid Values:<br>- <code>sflow</code><br>- <code>drop-report</code> | Configure flow export format. Valid values are platform dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "flow_tracking.mirror_on_drop.trackers.[].exporters.[].dscp") | Integer |  |  | Min: 0<br>Max: 63 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.mirror_on_drop.shutdown") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    flow_tracking:
      sampled:
        encapsulation:
          ipv4_ipv6: <bool>
          mpls: <bool>
        sample: <int; 1-4294967295>
        hardware_offload:

          # Configure hardware offload for IPv4 traffic.
          ipv4: <bool>

          # Configure hardware offload for IPv6 traffic.
          ipv6: <bool>

          # Minimum number of samples.
          threshold_minimum: <int; 1-4294967295>
        trackers:

            # Maximum number of entries in flow table.
          - table_size: <int; 1-614400>
            record_export:

              # Export MPLS forwarding information.
              mpls: <bool>

              # Flow record inactive export timeout in milliseconds.
              on_inactive_timeout: <int; 3000-900000>

              # Flow record export interval in milliseconds.
              on_interval: <int; 1000-36000000>

            # Tracker Name.
            name: <str; required; unique>
            exporters:

                # Exporter Name.
              - name: <str; required; unique>
                # This key is deprecated.
                # Support will be removed in AVD version 6.0.0.
                # Use `collectors` instead.
                collector:

                  # Collector IPv4 address or IPv6 address or fully qualified domain name.
                  host: <str>

                  # Collector Port Number.
                  port: <int; 1-65535>
                collectors:

                    # Flow collector name.
                    # The collector name can be an IPv4 address, IPv6 address and fully qualified domain name.
                  - host: <str; required; unique>

                    # Collector Port Number.
                    port: <int; 1-65535>
                format:
                  ipfix_version: <int>

                # Local Source Interface.
                local_interface: <str>

                # Template interval in milliseconds.
                template_interval: <int; 5000-3600000>
        shutdown: <bool>
      hardware:
        record:

          # Enable software export of IPFIX data records.
          format_ipfix_standard_timestamps_counters: <bool>
        trackers:

            # Tracker Name.
          - name: <str; required; unique>
            record_export:

              # Flow record inactive export timeout in milliseconds.
              on_inactive_timeout: <int; 3000-900000>

              # Flow record export interval in milliseconds.
              on_interval: <int; 1000-36000000>
            exporters:

                # Exporter Name.
              - name: <str; required; unique>
                # This key is deprecated.
                # Support will be removed in AVD version 6.0.0.
                # Use `collectors` instead.
                collector:

                  # Collector IPv4 address or IPv6 address or fully qualified domain name.
                  host: <str>

                  # Collector Port Number.
                  port: <int; 1-65535>
                collectors:

                    # Flow collector name.
                    # The collector name can be an IPv4 address, IPv6 address and fully qualified domain name.
                  - host: <str; required; unique>

                    # Collector Port Number.
                    port: <int; 1-65535>
                format:
                  ipfix_version: <int>

                # Local Source Interface.
                local_interface: <str>

                # Template interval in milliseconds.
                template_interval: <int; 5000-3600000>
        shutdown: <bool>
      mirror_on_drop:
        encapsulation:

          # Set IPv4 and IPv6 encapsulations.
          # Both IPv4 and IPv6 encapsulations must be set together.
          ipv4_ipv6: <bool>
          mpls: <bool>

        # Limit the number of packets sampled.
        sample_limit: <int; 1-4294967295>
        trackers:

            # Tracker Name.
          - name: <str; required; unique>
            record_export:

              # Flow record inactive export timeout in milliseconds.
              on_inactive_timeout: <int; 3000-900000>

              # Flow record export interval in milliseconds.
              on_interval: <int; 1000-36000000>
            exporters:

                # Exporter Name.
              - name: <str; required; unique>
                collectors:

                    # Flow collector name.
                    # The collector name can be an IPv4 address, IPv6 address, fully qualified domain name or `"sflow"`.
                  - host: <str; required; unique>

                    # Collector Port Number.
                    port: <int; 1-65535>

                # Configure flow export format. Valid values are platform dependent.
                format: <str; "sflow" | "drop-report">

                # Local Source Interface.
                local_interface: <str>

                # Template interval in milliseconds.
                template_interval: <int; 5000-3600000>
                dscp: <int; 0-63>
        shutdown: <bool>
    ```
