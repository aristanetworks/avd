<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_connected_endpoints_keys</samp>](## "custom_connected_endpoints_keys") | List, items: Dictionary |  |  |  | `custom_connected_endpoints_keys` offers a flexible way to extend endpoint definitions without altering the `connected_endpoints_keys`.<br>The values defined in `custom_connected_endpoints_keys`, are prepended to the ones in `connected_endpoint_keys`, taking precedence over any values in `connected_endpoint_keys`.<br>This approach helps preserving the default `connected_endpoints_keys`, unlike directly overriding it. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "custom_connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "custom_connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "custom_connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  | See (+) on YAML tab |  | Endpoints connecting to the fabric can be grouped by using separate keys.<br>The keys can be customized to provide a better organization or grouping of your data.<br>`connected_endpoints_keys` should be defined in the top level group_vars for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.<br>If you need to add custom `connected_endpoints_keys`, create them under `custom_connected_endpoints_keys`.<br>Entries under `custom_connected_endpoint_keys` will take precedence over entries in `connected_endpoint_keys`.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |

=== "YAML"

    ```yaml
    # `custom_connected_endpoints_keys` offers a flexible way to extend endpoint definitions without altering the `connected_endpoints_keys`.
    # The values defined in `custom_connected_endpoints_keys`, are prepended to the ones in `connected_endpoint_keys`, taking precedence over any values in `connected_endpoint_keys`.
    # This approach helps preserving the default `connected_endpoints_keys`, unlike directly overriding it.
    custom_connected_endpoints_keys:
      - key: <str; required; unique>

        # Type used for documentation.
        type: <str>

        # Description used for documentation.
        description: <str>

    # Endpoints connecting to the fabric can be grouped by using separate keys.
    # The keys can be customized to provide a better organization or grouping of your data.
    # `connected_endpoints_keys` should be defined in the top level group_vars for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    # If you need to add custom `connected_endpoints_keys`, create them under `custom_connected_endpoints_keys`.
    # Entries under `custom_connected_endpoint_keys` will take precedence over entries in `connected_endpoint_keys`.
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
        - key: servers
          type: server
          description: Server
        - key: firewalls
          type: firewall
          description: Firewall
        - key: routers
          type: router
          description: Router
        - key: load_balancers
          type: load_balancer
          description: Load Balancer
        - key: storage_arrays
          type: storage_array
          description: Storage Array
        - key: cpes
          type: cpe
          description: CPE
        - key: workstations
          type: workstation
          description: Workstation
        - key: access_points
          type: access_point
          description: Access Point
        - key: phones
          type: phone
          description: Phone
        - key: printers
          type: printer
          description: Printer
        - key: cameras
          type: camera
          description: Camera
        - key: generic_devices
          type: generic_device
          description: Generic Device
        ```
