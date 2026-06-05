<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x_settings</samp>](## "dot1x_settings") | Dictionary |  |  |  | Settings for 802.1X deployments. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.enabled") | Boolean |  | `False` |  | Globally enable 802.1X port authentication on the switch.<br>Must be true for 802.1X to be active on any interface. |
    | [<samp>&nbsp;&nbsp;authentication</samp>](## "dot1x_settings.authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;radius_groups</samp>](## "dot1x_settings.authentication.radius_groups") | List, items: String |  |  | Min Length: 1 | List of RADIUS server groups to be used for 802.1X authentication when globally enabled. If not provided, all defined RADIUS hosts are used.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on any server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.authentication.radius_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;accounting</samp>](## "dot1x_settings.accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.accounting.enabled") | Boolean |  | `True` |  | Enable 802.1X accounting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "dot1x_settings.accounting.mode") | String |  | `start-stop` | Valid Values:<br>- <code>start-stop</code><br>- <code>stop-only</code> | Determines whether to send accounting records when a session is established and<br>when it ends (`start-stop`), or only when the session ends (`stop-only`). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;radius_groups</samp>](## "dot1x_settings.accounting.radius_groups") | List, items: String |  |  | Min Length: 1 | List of RADIUS server groups to be used for 802.1X accounting when enabled. If not provided, all defined RADIUS hosts are used.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on any server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.accounting.radius_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "dot1x_settings.accounting.multicast") | Boolean |  | `False` |  | Send Accounting-Request messages to all servers in a RADIUS group at the same time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;syslog</samp>](## "dot1x_settings.accounting.syslog") | Boolean |  | `False` |  | Log all accounting messages to syslog if all RADIUS servers are unavailable or unresponsive. |
    | [<samp>&nbsp;&nbsp;bypass_bpdu</samp>](## "dot1x_settings.bypass_bpdu") | Boolean |  | `True` |  | Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection. |
    | [<samp>&nbsp;&nbsp;bypass_lldp</samp>](## "dot1x_settings.bypass_lldp") | Boolean |  | `True` |  | Allow LLDP packets to be processed even if the port is not authorized. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x_settings.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.dynamic_authorization.enabled") | Boolean |  | `True` |  | Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;additional_groups</samp>](## "dot1x_settings.dynamic_authorization.additional_groups") | List, items: String |  |  |  | List of additional RADIUS server groups for dynamic authorization purposes only.<br>The order of the list defines the server group priority.<br>Each group name must also be defined on any server under `aaa_settings.radius.servers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dot1x_settings.dynamic_authorization.additional_groups.[]") | String |  |  |  | RADIUS server group name. |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x_settings.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username_format</samp>](## "dot1x_settings.mac_based_authentication.username_format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimiter</samp>](## "dot1x_settings.mac_based_authentication.username_format.delimiter") | String | Required |  | Valid Values:<br>- <code>colon</code><br>- <code>hyphen</code><br>- <code>none</code><br>- <code>period</code> | RADIUS User-Name attribute delimiter to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter_case</samp>](## "dot1x_settings.mac_based_authentication.username_format.letter_case") | String | Required |  | Valid Values:<br>- <code>lowercase</code><br>- <code>uppercase</code> | RADIUS User-Name attribute letter case to use on the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "dot1x_settings.mac_based_authentication.delay") | Integer |  |  | Min: 0<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hold_period</samp>](## "dot1x_settings.mac_based_authentication.hold_period") | Integer |  |  | Min: 1<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;radius_av_pairs</samp>](## "dot1x_settings.radius_av_pairs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_type</samp>](## "dot1x_settings.radius_av_pairs.service_type") | Boolean |  | `False` |  | Send RADIUS Service-Type attribute in Access-Request and Accounting messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;framed_mtu</samp>](## "dot1x_settings.radius_av_pairs.framed_mtu") | Integer |  |  | Min: 68<br>Max: 9236 |  |
    | [<samp>&nbsp;&nbsp;device_profiling</samp>](## "dot1x_settings.device_profiling") | Dictionary |  |  |  | Device profiling feature.<br>Allows EOS to send authenticated host attributes (DHCP options/LLDP TLVs)<br>to the RADIUS server via Arista VSA "Arista-Device-Profiling" accounting messages.<br>Requires `dot1x_settings.accounting.enabled: true` and `dot1x_settings.accounting.mode: start-stop`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.device_profiling.enabled") | Boolean |  | `False` |  | Enable all DHCP and LLDP TLV profiling options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "dot1x_settings.device_profiling.dhcp") | Dictionary |  |  |  | DHCP options profiling.<br>Enables profiling via DHCP Discover/Request packets.<br>Limitations:<br>  - IPv4 only. IPv6 address assignments via DHCPv6 or SLAAC are not supported.<br>  - Not supported on VTEP devices.<br>  - Not supported with IP Locking features.<br>  - MLAG support requires EOS 4.34.3+. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.device_profiling.dhcp.enabled") | Boolean |  | `True` |  | Enable all DHCP profiling options collectively. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "dot1x_settings.device_profiling.dhcp.hostname") | Dictionary |  |  |  | DHCP Option 12 (Hostname). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.device_profiling.dhcp.hostname.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x_settings.device_profiling.dhcp.hostname.auth_only") | Boolean |  | `False` |  | Sends the attribute only once when first learned. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter_request_list</samp>](## "dot1x_settings.device_profiling.dhcp.parameter_request_list") | Dictionary |  |  |  | DHCP Option 55 (Parameter Request List). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.device_profiling.dhcp.parameter_request_list.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x_settings.device_profiling.dhcp.parameter_request_list.auth_only") | Boolean |  | `False` |  | Sends the attribute only once when first learned. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vendor_class_id</samp>](## "dot1x_settings.device_profiling.dhcp.vendor_class_id") | Dictionary |  |  |  | DHCP Option 60 (Vendor Class ID). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.device_profiling.dhcp.vendor_class_id.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x_settings.device_profiling.dhcp.vendor_class_id.auth_only") | Boolean |  | `False` |  | Sends the attribute only once when first learned. |
    | [<samp>&nbsp;&nbsp;redistribute_in_evpn</samp>](## "dot1x_settings.redistribute_in_evpn") | Boolean |  | `True` |  | Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs. |

=== "YAML"

    ```yaml
    # Settings for 802.1X deployments.
    dot1x_settings:

      # Globally enable 802.1X port authentication on the switch.
      # Must be true for 802.1X to be active on any interface.
      enabled: <bool; default=False>
      authentication:

        # List of RADIUS server groups to be used for 802.1X authentication when globally enabled. If not provided, all defined RADIUS hosts are used.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on any server under `aaa_settings.radius.servers`.
        radius_groups: # >=1 items

            # RADIUS server group name.
          - <str>
      accounting:

        # Enable 802.1X accounting.
        enabled: <bool; default=True>

        # Determines whether to send accounting records when a session is established and
        # when it ends (`start-stop`), or only when the session ends (`stop-only`).
        mode: <str; "start-stop" | "stop-only"; default="start-stop">

        # List of RADIUS server groups to be used for 802.1X accounting when enabled. If not provided, all defined RADIUS hosts are used.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on any server under `aaa_settings.radius.servers`.
        radius_groups: # >=1 items

            # RADIUS server group name.
          - <str>

        # Send Accounting-Request messages to all servers in a RADIUS group at the same time.
        multicast: <bool; default=False>

        # Log all accounting messages to syslog if all RADIUS servers are unavailable or unresponsive.
        syslog: <bool; default=False>

      # Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection.
      bypass_bpdu: <bool; default=True>

      # Allow LLDP packets to be processed even if the port is not authorized.
      bypass_lldp: <bool; default=True>
      dynamic_authorization:

        # Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session.
        enabled: <bool; default=True>

        # List of additional RADIUS server groups for dynamic authorization purposes only.
        # The order of the list defines the server group priority.
        # Each group name must also be defined on any server under `aaa_settings.radius.servers`.
        additional_groups:

            # RADIUS server group name.
          - <str>
      mac_based_authentication:
        username_format:

          # RADIUS User-Name attribute delimiter to use on the MAC address.
          delimiter: <str; "colon" | "hyphen" | "none" | "period"; required>

          # RADIUS User-Name attribute letter case to use on the MAC address.
          letter_case: <str; "lowercase" | "uppercase"; required>
        delay: <int; 0-300>
        hold_period: <int; 1-300>
      radius_av_pairs:

        # Send RADIUS Service-Type attribute in Access-Request and Accounting messages.
        service_type: <bool; default=False>
        framed_mtu: <int; 68-9236>

      # Device profiling feature.
      # Allows EOS to send authenticated host attributes (DHCP options/LLDP TLVs)
      # to the RADIUS server via Arista VSA "Arista-Device-Profiling" accounting messages.
      # Requires `dot1x_settings.accounting.enabled: true` and `dot1x_settings.accounting.mode: start-stop`.
      device_profiling:

        # Enable all DHCP and LLDP TLV profiling options.
        enabled: <bool; default=False>

        # DHCP options profiling.
        # Enables profiling via DHCP Discover/Request packets.
        # Limitations:
        #   - IPv4 only. IPv6 address assignments via DHCPv6 or SLAAC are not supported.
        #   - Not supported on VTEP devices.
        #   - Not supported with IP Locking features.
        #   - MLAG support requires EOS 4.34.3+.
        dhcp:

          # Enable all DHCP profiling options collectively.
          enabled: <bool; default=True>

          # DHCP Option 12 (Hostname).
          hostname:
            enabled: <bool; default=True>

            # Sends the attribute only once when first learned.
            auth_only: <bool; default=False>

          # DHCP Option 55 (Parameter Request List).
          parameter_request_list:
            enabled: <bool; default=True>

            # Sends the attribute only once when first learned.
            auth_only: <bool; default=False>

          # DHCP Option 60 (Vendor Class ID).
          vendor_class_id:
            enabled: <bool; default=True>

            # Sends the attribute only once when first learned.
            auth_only: <bool; default=False>

      # Globally enable the redistribution of static 802.1X-learned MAC addresses into EVPN under all configured MAC-VRFs.
      redistribute_in_evpn: <bool; default=True>
    ```
