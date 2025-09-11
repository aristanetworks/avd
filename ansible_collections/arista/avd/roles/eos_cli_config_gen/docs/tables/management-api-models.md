<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_api_models</samp>](## "management_api_models") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;providers</samp>](## "management_api_models.providers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>provider</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_api_models.providers.[].name") | String |  |  | Valid Values:<br>- <code>sysdb</code><br>- <code>smash</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.providers.[].paths") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;path</samp>](## "management_api_models.providers.[].paths.[].path") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.providers.[].paths.[].disabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;provider</samp>](## "management_api_models.provider") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sysdb</samp>](## "management_api_models.provider.sysdb") | Dictionary |  |  |  | Sysdb provider configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled_paths</samp>](## "management_api_models.provider.sysdb.disabled_paths") | List, items: String |  |  |  | List of disabled Sysdb paths for Octa. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_api_models.provider.sysdb.disabled_paths.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;smash</samp>](## "management_api_models.provider.smash") | Dictionary |  |  |  | Smash provider configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.provider.smash.paths") | List, items: Dictionary |  |  |  | List of Smash paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;path</samp>](## "management_api_models.provider.smash.paths.[].path") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.provider.smash.paths.[].disabled") | Boolean |  |  |  | Disabled Smash path for Octa. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;macsec</samp>](## "management_api_models.provider.macsec") | Dictionary |  |  |  | MACsec provider configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "management_api_models.provider.macsec.interfaces") | Boolean |  |  |  | Enable MACsec for interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp>](## "management_api_models.provider.macsec.mka") | Boolean |  |  |  | Enable MKA for MACsec. |

=== "YAML"

    ```yaml
    management_api_models:
      # This key is deprecated.
      # Support will be removed in AVD version 6.0.0.
      # Use `provider` instead.
      providers:
        - name: <str; "sysdb" | "smash">
          paths:
            - path: <str>
              disabled: <bool; default=False>
      provider:

        # Sysdb provider configuration.
        sysdb:

          # List of disabled Sysdb paths for Octa.
          disabled_paths:
            - <str>

        # Smash provider configuration.
        smash:

          # List of Smash paths.
          paths:
            - path: <str; required; unique>

              # Disabled Smash path for Octa.
              disabled: <bool>

        # MACsec provider configuration.
        macsec:

          # Enable MACsec for interfaces.
          interfaces: <bool>

          # Enable MKA for MACsec.
          mka: <bool>
    ```
