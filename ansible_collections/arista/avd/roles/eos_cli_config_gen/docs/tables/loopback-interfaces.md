<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>loopback_interfaces</samp>](## "loopback_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "loopback_interfaces.[].name") | String | Required, Unique |  |  | Loopback interface name e.g. "Loopback0". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "loopback_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "loopback_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "loopback_interfaces.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "loopback_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "loopback_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "loopback_interfaces.[].ip_address_secondaries.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "loopback_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "loopback_interfaces.[].ipv6_address") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ipv6_addresses</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "loopback_interfaces.[].ipv6_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "loopback_interfaces.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address with prefix length.<br>This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_auto_config</samp>](## "loopback_interfaces.[].ipv6_address_auto_config") | Boolean |  |  |  | Use SLAAC to automatically configure the IPv6 address.<br>This option is mutually exclusive with `ipv6_addresses`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "loopback_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "loopback_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "loopback_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "loopback_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "loopback_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "loopback_interfaces.[].isis_enable") | String |  |  |  | ISIS instance name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_bfd</samp>](## "loopback_interfaces.[].isis_bfd") | Boolean |  |  |  | Enable BFD for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "loopback_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "loopback_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "loopback_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_segment</samp>](## "loopback_interfaces.[].node_segment") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_index</samp>](## "loopback_interfaces.[].node_segment.ipv4_index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_index</samp>](## "loopback_interfaces.[].node_segment.ipv6_index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_forwarding_id</samp>](## "loopback_interfaces.[].hardware_forwarding_id") | Boolean |  |  |  | Enable hardware forwarding for the VRF where this loopback interface belongs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "loopback_interfaces.[].eos_cli") | String |  |  |  | EOS CLI rendered directly on the loopback interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    loopback_interfaces:

        # Loopback interface name e.g. "Loopback0".
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # VRF name.
        vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
        ip_address_secondaries:

            # IPv4_address/Mask.
          - <str>
        ipv6_enable: <bool>

        # IPv6_address/Mask.
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `ipv6_addresses` instead.
        ipv6_address: <str>
        ipv6_addresses:

            # IPv6 address with prefix length.
            # This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined.
          - <str>

        # Use SLAAC to automatically configure the IPv6 address.
        # This option is mutually exclusive with `ipv6_addresses`.
        ipv6_address_auto_config: <bool>
        ip_proxy_arp: <bool>
        ospf_area: <str>
        mpls:
          ldp:
            interface: <bool>

        # ISIS instance name.
        isis_enable: <str>

        # Enable BFD for ISIS.
        isis_bfd: <bool>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        node_segment:
          ipv4_index: <int>
          ipv6_index: <int>

        # Enable hardware forwarding for the VRF where this loopback interface belongs.
        hardware_forwarding_id: <bool>

        # EOS CLI rendered directly on the loopback interface in the final EOS configuration.
        eos_cli: <str>
    ```
