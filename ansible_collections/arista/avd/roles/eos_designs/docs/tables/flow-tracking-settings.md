<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>flow_tracking_settings</samp>](## "flow_tracking_settings") | Dictionary |  |  |  | Define the flow tracking parameters for this topology. |
    | [<samp>&nbsp;&nbsp;flow_tracker_name</samp>](## "flow_tracking_settings.flow_tracker_name") | String |  | `FLOW-TRACKER` |  | Flow Tracker Name |
    | [<samp>&nbsp;&nbsp;record_export</samp>](## "flow_tracking_settings.record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking_settings.record_export.on_inactive_timeout") | Integer |  | `70000` | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking_settings.record_export.on_interval") | Integer |  | `300000` | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
    | [<samp>&nbsp;&nbsp;exporter</samp>](## "flow_tracking_settings.exporter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "flow_tracking_settings.exporter.name") | String |  | `CV-TELEMETRY` |  | Exporter Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking_settings.exporter.template_interval") | Integer |  | `3600000` | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |

=== "YAML"

    ```yaml
    # Define the flow tracking parameters for this topology.
    flow_tracking_settings:

      # Flow Tracker Name
      flow_tracker_name: <str; default="FLOW-TRACKER">
      record_export:

        # Flow record inactive export timeout in milliseconds
        on_inactive_timeout: <int; 3000-900000; default=70000>

        # Flow record export interval in milliseconds
        on_interval: <int; 1000-36000000; default=300000>
      exporter:

        # Exporter Name
        name: <str; default="CV-TELEMETRY">

        # Template interval in milliseconds
        template_interval: <int; 5000-3600000; default=3600000>
    ```
