<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tunnel_interfaces</samp>](## "tunnel_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "tunnel_interfaces.[].name") | String | Required, Unique |  |  | Tunnel Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "tunnel_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "tunnel_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "tunnel_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tunnel_interfaces.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_vrf</samp>](## "tunnel_interfaces.[].underlay_vrf") | String |  |  |  | Underlay VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "tunnel_interfaces.[].ip_address") | String |  |  | Format: ipv4_cidr | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "tunnel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "tunnel_interfaces.[].ipv6_address") <span style="color:red">deprecated</span> | String |  |  | Format: ipv6_cidr | IPv6_address/Mask.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ipv6_addresses</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "tunnel_interfaces.[].ipv6_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "tunnel_interfaces.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address with prefix length.<br>This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_auto_config</samp>](## "tunnel_interfaces.[].ipv6_address_auto_config") | Boolean |  |  |  | Use SLAAC to automatically configure the IPv6 address.<br>This option is mutually exclusive with `ipv6_addresses`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd</samp>](## "tunnel_interfaces.[].ipv6_nd") | Dictionary |  |  |  | IPv6 Neighbor Discovery protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cache</samp>](## "tunnel_interfaces.[].ipv6_nd.cache") | Dictionary |  |  |  | Neighbor cache options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_capacity</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 | Capacity of dynamic cache entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expire</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.expire") | Integer |  |  | Min: 1<br>Max: 65535 | Cache entries expiry in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_always</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.refresh_always") | Boolean |  |  |  | Force refresh on cache expiry. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ra</samp>](## "tunnel_interfaces.[].ipv6_nd.ra") | Dictionary |  |  |  | Router Advertisement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.disabled") | Boolean |  |  |  | Disable Router Advertisement messages on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_accept</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept.default_route") | Boolean |  |  |  | Accept default route from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_preference</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept.route_preference") | Boolean |  |  |  | Accept route preference from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;managed_config_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.managed_config_flag") | Boolean |  |  |  | Set the "Managed Address Configuration" (M) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes") | List, items: Dictionary |  |  |  | IPv6 prefixes to include in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].valid_lifetime") | String |  |  |  | Valid lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].preferred_lifetime") | String |  |  |  | Preferred lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].no_autoconfig_flag") | Boolean |  |  |  | Indicate that the prefix cannot be used for stateless address autoconfiguration (SLAAC). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_config_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.other_config_flag") | Boolean |  |  |  | Set the "Other Stateful Configuration" (O) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "tunnel_interfaces.[].access_group_in") | String |  |  |  | IPv4 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "tunnel_interfaces.[].access_group_out") | String |  |  |  | IPv4 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "tunnel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "tunnel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> | Optional direction ('ingress', 'egress')  for tcp mss ceiling.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_mode</samp>](## "tunnel_interfaces.[].tunnel_mode") | String |  |  | Valid Values:<br>- <code>gre</code><br>- <code>ipsec</code> | Tunnel encapsulation method.<br>`gre`: Generic route encapsulation protocol,<br>`ipsec`: IPsec-over-IP encapsulation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "tunnel_interfaces.[].source_interface") | String |  |  |  | Tunnel Source Interface Name.<br>Mutually exclusive with `source`, if both are defined `source_interface` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "tunnel_interfaces.[].source") | String |  |  |  | Tunnel Source IPv4/IPv6 address.<br>Mutually exclusive with `source_interface`, if both are defined `source_interface` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "tunnel_interfaces.[].destination") | String |  |  |  | IPv4 or IPv6 Address Tunnel Destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_mtu_discovery</samp>](## "tunnel_interfaces.[].path_mtu_discovery") | Boolean |  |  |  | Enable Path MTU Discovery On Tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec_profile</samp>](## "tunnel_interfaces.[].ipsec_profile") | String |  |  |  | Used only when `tunnel_mode` is set to `ipsec`.<br>It must target a defined IPsec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nat_profile</samp>](## "tunnel_interfaces.[].nat_profile") | String |  |  |  | NAT interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "tunnel_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    tunnel_interfaces:

        # Tunnel Interface Name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>
        mtu: <int; 68-65535>

        # VRF Name.
        vrf: <str>

        # Underlay VRF Name.
        underlay_vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
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

        # IPv6 Neighbor Discovery protocol.
        ipv6_nd:

          # Neighbor cache options.
          cache:

            # Capacity of dynamic cache entries.
            dynamic_capacity: <int; 0-4294967295>

            # Cache entries expiry in seconds.
            expire: <int; 1-65535>

            # Force refresh on cache expiry.
            refresh_always: <bool>

          # Router Advertisement.
          ra:

            # Disable Router Advertisement messages on the interface.
            disabled: <bool>
            rx_accept:

              # Accept default route from received Router Advertisements.
              default_route: <bool>

              # Accept route preference from received Router Advertisements.
              route_preference: <bool>

          # Set the "Managed Address Configuration" (M) flag in Router Advertisements.
          managed_config_flag: <bool>

          # IPv6 prefixes to include in Router Advertisements.
          prefixes:
            - ipv6_prefix: <str; required; unique>

              # Valid lifetime in seconds '<0-4294967295>' or 'infinite'.
              valid_lifetime: <str>

              # Preferred lifetime in seconds '<0-4294967295>' or 'infinite'.
              preferred_lifetime: <str>

              # Indicate that the prefix cannot be used for stateless address autoconfiguration (SLAAC).
              no_autoconfig_flag: <bool>

          # Set the "Other Stateful Configuration" (O) flag in Router Advertisements.
          other_config_flag: <bool>

        # IPv4 ACL Name for ingress.
        access_group_in: <str>

        # IPv4 ACL Name for egress.
        access_group_out: <str>

        # IPv6 ACL Name for ingress.
        ipv6_access_group_in: <str>

        # IPv6 ACL Name for egress.
        ipv6_access_group_out: <str>
        tcp_mss_ceiling:

          # Segment Size for IPv4.
          ipv4: <int; 64-65495>

          # Segment Size for IPv6.
          ipv6: <int; 64-65475>

          # Optional direction ('ingress', 'egress')  for tcp mss ceiling.
          direction: <str; "ingress" | "egress">

        # Tunnel encapsulation method.
        # `gre`: Generic route encapsulation protocol,
        # `ipsec`: IPsec-over-IP encapsulation.
        tunnel_mode: <str; "gre" | "ipsec">

        # Tunnel Source Interface Name.
        # Mutually exclusive with `source`, if both are defined `source_interface` takes precedence.
        source_interface: <str>

        # Tunnel Source IPv4/IPv6 address.
        # Mutually exclusive with `source_interface`, if both are defined `source_interface` takes precedence.
        source: <str>

        # IPv4 or IPv6 Address Tunnel Destination.
        destination: <str>

        # Enable Path MTU Discovery On Tunnel.
        path_mtu_discovery: <bool>

        # Used only when `tunnel_mode` is set to `ipsec`.
        # It must target a defined IPsec profile.
        ipsec_profile: <str>

        # NAT interface profile.
        nat_profile: <str>

        # Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.
        eos_cli: <str>
    ```
