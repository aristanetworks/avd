<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_version</samp>](## "avd_version") | String |  |  | Pattern: `[0-9]+\.[0-9]+\.[0-9]+` | Opt in to future behaviors introduced in the selected AVD release or earlier.<br>Specify a version string in major.minor.patch format, for example "6.5.0".<br>Sets defaults for `avd_design_future` and `eos_config_future` flags available in the installed AVD version.<br>Explicit values for individual flags take precedence, including `false`.<br>Flags introduced after the selected version retain their existing defaults.<br>When omitted, future behavior defaults are unchanged. |

=== "YAML"

    ```yaml
    # Opt in to future behaviors introduced in the selected AVD release or earlier.
    # Specify a version string in major.minor.patch format, for example "6.5.0".
    # Sets defaults for `avd_design_future` and `eos_config_future` flags available in the installed AVD version.
    # Explicit values for individual flags take precedence, including `false`.
    # Flags introduced after the selected version retain their existing defaults.
    # When omitted, future behavior defaults are unchanged.
    avd_version: <str>
    ```
