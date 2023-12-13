<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  | Define Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`node_type_keys` should be defined in top level group_var for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_wan_role</samp>](## "node_type_keys.[].default_wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | PREVIEW: This key is currently not supported<br>Set the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_cv_pathfinder_role</samp>](## "node_type_keys.[].default_cv_pathfinder_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit region</code><br>- <code>pathfinder</code> | PREVIEW: This key is currently not supported<br>Set the default CV Pathfinder role.<br><br>This key is used for Pathfinder designs only when the `wan_mode` root<br>key is set to `cv-pathfinder`.<br><br>`pathfinder` is only a valid if `wan_role` is `server`.<br>`edge` and `transit` are only valid if `wan_role` is `client`.<br> |

=== "YAML"

    ```yaml
    # Define Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `node_type_keys` should be defined in top level group_var for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    node_type_keys:
      - key: <str; required; unique>

        # PREVIEW: This key is currently not supported
        # Set the default WAN role.

        # This is used both for AutoVPN and Pathfinder designs.
        # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
        # `server` indicates that the router is a route-reflector.

        # Only supported if `overlay_routing_protocol` is set to `ibgp`.
        default_wan_role: <str; "client" | "server">

        # PREVIEW: This key is currently not supported
        # Set the default CV Pathfinder role.

        # This key is used for Pathfinder designs only when the `wan_mode` root
        # key is set to `cv-pathfinder`.

        # `pathfinder` is only a valid if `wan_role` is `server`.
        # `edge` and `transit` are only valid if `wan_role` is `client`.
        default_cv_pathfinder_role: <str; "edge" | "transit region" | "pathfinder">
    ```
