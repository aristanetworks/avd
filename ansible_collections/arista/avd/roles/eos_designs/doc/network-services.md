# Network Services Variables - VRFs/VLANs

- The network services variables provide an abstracted model to create L2 and L3 network services across the fabric.
- The network services are grouped by tenants. The definition of a tenant may vary between organizations.
  - e.g. Tenants can be organizations or departments.
- The tenant shares a common vni range for mac vrf assignment.
- The filtering model allows for granular deployment of network service to the fabric leveraging the tenant name and tags applied to the service definition.
  - This allows for the re-use of SVIs and VLANs across the fabric.

## Variables and Options

```yaml
# On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering. | Required (when mlag leafs in topology)
# The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + vrf_vni - 1
# The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.
mlag_ibgp_peering_vrfs:
  base_vlan: < 1-4000 | default -> 3000 >

# Specify RD type | Optional
# Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
# By configuring evpn_rd_type the Administrator subfield (first part of RD) can be set to other values.
#
# Note:
# RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
# For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.
# For 16-bit ASN/number the VNI can be a 32-bit number.
evpn_rd_type:
  admin_subfield: < "overlay_loopback" | "vtep_loopback" | "bgp_as" | < IPv4 Address > | <0-65535> | <0-4294967295> | default -> "overlay_loopback" >

# Specify RT type | Optional
# Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default
# By configuring evpn_rt_type the Administrator subfield (first part of RT) can be set to other values.
#
# Note:
# RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
# For 32-bit ASN/number the VNI can only be a 16-bit number.
# For 16-bit ASN/number the VNI can be a 32-bit number.
evpn_rt_type:
  admin_subfield: < "bgp_as" | "vni" | <0-65535> | <0-4294967295> | default -> "vni" >

# Internal vlan allocation order and range | Required
internal_vlan_order:
  allocation: < ascending or descending | default -> ascending >
  range:
    beginning: < vlan_id | default -> 1006 >
    ending: < vlan_id | default -> 1199 >

# MAC address-table aging time | Optional
# Use to change the EOS default of 300
mac_address_table:
  aging_time: < time_in_seconds >

# Optional profiles to apply on SVI interfaces
# Each profile can support all or some of the following keys according to your own needs.
# Keys are the same used under SVI.
svi_profiles:
  < profile_name >:
    mtu: < mtu >
    enabled: < true | false >
    ip_virtual_router_addresses:
      - < IPv4_address/Mask | IPv4_address >
      - < IPv4_address/Mask | IPv4_address >
    ip_address_virtual: < IPv4_address/Mask >
    ip_address_virtual_secondaries:
      - < IPv4_address/Mask >
      - < IPv4_address/Mask >
    igmp_snooping_enabled: < true | false | default true (eos) >
    ip_helpers:
      < IPv4 dhcp server IP >:
        source_interface: < interface-name >
        source_vrf: < VRF to originate DHCP relay packets to DHCP server >

# Dictionary of tenants, to define network services: L3 VRFs and L2 VLANS.

tenants:

  # Specify a tenant name. | Required
  # Tenant provide a construct to group L3 VRFs and L2 VLANs.
  # Networks services can be filtered by tenant name.
  < tenant_a >:

    # VXLAN Network Identifier for MAC VRF | Required.
    # VXLAN VNI is derived from the base number with simple addition.
    # e.g. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.
    mac_vrf_vni_base: < 10000-16770000 >

    # Base number for vlan_aware_bundle | Optional.
    # The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.
    vlan_aware_bundle_number_base: < number | default -> 0 >

    # MLAG IBGP peering per VRF | Optional
    # By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.
    # Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.
    # This setting can be overridden per VRF.
    enable_mlag_ibgp_peering_vrfs: < true | false >

    # Define L3 network services organized by vrf.
    vrfs:
      # VRF name | Required
      < tenant_a_vrf_1 >:

        # VRF VNI | Required.
        # The VRF VNI range is not limited, but it is recommended to keep vrf_vni <= 1024
        # It is necessary to keep [ vrf_vni + MLAG IBGP base_vlan ] < 4094 to support MLAG IBGP peering in VRF.
        # If vrf_vni > 1094 make sure to change mlag_ibgp_peering_vrfs: { base_vlan: < > } to a lower value (default 3000).
        # If vrf_vni > 10000 make sure to adjust mac_vrf_vni_base accordingly to avoid overlap.
        vrf_vni: < 1-1024 >

        # IP Helper for DHCP relay
        ip_helpers:
          < IPv4 dhcp server IP >:
            source_interface: < interface-name >
            source_vrf: < VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF >

        # MLAG IBGP peering per VRF | Optional
        # By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.
        # Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting
        enable_mlag_ibgp_peering_vrfs: < true | false >

        # Manually define the VLAN used on the MLAG pair for the iBGP session. | Optional
        # By default this parameter is calculated using the following formula: <base_vlan> + <vrf_vni> - 1
        mlag_ibgp_peering_vlan: <1-4096>

        # Enable VTEP Network diagnostics | Optional.
        # This will create a loopback with virtual source-nat enable to perform diagnostics from the switch.
        vtep_diagnostic:

          # Loopback interface number | Required (when vtep_diagnotics defined)
          loopback: < 2-2100 >

          # Loopback ip range, a unique ip is derived from this ranged and assigned
          # to each l3 leaf based on it's unique id. | Optional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)
          loopback_ip_range: < IPv4_address/Mask >

          # For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.
          # This only takes effect when loopback_ip_range is not defined. | Optional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)
          loopback_ip_pools:
            - pod: < pod_name >
              ipv4_pool: < IPv4_address/Mask >

        # Dictionary of SVIs | Required.
        # This will create both the L3 SVI and L2 VLAN based on filters applied to l3leaf and l2leaf.
        svis:

          # SVI interface id and VLAN id. | Required
          < 1-4096 >:

            # By default the vni will be derived from "mac_vrf_vni_base:"
            # The vni_override allows us to override this value and statically define it. | Optional
            vni_override: < 1-16777215 >

            # SVI profile to apply
            # If variables are configured in profile AND SVI, SVI information will overwrite profile.
            profile: < svi-profile-name >

            # vlan name | Required
            name: < name >

            # SVI description. | Optional
            description: < description | Default -> vlan name >

            # Tags leveraged for networks services filtering. | Required
            tags: [ < tag_1 >, < tag_2 > ]

            # Enable or disable interface
            enabled: < true | false >

            # Enable IGMP Snooping
            igmp_snooping_enabled: < true | false | default true (eos) >

            # ip address virtual to configure VXLAN Anycast IP address
            # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
            # Optional
            ip_address_virtual: < IPv4_address/Mask >
            ip_address_virtual_secondaries:
              - < IPv4_address/Mask >
              - < IPv4_address/Mask >

            # ip virtual-router address
            # note, also requires an IP address to be configured on the SVI where it is applied.
            # Optional
            ip_virtual_router_addresses:
              - < IPv4_address/Mask | IPv4_address >
              - < IPv4_address/Mask | IPv4_address >

            # IP Helper for DHCP relay
            ip_helpers:
              < IPv4 dhcp server IP >:
                source_interface: < interface-name >
                source_vrf: < VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF >

            # VXLAN | Optional - default true
            # Extend this SVI over VXLAN
            vxlan: < true | false | default -> true >

            # Define node specific configuration, such as unique IP addresses.
            nodes:
              < l3_leaf_inventory_hostname_1 >:
                # device unique IP address for node.
                ip_address: < IPv4_address/Mask >

                # EOS CLI rendered directly on the VLAN interface in the final EOS configuration
                # Overrides the setting on SVI level.
                raw_eos_cli: |
                  < multiline eos cli >

                # Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen
                # Overrides the setting on SVI level.
                structured_config: < dictionary >

              < l3_leaf_inventory_hostname_2 >:
                ip_address: < IPv4_address/Mask >

            # Defined interface MTU
            mtu: < mtu >

            # EOS CLI rendered directly on the VLAN interface in the final EOS configuration
            raw_eos_cli: |
              < multiline eos cli >

            # Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen
            structured_config: < dictionary >

          < 1-4096 >:
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >

        # List of L3 interfaces | Optional.
        # This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.
        l3_interfaces:
          - interfaces: [ <interface_name1>, <interface_name2>, <interface_name3> ]
            ip_addresses: [ <IPv4_address/Mask>, <IPv4_address/Mask>, <IPv4_address/Mask> ]
            nodes: [ < node_1 >, < node_2 >, < node_1 > ]
            description: < description >
            enabled: < true | false >
            mtu: < mtu >
            # EOS CLI rendered directly on the Ethernet interface in the final EOS configuration
            raw_eos_cli: |
              < multiline eos cli >
            # Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen
            structured_config: < dictionary >

          # For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
          - interfaces: [ <interface_name1.sub-if-id>, <interface_name2.sub-if-id> ]
            encapsulation_dot1q_vlan: [ <vlan id>, <vlan id> ]
            ip_addresses: [ <IPv4_address/Mask>, <IPv4_address/Mask> ]
            nodes: [ < node_1 >, < node_2 > ]
            description: < description >
            enabled: < true | false >
            mtu: < mtu - should only be used for platforms supporting mtu per subinterface >

        # Dictionary of static routes | Optional.
        # This will create static routes inside the tenant VRF.
        # If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.
        # If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.
        # This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.
        static_routes:
          - destination_address_prefix: < IPv4_address/Mask >
            gateway: < IPv4_address >
            distance: < 1-255 >
            tag: < 0-4294967295 >
            name: < description >
            metric: < 0-4294967295 >
            interface: < interface >
            nodes: [ < node_1 >, < node_2 >]

        # Non-selectively enabling or disabling redistribute static inside the VRF | Optional.
        redistribute_static: < true | false >

        # Dictionary of BGP peer definitions | Optional.
        # This will configure BGP neighbors inside the tenant VRF for peering with external devices.
        # The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.
        # Note, only ipv4 and ipv6 address families are currently supported in eos_designs.
        # For other address families, use custom_structured configuration with eos_cli_config_gen.
        bgp_peers:
          < IPv4_address or IPv6_address >:
            remote_as: < remote ASN >
            description: < description >
            password: < encrypted password >
            send_community: < standard | extended | large | all >
            next_hop_self: < true | false >
            maximum_routes: < 0-4294967294 >
            default_originate:
              always: < true | false >
            update_source: < interface >
            ebgp_multihop: < 1-255 >
            # Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
            nodes: [ < node_1 >, < node_2> ]
            # Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.
            # Next hop takes precedence over route_map_out.
            set_ipv4_next_hop: < IPv4_address >
            set_ipv6_next_hop: < IPv6_address >
            route_map_out: < route-map name >
            route_map_in: < route-map name >
            local_as: < local BGP ASN >
            weight: < 0-65535>

        bgp:
          # EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration
          raw_eos_cli: |
            < multiline eos cli >
          # Custom structured config added under router_bgp.vrfs.<vrf> for eos_cli_config_gen
          structured_config: < dictionary >

        # Optional configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families.
        additional_route_targets:
          - type: < import | export >
            address_family: < address_family >
            route_target: "< route_target >"
            # Nodes is optional. Default is all nodes where the VRF is defined.
            nodes: [ < node_1 >, < node_2> ]

        # EOS CLI rendered directly on the root level of the final EOS configuration
        raw_eos_cli: |
          < multiline eos cli >
        # Custom structured config for eos_cli_config_gen
        structured_config: < dictionary >

      < tenant_a_vrf_2 >:
        vrf_vni: < 1-1024 >
        svis:
          < 1-4096 >:
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
          < 1-4096 >:
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >

   # Define L2 network services organized by vlan id.
    l2vlans:

      # VLAN id.
      < 1-4096 >:
        # By default the vni will be derived from "mac_vrf_vni_base:"
        # The vni_override, allows to override this value and statically define it.
        vni_override: < 1-16777215 >

        # VLAN name.
        name: < description >

        # Tags leveraged for networks services filtering.
        tags: [ < tag_1 >, < tag_2 > ]

        # VXLAN | Optional - default true
        # Extend this L2VLAN over VXLAN
        vxlan: < true | false | default -> true >

      < 1-4096 >:
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
        # Activate or deactivate IGMP snooping | Optional, default is true
        igmp_snooping_enabled: < true | false >

  < tenant_a >:
    mac_vrf_vni_base: < 10000-16770000 >
    vrfs:
      < tenant_b_vrf_1 >:
        vrf_vni: < 1-1024 >
        vtep_diagnostic:
          loopback: < 2-2100 >
          loopback_ip_range: < IPv4_address/Mask >
        svis:
          < 1-4096 >:
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
          < 1-4096 >:
            vni_override: < 1-16777215 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
    l2vlans:
      < 1-4096 >:
        vni_override: < 1-16777215 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
      < 1-4096 >:
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
```

