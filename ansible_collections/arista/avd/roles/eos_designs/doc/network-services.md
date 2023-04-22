# Network Services Variables - VRFs/VLANs

- The network services variables provide an abstracted model to create L2 and L3 network services across the fabric.
- The network services are grouped by tenants. The definition of a tenant may vary between organizations.
  - e.g. Tenants can be organizations or departments.
- The tenant shares a common vni range for mac vrf assignment.
- The filtering model allows for granular deployment of network service to the fabric leveraging the tenant name and tags applied to the service definition.
  - This allows for the re-use of SVI/VLAN IDs across the fabric.
  - An error will be returned at runtime in case of duplicate SVI/VLAN IDs, VRF names or VNIs targeted towards the same device.

## Variables and Options

### Global Network Services Parameters

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
# Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
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
  admin_subfield: < "vtep_loopback" | "bgp_as" | "switch_id" | < IPv4_address > | <0-65535> | <0-4294967295> | default -> <overlay_loopback_ip> >
  # Offset can only be used if admin_subfield is an interger between <0-4294967295> or "switch_id".
  # Total value of admin_subfield + admin_subfield_offset must be <= 4294967295.
  admin_subfield_offset: < int > | default -> 0 >

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
```

### Tenant Network Service Definitions

```yaml
# Dictionary of network services: L3 VRFs and L2 VLANS.
# The network service key from network_services_keys
< network_services_keys.key_1 >:
  # Specify a tenant name. | Required
  # Tenant provide a construct to group L3 VRFs and L2 VLANs.
  # Networks services can be filtered by tenant name.
  < tenant_a >:

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

    # Dictionary of BGP peer groups definitions | Optional.
    # This will configure BGP peer groups to be used inside the tenant for peering with external devices.
    # Since BGP peer groups are configured at higher BGP level, shared between VRFs,
    # peer_group names should not overlap between VRFs.
    bgp_peer_groups:
      - name: < BGP peer group name >
        remote_as: < bgp_as >
        description: "< description as string >"
        send_community: < standard | extended | large | all >
        next_hop_self: < true | false >
        maximum_routes: < 0-4294967294 >
        default_originate:
          enabled: < true | false >
          always: < true | false >
        # Nodes is required to restrict configuration of BGP peer groups to certain nodes in the network.
        # If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.
        nodes: [ < node_1 >, < node_2 > ]
        update_source: < interface >
        bfd: < true | false >
        ebgp_multihop: < 1-255 >
        route_map_out: < route-map name >
        route_map_in: < route-map name >
        local_as: < local BGP ASN >

    # Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant | Optional
    # - Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication
    # - Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:
    #   < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.
    # - The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.
    # - Enables `redistribute igmp` on the router bgp MAC VRF.
    # - When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.
    evpn_l2_multicast:
      enabled: < true | false >
      underlay_l2_multicast_group_ipv4_pool: < IPv4_address/Mask >
      underlay_l2_multicast_group_ipv4_pool_offset: < int >

    # Enable L3 Multicast for all SVIs and l3vlans within Tenant | Optional
    # - In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)
    # - Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication
    # - Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:
    #   < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.
    # - The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.
    # - If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.
    # - Enables `evpn multicast` on the router bgp VRF.
    # - When enabled on an SVI:
    #     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.
    #     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.
    #     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF
    evpn_l3_multicast:
      enabled: < true | false >
      evpn_underlay_l3_multicast_group_ipv4_pool: < IPv4_address/Mask > # Required
      evpn_underlay_l3_multicast_group_ipv4_pool_offset: < int > # Optional
      evpn_peg:
        # For each group of nodes, allow configuration of EVPN PEG options | Optional
        # The first group of settings where the device's hostname is present in the 'nodes' list will be used.
        - nodes: [ < node_1 >, < node_2 >, < node_N > ]                # Optional - will apply to all nodes with RP addresses configured if not set.
          transit: < true | false >                    # Enable EVPN PEG transit mode
    pim_rp_addresses:
      # For each group of nodes, allow configuration of RP Addresses & associated groups
      - rps: [ < rp_address_1 >, < rp_address_2 > ]                  # A minimum of one RP must be specified
        nodes: [ < node_1 >, < node_2 >, < node_N > ]                # Optional - will apply to all nodes if not set.
        groups: [ < group_prefix_1/mask >, < group_prefix_1/mask > ] # Optional

    # Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.
    # When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.
    igmp_snooping_querier:
      # Will be enabled automatically if "evpn_l2_multicast" is enabled.
       enabled: < true | false >
       source_address: < ipv4_address -> default ip address of Loopback0 >
       version: < 1, 2, 3 -> default 2 (EOS) >

    # Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains.
    evpn_l2_multi_domain: < true | false | default --> true >

    # Define L3 network services organized by vrf.
    vrfs:
      # VRF name | Required
      # vrf "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,
      # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
      # Static-routes and vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
      < tenant_a_vrf_1 >:

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
          < IPv4 dhcp server IP >:
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

          # Loopback interface number | Required (when vtep_diagnostic defined)
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

        # Explicitly enable or disable evpn_l3_multicast to override setting of tenants.<tenant>.evpn_l3_multicast.enabled.
        # Allow override of tenants.<tenant>.evpn_l3_multicast.node_settings
        evpn_l3_multicast:
          enabled: < true | false >
          evpn_peg:
            # For each group of nodes, allow configuration of EVPN PEG features | Optional
            - nodes: [ < node_1 >, < node_2 >, < node_N > ]                # Optional - will apply to all nodes with RP addresses configured if not set.
              transit: < true | false | default false >                    # Enable EVPN PEG transit mode
        pim_rp_addresses:                                                  # For each group of nodes, allow configuration of RP Addresses & associated groups
          - rps: [ < rp_address_1 >, < rp_address_2 > ]                    # A minimum of one RP must be specified
            nodes: [ < node_1 >, < node_2 >, < node_N > ]                  # Optional - will apply to all nodes if not set.
            groups: [ < group_prefix_1/mask >, < group_prefix_1/mask > ]   # Optional

        # Non-selectively enabling or disabling redistribute ospf inside the VRF | Optional.
        redistribute_ospf: < true | false, Default -> true >

        # Explicitly extend all VLANs/VLAN-Aware Bundles inside the VRF to remote EVPN domains.
        # Overrides tenants.<tenant>.evpn_l2_multi_domain.
        evpn_l2_multi_domain: < true | false >

        # Dictionary of SVIs | Required.
        # This will create both the L3 SVI and L2 VLAN based on filters applied to l3leaf and l2leaf.
        # Any SVI setting, defined under svis[svi] can also be defined under the svis[svi].nodes[node]
        svis:

          # SVI interface id and VLAN id. | Required
          < 1-4096 >:

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

            # Trunk Groups | optional
            # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group
            # Requires "enable_trunk_groups: true"
            trunk_groups: [ < trunk_group_1 >, < trunk_group_2 > ]

            # Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.
            # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.
            evpn_l2_multicast:
              enabled: < true | false >

            # Explicitly enable or disable evpn_l3_multicast to override setting of tenants <tenant>.evpn_l3_multicast.enabled and
            # tenants.<tenant>.vrfs.<vrf>.evpn_l3_multicast.enabled
            evpn_l3_multicast:
              enabled: < true | false >

            # Enable IGMP Snooping
            igmp_snooping_enabled: < true | false | default true (EOS) >

            # Enable igmp snooping querier, by default using IP address of Loopback 0.
            # When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.
            igmp_snooping_querier:
              # Will be enabled automatically if "evpn_l2_multicast" is enabled.
              enabled: < true | false | default false >
              source_address: < ipv4_address -> default ip address of Loopback0 >
              version: < 1, 2, 3 -> default 2 (EOS) >

            # ip address virtual to configure VXLAN Anycast IP address
            # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
            # Optional
            ip_address_virtual: < IPv4_address/Mask >
            ip_address_virtual_secondaries:
              - < IPv4_address/Mask >

            # ipv6 address virtuals to configure VXLAN Anycast IP address | Optional
            # The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"
            # If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured
            ipv6_address_virtual: < IPv6_address/Mask >
            # The new "ipv6_address_virtuals" key support multiple virtual ip addresses.
            ipv6_address_virtuals:
              - < IPv6_address/Mask >
              - < IPv6_address/Mask >

            # ip virtual-router address
            # note, also requires an IP address to be configured on the SVI where it is applied.
            # Optional
            # When ip_address_virtual and ip_virtual_router_addresses are defined in an SVI the node that was defined with the ip_address
            # will be configured with ip_virtual_router_addresses. For ip_virtual_router_addresses to be configured, ip_address must be defined
            ip_virtual_router_addresses:
              - < IPv4_address/Mask | IPv4_address >

            # ipv6 virtual-router address
            # note, also requires an IPv6 address to be configured on the SVI where it is applied.
            # Optional
            # When ipv6_address_virtual and ipv6_virtual_router_addresses are defined in an SVI the node that was defined with the ipv6_address
            # will be configured with ipv6_virtual_router_addresses. For ipv6_virtual_router_addresses to be configured, ipv6_address must be defined
            ipv6_virtual_router_addresses:
              - < IPv6_address >

            # IP Helper for DHCP relay
            ip_helpers:
              < IPv4 dhcp server IP >:
                source_interface: < interface-name >
                source_vrf: < VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF >

            # VXLAN | Optional - default true
            # Extend this SVI over VXLAN
            vxlan: < true | false | default -> true >

            # Explicitly extend this VLAN to remote EVPN domains.
            # Overrides tenants.<tenant>.evpn_l2_multi_domain.
            # Overrides tenants.<tenant>.vrf.<vrf>.evpn_l2_multi_domain.
            evpn_l2_multi_domain: < true | false >

            # Define node specific configuration, such as unique IP addresses.
            nodes:
              < l3_leaf_inventory_hostname_1 >:
                # device unique IP address for node.
                ip_address: < IPv4_address/Mask >
                # device unique IPv6 address for node.
                ipv6_address: < IPv6_address/Mask >

                # EOS CLI rendered directly on the VLAN interface in the final EOS configuration
                # Overrides the setting on SVI level.
                raw_eos_cli: |
                  < multiline eos cli >

                # Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen
                # Overrides the setting on SVI level.
                structured_config: < dictionary >

              < l3_leaf_inventory_hostname_2 >:
                ip_address: < IPv4_address/Mask >
                ipv6_address: < IPv6_address/Mask >

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

          < 1-4096 >:
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

            # Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant
            # Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.
            # At least one RP address must be configured for EVPN PEG to be configured.
            pim:
              enabled: true

          # For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
          - interfaces: [ <interface_name1.sub-if-id>, <interface_name2.sub-if-id> ]
            encapsulation_dot1q_vlan: [ <vlan id>, <vlan id> ]
            ip_addresses: [ <IPv4_address/Mask>, <IPv4_address/Mask> ]
            nodes: [ < node_1 >, < node_2 > ]
            description: < description >
            enabled: < true | false >
            mtu: < mtu - should only be used for platforms supporting mtu per subinterface >

        # Dictionary of static routes for v4 and/or v6 | Optional.
        # This will create static routes inside the tenant VRF.
        # If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.
        # If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.
        # This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.
        static_routes:
          - destination_address_prefix: < IPv4_address/Mask >
            gateway: < IPv4_address >
            track_bfd: < boolean >
            distance: < 1-255 >
            tag: < 0-4294967295 >
            name: < description >
            metric: < 0-4294967295 >
            interface: < interface >
            nodes: [ < node_1 >, < node_2 >]

        ipv6_static_routes:
          - destination_address_prefix: < IPv6_address/Mask >
            gateway: < IPv6_address >
            track_bfd: < boolean >
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
          < IPv4_address or IPv6_address >:
            peer_group: < peer_group_name >
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
            nodes: [ < node_1 >, < node_2 > ]
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

        # Dictionary of BGP peer groups definitions | Optional.
        # This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.
        # Since BGP peer groups are configured at higher BGP level, shared between VRFs,
        # peer_group names should not overlap between VRFs.
        bgp_peer_groups:
          - name: < BGP peer group name >
            remote_as: < bgp_as >
            description: "< description as string >"
            send_community: < standard | extended | large | all >
            next_hop_self: < true | false >
            maximum_routes: < 0-4294967294 >
            default_originate:
              enabled: < true | false >
              always: < true | false >
            # Nodes is required to restrict configuration of BGP peer groups to certain nodes in the network.
            # If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.
            nodes: [ < node_1 >, < node_2 > ]
            update_source: < interface >
            bfd: < true | false >
            ebgp_multihop: < 1-255 >
            route_map_out: < route-map name >
            route_map_in: < route-map name >
            local_as: < local BGP ASN >
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
        vrf_id: < 1-1024 >
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
            ipv6_address_virtual: < IPv6_address/Mask >
          < 1-4096 >:
            name: < description >
            tags: [ < tag_1 >, < tag_2 > ]
            enabled: < true | false >
            ip_address_virtual: < IPv4_address/Mask >
            ipv6_address_virtual: < IPv6_address/Mask >

   # Define L2 network services organized by vlan id.
    l2vlans:

      # VLAN id.
      < 1-4096 >:
        # By default the vni will be derived from "mac_vrf_vni_base"
        # The vni_override, allows to override this value and statically define it.
        vni_override: < 1-16777215 >

        # By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"
        # The rt_override allows us to override this value and statically define it. | Optional
        rt_override: < 1-16777215 | default -> vni_override >

        # VLAN name | Required
        # For EVPN vlan-aware-bundles the VLAN name is also used as the bundle name for l2vlans.
        # If the same name is used on multiple VLANs they will be added to the same bundle.
        name: < description >

        # Tags leveraged for network services filtering. | Optional
        # Tags are matched against "filter.tags" defined under Fabric Topology variables
        # Tags are also matched against the "node_group" name under Fabric Topology variables
        tags: [ < tag_1 >, < tag_2 > | default -> all ]

        # Trunk Groups | optional
        # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group
        # Requires "enable_trunk_groups: true"
        trunk_groups: [ < trunk_group_1 >, < trunk_group_2 > ]

        # VXLAN | Optional - default true
        # Extend this L2VLAN over VXLAN
        vxlan: < true | false | default -> true >

        # Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.
        # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.
        evpn_l2_multicast:
          enabled: < true | false >

        # Activate or deactivate IGMP snooping | Optional, default is true
        igmp_snooping_enabled: < true | false | default true (EOS) >

        # Enable igmp snooping querier, by default using IP address of Loopback 0.
        # When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.
        igmp_snooping_querier:
          # Will be enabled automatically if "evpn_l2_multicast" is enabled.
          enabled: < true | false | default false >
          source_address: < ipv4_address -> default ip address of Loopback0 >
          version: < 1, 2, 3 -> default 2 (EOS) >

        # Explicitly extend this VLAN to remote EVPN domains.
        # Overrides tenants.<tenant>.evpn_l2_multi_domain.
        evpn_l2_multi_domain: < true | false >

        # Structured configuration and eos cli commands rendered on router_bgp.vlans
        # This configuration will not be applied to vlan aware bundles
        bgp:
          raw_eos_cli: |
            < multiline eos cli >
          structured_config: < dictionary >

  < tenant_b >:
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

