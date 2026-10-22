<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopbacks</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks") | List, items: Dictionary |  |  |  | List of Loopback interfaces.<br>This will create Loopback interfaces inside the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].node") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].loopback") | Integer | Required |  | Min: 0<br>Max: 8191 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ip_address") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ipv6_addresses") | List, items: String |  |  | Min Length: 1 | IPv6 addresses with prefix length, e.g., '2001:db8::1/64'.<br>Can be used instead of or together with `ip_address`.<br>At least one of `ip_address` or `ipv6_addresses` must be set.<br>For IPv6 virtual source NAT, AVD uses the first value from this input list when this loopback is selected. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ospf") | Dictionary |  |  |  | OSPFv2 interface configuration.<br>Requires `ip_address` to be set when OSPF is enabled on both the VRF and this loopback. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ospf.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].ospf.area") | String |  | `0.0.0.0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_forwarding</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].hardware_forwarding") | Boolean |  |  |  | Enable hardware forwarding for this loopback. This is required for correct forwarding in VRFs without physical interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].loopbacks.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Loopback interface in the final EOS configuration.<br> |
    | [<samp>network_services</samp>](## "network_services") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "network_services.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "network_services.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "network_services.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopbacks</samp>](## "network_services.[].vrfs.[].loopbacks") | List, items: Dictionary |  |  |  | List of Loopback interfaces.<br>This will create Loopback interfaces inside the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "network_services.[].vrfs.[].loopbacks.[].node") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "network_services.[].vrfs.[].loopbacks.[].loopback") | Integer | Required |  | Min: 0<br>Max: 8191 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "network_services.[].vrfs.[].loopbacks.[].ip_address") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "network_services.[].vrfs.[].loopbacks.[].ipv6_addresses") | List, items: String |  |  | Min Length: 1 | IPv6 addresses with prefix length, e.g., '2001:db8::1/64'.<br>Can be used instead of or together with `ip_address`.<br>At least one of `ip_address` or `ipv6_addresses` must be set.<br>For IPv6 virtual source NAT, AVD uses the first value from this input list when this loopback is selected. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "network_services.[].vrfs.[].loopbacks.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].vrfs.[].loopbacks.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].loopbacks.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "network_services.[].vrfs.[].loopbacks.[].ospf") | Dictionary |  |  |  | OSPFv2 interface configuration.<br>Requires `ip_address` to be set when OSPF is enabled on both the VRF and this loopback. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].loopbacks.[].ospf.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "network_services.[].vrfs.[].loopbacks.[].ospf.area") | String |  | `0.0.0.0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_forwarding</samp>](## "network_services.[].vrfs.[].loopbacks.[].hardware_forwarding") | Boolean |  |  |  | Enable hardware forwarding for this loopback. This is required for correct forwarding in VRFs without physical interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].loopbacks.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Loopback interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of Loopback interfaces.
            # This will create Loopback interfaces inside the VRF.
            loopbacks:
              - node: <str; required>
                loopback: <int; 0-8191; required>

                # IPv4 address/Mask.
                ip_address: <str>

                # IPv6 addresses with prefix length, e.g., '2001:db8::1/64'.
                # Can be used instead of or together with `ip_address`.
                # At least one of `ip_address` or `ipv6_addresses` must be set.
                # For IPv6 virtual source NAT, AVD uses the first value from this input list when this loopback is selected.
                ipv6_addresses: # >=1 items

                    # IPv6 address/Mask.
                  - <str>
                description: <str>
                enabled: <bool; default=True>

                # OSPFv2 interface configuration.
                # Requires `ip_address` to be set when OSPF is enabled on both the VRF and this loopback.
                ospf:
                  enabled: <bool; default=False>

                  # OSPF area ID.
                  area: <str; default="0.0.0.0">

                # Enable hardware forwarding for this loopback. This is required for correct forwarding in VRFs without physical interfaces.
                hardware_forwarding: <bool>

                # EOS CLI rendered directly on the Loopback interface in the final EOS configuration.
                raw_eos_cli: <str>
    network_services:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of Loopback interfaces.
            # This will create Loopback interfaces inside the VRF.
            loopbacks:
              - node: <str; required>
                loopback: <int; 0-8191; required>

                # IPv4 address/Mask.
                ip_address: <str>

                # IPv6 addresses with prefix length, e.g., '2001:db8::1/64'.
                # Can be used instead of or together with `ip_address`.
                # At least one of `ip_address` or `ipv6_addresses` must be set.
                # For IPv6 virtual source NAT, AVD uses the first value from this input list when this loopback is selected.
                ipv6_addresses: # >=1 items

                    # IPv6 address/Mask.
                  - <str>
                description: <str>
                enabled: <bool; default=True>

                # OSPFv2 interface configuration.
                # Requires `ip_address` to be set when OSPF is enabled on both the VRF and this loopback.
                ospf:
                  enabled: <bool; default=False>

                  # OSPF area ID.
                  area: <str; default="0.0.0.0">

                # Enable hardware forwarding for this loopback. This is required for correct forwarding in VRFs without physical interfaces.
                hardware_forwarding: <bool>

                # EOS CLI rendered directly on the Loopback interface in the final EOS configuration.
                raw_eos_cli: <str>
    ```
