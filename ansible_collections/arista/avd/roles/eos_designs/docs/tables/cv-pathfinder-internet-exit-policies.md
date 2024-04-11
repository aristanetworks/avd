<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_pathfinder_internet_exit_policies</samp>](## "cv_pathfinder_internet_exit_policies") | List, items: Dictionary |  |  |  | PREVIEW: These keys are in preview mode.<br><br>List of internet-exit policies used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_internet_exit_policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "cv_pathfinder_internet_exit_policies.[].type") | String | Required |  | Valid Values:<br>- <code>zscaler</code> | Internet-exit policy type.<br>Only Zscaler supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fallback_to_system_default</samp>](## "cv_pathfinder_internet_exit_policies.[].fallback_to_system_default") | Boolean |  | `True` |  | Add system default exit-group at the end of the policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;zscaler</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler") | Dictionary |  |  |  | Zscaler information. Only used if `type` is 'zscaler'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec_key</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.ipsec_key") | String | Required |  |  | Encryption key used for IPsec tunnels to Zscaler. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;download_bandwidth</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.download_bandwidth") | Integer |  |  |  | Maximum allowed download bandwidth in Mbps for each device using this policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload_bandwidth</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.upload_bandwidth") | Integer |  |  |  | Maximum allowed upload bandwidth in Mbps for each device using this policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firewall</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall.enabled") | Boolean |  | `False` |  | Enforce firewall controls. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ips</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall.ips") | Boolean |  | `False` |  | Enable IPS Controls for the firewall. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acceptable_use_policy</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.acceptable_use_policy") | Boolean |  | `False` |  | Display an Acceptable Use Policy (AUP) and require users to accept it. |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # List of internet-exit policies used for the WAN configuration.
    cv_pathfinder_internet_exit_policies:

        # Internet-exit policy name.
      - name: <str; required; unique>

        # Internet-exit policy type.
        # Only Zscaler supported.
        type: <str; "zscaler"; required>

        # Add system default exit-group at the end of the policy.
        fallback_to_system_default: <bool; default=True>

        # Zscaler information. Only used if `type` is 'zscaler'.
        zscaler:

          # Encryption key used for IPsec tunnels to Zscaler.
          ipsec_key: <str; required>

          # Maximum allowed download bandwidth in Mbps for each device using this policy.
          download_bandwidth: <int>

          # Maximum allowed upload bandwidth in Mbps for each device using this policy.
          upload_bandwidth: <int>
          firewall:

            # Enforce firewall controls.
            enabled: <bool; default=False>

            # Enable IPS Controls for the firewall.
            ips: <bool; default=False>

          # Display an Acceptable Use Policy (AUP) and require users to accept it.
          acceptable_use_policy: <bool; default=False>
    ```
