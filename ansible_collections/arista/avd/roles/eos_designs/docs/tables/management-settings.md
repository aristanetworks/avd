<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_settings</samp>](## "management_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;console</samp>](## "management_settings.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;idle_timeout</samp>](## "management_settings.console.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 |  |
    | [<samp>&nbsp;&nbsp;banners</samp>](## "management_settings.banners") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;login</samp>](## "management_settings.banners.login") | String |  |  |  | Legal notification or security warning displayed to all users before authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;motd</samp>](## "management_settings.banners.motd") | String |  |  |  | Informational or operational message displayed to authorized users after a successful login. |

=== "YAML"

    ```yaml
    management_settings:
      console:
        idle_timeout: <int; 0-86400>
      banners:

        # Legal notification or security warning displayed to all users before authentication.
        login: <str>

        # Informational or operational message displayed to authorized users after a successful login.
        motd: <str>
    ```
