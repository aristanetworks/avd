<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | `True` |  | When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.<br> |
    | [<samp>default_interface_mtu</samp>](## "default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Can be overridden per platform under platform settings.<br> |
    | [<samp>general_settings</samp>](## "general_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_defaults</samp>](## "general_settings.interface_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ethernet_shutdown</samp>](## "general_settings.interface_defaults.ethernet_shutdown") | Boolean |  | `False` |  | Shutdown Ethernet interfaces by default unless they are explicitly enabled. |
    | [<samp>&nbsp;&nbsp;arp</samp>](## "general_settings.arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;persistent</samp>](## "general_settings.arp.persistent") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "general_settings.arp.persistent.enabled") | Boolean | Required |  |  | Restore the ARP cache after reboot. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_delay</samp>](## "general_settings.arp.persistent.refresh_delay") | Integer |  |  | Min: 600<br>Max: 3600 | Time to wait in seconds before refreshing the ARP cache after reboot (EOS default 600). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;aging</samp>](## "general_settings.arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "general_settings.arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;ip_icmp_redirect</samp>](## "general_settings.ip_icmp_redirect") | Boolean |  |  |  |  |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsibility of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "hardware_counters.features.[].name") | String | Required |  | Valid Values:<br>- <code>acl</code><br>- <code>decap-group</code><br>- <code>directflow</code><br>- <code>ecn</code><br>- <code>flow-spec</code><br>- <code>gre tunnel interface</code><br>- <code>ip</code><br>- <code>mpls interface</code><br>- <code>mpls lfib</code><br>- <code>mpls tunnel</code><br>- <code>multicast</code><br>- <code>nexthop</code><br>- <code>pbr</code><br>- <code>pdp</code><br>- <code>policing interface</code><br>- <code>qos</code><br>- <code>qos dual-rate-policer</code><br>- <code>route</code><br>- <code>routed-port</code><br>- <code>segment-security</code><br>- <code>subinterface</code><br>- <code>tapagg</code><br>- <code>traffic-class</code><br>- <code>traffic-policy</code><br>- <code>traffic-policy vlan-interface</code><br>- <code>vlan</code><br>- <code>vlan-interface</code><br>- <code>vni decap</code><br>- <code>vni encap</code><br>- <code>vtep decap</code><br>- <code>vtep encap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>cpu</code> | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "hardware_counters.features.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>mac</code> | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  | See (+) on YAML tab |  | Internal vlan allocation order and range. |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required |  | Valid Values:<br>- <code>ascending</code><br>- <code>descending</code> |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |
    | [<samp>&nbsp;&nbsp;notification_host_flap</samp>](## "mac_address_table.notification_host_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "mac_address_table.notification_host_flap.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "mac_address_table.notification_host_flap.detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "mac_address_table.notification_host_flap.detection.window") | Integer |  |  | Min: 2<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp>](## "mac_address_table.notification_host_flap.detection.moves") | Integer |  |  | Min: 2<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "mac_address_table.static_entries") | List, items: Dictionary |  |  |  | Add static MAC address entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;mac_address</samp>](## "mac_address_table.static_entries.[].mac_address") | String | Required |  | Pattern: `[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}` | The static MAC address to configure.<br>The combination of 'mac_address' and 'vlan' must be unique across all static entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "mac_address_table.static_entries.[].vlan") | Integer | Required |  |  | The VLAN ID associated with the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "mac_address_table.static_entries.[].drop") | Boolean |  |  |  | If true, traffic destined for this MAC address on the specified VLAN will be dropped.<br>This option is mutually exclusive with 'interface' and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "mac_address_table.static_entries.[].interface") | String |  |  |  | The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.<br>This option is mutually exclusive with 'drop'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eligibility_forwarding</samp>](## "mac_address_table.static_entries.[].eligibility_forwarding") | Boolean |  |  |  | Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.<br>This option is only applicable when 'interface' is defined. |
    | [<samp>monitor_connectivity</samp>](## "monitor_connectivity") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "monitor_connectivity.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "monitor_connectivity.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.interface_sets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.interface_sets.[].interfaces") | String | Required |  |  | Interface range(s) should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interface ranges can be specified separated by ",".<br> |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.hosts.[].name") | String | Required, Unique |  |  | Host Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.hosts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.hosts.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.hosts.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;name_server_group</samp>](## "monitor_connectivity.name_server_group") | String |  |  |  | Set name-server group. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "monitor_connectivity.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.vrfs.[].interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Host name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.vrfs.[].hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.vrfs.[].hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].hosts.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.vrfs.[].hosts.[].url") | String |  |  |  |  |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | If True, Arista AVD will configure `queue-monitor length notifying` according to the<br>`platform_settings.[].feature_support.queue_monitor_length_notify` setting.<br> |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tx_latency</samp>](## "queue_monitor_length.tx_latency") | Boolean |  |  |  | Enable tx-latency mode. |
    | [<samp>&nbsp;&nbsp;mirror</samp>](## "queue_monitor_length.mirror") | Dictionary |  |  |  | Enable frame mirroring during congestion. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.mirror.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "queue_monitor_length.mirror.destination") | Dictionary |  |  |  | Mirror destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.mirror.destination.cpu") | Boolean |  |  |  | CPU ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_interfaces</samp>](## "queue_monitor_length.mirror.destination.ethernet_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "queue_monitor_length.mirror.destination.ethernet_interfaces.[]") | String |  |  |  | Ethernet interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_mode_gre</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.source") | String | Required |  |  | Source IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.destination") | String | Required |  |  | Destination IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.dscp") | Integer |  |  | Min: 0<br>Max: 63 | DSCP of the GRE tunnel. EOS default is 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.ttl") | Integer |  |  | Min: 1<br>Max: 255 | TTL range. EOS default is 128. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.protocol") | String |  |  |  | Protocol type in GRE header. Protocol range - 0x0000-0xFFFF.<br>EOS default is 0x88BE. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.vrf") | String |  |  |  | VRF name of the GRE tunnel. EOS default is "default". |
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  | Redundancy for chassis platforms with dual supervisors | Optional. |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- <code>sso</code><br>- <code>rpr</code> |  |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  | Serial Number of the device.<br>Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.<br>"serial_number" can also be set directly under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  | Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |

=== "YAML"

    ```yaml
    # When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.
    default_igmp_snooping_enabled: <bool; default=True>

    # Default interface MTU configured on EOS under "interface defaults".
    # Can be overridden per platform under platform settings.
    default_interface_mtu: <int; 68-65535>
    general_settings:
      interface_defaults:

        # Shutdown Ethernet interfaces by default unless they are explicitly enabled.
        ethernet_shutdown: <bool; default=False>
      arp:
        persistent:

          # Restore the ARP cache after reboot.
          enabled: <bool; required>

          # Time to wait in seconds before refreshing the ARP cache after reboot (EOS default 600).
          refresh_delay: <int; 600-3600>
        aging:

          # Timeout in seconds.
          timeout_default: <int; 60-65535>
      ip_icmp_redirect: <bool>
    hardware_counters:

      # This data model allows to configure the list of hardware counters feature
      # available on Arista platforms.
      #
      # The `name` key accepts a list of valid_values which MUST be updated to support
      # new feature as they are released in EOS.
      #
      # The available values of the different keys like 'direction' or 'address_type'
      # are feature and hardware dependent and this model DOES NOT validate that the
      # combinations are valid. It is the responsibility of the user of this data model
      # to make sure that the rendered CLI is accepted by the targeted device.
      #
      # Examples:
      #
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: ip
      #           direction: out
      #           layer3: true
      #           units_packets: true
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature ip out layer3 units packets
      #     ```
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: route
      #           address_type: ipv4
      #           vrf: test
      #           prefix: 192.168.0.0/24
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature route ipv4 vrf test 192.168.0.0/24
      #     ```
      features:
        - name: <str; "acl" | "decap-group" | "directflow" | "ecn" | "flow-spec" | "gre tunnel interface" | "ip" | "mpls interface" | "mpls lfib" | "mpls tunnel" | "multicast" | "nexthop" | "pbr" | "pdp" | "policing interface" | "qos" | "qos dual-rate-policer" | "route" | "routed-port" | "segment-security" | "subinterface" | "tapagg" | "traffic-class" | "traffic-policy" | "traffic-policy vlan-interface" | "vlan" | "vlan-interface" | "vni decap" | "vni encap" | "vtep decap" | "vtep encap"; required>

          # Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
          # Some features DO NOT have any direction.
          # This validation IS NOT made by the schemas.
          direction: <str; "in" | "out" | "cpu">
          enabled: <bool; default=True>

          # Supported only for the following features:
          # - acl: [ipv4, ipv6, mac] if direction is 'out'
          # - multicast: [ipv4, ipv6]
          # - route: [ipv4, ipv6]
          # This validation IS NOT made by the schemas.
          address_type: <str; "ipv4" | "ipv6" | "mac">

          # Supported only for the 'ip' feature.
          layer3: <bool>

          # Supported only for the 'route' feature.
          # This validation IS NOT made by the schemas.
          vrf: <str>

          # Supported only for the 'route' feature.
          # Mandatory for the 'route' feature.
          # This validation IS NOT made by the schemas.
          prefix: <str>
          units_packets: <bool>

    # Internal vlan allocation order and range.
    internal_vlan_order: # (1)!
      allocation: <str; "ascending" | "descending"; required>
      range:

        # First VLAN ID.
        beginning: <int; 2-4094; required>

        # Last VLAN ID.
        ending: <int; 2-4094; required>
    mac_address_table:

      # Aging time in seconds 10-1000000.
      # Enter 0 to disable aging.
      aging_time: <int; 0-1000000>
      notification_host_flap:
        logging: <bool>
        detection:
          window: <int; 2-300>
          moves: <int; 2-10>

      # Add static MAC address entries.
      static_entries:

          # The static MAC address to configure.
          # The combination of 'mac_address' and 'vlan' must be unique across all static entries.
        - mac_address: <str; required>

          # The VLAN ID associated with the MAC address.
          vlan: <int; required>

          # If true, traffic destined for this MAC address on the specified VLAN will be dropped.
          # This option is mutually exclusive with 'interface' and takes precedence if both are defined.
          drop: <bool>

          # The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.
          # This option is mutually exclusive with 'drop'.
          interface: <str>

          # Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.
          # This option is only applicable when 'interface' is defined.
          eligibility_forwarding: <bool>
    monitor_connectivity:
      shutdown: <bool>
      interval: <int>
      interface_sets:
        - name: <str; required; unique>

          # Interface range(s) should be of same type, Ethernet, Loopback, Management etc.
          # Multiple interface ranges can be specified separated by ",".
          interfaces: <str; required>
      local_interfaces: <str>

      # When address-only is configured, the source IP of the packet is set to the interface
      # IP but the packet may exit the device via a different interface.
      # When set to `false`, the probe uses the interface to exit the device.
      address_only: <bool; default=True>
      hosts:

          # Host Name.
        - name: <str; required; unique>
          description: <str>
          ip: <str>

          # Size of ICMP probe in bytes.
          icmp_echo_size: <int; 36-18024>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=True>
          url: <str>

      # Set name-server group.
      name_server_group: <str>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>
          description: <str>
          interface_sets:
            - name: <str; required; unique>
              interfaces: <str>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=True>
          hosts:

              # Host name.
            - name: <str; required; unique>
              description: <str>
              ip: <str>

              # Size of ICMP probe in bytes.
              icmp_echo_size: <int; 36-18024>
              local_interfaces: <str>

              # When address-only is configured, the source IP of the packet is set to the interface
              # IP but the packet may exit the device via a different interface.
              # When set to `false`, the probe uses the interface to exit the device.
              address_only: <bool; default=True>
              url: <str>
    queue_monitor_length:
      enabled: <bool; required>

      # If True, Arista AVD will configure `queue-monitor length notifying` according to the
      # `platform_settings.[].feature_support.queue_monitor_length_notify` setting.
      notifying: <bool>
      default_thresholds:

        # Default high threshold for Ethernet Interfaces.
        high: <int; required>

        # Default low threshold for Ethernet Interfaces.
        # Low threshold support is platform dependent.
        low: <int>

      # Logging interval in seconds.
      log: <int>
      cpu:
        thresholds:
          high: <int; required>
          low: <int>

      # Enable tx-latency mode.
      tx_latency: <bool>

      # Enable frame mirroring during congestion.
      mirror:
        enabled: <bool>

        # Mirror destination.
        destination:

          # CPU ports.
          cpu: <bool>
          ethernet_interfaces:

              # Ethernet interface name.
            - <str>
          tunnel_mode_gre:

            # Source IP address of GRE tunnel.
            source: <str; required>

            # Destination IP address of GRE tunnel.
            destination: <str; required>

            # DSCP of the GRE tunnel. EOS default is 0.
            dscp: <int; 0-63>

            # TTL range. EOS default is 128.
            ttl: <int; 1-255>

            # Protocol type in GRE header. Protocol range - 0x0000-0xFFFF.
            # EOS default is 0x88BE.
            protocol: <str>

            # VRF name of the GRE tunnel. EOS default is "default".
            vrf: <str>

    # Redundancy for chassis platforms with dual supervisors | Optional.
    redundancy:
      protocol: <str; "sso" | "rpr">

    # Serial Number of the device.
    # Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.
    # "serial_number" can also be set directly under node type settings.
    # If both are set, the value under node type settings takes precedence.
    serial_number: <str>

    # Set to the same MAC address as available in "show version" on the device.
    # "system_mac_address" can also be set under node type settings.
    # If both are set, the value under node type settings takes precedence.
    system_mac_address: <str>
    ```

    1. Default Value

        ```yaml
        internal_vlan_order:
          allocation: ascending
          range:
            beginning: 1006
            ending: 1199
        ```
