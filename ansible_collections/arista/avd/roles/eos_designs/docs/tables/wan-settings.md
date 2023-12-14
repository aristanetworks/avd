<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_carriers</samp>](## "wan_carriers") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>List of carriers used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_carriers.[].name") | String | Required, Unique |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "wan_carriers.[].description") | String |  |  |  | Additional information about the carrier for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "wan_carriers.[].ipsec") | Boolean |  |  |  | Flag to configure IPsec on the carrier (default is True). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;accessibility</samp>](## "wan_carriers.[].accessibility") | String |  |  | Valid Values:<br>- <code>public</code><br>- <code>private</code> | Indicates if the carrier has access to the Internet (`public`)<br>or not (`private`). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;characteristics</samp>](## "wan_carriers.[].characteristics") | List, items: String |  |  |  | A list of characteristics to assign to the carrier.<br>TODO: Explain further how these are used (or removed before removing preview). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_carriers.[].characteristics.[]") | String |  |  | Valid Values:<br>- <code>backup</code><br>- <code>metered</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;circuit_type</samp>](## "wan_carriers.[].circuit_type") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>both</code> | TBC - edge or transit or both.<br>Unclear if this should be at the carrier level or some other place. |
    | [<samp>wan_ipsec_profiles</samp>](## "wan_ipsec_profiles") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Define IPsec profiles parameters for WAN configuration.<br><br>If `data_plane` is not defined, `control_plane` information is<br>used for both. |
    | [<samp>&nbsp;&nbsp;control_plane</samp>](## "wan_ipsec_profiles.control_plane") | Dictionary | Required |  |  | The `control_plane` profile uses the following defaults:<br>  * IKE policy name: CP-IKE-POLICY<br>  * SA policy name: CP-SA-POLICY<br>  * Profile name: CP-PROFILE |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.control_plane.ike_policy_name") | String |  |  |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.control_plane.sa_policy_name") | String |  |  |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.control_plane.profile_name") | String |  |  |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.control_plane.shared_key") | String | Required |  |  | The IPSec shared key.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;data_plane</samp>](## "wan_ipsec_profiles.data_plane") | Dictionary |  |  |  | The `data_plane` profile uses the following defaults:<br>  * IKE policy name: DP-IKE-POLICY<br>  * SA policy name: DP-SA-POLICY<br>  * Profile name: DP-PROFILE |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.data_plane.ike_policy_name") | String |  |  |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.data_plane.sa_policy_name") | String |  |  |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.data_plane.profile_name") | String |  |  |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.data_plane.shared_key") | String | Required |  |  | The IPSec shared key.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>wan_mode</samp>](## "wan_mode") | String |  |  | Valid Values:<br>- <code>autovpn</code><br>- <code>cv-pathfinder</code> | PREVIEW: This key is currently not supported<br><br>Select if the WAN should be run using CV Pathfinder (`cv-pathfinder`) or Auto VPN only.<br>The default is `cv-pathfinder` |
    | [<samp>wan_route_servers</samp>](## "wan_route_servers") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>List of the AutoVPN RRs when using `wan_mode`=`autovpn`, or the Pathfinders<br>when using `wan_mode`=`cv-pathfinder`, to which the device should connect to.<br><br>When the route server is part of the same inventory as the WAN routers,<br>only the name is required. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "wan_route_servers.[].hostname") | String | Required, Unique |  |  | Route-Reflector hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "wan_route_servers.[].router_id") | String |  |  |  | Route-Reflector router id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_carriers</samp>](## "wan_route_servers.[].wan_carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_route_servers.[].wan_carriers.[].name") | String |  |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "wan_route_servers.[].wan_carriers.[].ip_address") | String |  |  |  | The public IP address for this carrier. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported
    # List of carriers used for the WAN configuration.
    wan_carriers:

        # Carrier name.
      - name: <str; required; unique>

        # Additional information about the carrier for documentation purposes.
        description: <str>

        # Flag to configure IPsec on the carrier (default is True).
        ipsec: <bool>

        # Indicates if the carrier has access to the Internet (`public`)
        # or not (`private`).
        accessibility: <str; "public" | "private">

        # A list of characteristics to assign to the carrier.
        # TODO: Explain further how these are used (or removed before removing preview).
        characteristics:
          - <str; "backup" | "metered">

        # TBC - edge or transit or both.
        # Unclear if this should be at the carrier level or some other place.
        circuit_type: <str; "edge" | "transit" | "both">

    # PREVIEW: This key is currently not supported
    # Define IPsec profiles parameters for WAN configuration.

    # If `data_plane` is not defined, `control_plane` information is
    # used for both.
    wan_ipsec_profiles:

      # The `control_plane` profile uses the following defaults:
      #   * IKE policy name: CP-IKE-POLICY
      #   * SA policy name: CP-SA-POLICY
      #   * Profile name: CP-PROFILE
      control_plane: # required

        # Name of the IKE policy.
        ike_policy_name: <str>

        # Name of the SA policy.
        sa_policy_name: <str>

        # Name of the IPSec profile.
        profile_name: <str>

        # The IPSec shared key.
        # This variable is sensitive and SHOULD be configured using some vault mechanism.
        shared_key: <str; required>

      # The `data_plane` profile uses the following defaults:
      #   * IKE policy name: DP-IKE-POLICY
      #   * SA policy name: DP-SA-POLICY
      #   * Profile name: DP-PROFILE
      data_plane:

        # Name of the IKE policy.
        ike_policy_name: <str>

        # Name of the SA policy.
        sa_policy_name: <str>

        # Name of the IPSec profile.
        profile_name: <str>

        # The IPSec shared key.
        # This variable is sensitive and SHOULD be configured using some vault mechanism.
        shared_key: <str; required>

    # PREVIEW: This key is currently not supported

    # Select if the WAN should be run using CV Pathfinder (`cv-pathfinder`) or Auto VPN only.
    # The default is `cv-pathfinder`
    wan_mode: <str; "autovpn" | "cv-pathfinder">

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
        wan_carriers:

            # Carrier name.
          - name: <str>

            # The public IP address for this carrier.
            ip_address: <str>
    ```
