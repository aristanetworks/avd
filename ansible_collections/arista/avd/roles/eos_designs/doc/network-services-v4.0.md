# Network Services Variables - VRFs/VLANs

- The network services variables provide an abstracted model to create L2 and L3 network services across the fabric.
- The network services are grouped by tenants. The definition of a tenant may vary between organizations.
  - e.g. Tenants can be organizations or departments.
- The tenant shares a common vni range for mac vrf assignment.
- The filtering model allows for granular deployment of network service to the fabric leveraging the tenant name and tags applied to the service definition.
  - This allows for the re-use of SVIs and VLANs across the fabric.

## Variables and Options

### Tenants Keys

```yaml
# Define network services keys, to define grouping of network services.
# This provides the ability to define various keys of your choice to better organize/group your data.
# This should be defined in top level group_var for the fabric.
network_services_keys:
  - name: < key_1 >
  - name: < key_2 >
```

```yaml
# Example
# The below key/pair values are the role defaults.
network_services_keys:
  - name: tenants
```

```yaml
# On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering. | Required (when mlag leafs in topology)
# The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1
# Depending on the values of vrf_id / vrf_id it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
# The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.
mlag_ibgp_peering_vrfs:
  base_vlan: < 1-4000 | default -> 3000 >

# Specify RD type | Optional
# Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
# By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.
#
# Note:
# RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
# For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.
# For 16-bit ASN/number the VNI can be a 32-bit number.
overlay_rd_type:
  admin_subfield: < "vtep_loopback" | "bgp_as" | < IPv4 Address > | <0-65535> | <0-4294967295> | default -> <overlay_loopback_ip> >

# Specify RT type | Optional
# Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default
# By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.
#
# Note:
# RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
# For 32-bit ASN/number the VNI can only be a 16-bit number.
# For 16-bit ASN/number the VNI can be a 32-bit number.
overlay_rt_type:
  admin_subfield: < "bgp_as" | <0-65535> | <0-4294967295> | default -> <mac_vrf_id> >

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
# Svi_profiles can refer to another svi_profiles to inherit settings in up to two levels (svi->profile->parent_profile).
svi_profiles:
  - profile: < profile_name >
    parent_profile: < svi_profile_name >
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
      - ip_helper: < IPv4 dhcp server IP >
        source_interface: < interface-name >
        source_vrf: < VRF to originate DHCP relay packets to DHCP server >

# Dictionary of network services: L3 VRFs and L2 VLANS.
# The network service key from network_services_keys
< network_services_keys.key_1 >:
  # Specify a tenant name. | Required
  # Tenant provide a construct to group L3 VRFs and L2 VLANs.
  # Networks services can be filtered by tenant name.
  - name: < tenant_a >

    # Base number for MAC VRF VXLAN Network Identifier | Required with VXLAN
    # VXLAN VNI is derived from the base number with simple addition.
    # e.g. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.
    mac_vrf_vni_base: < 10000-16770000 >

    # Base number for MAC VRF RD/RT ID | Required unless mac_vrf_vni_base is set.
    # ID is derived from the base number with simple addition.
    # e.g. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.
    mac_vrf_id_base: < 10000-16770000 | default -> <mac_vrf_vni_base> >

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
      # vrf "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,
      # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
      # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
      - name: < tenant_a_vrf_1 >

        # Optional
        description: < vrf_description >

        # VRF VNI | Optional (required if "vrf_id" is not set).
        # The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG IBGP peering vlan id.
        # See "mlag_ibgp_peering_vrfs.base_vlan" for details.
        # If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.
        vrf_vni: < 1-1024 | default -> vrf_id >

        # VRF ID | Optional (required if "vrf_vni" is not set)
        # "vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.
        # "vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni
        # "vrf_id" is preferred over "vrf_vni" for MLAG IBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details
        vrf_id: < 1-1024 >

        # MLAG IBGP Peering IPv4 Pool | Optional
        # The subnet used for iBGP peering in the VRF.
        # Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch
        # If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used
        mlag_ibgp_peering_ipv4_pool: < IPv4_address/Mask >

        # IP Helper for DHCP relay
        ip_helpers:
          - ip_helper: < IPv4 dhcp server IP >
            source_interface: < interface-name >
            source_vrf: < VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF >

        # MLAG IBGP peering per VRF | Optional
        # By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.
        # Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting
        enable_mlag_ibgp_peering_vrfs: < true | false >

        # Manually define the VLAN used on the MLAG pair for the iBGP session. | Optional
        # By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1
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

        # Dictionary for router OSPF configuration | Optional.
        # This will create an ospf routing instance in the tenant VRF. If there is no nodes definition, the ospf instance will be
        # created on all leafs where the vrf is deployed. This will also cause automatic ospf redistribution into bgp unless
        # explicitly turned off with "redistribute_ospf: false".
        ospf:
          enabled: < true | false >
          process_id: < int, Default -> vrf_id >
          router_id: < router-id, Default -> switch router_id >
          max_lsa: < int >
          bfd: < true | false, Default -> false >
          redistribute_bgp:
            enabled: < true | false, Default -> true >
            route_map: < route-map name >
          nodes:
            - < hostname1 >
            - < hostname2 >

        # Non-selectively enabling or disabling redistribute ospf inside the VRF | Optional.
        redistribute_ospf: < true | false, Default -> true >

        # Dictionary of SVIs | Required.
        # This will create both the L3 SVI and L2 VLAN based on filters applied to l3leaf and l2leaf.
        svis:

          # SVI interface id and VLAN id. | Required
          - id: < 1-4096 >

            # By default the vni will be derived from "mac_vrf_vni_base"
            # The vni_override allows us to override this value and statically define it. | Optional
            vni_override: < 1-16777215 >

            # By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"
            # The rt_override allows us to override this value and statically define it. | Optional
            rt_override: < 1-16777215 | default -> vni_override >

            # SVI profile to apply
            # If variables are configured in profile AND SVI, SVI information will overwrite profile.
            profile: < svi-profile-name >

            # vlan name | Required
            name: < name >

            # SVI description. | Optional
            description: < description | Default -> vlan name >

            # Tags leveraged for networks services filtering. | Optional
            # Tags are matched against "filter.tags" defined under Fabric Topology variables
            # Tags are also matched against the "node_group" name under Fabric Topology variables
            tags: [ < tag_1 >, < tag_2 > | default -> all ]

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
              - ip_helper: < IPv4 dhcp server IP >
                source_interface: < interface-name >
                source_vrf: < VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF >

            # VXLAN | Optional - default true
            # Extend this SVI over VXLAN
            vxlan: < true | false | default -> true >

            # Define node specific configuration, such as unique IP addresses.
            nodes:
              - node: < l3_leaf_inventory_hostname_1 >
                # device unique IP address for node.
                ip_address: < IPv4_address/Mask >

                # EOS CLI rendered directly on the VLAN interface in the final EOS configuration
                # Overrides the setting on SVI level.
                raw_eos_cli: |
                  < multiline eos cli >

                # Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen
                # Overrides the setting on SVI level.
                structured_config: < dictionary >

              - node: < l3_leaf_inventory_hostname_2 >
                ip_address: < IPv4_address/Mask >

            # Defined interface MTU
            mtu: < mtu >

            # OSPF interface configuration
            ospf:
              enabled: < true | false >
              point_to_point: < true | false, Default -> false >
              area: < ospf area id, Default -> 0 >
              cost: < ospf link cost >
              authentication: < simple | message-digest >
              simple_auth_key: < password used with simple authentication >
              message_digest_keys:
                - id: < int >
                  hash_algorithm: < md5 | sha1 | sha256 | sha384 | sha512, Default -> sha512 >
                  key: < key password >

            # Structured configuration and eos cli commands rendered on router_bgp.vlans
            # This configuration will not be applied to vlan aware bundles
            bgp:
              raw_eos_cli: |
                < multiline eos cli >
              structured_config: < dictionary >

            # EOS CLI rendered directly on the VLAN interface in the final EOS configuration
            raw_eos_cli: |
              < multiline eos cli >

            # Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen
            structured_config: < dictionary >

          - id: < 1-4096 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >

        # List of L3 interfaces | Optional.
        # This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses and descriptions (if used) must match.
        l3_interfaces:
          - interfaces: [ <interface_name1>, <interface_name2>, <interface_name3> ]
            ip_addresses: [ <IPv4_address/Mask>, <IPv4_address/Mask>, <IPv4_address/Mask> ]
            nodes: [ < node_1 >, < node_2 >, < node_1 > ]
            description: < description >
            # `descriptions` has precedence over `description`
            descriptions: [ <description1>, <description2>, description3> ]
            enabled: < true | false >
            mtu: < mtu >
            # EOS CLI rendered directly on the Ethernet interface in the final EOS configuration
            raw_eos_cli: |
              < multiline eos cli >
            # Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen
            structured_config: < dictionary >

            ospf:
              enabled: < true | false >
              point_to_point: < true | false, Default -> true >
              area: < ospf area id, Default -> 0 >
              cost: < ospf link cost >
              authentication: < simple | message-digest >
              simple_auth_key: < password used with simple authentication >
              message_digest_keys:
                - id: < int >
                  hash_algorithm: < md5 | sha1 | sha256 | sha384 | sha512, Default -> sha512 >
                  key: < key password >

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

        # Non-selectively enabling or disabling redistribute static inside the VRF | Optional.
        redistribute_static: < true | false >

        # Dictionary of BGP peer definitions | Optional.
        # This will configure BGP neighbors inside the tenant VRF for peering with external devices.
        # The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.
        # Note, only ipv4 and ipv6 address families are currently supported in eos_designs.
        # For other address families, use custom_structured configuration with eos_cli_config_gen.
        bgp_peers:
          - ip_address: < IPv4_address or IPv6_address >
            remote_as: < remote ASN >
            description: < description >
            password: < encrypted password >
            send_community: < standard | extended | large | all >
            next_hop_self: < true | false >
            timers: < keepalive_hold_timer_values >
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
            prefix_list_in: < prefix_list_name >
            prefix_list_out: < prefix_list_name >
            local_as: < local BGP ASN >
            weight: < 0-65535>
            bfd: < true | false >

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

      - name: < tenant_a_vrf_2 >
        vrf_vni: < 1-1024 >
        vrf_id: < 1-1024 >
        svis:
          - id: < 1-4096 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
          - id: < 1-4096 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >

   # Define L2 network services organized by vlan id.
    l2vlans:

      # VLAN id.
      - id: < 1-4096 >
        # By default the vni will be derived from "mac_vrf_vni_base"
        # The vni_override, allows to override this value and statically define it.
        vni_override: < 1-16777215 >

        # By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"
        # The rt_override allows us to override this value and statically define it. | Optional
        rt_override: < 1-16777215 | default -> vni_override >

        # VLAN name | Required
        name: < description >

        # Tags leveraged for network services filtering. | Optional
        # Tags are matched against "filter.tags" defined under Fabric Topology variables
        # Tags are also matched against the "node_group" name under Fabric Topology variables
        tags: [ < tag_1 >, < tag_2 > | default -> all ]

        # VXLAN | Optional - default true
        # Extend this L2VLAN over VXLAN
        vxlan: < true | false | default -> true >

      - id: < 1-4096 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
        # Activate or deactivate IGMP snooping | Optional, default is true
        igmp_snooping_enabled: < true | false >

        # Structured configuration and eos cli commands rendered on router_bgp.vlans
        # This configuration will not be applied to vlan aware bundles
        bgp:
          raw_eos_cli: |
            < multiline eos cli >
          structured_config: < dictionary >

  - name: < tenant_b >
    mac_vrf_vni_base: < 10000-16770000 >
    vrfs:
      - name: < tenant_b_vrf_1 >
        vrf_vni: < 1-1024 >
        vtep_diagnostic:
          loopback: < 2-2100 >
          loopback_ip_range: < IPv4_address/Mask >
        svis:
          - id: < 1-4096 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
          - id: < 1-4096 >
            vni_override: < 1-16777215 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
    l2vlans:
      - id: < 1-4096 >
        vni_override: < 1-16777215 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
      - id: < 1-4096 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]

< network_services_keys.key_2 >:
  - name: < tenant_c >
    mac_vrf_vni_base: < 10000-16770000 >
    vrfs:
      - name: < tenant_b_vrf_1 >
        vrf_vni: < 1-1024 >
        vtep_diagnostic:
          loopback: < 2-2100 >
          loopback_ip_range: < IPv4_address/Mask >
        svis:
          - id: < 1-4096 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
          - id: < 1-4096 >
            vni_override: < 1-16777215 >
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
    l2vlans:
      - id: < 1-4096 >
        vni_override: < 1-16777215 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
      - id: < 1-4096 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
```

