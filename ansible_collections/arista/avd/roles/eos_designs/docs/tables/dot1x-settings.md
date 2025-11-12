<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x_settings</samp>](## "dot1x_settings") | Dictionary |  |  |  | Settings for 802.1X deployments. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.enabled") | Boolean |  | `False` |  | Globally enable 802.1X port authentication on the switch.<br>This must be `true` for 802.1X to be active on any interface.<br>When `true`, `dot1x_settings.radius_groups` is required. |
    | [<samp>&nbsp;&nbsp;radius_groups</samp>](## "dot1x_settings.radius_groups") | List, items: String |  |  |  | List of RADIUS server groups to be used for 802.1X authentication and accounting.<br>The order of the list defines the priority. Each group name must also be defined on at least one server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.radius_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;bypass_bpdu</samp>](## "dot1x_settings.bypass_bpdu") | Boolean |  | `True` |  | Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection. |
    | [<samp>&nbsp;&nbsp;bypass_lldp</samp>](## "dot1x_settings.bypass_lldp") | Boolean |  | `True` |  | Allow LLDP packets to be processed even if the port is not authenticated. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x_settings.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.dynamic_authorization.enabled") | Boolean |  | `True` |  | Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session. |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x_settings.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username_delimiter</samp>](## "dot1x_settings.mac_based_authentication.username_delimiter") | String |  | `none` | Valid Values:<br>- <code>colon</code><br>- <code>hyphen</code><br>- <code>none</code><br>- <code>period</code> | RADIUS User-Name attribute delimiter to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username_letter_case</samp>](## "dot1x_settings.mac_based_authentication.username_letter_case") | String |  | `lowercase` | Valid Values:<br>- <code>lowercase</code><br>- <code>uppercase</code> | RADIUS User-Name attribute letter case to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;redistribute_in_evpn</samp>](## "dot1x_settings.redistribute_in_evpn") | Boolean |  | `True` |  | Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs. |

=== "YAML"

    ```yaml
    # Settings for 802.1X deployments.
    dot1x_settings:

      # Globally enable 802.1X port authentication on the switch.
      # This must be `true` for 802.1X to be active on any interface.
      # When `true`, `dot1x_settings.radius_groups` is required.
      enabled: <bool; default=False>

      # List of RADIUS server groups to be used for 802.1X authentication and accounting.
      # The order of the list defines the priority. Each group name must also be defined on at least one server under `aaa_settings.radius.servers`.
      radius_groups:

          # RADIUS server group name.
        - <str>

      # Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection.
      bypass_bpdu: <bool; default=True>

      # Allow LLDP packets to be processed even if the port is not authenticated.
      bypass_lldp: <bool; default=True>
      dynamic_authorization:

        # Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session.
        enabled: <bool; default=True>
      mac_based_authentication:

        # RADIUS User-Name attribute delimiter to use on the MAC address.
        username_delimiter: <str; "colon" | "hyphen" | "none" | "period"; default="none">

        # RADIUS User-Name attribute letter case to use on the MAC address.
        username_letter_case: <str; "lowercase" | "uppercase"; default="lowercase">

      # Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs.
      redistribute_in_evpn: <bool; default=True>
    ```
