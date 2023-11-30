<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>autovpn_rrs</samp>](## "autovpn_rrs") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>The AutoVPN RRs information for the WAN.<br><br>When the AutoVPN RR is part of the same inventory as the WAN routers,<br>only the name is required. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "autovpn_rrs.[].hostname") | String | Required, Unique |  |  | Pathfinder hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "autovpn_rrs.[].router_id") | String |  |  |  | Pathfinder router_id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;carriers</samp>](## "autovpn_rrs.[].carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "autovpn_rrs.[].carriers.[].name") | String |  |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "autovpn_rrs.[].carriers.[].ip_address") | String |  |  |  | The Pathfinder public IP address. |
    | [<samp>carriers</samp>](## "carriers") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>List of carriers used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "carriers.[].name") | String | Required, Unique |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "carriers.[].description") | String |  |  |  | Additional information about the carrier for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "carriers.[].ipsec") | Boolean |  |  |  | Flag to configure IPsec on the carrier (default is True). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;accessibility</samp>](## "carriers.[].accessibility") | String |  |  | Valid Values:<br>- <code>public</code><br>- <code>private</code> | Indicates if the carrier has access to the Internet (`public`)<br>or not (`private). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;characteristics</samp>](## "carriers.[].characteristics") | List, items: String |  |  |  | A list of characteristics to assign to the carrier.<br>TODO: Explain further how these are used (or removed before removing preview). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "carriers.[].characteristics.[]") | String |  |  | Valid Values:<br>- <code>backup</code><br>- <code>metered</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;circuit_type</samp>](## "carriers.[].circuit_type") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>transit</code><br>- <code>both.</code> | TBC - edge or transit or both.<br>Unclear if this should be at the carrier level or some other place. |
    | [<samp>sdwan_pathfinders</samp>](## "sdwan_pathfinders") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>The Pathfinder(s) information for the WAN.<br><br>When the pathfinder is part of the same inventory as the WAN routers,<br>only the name is required. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "sdwan_pathfinders.[].hostname") | String | Required, Unique |  |  | Pathfinder hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "sdwan_pathfinders.[].router_id") | String |  |  |  | Pathfinder router_id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;carriers</samp>](## "sdwan_pathfinders.[].carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "sdwan_pathfinders.[].carriers.[].name") | String |  |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "sdwan_pathfinders.[].carriers.[].ip_address") | String |  |  |  | The Pathfinder public IP address. |
    | [<samp>sdwan_region</samp>](## "sdwan_region") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Define the SDWAN region for the device. |
    | [<samp>&nbsp;&nbsp;name</samp>](## "sdwan_region.name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;id</samp>](## "sdwan_region.id") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>sdwan_zone</samp>](## "sdwan_zone") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Define the SDWAN zone for the device. |
    | [<samp>&nbsp;&nbsp;name</samp>](## "sdwan_zone.name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;id</samp>](## "sdwan_zone.id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
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
    | [<samp>wan_mode</samp>](## "wan_mode") | String |  |  | Valid Values:<br>- <code>autovpn</code><br>- <code>sdwan</code> | Select if the WAN should be run using Pathfinder (`sdwan`) or Auto VPN only.<br>The default is `sdwan`<br>PREVIEW: This key is currently not supported |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported
    # The AutoVPN RRs information for the WAN.

    # When the AutoVPN RR is part of the same inventory as the WAN routers,
    # only the name is required.
    autovpn_rrs:

        # Pathfinder hostname.
      - hostname: <str; required; unique>

        # Pathfinder router_id.
        router_id: <str>
        carriers:

            # Carrier name.
          - name: <str>

            # The Pathfinder public IP address.
            ip_address: <str>

    # PREVIEW: This key is currently not supported
    # List of carriers used for the WAN configuration.
    carriers:

        # Carrier name.
      - name: <str; required; unique>

        # Additional information about the carrier for documentation purposes.
        description: <str>

        # Flag to configure IPsec on the carrier (default is True).
        ipsec: <bool>

        # Indicates if the carrier has access to the Internet (`public`)
        # or not (`private).
        accessibility: <str; "public" | "private">

        # A list of characteristics to assign to the carrier.
        # TODO: Explain further how these are used (or removed before removing preview).
        characteristics:
          - <str; "backup" | "metered">

        # TBC - edge or transit or both.
        # Unclear if this should be at the carrier level or some other place.
        circuit_type: <str; "edge" | "transit" | "both.">

    # PREVIEW: This key is currently not supported
    # The Pathfinder(s) information for the WAN.

    # When the pathfinder is part of the same inventory as the WAN routers,
    # only the name is required.
    sdwan_pathfinders:

        # Pathfinder hostname.
      - hostname: <str; required; unique>

        # Pathfinder router_id.
        router_id: <str>
        carriers:

            # Carrier name.
          - name: <str>

            # The Pathfinder public IP address.
            ip_address: <str>

    # PREVIEW: This key is currently not supported
    # Define the SDWAN region for the device.
    sdwan_region:
      name: <str; required>
      id: <int; 1-255; required>

    # PREVIEW: This key is currently not supported
    # Define the SDWAN zone for the device.
    sdwan_zone:
      name: <str; required>
      id: <int; 1-10000; required>

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

    # Select if the WAN should be run using Pathfinder (`sdwan`) or Auto VPN only.
    # The default is `sdwan`
    # PREVIEW: This key is currently not supported
    wan_mode: <str; "autovpn" | "sdwan">
    ```