< network_services_keys.key_2 >:
  < tenant_c >:
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
            ipv6_address_virtual: < IPv6_address/Mask >
    l2vlans:
      < 1-4096 >:
        vni_override: < 1-16777215 >
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
      < 1-4096 >:
        name: < description >
        tags: [ < tag_1 >, < tag_2 > ]
```

### SVI Profiles

```yaml
# Optional profiles to share common settings for SVIs
# Keys are the same used under SVIs. Keys defined under SVIs take precedence.
# Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
# 1. svi.nodes[inventory_hostname].structured_config
# 2. svi_profile.nodes[inventory_hostname].structured_config
# 3. svi_parent_profile.nodes[inventory_hostname].structured_config
# 4. svi.structured_config
# 5. svi_profile.structured_config
# 6. svi_parent_profile.structured_config
svi_profiles:
  < profile_name >:
    # Parent Profile | Optional
    # svi_profiles can refer to another svi_profile to inherit settings in up to two levels (adapter->svi_profile->svi_parent_profile).
    parent_profile: < svi_profile_name >
```

## Examples

```yaml
# mlag_ibgp_peering_vrfs:
#   base_vlan: 3000

network_services_keys:
  - name: dc1_tenants

dc1_tenants:
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
          251:
            name: Tenant_B_WAN_Zone_2
            tags: [ wan ]
            enabled: true
            ipv6_address_virtual: 2001:db8:251::/64
          252:
            name: Tenant_B_WAN_Zone_3
            tags: [ wan ]
            enabled: true
            ip_address_virtual: 10.2.52.0/24
            ipv6_address_virtual: 2001:db8:252::/64
          253:
            name: Tenant_B_WAN_Zone_4
            tags: [ DC1_BL1, DC1_BL2 ]
            enabled: true
            ipv6_virtual_router_addresses:
              - 2001:db8:253::1
            nodes:
              DC1-BL1A:
                ip_address: 2001:db8:253::2/64
              DC1-BL1B:
                ip_address: 2001:db8:253::3/64
```
