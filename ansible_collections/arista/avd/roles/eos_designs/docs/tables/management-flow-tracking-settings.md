<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_flow_tracking</samp>](## "fabric_flow_tracking") | Dictionary |  |  |  | Default enabling of flow-tracking(IPFIX) for various interface types across the fabric.<br>Flow Tracking can also be enabled/disabled under each of the specific data models.<br>For general flow-tracking settings see `flow_tracking_settings`. |
    | [<samp>&nbsp;&nbsp;uplinks</samp>](## "fabric_flow_tracking.uplinks") | Dictionary |  |  |  | Enable flow-tracking on all fabric uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.uplinks.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.uplinks.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.uplinks.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;downlinks</samp>](## "fabric_flow_tracking.downlinks") | Dictionary |  |  |  | Enable flow-tracking on all fabric downlinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.downlinks.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.downlinks.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.downlinks.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;endpoints</samp>](## "fabric_flow_tracking.endpoints") | Dictionary |  |  |  | Enable flow-tracking on all endpoints ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.endpoints.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.endpoints.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.endpoints.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;l3_edge</samp>](## "fabric_flow_tracking.l3_edge") | Dictionary |  |  |  | Enable flow-tracking on all p2p_links defined under l3_edge. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.l3_edge.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.l3_edge.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.l3_edge.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;core_interfaces</samp>](## "fabric_flow_tracking.core_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all p2p_links defined under core_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.core_interfaces.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.core_interfaces.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.core_interfaces.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;mlag_interfaces</samp>](## "fabric_flow_tracking.mlag_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all MLAG peer interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.mlag_interfaces.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.mlag_interfaces.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.mlag_interfaces.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;node_l3_interfaces</samp>](## "fabric_flow_tracking.node_l3_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all node.l3_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.node_l3_interfaces.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.node_l3_interfaces.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.node_l3_interfaces.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;tenants_vrfs_l3_interfaces</samp>](## "fabric_flow_tracking.tenants_vrfs_l3_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all tenants.vrfs.l3_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.tenants_vrfs_l3_interfaces.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.tenants_vrfs_l3_interfaces.type") | String |  |  | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.tenants_vrfs_l3_interfaces.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;dps_interfaces</samp>](## "fabric_flow_tracking.dps_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all dps_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.dps_interfaces.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "fabric_flow_tracking.dps_interfaces.type") | String |  | `hardware` | Valid Values:<br>- <code>sampled</code><br>- <code>hardware</code> | Flow tracker type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.dps_interfaces.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |

=== "YAML"

    ```yaml
    # Default enabling of flow-tracking(IPFIX) for various interface types across the fabric.
    # Flow Tracking can also be enabled/disabled under each of the specific data models.
    # For general flow-tracking settings see `flow_tracking_settings`.
    fabric_flow_tracking:

      # Enable flow-tracking on all fabric uplinks.
      uplinks:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all fabric downlinks.
      downlinks:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all endpoints ports.
      endpoints:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all p2p_links defined under l3_edge.
      l3_edge:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all p2p_links defined under core_interfaces.
      core_interfaces:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all MLAG peer interfaces.
      mlag_interfaces:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all node.l3_interfaces
      node_l3_interfaces:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all tenants.vrfs.l3_interfaces
      tenants_vrfs_l3_interfaces:
        enabled: <bool>

        # Flow tracker type.
        type: <str; "sampled" | "hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str>

      # Enable flow-tracking on all dps_interfaces
      dps_interfaces:
        enabled: <bool; default=True>

        # Flow tracker type.
        type: <str; "sampled" | "hardware"; default="hardware">

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">
    ```
