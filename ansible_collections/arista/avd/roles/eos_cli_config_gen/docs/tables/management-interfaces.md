<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_interfaces</samp>](## "management_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "management_interfaces.[].name") | String | Required, Unique |  |  | Management Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "management_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "management_interfaces.[].speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Interface Speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "management_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_interfaces.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "management_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "management_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].ipv6_address") <span style="color:red">deprecated</span> | String |  |  |  | IPv6 address with prefix length.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ipv6_addresses</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "management_interfaces.[].ipv6_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address with prefix length.<br>This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_auto_config</samp>](## "management_interfaces.[].ipv6_address_auto_config") | Boolean |  |  |  | Use SLAAC to automatically configure the IPv6 address.<br>This option is mutually exclusive with `ipv6_addresses`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd</samp>](## "management_interfaces.[].ipv6_nd") | Dictionary |  |  |  | IPv6 Neighbor Discovery protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cache</samp>](## "management_interfaces.[].ipv6_nd.cache") | Dictionary |  |  |  | Neighbor cache options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_capacity</samp>](## "management_interfaces.[].ipv6_nd.cache.dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 | Capacity of dynamic cache entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expire</samp>](## "management_interfaces.[].ipv6_nd.cache.expire") | Integer |  |  | Min: 1<br>Max: 65535 | Cache entries expiry in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_always</samp>](## "management_interfaces.[].ipv6_nd.cache.refresh_always") | Boolean |  |  |  | Force refresh on cache expiry. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ra</samp>](## "management_interfaces.[].ipv6_nd.ra") | Dictionary |  |  |  | Router Advertisement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_interfaces.[].ipv6_nd.ra.disabled") | Boolean |  |  |  | Disable Router Advertisement messages on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_accept</samp>](## "management_interfaces.[].ipv6_nd.ra.rx_accept") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "management_interfaces.[].ipv6_nd.ra.rx_accept.default_route") | Boolean |  |  |  | Accept default route from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_preference</samp>](## "management_interfaces.[].ipv6_nd.ra.rx_accept.route_preference") | Boolean |  |  |  | Accept route preference from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns_servers</samp>](## "management_interfaces.[].ipv6_nd.ra.dns_servers") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].ipv6_nd.ra.dns_servers.[]") | String |  |  |  | IPv6 address of DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;managed_config_flag</samp>](## "management_interfaces.[].ipv6_nd.managed_config_flag") | Boolean |  |  |  | Set the "Managed Address Configuration" (M) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "management_interfaces.[].ipv6_nd.prefixes") | List, items: Dictionary |  |  |  | IPv6 prefixes to include in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "management_interfaces.[].ipv6_nd.prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "management_interfaces.[].ipv6_nd.prefixes.[].valid_lifetime") | String |  |  |  | Valid lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "management_interfaces.[].ipv6_nd.prefixes.[].preferred_lifetime") | String |  |  |  | Preferred lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "management_interfaces.[].ipv6_nd.prefixes.[].no_autoconfig_flag") | Boolean |  |  |  | Indicate that the prefix cannot be used for stateless address autoconfiguration (SLAAC). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_config_flag</samp>](## "management_interfaces.[].ipv6_nd.other_config_flag") | Boolean |  |  |  | Set the "Other Stateful Configuration" (O) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_interfaces.[].type") | String |  | `oob` | Valid Values:<br>- <code>oob</code><br>- <code>inband</code> | For documentation purposes only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "management_interfaces.[].gateway") | String |  |  |  | IPv4 address of default gateway in management VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_gateway</samp>](## "management_interfaces.[].ipv6_gateway") | String |  |  |  | IPv6 address of default gateway in management VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "management_interfaces.[].mac_address") | String |  |  |  | MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_client_accept_default_route</samp>](## "management_interfaces.[].dhcp_client_accept_default_route") | Boolean |  |  |  | Install default-route obtained via DHCP. This is only applicable when `ip_address` is configured as `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "management_interfaces.[].lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "management_interfaces.[].lldp.transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "management_interfaces.[].lldp.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "management_interfaces.[].lldp.ztp_vlan") | Integer |  |  |  | ZTP vlan number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "management_interfaces.[].redundancy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback_delay</samp>](## "management_interfaces.[].redundancy.fallback_delay") | String |  |  |  | The duration to wait before falling back to the higher-priority interface.<br>Accepts a value between 0 and 3600 seconds, or the string `infinity` to disable fallback. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "management_interfaces.[].redundancy.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_state</samp>](## "management_interfaces.[].redundancy.monitor.link_state") | Boolean |  |  |  | Link state of interface.<br>`neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "management_interfaces.[].redundancy.monitor.neighbor") | Dictionary |  |  |  | To configure an IPv6 neighbor as monitor, `fallback_delay` must be set as infinity.<br>`neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.ipv6_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.interval") | Integer |  |  | Min: 1<br>Max: 300000 | Interval between neighbor probes in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.multiplier") | Integer |  |  | Min: 1<br>Max: 100 | Number of missed neighbor replies after which it is timed out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supervisor_1</samp>](## "management_interfaces.[].redundancy.supervisor_1") | Dictionary |  |  |  | Configuration for supervisor 1, including its primary and backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_management_interface</samp>](## "management_interfaces.[].redundancy.supervisor_1.primary_management_interface") | String | Required |  |  | Primary management interface name like 'Management1/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_management_interfaces</samp>](## "management_interfaces.[].redundancy.supervisor_1.backup_management_interfaces") | List, items: String | Required |  | Min Length: 1 | Backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].redundancy.supervisor_1.backup_management_interfaces.[]") | String |  |  |  | Management interface name like 'Management2/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supervisor_2</samp>](## "management_interfaces.[].redundancy.supervisor_2") | Dictionary |  |  |  | Configuration for supervisor 2, including its primary and backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_management_interface</samp>](## "management_interfaces.[].redundancy.supervisor_2.primary_management_interface") | String | Required |  |  | Primary management interface name like 'Management1/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_management_interfaces</samp>](## "management_interfaces.[].redundancy.supervisor_2.backup_management_interfaces") | List, items: String | Required |  | Min Length: 1 | Backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].redundancy.supervisor_2.backup_management_interfaces.[]") | String |  |  |  | Management interface name like 'Management2/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "management_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the management interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    management_interfaces:

        # Management Interface Name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # Interface Speed.
        speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">
        mtu: <int>

        # VRF Name.
        vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
        ipv6_enable: <bool>

        # IPv6 address with prefix length.
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
            dns_servers: # >=1 items

                # IPv6 address of DNS server.
              - <str>

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

        # For documentation purposes only.
        type: <str; "oob" | "inband"; default="oob">

        # IPv4 address of default gateway in management VRF.
        gateway: <str>

        # IPv6 address of default gateway in management VRF.
        ipv6_gateway: <str>

        # MAC address.
        mac_address: <str>

        # Install default-route obtained via DHCP. This is only applicable when `ip_address` is configured as `dhcp`.
        dhcp_client_accept_default_route: <bool>
        lldp:
          transmit: <bool>
          receive: <bool>

          # ZTP vlan number.
          ztp_vlan: <int>
        redundancy:

          # The duration to wait before falling back to the higher-priority interface.
          # Accepts a value between 0 and 3600 seconds, or the string `infinity` to disable fallback.
          fallback_delay: <str>
          monitor:

            # Link state of interface.
            # `neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence.
            link_state: <bool>

            # To configure an IPv6 neighbor as monitor, `fallback_delay` must be set as infinity.
            # `neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence.
            neighbor:
              ipv6_address: <str; required>

              # Interval between neighbor probes in milliseconds.
              interval: <int; 1-300000>

              # Number of missed neighbor replies after which it is timed out.
              multiplier: <int; 1-100>

          # Configuration for supervisor 1, including its primary and backup management interfaces.
          supervisor_1:

            # Primary management interface name like 'Management1/1'.
            primary_management_interface: <str; required>

            # Backup management interfaces.
            backup_management_interfaces: # >=1 items; required

                # Management interface name like 'Management2/1'.
              - <str>

          # Configuration for supervisor 2, including its primary and backup management interfaces.
          supervisor_2:

            # Primary management interface name like 'Management1/1'.
            primary_management_interface: <str; required>

            # Backup management interfaces.
            backup_management_interfaces: # >=1 items; required

                # Management interface name like 'Management2/1'.
              - <str>

        # Multiline EOS CLI rendered directly on the management interface in the final EOS configuration.
        eos_cli: <str>
    ```
