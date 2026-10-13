<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>inband_ztp_bootstrap_file</samp>](## "inband_ztp_bootstrap_file") | String |  |  |  | Bootstrap URL configured in DHCP to use for inband ZTP.<br>By default the URL will be `https://<first cv server>/ztp/bootstrap` if `cv_settings` are used.<br>Otherwise no value will be configured. |

=== "YAML"

    ```yaml
    # Bootstrap URL configured in DHCP to use for inband ZTP.
    # By default the URL will be `https://<first cv server>/ztp/bootstrap` if `cv_settings` are used.
    # Otherwise no value will be configured.
    inband_ztp_bootstrap_file: <str>
    ```
