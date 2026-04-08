<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_mgmt_method</samp>](## "default_mgmt_method") | String |  | `oob` | Valid Values:<br>- <code>oob</code><br>- <code>inband</code><br>- <code>none</code> | `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:<br>  - `aaa_settings`<br>  - `cv_settings`<br>  - `logging_settings`<br>  - `management_eapi`<br>  - `ntp_settings`<br>  - `sflow_settings`<br>  - `snmp_settings`<br>  - `ssh_settings`<br><br>`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.<br>`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.<br>`none` means the VRF and or interface must be manually set for each protocol.<br>This can be overridden under the settings for each protocol.<br> |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.<br> |
    | [<samp>management_interface_settings</samp>](## "management_interface_settings") | Dictionary |  |  |  | Global OOB (Out-of-Band) management interface settings applied to all devices in the fabric. |
    | [<samp>&nbsp;&nbsp;interface</samp>](## "management_interface_settings.interface") | String |  | `Management1` |  | OOB Management interface name applied to all devices.<br>Resolution order (highest priority first):<br>  1. Per-device `management.interface`<br>  2. Platform `platform_settings.management_interface`<br>  3. `management_interface_settings.interface`<br>  4. Default: "Management1" |
    | [<samp>&nbsp;&nbsp;description</samp>](## "management_interface_settings.description") | String |  | `OOB_MANAGEMENT` |  | OOB Management interface description applied to all devices. |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "management_interface_settings.vrf") | String |  | `MGMT` |  | OOB Management VRF applied to all devices. |
    | [<samp>&nbsp;&nbsp;vrf_routing</samp>](## "management_interface_settings.vrf_routing") | Boolean |  | `False` |  | Configure IP routing for the OOB Management VRF. |
    | [<samp>&nbsp;&nbsp;gateway</samp>](## "management_interface_settings.gateway") | String |  |  | Format: ipv4 | OOB Management gateway in IPv4 format applied to all devices.<br>Used as next-hop for the default route or static routes defined under `destination_networks`.<br>Per-device override: `management.gateway` (takes precedence).<br>This setting is ignored when `management.ip` is set to 'dhcp' and<br>'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server<br>will provide the gateway. |
    | [<samp>&nbsp;&nbsp;destination_networks</samp>](## "management_interface_settings.destination_networks") | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management gateway.<br>When set, these specific prefixes replace the default route (0.0.0.0/0).<br>This setting is ignored when `management.ip` is set to 'dhcp' and<br>'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server<br>will provide the default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interface_settings.destination_networks.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;ipv6</samp>](## "management_interface_settings.ipv6") | Dictionary |  |  |  | IPv6 OOB Management settings applied fabric-wide. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_interface_settings.ipv6.enable") | Boolean |  |  |  | Enable IPv6 on the OOB Management interface.<br>Generates `ipv6 enable` on the management interface.<br>Automatically set to `true` when any other `ipv6` key is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_auto_config</samp>](## "management_interface_settings.ipv6.address_auto_config") | Boolean |  |  |  | Use SLAAC to automatically configure the IPv6 address on the OOB Management interface.<br>Generates `ipv6 address auto-config`.<br>Mutually exclusive with per-device `management.ipv6.ip` — static assignment takes precedence<br>when both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nd</samp>](## "management_interface_settings.ipv6.nd") | Dictionary |  |  |  | IPv6 Neighbor Discovery settings for the OOB Management interface.<br>Only RA receive-path options are exposed here since management interfaces act as ND clients,<br>not routers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ra</samp>](## "management_interface_settings.ipv6.nd.ra") | Dictionary |  |  |  | Router Advertisement receive settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_accept</samp>](## "management_interface_settings.ipv6.nd.ra.rx_accept") | Dictionary |  |  |  | Options controlling which information is accepted from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "management_interface_settings.ipv6.nd.ra.rx_accept.default_route") | Boolean |  |  |  | Accept the default route from received Router Advertisements.<br>Generates `ipv6 nd ra rx accept default-route`.<br>Required when using SLAAC (`ipv6.address_auto_config: true`) and relying on the<br>router to advertise the default route instead of configuring a static `ipv6.gateway`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_preference</samp>](## "management_interface_settings.ipv6.nd.ra.rx_accept.route_preference") | Boolean |  |  |  | Accept route preference from received Router Advertisements.<br>Generates `ipv6 nd ra rx accept route-preference`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "management_interface_settings.ipv6.gateway") | String |  |  | Format: ipv6 | OOB Management gateway in IPv6 format applied to all devices.<br>Used as next-hop for the default IPv6 route or static routes defined under `ipv6.destination_networks`.<br>Not required when `ipv6.address_auto_config: true` and `ipv6.nd.ra.rx_accept.default_route: true`<br>are set, since the default route is then learned from the Router Advertisement.<br>Per-device override: `management.ipv6.gateway` (takes precedence). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_networks</samp>](## "management_interface_settings.ipv6.destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management gateway.<br>When set, these specific prefixes replace the default IPv6 route (::/0). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interface_settings.ipv6.destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.<br>Replaces the default route.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mgmt_destination_networks.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  | OOB Management interface gateway in IPv4 format.<br>Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.<br> |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | `Management1` |  | OOB Management interface. |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") | String |  | `OOB_MANAGEMENT` |  | Management interface description.<br> |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | `MGMT` |  | OOB Management VRF. |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | `False` |  | Configure IP routing for the OOB Management VRF. |

=== "YAML"

    ```yaml
    # `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:
    #   - `aaa_settings`
    #   - `cv_settings`
    #   - `logging_settings`
    #   - `management_eapi`
    #   - `ntp_settings`
    #   - `sflow_settings`
    #   - `snmp_settings`
    #   - `ssh_settings`
    #
    # `oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.
    # `inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.
    # `none` means the VRF and or interface must be manually set for each protocol.
    # This can be overridden under the settings for each protocol.
    default_mgmt_method: <str; "oob" | "inband" | "none"; default="oob">

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>

    # Global OOB (Out-of-Band) management interface settings applied to all devices in the fabric.
    management_interface_settings:

      # OOB Management interface name applied to all devices.
      # Resolution order (highest priority first):
      #   1. Per-device `management.interface`
      #   2. Platform `platform_settings.management_interface`
      #   3. `management_interface_settings.interface`
      #   4. Default: "Management1"
      interface: <str; default="Management1">

      # OOB Management interface description applied to all devices.
      description: <str; default="OOB_MANAGEMENT">

      # OOB Management VRF applied to all devices.
      vrf: <str; default="MGMT">

      # Configure IP routing for the OOB Management VRF.
      vrf_routing: <bool; default=False>

      # OOB Management gateway in IPv4 format applied to all devices.
      # Used as next-hop for the default route or static routes defined under `destination_networks`.
      # Per-device override: `management.gateway` (takes precedence).
      # This setting is ignored when `management.ip` is set to 'dhcp' and
      # 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server
      # will provide the gateway.
      gateway: <str>

      # List of IPv4 prefixes to configure as static routes towards the OOB Management gateway.
      # When set, these specific prefixes replace the default route (0.0.0.0/0).
      # This setting is ignored when `management.ip` is set to 'dhcp' and
      # 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server
      # will provide the default route.
      destination_networks:

          # IPv4_address/Mask.
        - <str>

      # IPv6 OOB Management settings applied fabric-wide.
      ipv6:

        # Enable IPv6 on the OOB Management interface.
        # Generates `ipv6 enable` on the management interface.
        # Automatically set to `true` when any other `ipv6` key is configured.
        enable: <bool>

        # Use SLAAC to automatically configure the IPv6 address on the OOB Management interface.
        # Generates `ipv6 address auto-config`.
        # Mutually exclusive with per-device `management.ipv6.ip` — static assignment takes precedence
        # when both are defined.
        address_auto_config: <bool>

        # IPv6 Neighbor Discovery settings for the OOB Management interface.
        # Only RA receive-path options are exposed here since management interfaces act as ND clients,
        # not routers.
        nd:

          # Router Advertisement receive settings.
          ra:

            # Options controlling which information is accepted from received Router Advertisements.
            rx_accept:

              # Accept the default route from received Router Advertisements.
              # Generates `ipv6 nd ra rx accept default-route`.
              # Required when using SLAAC (`ipv6.address_auto_config: true`) and relying on the
              # router to advertise the default route instead of configuring a static `ipv6.gateway`.
              default_route: <bool>

              # Accept route preference from received Router Advertisements.
              # Generates `ipv6 nd ra rx accept route-preference`.
              route_preference: <bool>

        # OOB Management gateway in IPv6 format applied to all devices.
        # Used as next-hop for the default IPv6 route or static routes defined under `ipv6.destination_networks`.
        # Not required when `ipv6.address_auto_config: true` and `ipv6.nd.ra.rx_accept.default_route: true`
        # are set, since the default route is then learned from the Router Advertisement.
        # Per-device override: `management.ipv6.gateway` (takes precedence).
        gateway: <str>

        # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management gateway.
        # When set, these specific prefixes replace the default IPv6 route (::/0).
        destination_networks:

            # IPv6_network/Mask.
          - <str>

    # List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
    # Replaces the default route.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route.
    mgmt_destination_networks:

        # IPv4_address/Mask.
      - <str>

    # OOB Management interface gateway in IPv4 format.
    # Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.
    mgmt_gateway: <str>

    # OOB Management interface.
    mgmt_interface: <str; default="Management1">

    # Management interface description.
    mgmt_interface_description: <str; default="OOB_MANAGEMENT">

    # OOB Management VRF.
    mgmt_interface_vrf: <str; default="MGMT">

    # Configure IP routing for the OOB Management VRF.
    mgmt_vrf_routing: <bool; default=False>
    ```
