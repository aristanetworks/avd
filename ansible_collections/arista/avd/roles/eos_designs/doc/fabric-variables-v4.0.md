# Fabric Variables

- The fabric underlay and overlay topology variables, define the elements related to build the L3 Leaf and Spine fabric.
- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - OSPF-LDP*.
- The following overlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - IBGP (only with OSPF or ISIS variants in underlay)
- Only summary network addresses need to be defined. IP addresses are then assigned to each node, based on its unique device id.
  - To view IP address allocation and consumption, a summary is provided in the auto-generated fabric documentation in Markdown and CSV format.
- The variables should be applied to all devices in the fabric.

*Only supported with core_interfaces data model.

**Variables and Options:**

```yaml
# Underlay routing protocol | Required.
underlay_routing_protocol: < EBGP | OSPF | ISIS | ISIS-SR | ISIS-LDP | ISIS-SR-LDP | OSPF-LDP | default for l3ls-evpn -> EBGP >
overlay_routing_protocol: < EBGP | IBGP | default for l3ls-evpn -> EBGP >

# Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
# Requires "underlay_routing_protocol: EBGP"
underlay_rfc5549: < true | false | default -> false >

# Underlay OSFP | Required when < underlay_routing_protocol > == OSPF variants
underlay_ospf_process_id: < process_id | default -> 100 >
underlay_ospf_area: < ospf_area | default -> 0.0.0.0 >
underlay_ospf_max_lsa: < lsa | default -> 12000 >
underlay_ospf_bfd_enable: < true | false | default -> false >

# Underlay ISIS | Required when < underlay_routing_protocol > == ISIS variants
isis_area_id: < isis area | default -> "49.0001" >

# Additional underlay ISIS parameters | Optional.
isis_default_is_type: < level-1-2, | level-1 | level-2 | default -> level-2 >
isis_advertise_passive_only: < true | false | default -> false >
underlay_isis_instance_name: < name | default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls >

# ISIS TI-LFA parameters | Optional.
isis_ti_lfa:
  enabled: < true | false | default -> false >
  protection: < link | node >
  local_convergence_delay: < local_convergence_delay_in_ms | default -> 10000 >

# AS number to use to configure overlay when < overlay_routing_protocol > == IBGP
bgp_as: < AS number >

# Point to Point Links MTU | Required.
p2p_uplinks_mtu: < 0-9216 | default -> 9000 >

# IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1 | Optional
# This is only needed for centralized routing designs
vtep_vvtep_ip: < IPv4_address/Mask >

# Customizable overlay loopback description | Optional
overlay_loopback_description: < description >

# BGP multi-path | Optional
bgp_maximum_paths: < number_of_max_paths | default -> 4 >
bgp_ecmp: < number_of_ecmp_paths | default -> 4 >

# EVPN ebgp-multihop | Optional
# Default of 3, the recommended value for a 3 stage spine and leaf topology.
# Set to a higher value to allow for very large and complex topologies.
evpn_ebgp_multihop: < ebgp_multihop | default -> 3 >

# BGP peer group names and encrypted password | Optional
# Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
# Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
bgp_peer_groups:
   # Old mixed case key "IPv4_UNDERLAY_PEERS" is supported for backward-compatibility
  ipv4_underlay_peers:
    name: < name of peer group | default -> IPv4-UNDERLAY-PEERS >
    password: "< encrypted password >"
   # Old mixed case key "MLAG_IPv4_UNDERLAY_PEER" is supported for backward-compatibility
  mlag_ipv4_underlay_peer:
    name: < name of peer group | default -> MLAG-IPv4-UNDERLAY-PEER >
    password: "< encrypted password >"
   # Old upper case key "EVPN_OVERLAY_PEERS" is supported for backward-compatibility
  evpn_overlay_peers:
    name: < name of peer group | default -> EVPN-OVERLAY-PEERS >
    password: "< encrypted password >"

# Enable vlan aware bundles for EVPN MAC-VRF | Required.
# Old variable name vxlan_vlan_aware_bundles, supported for backward-compatibility.
evpn_vlan_aware_bundles: < boolean | default -> false >

# Disable IGMP snooping at fabric level.
# If set, it overrides per vlan settings
default_igmp_snooping_enabled: < boolean | default -> true >

# BFD Multihop tunning | Required.
bfd_multihop:
  interval: < | default -> 300 >
  min_rx: < | default -> 300 >
  multiplier: < | default -> 3 >

## EVPN Host Flapping Settings
evpn_hostflap_detection:

  # If set to false it will disable EVPN host-flap detection
  enabled: < true | false | default -> true >

  # Minimum number of MAC moves that indicate a MAC duplication issue
  threshold: < number | default -> 5 >

  # Time (in seconds) to detect a MAC duplication issue
  window: < seconds | default -> 180 >

  # Time (in seconds) to purge a MAC duplication issue
  expiry_timeout: < integer >

# Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
# Requires use eBGP as overlay protocol.
evpn_overlay_bgp_rtc: < true | false | default -> false >

# Enable VPN import pruning (Min. EOS 4.24.2F)
# The Route Target extended communities carried by incoming VPN paths will
# be examined. If none of those Route Targets have been configured for import,
# the path will be immediately discarded
evpn_import_pruning: < true | false | default -> false >

# Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
# This is very useful in very large scale networks, where convergence will be quicker by not having to return all updates received
# from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.
evpn_prevent_readvertise_to_server : < true | false | default -> false >

# Configure prefix for "short_esi" values | Optional
evpn_short_esi_prefix: < string | default -> "0000:0000:" >

# Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
# Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
# SVI IP address will be assigned as follows:
# virtual-router: <subnet> + 1
# l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
# l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
# l2leafs       : <subnet> + 3 + <l2leaf id>
# GW on l2leafs : <subnet> + 1
# Assign range larger than total l2leafs + 5
inband_management_subnet: < IPv4_network/Mask >

# VLAN number assigned to Inband Management SVI on l2leafs in default VRF.
# Optional - default -> 4092
inband_management_vlan: < vlan_id >

# QOS Profile assigned on all infrastructure links | Optional
p2p_uplinks_qos_profile: < qos_profile_name >

# Enable PTP on all infrastructure links | Optional
uplink_ptp:
  enable: < boolean | default -> false >
```
