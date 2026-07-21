<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ntp_settings</samp>](## "ntp_settings") | Dictionary |  |  |  | NTP settings |
    | [<samp>&nbsp;&nbsp;server_vrf</samp>](## "ntp_settings.server_vrf") | String |  | `use_default_mgmt_method_vrf` |  | EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.<br>- `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF for NTP server(s) and local-interface for NTP depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed. |
    | [<samp>&nbsp;&nbsp;set_first_ntp_server_as_preferred</samp>](## "ntp_settings.set_first_ntp_server_as_preferred") | Boolean |  | `True` |  | If 'true', AVD marks the first entry under 'ntp_settings.servers' as 'preferred'.<br>Set to 'false' to avoid automatically setting any server as 'preferred'. |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "ntp_settings.servers") | List, items: Dictionary |  |  |  | By default, AVD marks the first server as `preferred`.<br>Set 'ntp_settings.set_first_ntp_server_as_preferred: false' to disable this behavior. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ntp_settings.servers.[].name") | String | Required, Unique |  |  | IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp_settings.servers.[].burst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp_settings.servers.[].iburst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp_settings.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp_settings.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp_settings.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp_settings.authenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp_settings.authenticate_servers_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp_settings.authentication_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;key</samp>](## "ntp_settings.authentication_keys.[].key") | String |  |  |  | Authentication provided using the `key_type` format.<br>Will be rendered as such.<br>Takes precedence over `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "ntp_settings.authentication_keys.[].cleartext_key") | String |  |  |  | Cleartext key for the NTP authentication key. Encrypted to Type 7 by AVD.<br>`key_type` does not influence this key.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp_settings.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Key type of the `key`.<br>Does not have any influence on `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "ntp_settings.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp_settings.authentication_keys.[].hash_algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code> |  |
    | [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp_settings.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15. |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  | Clock timezone like "CET" or "US/Pacific". |

=== "YAML"

    ```yaml
    # NTP settings
    ntp_settings:

      # EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.
      # - `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.
      #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
      # - `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.
      #   An error will be raised if inband management is not configured for the device.
      # - `use_default_mgmt_method_vrf` will configure the VRF for NTP server(s) and local-interface for NTP depending on the value of `default_mgmt_method`.
      # - Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.
      server_vrf: <str; default="use_default_mgmt_method_vrf">

      # If 'true', AVD marks the first entry under 'ntp_settings.servers' as 'preferred'.
      # Set to 'false' to avoid automatically setting any server as 'preferred'.
      set_first_ntp_server_as_preferred: <bool; default=True>

      # By default, AVD marks the first server as `preferred`.
      # Set 'ntp_settings.set_first_ntp_server_as_preferred: false' to disable this behavior.
      servers:

          # IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org.
        - name: <str; required; unique>
          burst: <bool>
          iburst: <bool>
          key: <int; 1-65535>

          # Value of maxpoll between 3 - 17 (Logarithmic).
          maxpoll: <int; 3-17>

          # Value of minpoll between 3 - 17 (Logarithmic).
          minpoll: <int; 3-17>
          version: <int; 1-4>
      authenticate: <bool>
      authenticate_servers_only: <bool>
      authentication_keys:

          # Authentication provided using the `key_type` format.
          # Will be rendered as such.
          # Takes precedence over `cleartext_key`.
        - key: <str>

          # Cleartext key for the NTP authentication key. Encrypted to Type 7 by AVD.
          # `key_type` does not influence this key.
          # To protect the password at rest it is strongly recommended to make use of a vault or similar.
          cleartext_key: <str>

          # Key type of the `key`.
          # Does not have any influence on `cleartext_key`.
          key_type: <str; "0" | "7" | "8a">

          # Key identifier.
          id: <int; 1-65534; required; unique>
          hash_algorithm: <str; "md5" | "sha1"; required>

      # List of trusted-keys as string ex. 10-12,15.
      trusted_keys: <str>

    # Clock timezone like "CET" or "US/Pacific".
    timezone: <str>
    ```
