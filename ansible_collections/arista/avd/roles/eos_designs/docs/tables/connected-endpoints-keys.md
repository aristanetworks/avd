<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_connected_endpoints_keys</samp>](## "custom_connected_endpoints_keys") | List, items: Dictionary |  |  |  | Use this setting to specify values for `connected_endpoints_keys` in addition to the default ones.<br>This method preserves the default values while adding the new keys. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "custom_connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "custom_connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "custom_connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  | See (+) on YAML tab |  | Endpoints connecting to the fabric can be grouped by using separate keys.<br>The keys can be customized to provide a better organization or grouping of your data.<br>`connected_endpoints_keys` should be defined in the top level group_vars for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them or utilize the `custom_connected_endpoints_keys` key,<br>which serves to augment rather than replace the default configuration.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |

=== "YAML"

    ```yaml
    # Use this setting to specify values for `connected_endpoints_keys` in addition to the default ones.
    # This method preserves the default values while adding the new keys.
    custom_connected_endpoints_keys:
      - key: <str; required; unique>

        # Type used for documentation.
        type: <str>

        # Description used for documentation.
        description: <str>

    # Endpoints connecting to the fabric can be grouped by using separate keys.
    # The keys can be customized to provide a better organization or grouping of your data.
    # `connected_endpoints_keys` should be defined in the top level group_vars for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them or utilize the `custom_connected_endpoints_keys` key,
    # which serves to augment rather than replace the default configuration.
    connected_endpoints_keys: # (1)!
      - key: <str; required; unique>

        # Type used for documentation.
        type: <str>

        # Description used for documentation.
        description: <str>
    ```

    1. Default Value

        ```yaml
        connected_endpoints_keys:
        - description: Server
          key: servers
          type: server
        - description: Firewall
          key: firewalls
          type: firewall
        - description: Router
          key: routers
          type: router
        - description: Load Balancer
          key: load_balancers
          type: load_balancer
        - description: Storage Array
          key: storage_arrays
          type: storage_array
        - description: CPE
          key: cpes
          type: cpe
        - description: Workstation
          key: workstations
          type: workstation
        - description: Access Point
          key: access_points
          type: access_point
        - description: Phone
          key: phones
          type: phone
        - description: Printer
          key: printers
          type: printer
        - description: Camera
          key: cameras
          type: camera
        - description: Generic Device
          key: generic_devices
          type: generic_device
        ```