## Examples

```yaml
# mlag_ibgp_peering_vrfs:
#   base_vlan: 3000

tenants:
  Tenant_A:
    mac_vrf_vni_base: 10000
    vrfs:
      Tenant_A_OP_Zone:
        vrf_vni: 10
        vtep_diagnostic:
          loopback: 100
          loopback_ip_range: 10.255.1.0/24
        svis:
          110:
            name: Tenant_A_OP_Zone_1
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.1.10.0/24
            mtu: 1400
          111:
            vni_override: 50111
            name: Tenant_A_OP_Zone_2
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.1.11.0/24
          112:
            name: Tenant_A_OP_Zone_3
            tags: [ DC1_LEAF2 ]
            enabled: true
            ip_virtual_router_addresses:
              - 10.1.12.1
              - 10.2.12.1/24
            nodes:
              DC1-LEAF2A:
                ip_address: 10.1.12.2/24
              DC1-LEAF2B:
                ip_address: 10.1.12.3/24
          113:
            name: Tenant_A_OP_Zone_WAN
            tags: [ DC1_BL1 ]
            enabled: true
            nodes:
              DC1-BL1A:
                ip_address: 10.1.13.1/24
              DC1-BL1B:
                ip_address: 10.1.13.2/24
      Tenant_A_WEB_Zone:
        vrf_vni: 11
        svis:
          120:
            name: Tenant_A_WEB_Zone_1
            tags: [ web, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.20.0/24
          121:
            name: Tenant_A_WEBZone_2
            tags: [ web ]
            enabled: true
            ip_address_virtual: 10.1.21.0/24
      Tenant_A_APP_Zone:
        vrf_vni: 12
        svis:
          130:
            name: Tenant_A_APP_Zone_1
            tags: [ app, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.30.0/24
          131:
            name: Tenant_A_APP_Zone_2
            tags: [ app ]
            enabled: true
            ip_address_virtual: 10.1.31.0/24
      Tenant_A_DB_Zone:
        vrf_vni: 13
        svis:
          140:
            name: Tenant_A_DB_BZone_1
            tags: [ db, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.40.0/24
          141:
            name: Tenant_A_DB_Zone_2
            tags: [ db ]
            enabled: true
            ip_address_virtual: 10.1.41.0/24
      Tenant_A_WAN_Zone:
        vrf_vni: 14
        svis:
          150:
            name: Tenant_A_WAN_Zone_1
            tags: [ wan ]
            enabled: true
            ip_address_virtual: 10.1.40.0/24
    l2vlans:
      160:
        vni_override: 55160
        name: Tenant_A_VMOTION
        tags: [ vmotion ]
      161:
        name: Tenant_A_NFS
        tags: [ nfs ]

  Tenant_B:
    mac_vrf_vni_base: 20000
    vrfs:
      Tenant_B_OP_Zone:
        vrf_vni: 20
        svis:
          210:
            name: Tenant_B_OP_Zone_1
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.2.10.0/24
          211:
            name: Tenant_B_OP_Zone_2
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.2.11.0/24
      Tenant_B_WAN_Zone:
        vrf_vni: 21
        svis:
          250:
            name: Tenant_B_WAN_Zone_1
            tags: [ wan ]
            enabled: true
            ip_address_virtual: 10.2.50.0/24
```
