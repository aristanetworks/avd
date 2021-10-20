# Fabric Variables

- The fabric underlay and overlay topology variables, define the elements related to build the L3 Leaf and Spine fabric.
- The following underlay routing protocols are supported:
  - EBGP (default)
  - OSPF.
  - ISIS.
- The following overlay routing protocols are supported:
  - EBGP (default)
  - IBGP (only with OSPF or ISIS in underlay)
- Only summary network addresses need to be defined. IP addresses are then assigned to each node, based on its unique device id.
  - To view IP address allocation and consumption, a summary is provided in the auto-generated fabric documentation in Markdown and CSV format.
- The variables should be applied to all devices in the fabric.

**Variables and Options:**

```yaml
# Underlay routing protocol | Required.
underlay_routing_protocol: < EBGP or OSPF or ISIS | Default -> EBGP >
overlay_routing_protocol: <EBGP or IBGP | default -> EBGP >

# Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumberred.
# Requires "underlay_routing_protocol: EBGP"
underlay_rfc5549: < true | false | Default -> false >

# Underlay OSFP | Required when < underlay_routing_protocol > == OSPF
underlay_ospf_process_id: < process_id | Default -> 100 >
underlay_ospf_area: < ospf_area | Default -> 0.0.0.0 >
underlay_ospf_max_lsa: < lsa | Default -> 12000 >
underlay_ospf_bfd_enable: < true | false | Default -> false >

# Underlay ISIS | Required when < underlay_routing_protocol > == ISIS
isis_area_id: < isis area | Default -> "49.0001" >

# AS number to use to configure overlay when < overlay_routing_protocol > == IBGP
bgp_as: < AS number >

# Point to Point Links MTU | Required.
p2p_uplinks_mtu: < 0-9216 | default -> 9000 >

# IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1 | Optional
# This is only needed for centralized routing designs
vtep_vvtep_ip: < IPv4_address/Mask >

# BGP multi-path | Optional
bgp_maximum_paths: < number_of_max_paths | default -> 4 >
bgp_ecmp: < number_of_ecmp_paths | default -> 4 >

# EVPN ebgp-multihop | Optional
# Default of 3, the recommended value for a 3 stage spine and leaf topology.
# Set to a higher value to allow for very large and complex topologies.
evpn_ebgp_multihop: < ebgp_multihop | default -> 3 >

# BGP peer groups encrypted password
# IPv4_UNDERLAY_PEERS and MLAG_IPv4_UNDERLAY_PEER | Optional
# EVPN_OVERLAY_PEERS | Optional
# Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
# Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
bgp_peer_groups:
  IPv4_UNDERLAY_PEERS:
    name: < name of peer group | default -> IPv4-UNDERLAY-PEERS >
    password: "< encrypted password >"
  MLAG_IPv4_UNDERLAY_PEER:
      name: < name of peer group | default -> MLAG-IPv4-UNDERLAY-PEER >
      password: "< encrypted password >"
  EVPN_OVERLAY_PEERS:
      name: < name of peer group | default -> EVPN-OVERLAY-PEERS >
      password: "< encrypted password >"

# Enable vlan aware bundles for EVPN MAC-VRF | Required.
vxlan_vlan_aware_bundles: < boolean | default -> false >

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
  threshold: < number | default 5 >

  # Time (in seconds) to detect a MAC duplication issue
  window: < seconds | default 180 >

# Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
# Requires use eBGP as overlay protocol.
evpn_overlay_bgp_rtc: < true | false , default -> false >

# Enable VPN import pruning (Min. EOS 4.24.2F)
# The Route Target extended communities carried by incoming VPN paths will
# be examined. If none of those Route Targets have been configured for import,
# the path will be immediately discarded
evpn_import_pruning: true

# Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
# This is very useful in very large scale networks, where convergence will be quicker by not having to return all updates received
# from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.
evpn_prevent_readvertise_to_server : < true | false , default -> false >

# Configure prefix for "short_esi" values | Optional
evpn_short_esi_prefix: < string, default -> "0000:0000:" >

# Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
# Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
# SVI IP address will be assigned as follows:
# virtual-router: <subnet> + 1
# l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
# l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
# l2leafs       : <subnet> + 3 + <l2leaf id>
# GW on l2leafs : <subnet> + 1
# Assign range larger than total l2leafs + 5
l2leaf_inband_management_subnet: < IPv4_network/Mask >

# VLAN number assigned to Inband Management SVI on l2leafs in default VRF.
# Optional - default -> 4092
l2leaf_inband_management_vlan: < vlan_id >

# QOS Profile assigned on all infrastructure links | Optional
p2p_uplinks_qos_profile: < qos_profile_name >

# Enable PTP on all infrastructure links | Optional
p2p_uplinks_ptp:
  enable: < boolean | default -> false >
```
