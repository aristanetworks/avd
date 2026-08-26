<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tcam_profiles</samp>](## "tcam_profiles") | List, items: Dictionary |  |  |  | TCAM profile definitions.<br>Only the profile referenced by `platform_settings[].tcam_profile` for the device platform is configured. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "tcam_profiles.[].name") | String | Required, Unique |  |  | Tcam-Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;config</samp>](## "tcam_profiles.[].config") | String |  |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "tcam_profiles.[].source") | String |  |  |  | TCAM profile local source path. Used to read the TCAM profile from a local path existing on the device.<br> |

=== "YAML"

    ```yaml
    # TCAM profile definitions.
    # Only the profile referenced by `platform_settings[].tcam_profile` for the device platform is configured.
    tcam_profiles:

        # Tcam-Profile Name.
      - name: <str; required; unique>

        # TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.
        # Example: "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}"
        config: <str>

        # TCAM profile local source path. Used to read the TCAM profile from a local path existing on the device.
        source: <str>
    ```
