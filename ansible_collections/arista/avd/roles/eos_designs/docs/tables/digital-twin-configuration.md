<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.<br>Global settings to configure the Digital Twin of the Fabric. |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code> | Targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;fabric</samp>](## "digital_twin.fabric") | Dictionary |  |  |  | Global Digital Twin settings related to the configuration of fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "digital_twin.fabric.os_version") | String |  |  |  | Desired Digital Twin OS version for fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ipv4_pool</samp>](## "digital_twin.fabric.mgmt_ipv4_pool") | String |  |  | Format: ipv4_pool | IPv4 address pool to automatically generate MGMT IPv4 addresses for digital twins of the Fabric nodes.<br>Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "digital_twin.fabric.username") | String |  |  |  | Desired Digital Twin username for fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "digital_twin.fabric.password") | String |  |  |  | Desired Digital Twin clear-text password for fabric nodes. |
    | [<samp>&nbsp;&nbsp;endpoints</samp>](## "digital_twin.endpoints") | Dictionary |  |  |  | Global Digital Twin settings related to the configuration of the endpoints. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "digital_twin.endpoints.enabled") | Boolean |  | `False` |  | Setting this flag to `true` will include all `connected_endpoints` in the generated Digital Twin topology data.<br>Specific endpoints may be suppressed by setiing `<connected_endpoints_keys.key>.digital_twin.enabled` to `false`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "digital_twin.endpoints.platform") | String |  | `generic` | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code><br>- <code>generic</code> | Desired Digital Twin virtual platform for endpoints. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "digital_twin.endpoints.os_version") | String |  |  |  | Desired Digital Twin OS version for endpoints. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ipv4_pool</samp>](## "digital_twin.endpoints.mgmt_ipv4_pool") | String |  |  | Format: ipv4_pool | IPv4 address pool to automatically generate MGMT IPv4 addresses for Digital Twin endpoints.<br>Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "digital_twin.endpoints.username") | String |  |  |  | Desired Digital Twin username for endpoints. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "digital_twin.endpoints.password") | String |  |  |  | Desired Digital Twin clear-text password for endpoints. |
    | [<samp>digital_twin_mode</samp>](## "digital_twin_mode") | Boolean |  | `False` |  | PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.<br>Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.). |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.
    # Global settings to configure the Digital Twin of the Fabric.
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act"; default="act">

      # Global Digital Twin settings related to the configuration of fabric nodes.
      fabric:

        # Desired Digital Twin OS version for fabric nodes.
        os_version: <str>

        # IPv4 address pool to automatically generate MGMT IPv4 addresses for digital twins of the Fabric nodes.
        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        mgmt_ipv4_pool: <str>

        # Desired Digital Twin username for fabric nodes.
        username: <str>

        # Desired Digital Twin clear-text password for fabric nodes.
        password: <str>

      # Global Digital Twin settings related to the configuration of the endpoints.
      endpoints:

        # Setting this flag to `true` will include all `connected_endpoints` in the generated Digital Twin topology data.
        # Specific endpoints may be suppressed by setiing `<connected_endpoints_keys.key>.digital_twin.enabled` to `false`.
        enabled: <bool; default=False>

        # Desired Digital Twin virtual platform for endpoints.
        platform: <str; "veos" | "cloudeos" | "generic"; default="generic">

        # Desired Digital Twin OS version for endpoints.
        os_version: <str>

        # IPv4 address pool to automatically generate MGMT IPv4 addresses for Digital Twin endpoints.
        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        mgmt_ipv4_pool: <str>

        # Desired Digital Twin username for endpoints.
        username: <str>

        # Desired Digital Twin clear-text password for endpoints.
        password: <str>

    # PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.
    # Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.).
    digital_twin_mode: <bool; default=False>
    ```