## Examples

```yaml
# mlag_ibgp_peering_vrfs:
#   base_vlan: 3000

network_services_keys:
  - name: dc1_tenants

dc1_tenants:
  - name: Tenant_A
    mac_vrf_vni_base: 10000
    vrfs:
      - name: Tenant_A_OP_Zone
        vrf_vni: 10
        vtep_diagnostic:
          loopback: 100
          loopback_ip_range: 10.255.1.0/24
        svis:
          - id: 110
            name: Tenant_A_OP_Zone_1
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.1.10.0/24
            mtu: 1400
          - id: 111
            vni_override: 50111
            name: Tenant_A_OP_Zone_2
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.1.11.0/24
          - id: 112
            name: Tenant_A_OP_Zone_3
            tags: [ DC1_LEAF2 ]
            enabled: true
            ip_virtual_router_addresses:
              - 10.1.12.1
              - 10.2.12.1/24
            nodes:
              - name: DC1-LEAF2A
                ip_address: 10.1.12.2/24
              - name: DC1-LEAF2B
                ip_address: 10.1.12.3/24
          - id: 113
            name: Tenant_A_OP_Zone_WAN
            tags: [ DC1_BL1 ]
            enabled: true
            nodes:
              - name: DC1-BL1A
                ip_address: 10.1.13.1/24
              - name: DC1-BL1B
                ip_address: 10.1.13.2/24
      - name: Tenant_A_WEB_Zone
        vrf_vni: 11
        svis:
          - id: 120
            name: Tenant_A_WEB_Zone_1
            tags: [ web, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.20.0/24
          - id: 121
            name: Tenant_A_WEBZone_2
            tags: [ web ]
            enabled: true
            ip_address_virtual: 10.1.21.0/24
      - name: Tenant_A_APP_Zone
        vrf_vni: 12
        svis:
          - id: 130
            name: Tenant_A_APP_Zone_1
            tags: [ app, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.30.0/24
          - id: 131
            name: Tenant_A_APP_Zone_2
            tags: [ app ]
            enabled: true
            ip_address_virtual: 10.1.31.0/24
      - name: Tenant_A_DB_Zone
        vrf_vni: 13
        svis:
          - id: 140
            name: Tenant_A_DB_BZone_1
            tags: [ db, erp1 ]
            enabled: true
            ip_address_virtual: 10.1.40.0/24
          - id: 141
            name: Tenant_A_DB_Zone_2
            tags: [ db ]
            enabled: true
            ip_address_virtual: 10.1.41.0/24
      - name: Tenant_A_WAN_Zone
        vrf_vni: 14
        svis:
          - id: 150
            name: Tenant_A_WAN_Zone_1
            tags: [ wan ]
            enabled: true
            ip_address_virtual: 10.1.40.0/24
    l2vlans:
      - id: 160
        vni_override: 55160
        name: Tenant_A_VMOTION
        tags: [ vmotion ]
      - id: 161
        name: Tenant_A_NFS
        tags: [ nfs ]

  - name: Tenant_B
    mac_vrf_vni_base: 20000
    vrfs:
      - name: Tenant_B_OP_Zone
        vrf_vni: 20
        svis:
          - id: 210
            name: Tenant_B_OP_Zone_1
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.2.10.0/24
          - id: 211
            name: Tenant_B_OP_Zone_2
            tags: [ opzone ]
            enabled: true
            ip_address_virtual: 10.2.11.0/24
      - name: Tenant_B_WAN_Zone
        vrf_vni: 21
        svis:
          - id: 250
            name: Tenant_B_WAN_Zone_1
            tags: [ wan ]
            enabled: true
            ip_address_virtual: 10.2.50.0/24
```
