<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ssh_settings</samp>](## "ssh_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ssh_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ssh_settings.vrfs.[].name") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ssh_settings.vrfs.[].enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "ssh_settings.vrfs.[].ipv4_acl") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "ssh_settings.vrfs.[].ipv6_acl") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "ssh_settings.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes. |

=== "YAML"

    ```yaml
    ssh_settings:
      vrfs:

          # VRF name.
        - name: <str>
          enabled: <bool; required>
          ipv4_acl: <str>
          ipv6_acl: <str>

      # Idle timeout in minutes.
      idle_timeout: <int; 0-86400>
    ```
