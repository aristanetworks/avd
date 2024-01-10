<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_ipsec_profiles</samp>](## "wan_ipsec_profiles") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>Define IPsec profiles parameters for WAN configuration. |
    | [<samp>&nbsp;&nbsp;control_plane</samp>](## "wan_ipsec_profiles.control_plane") | Dictionary | Required |  |  | PREVIEW: This key is currently not supported |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.control_plane.ike_policy_name") | String |  | `CP-IKE-POLICY` |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.control_plane.sa_policy_name") | String |  | `CP-SA-POLICY` |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.control_plane.profile_name") | String |  | `CP-PROFILE` |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.control_plane.shared_key") | String | Required |  |  | The IPSec shared key.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;data_plane</samp>](## "wan_ipsec_profiles.data_plane") | Dictionary |  |  |  | If `data_plane` is not defined, `control_plane` information is used for both. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.data_plane.ike_policy_name") | String |  | `DP-IKE-POLICY` |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.data_plane.sa_policy_name") | String |  | `DP-SA-POLICY` |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.data_plane.profile_name") | String |  | `DP-PROFILE` |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.data_plane.shared_key") | String | Required |  |  | The type 7 encrypted IPSec shared key.<br>This variable is sensitive and should be configured using some vault mechanism. |
    | [<samp>wan_mode</samp>](## "wan_mode") | String |  | `cv-pathfinder` | Valid Values:<br>- <code>autovpn</code><br>- <code>cv-pathfinder</code> | PREVIEW: This key is currently not supported<br><br>Select if the WAN should be run using CV Pathfinder or Auto VPN only. |
    | [<samp>wan_route_servers</samp>](## "wan_route_servers") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>List of the AutoVPN RRs when using `wan_mode`=`autovpn`, or the Pathfinders<br>when using `wan_mode`=`cv-pathfinder`, to which the device should connect to.<br><br>When the route server is part of the same inventory as the WAN routers,<br>only the name is required. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "wan_route_servers.[].hostname") | String | Required, Unique |  |  | Route-Reflector hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "wan_route_servers.[].router_id") | String |  |  |  | Route-Reflector router id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_route_servers.[].path_groups") | List, items: Dictionary |  |  |  | Path-groups through which the Route Reflector/Pathfinder is reached. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_route_servers.[].path_groups.[].name") | String | Required, Unique |  |  | Path-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "wan_route_servers.[].path_groups.[].interfaces") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_route_servers.[].path_groups.[].interfaces.[].name") | String | Required, Unique |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "wan_route_servers.[].path_groups.[].interfaces.[].ip_address") | String |  |  |  | The public IP address of the Route Reflector for this path-group. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported

    # Define IPsec profiles parameters for WAN configuration.
    wan_ipsec_profiles:

      # PREVIEW: This key is currently not supported
      control_plane: # required

        # Name of the IKE policy.
        ike_policy_name: <str; default="CP-IKE-POLICY">

        # Name of the SA policy.
        sa_policy_name: <str; default="CP-SA-POLICY">

        # Name of the IPSec profile.
        profile_name: <str; default="CP-PROFILE">

        # The IPSec shared key.
        # This variable is sensitive and SHOULD be configured using some vault mechanism.
        shared_key: <str; required>

      # If `data_plane` is not defined, `control_plane` information is used for both.
      data_plane:

        # Name of the IKE policy.
        ike_policy_name: <str; default="DP-IKE-POLICY">

        # Name of the SA policy.
        sa_policy_name: <str; default="DP-SA-POLICY">

        # Name of the IPSec profile.
        profile_name: <str; default="DP-PROFILE">

        # The type 7 encrypted IPSec shared key.
        # This variable is sensitive and should be configured using some vault mechanism.
        shared_key: <str; required>

    # PREVIEW: This key is currently not supported

    # Select if the WAN should be run using CV Pathfinder or Auto VPN only.
    wan_mode: <str; "autovpn" | "cv-pathfinder"; default="cv-pathfinder">

    # PREVIEW: This key is currently not supported

    # List of the AutoVPN RRs when using `wan_mode`=`autovpn`, or the Pathfinders
    # when using `wan_mode`=`cv-pathfinder`, to which the device should connect to.

    # When the route server is part of the same inventory as the WAN routers,
    # only the name is required.
    wan_route_servers:

        # Route-Reflector hostname.
      - hostname: <str; required; unique>

        # Route-Reflector router id.
        router_id: <str>

        # Path-groups through which the Route Reflector/Pathfinder is reached.
        path_groups:

            # Path-group name.
          - name: <str; required; unique>
            interfaces: # >=1 items; required

                # Interface name.
              - name: <str; required; unique>

                # The public IP address of the Route Reflector for this path-group.
                ip_address: <str>
    ```
