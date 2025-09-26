<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>is_deployed</samp>](## "is_deployed") | Boolean |  | `True` |  | If the device is already deployed in the fabric.<br>When set to false:<br>  - The `cv_deploy` role will not apply configurations to this device.<br>  - Peer interfaces toward this device may be shutdown based on the `shutdown_interfaces_towards_undeployed_peers` setting.<br>  - BGP peerings toward this device may be shutdown based on the `shutdown_bgp_towards_undeployed_peers` setting.<br>  - Validation tests by the `anta_runner` role are automatically skipped for this device. |

=== "YAML"

    ```yaml
    # If the device is already deployed in the fabric.
    # When set to false:
    #   - The `cv_deploy` role will not apply configurations to this device.
    #   - Peer interfaces toward this device may be shutdown based on the `shutdown_interfaces_towards_undeployed_peers` setting.
    #   - BGP peerings toward this device may be shutdown based on the `shutdown_bgp_towards_undeployed_peers` setting.
    #   - Validation tests by the `anta_runner` role are automatically skipped for this device.
    is_deployed: <bool; default=True>
    ```
