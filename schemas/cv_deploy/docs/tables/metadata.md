<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>metadata</samp>](## "metadata") | Dictionary |  |  |  | Metadata from the `eos_designs` role, loaded automatically from structured configs.<br>For standalone usage without `eos_designs`, use the other `cv_deploy` schema keys instead.<br>If both are provided, `metadata` takes precedence. |

=== "YAML"

    ```yaml
    # Metadata from the `eos_designs` role, loaded automatically from structured configs.
    # For standalone usage without `eos_designs`, use the other `cv_deploy` schema keys instead.
    # If both are provided, `metadata` takes precedence.
    metadata: <dict>
    ```
