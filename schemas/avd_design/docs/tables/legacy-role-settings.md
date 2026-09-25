<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_digital_twin_mode</samp>](## "avd_digital_twin_mode") | Boolean |  |  |  | Legacy alias for `eos_designs_digital_twin_mode`. |
    | [<samp>avd_eos_designs_structured_config</samp>](## "avd_eos_designs_structured_config") | Boolean |  |  |  | Legacy alias for `eos_designs_structured_config`. |
    | [<samp>avd_structured_config_file_format</samp>](## "avd_structured_config_file_format") | String |  |  | Valid Values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | Legacy alias for `eos_designs_structured_config_file_format`.<br> |
    | [<samp>avd_vault_id</samp>](## "avd_vault_id") | String |  |  |  | Legacy alias for `eos_designs_vault_id`. |

=== "YAML"

    ```yaml
    # Legacy alias for `eos_designs_digital_twin_mode`.
    avd_digital_twin_mode: <bool>

    # Legacy alias for `eos_designs_structured_config`.
    avd_eos_designs_structured_config: <bool>

    # Legacy alias for `eos_designs_structured_config_file_format`.
    avd_structured_config_file_format: <str; "yml" | "yaml" | "json">

    # Legacy alias for `eos_designs_vault_id`.
    avd_vault_id: <str>
    ```
