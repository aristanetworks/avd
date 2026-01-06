<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x_settings</samp>](## "dot1x_settings") | Dictionary |  |  |  | Settings for 802.1X deployments. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.enabled") | Boolean |  | `False` |  | Globally enable 802.1X port authentication on the switch.<br>Must be set for 802.1X to be active on any interface.<br>When set, `dot1x_settings.authentication.radius_groups` is required. |
    | [<samp>&nbsp;&nbsp;authentication</samp>](## "dot1x_settings.authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;radius_groups</samp>](## "dot1x_settings.authentication.radius_groups") | List, items: String |  |  | Min Length: 1 | Required list of RADIUS server groups to be used for 802.1X authentication when globally enabled.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on at least one server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.authentication.radius_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;accounting</samp>](## "dot1x_settings.accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.accounting.enabled") | Boolean |  | `True` |  | Enable 802.1X accounting. When set, at least one accounting method must be provided via<br>the `dot1x_settings.accounting.radius_groups` or `dot1x_settings.accounting.syslog` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "dot1x_settings.accounting.mode") | String |  | `start-stop` | Valid Values:<br>- <code>start-stop</code><br>- <code>stop-only</code> | Determines whether to send accounting records when a session is established and<br>when it ends (`start-stop`), or only when the session ends (`stop-only`). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;radius_groups</samp>](## "dot1x_settings.accounting.radius_groups") | List, items: String |  |  | Min Length: 1 | List of RADIUS server groups to be used for 802.1X accounting.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on at least one server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.accounting.radius_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "dot1x_settings.accounting.multicast") | Boolean |  | `False` |  | Send Accounting-Request packets to all servers in a RADIUS group at the same time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;syslog</samp>](## "dot1x_settings.accounting.syslog") | Boolean |  | `False` |  | Log all accounting messages to Syslog.<br>Acts as a fallback if RADIUS groups are configured, or as the primary method if no groups are defined. |
    | [<samp>&nbsp;&nbsp;bypass_bpdu</samp>](## "dot1x_settings.bypass_bpdu") | Boolean |  | `True` |  | Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection. |
    | [<samp>&nbsp;&nbsp;bypass_lldp</samp>](## "dot1x_settings.bypass_lldp") | Boolean |  | `True` |  | Allow LLDP packets to be processed even if the port is not authenticated. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x_settings.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.dynamic_authorization.enabled") | Boolean |  | `True` |  | Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;additional_groups</samp>](## "dot1x_settings.dynamic_authorization.additional_groups") | List, items: String |  |  |  | List of additional RADIUS server groups for dynamic authorization purposes only.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on at least one server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.dynamic_authorization.additional_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x_settings.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username_delimiter</samp>](## "dot1x_settings.mac_based_authentication.username_delimiter") | String |  | `none` | Valid Values:<br>- <code>colon</code><br>- <code>hyphen</code><br>- <code>none</code><br>- <code>period</code> | RADIUS User-Name attribute delimiter to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username_letter_case</samp>](## "dot1x_settings.mac_based_authentication.username_letter_case") | String |  | `lowercase` | Valid Values:<br>- <code>lowercase</code><br>- <code>uppercase</code> | RADIUS User-Name attribute letter case to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;redistribute_in_evpn</samp>](## "dot1x_settings.redistribute_in_evpn") | Boolean |  | `True` |  | Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs. |

=== "YAML"

    ```yaml
    # Settings for 802.1X deployments.
    dot1x_settings:

      # Globally enable 802.1X port authentication on the switch.
      # Must be set for 802.1X to be active on any interface.
      # When set, `dot1x_settings.authentication.radius_groups` is required.
      enabled: <bool; default=False>
      authentication:

        # Required list of RADIUS server groups to be used for 802.1X authentication when globally enabled.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on at least one server under `aaa_settings.radius.servers`.
        radius_groups: # >=1 items

            # RADIUS server group name.
          - <str>
      accounting:

        # Enable 802.1X accounting. When set, at least one accounting method must be provided via
        # the `dot1x_settings.accounting.radius_groups` or `dot1x_settings.accounting.syslog` key.
        enabled: <bool; default=True>

        # Determines whether to send accounting records when a session is established and
        # when it ends (`start-stop`), or only when the session ends (`stop-only`).
        mode: <str; "start-stop" | "stop-only"; default="start-stop">

        # List of RADIUS server groups to be used for 802.1X accounting.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on at least one server under `aaa_settings.radius.servers`.
        radius_groups: # >=1 items

            # RADIUS server group name.
          - <str>

        # Send Accounting-Request packets to all servers in a RADIUS group at the same time.
        multicast: <bool; default=False>

        # Log all accounting messages to Syslog.
        # Acts as a fallback if RADIUS groups are configured, or as the primary method if no groups are defined.
        syslog: <bool; default=False>

      # Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection.
      bypass_bpdu: <bool; default=True>

      # Allow LLDP packets to be processed even if the port is not authenticated.
      bypass_lldp: <bool; default=True>
      dynamic_authorization:

        # Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session.
        enabled: <bool; default=True>

        # List of additional RADIUS server groups for dynamic authorization purposes only.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on at least one server under `aaa_settings.radius.servers`.
        additional_groups:

            # RADIUS server group name.
          - <str>
      mac_based_authentication:

        # RADIUS User-Name attribute delimiter to use on the MAC address.
        username_delimiter: <str; "colon" | "hyphen" | "none" | "period"; default="none">

        # RADIUS User-Name attribute letter case to use on the MAC address.
        username_letter_case: <str; "lowercase" | "uppercase"; default="lowercase">

      # Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs.
      redistribute_in_evpn: <bool; default=True>
    ```
