<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.defaults.dps_mss_ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | MSS value for IPv4 the DPS interface.<br>If not set, and the device is WAN device, a default value of 1000 is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv6</samp>](## "<node_type_keys.key>.defaults.dps_mss_ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | MSS value for IPv6 the DPS interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.defaults.wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | PREVIEW: This key is currently not supported<br>Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_role</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>pathfinder</code> | PREVIEW: This key is currently not supported<br>Override the default CV Pathfinder role.<br><br>This key is used for Pathfinder designs only when the `wan_mode` root<br>key is set to `cv_pathfinder`.<br><br>`pathfinder` is only a valid if `wan_role` is `server`.<br>`edge` and `transit` are only valid if `wan_role` is `client`. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].dps_mss_ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | MSS value for IPv4 the DPS interface.<br>If not set, and the device is WAN device, a default value of 1000 is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv6</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].dps_mss_ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | MSS value for IPv6 the DPS interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | PREVIEW: This key is currently not supported<br>Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>pathfinder</code> | PREVIEW: This key is currently not supported<br>Override the default CV Pathfinder role.<br><br>This key is used for Pathfinder designs only when the `wan_mode` root<br>key is set to `cv_pathfinder`.<br><br>`pathfinder` is only a valid if `wan_role` is `server`.<br>`edge` and `transit` are only valid if `wan_role` is `client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.node_groups.[].dps_mss_ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | MSS value for IPv4 the DPS interface.<br>If not set, and the device is WAN device, a default value of 1000 is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv6</samp>](## "<node_type_keys.key>.node_groups.[].dps_mss_ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | MSS value for IPv6 the DPS interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.node_groups.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | PREVIEW: This key is currently not supported<br>Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_role</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>pathfinder</code> | PREVIEW: This key is currently not supported<br>Override the default CV Pathfinder role.<br><br>This key is used for Pathfinder designs only when the `wan_mode` root<br>key is set to `cv_pathfinder`.<br><br>`pathfinder` is only a valid if `wan_role` is `server`.<br>`edge` and `transit` are only valid if `wan_role` is `client`. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.nodes.[].dps_mss_ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | MSS value for IPv4 the DPS interface.<br>If not set, and the device is WAN device, a default value of 1000 is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv6</samp>](## "<node_type_keys.key>.nodes.[].dps_mss_ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | MSS value for IPv6 the DPS interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.nodes.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | PREVIEW: This key is currently not supported<br>Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_role</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>pathfinder</code> | PREVIEW: This key is currently not supported<br>Override the default CV Pathfinder role.<br><br>This key is used for Pathfinder designs only when the `wan_mode` root<br>key is set to `cv_pathfinder`.<br><br>`pathfinder` is only a valid if `wan_role` is `server`.<br>`edge` and `transit` are only valid if `wan_role` is `client`. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # The CV Pathfinder region name.
        cv_pathfinder_region: <str>

        # The CV Pathfinder site name.
        cv_pathfinder_site: <str>

        # MSS value for IPv4 the DPS interface.
        # If not set, and the device is WAN device, a default value of 1000 is used.
        dps_mss_ipv4: <int; 64-65495>

        # MSS value for IPv6 the DPS interface.
        dps_mss_ipv6: <int; 64-65475>

        # PREVIEW: This key is currently not supported
        # Override the default WAN role.

        # This is used both for AutoVPN and Pathfinder designs.
        # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
        # `server` indicates that the router is a route-reflector.

        # Only supported if `overlay_routing_protocol` is set to `ibgp`.
        wan_role: <str; "client" | "server">

        # PREVIEW: This key is currently not supported
        # Override the default CV Pathfinder role.

        # This key is used for Pathfinder designs only when the `wan_mode` root
        # key is set to `cv_pathfinder`.

        # `pathfinder` is only a valid if `wan_role` is `server`.
        # `edge` and `transit` are only valid if `wan_role` is `client`.
        cv_pathfinder_role: <str; "edge" | "transit" | "pathfinder">

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # The CV Pathfinder region name.
              cv_pathfinder_region: <str>

              # The CV Pathfinder site name.
              cv_pathfinder_site: <str>

              # MSS value for IPv4 the DPS interface.
              # If not set, and the device is WAN device, a default value of 1000 is used.
              dps_mss_ipv4: <int; 64-65495>

              # MSS value for IPv6 the DPS interface.
              dps_mss_ipv6: <int; 64-65475>

              # PREVIEW: This key is currently not supported
              # Override the default WAN role.

              # This is used both for AutoVPN and Pathfinder designs.
              # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
              # `server` indicates that the router is a route-reflector.

              # Only supported if `overlay_routing_protocol` is set to `ibgp`.
              wan_role: <str; "client" | "server">

              # PREVIEW: This key is currently not supported
              # Override the default CV Pathfinder role.

              # This key is used for Pathfinder designs only when the `wan_mode` root
              # key is set to `cv_pathfinder`.

              # `pathfinder` is only a valid if `wan_role` is `server`.
              # `edge` and `transit` are only valid if `wan_role` is `client`.
              cv_pathfinder_role: <str; "edge" | "transit" | "pathfinder">

          # The CV Pathfinder region name.
          cv_pathfinder_region: <str>

          # The CV Pathfinder site name.
          cv_pathfinder_site: <str>

          # MSS value for IPv4 the DPS interface.
          # If not set, and the device is WAN device, a default value of 1000 is used.
          dps_mss_ipv4: <int; 64-65495>

          # MSS value for IPv6 the DPS interface.
          dps_mss_ipv6: <int; 64-65475>

          # PREVIEW: This key is currently not supported
          # Override the default WAN role.

          # This is used both for AutoVPN and Pathfinder designs.
          # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
          # `server` indicates that the router is a route-reflector.

          # Only supported if `overlay_routing_protocol` is set to `ibgp`.
          wan_role: <str; "client" | "server">

          # PREVIEW: This key is currently not supported
          # Override the default CV Pathfinder role.

          # This key is used for Pathfinder designs only when the `wan_mode` root
          # key is set to `cv_pathfinder`.

          # `pathfinder` is only a valid if `wan_role` is `server`.
          # `edge` and `transit` are only valid if `wan_role` is `client`.
          cv_pathfinder_role: <str; "edge" | "transit" | "pathfinder">

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # The CV Pathfinder region name.
          cv_pathfinder_region: <str>

          # The CV Pathfinder site name.
          cv_pathfinder_site: <str>

          # MSS value for IPv4 the DPS interface.
          # If not set, and the device is WAN device, a default value of 1000 is used.
          dps_mss_ipv4: <int; 64-65495>

          # MSS value for IPv6 the DPS interface.
          dps_mss_ipv6: <int; 64-65475>

          # PREVIEW: This key is currently not supported
          # Override the default WAN role.

          # This is used both for AutoVPN and Pathfinder designs.
          # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
          # `server` indicates that the router is a route-reflector.

          # Only supported if `overlay_routing_protocol` is set to `ibgp`.
          wan_role: <str; "client" | "server">

          # PREVIEW: This key is currently not supported
          # Override the default CV Pathfinder role.

          # This key is used for Pathfinder designs only when the `wan_mode` root
          # key is set to `cv_pathfinder`.

          # `pathfinder` is only a valid if `wan_role` is `server`.
          # `edge` and `transit` are only valid if `wan_role` is `client`.
          cv_pathfinder_role: <str; "edge" | "transit" | "pathfinder">
    ```
