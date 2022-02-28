# Fabric Variables for mpls Design

- The mpls design supports any fabric variables already supported by l3ls-evpn, barring the exceptions outlined in this document.
- The mpls design additionally supports several new fabric variables that are outlined in this document.
- The fabric underlay and overlay topology variables, define the elements related to build the L3 Leaf and Spine fabric.
- The following underlay routing protocols are supported:
  - ISIS-SR.
  - ISIS + LDP.
  - ISIS-SR + LDP.
  - OSPF + LDP.
- The following overlay routing protocols are supported:
  - IBGP (default)
- Only summary network addresses need to be defined. IP addresses are then assigned to each node, based on its unique device id.
  - To view IP address allocation and consumption, a summary is provided in the auto-generated fabric documentation in Markdown and CSV format.
- The variables should be applied to all devices in the fabric.

**Variables and Options:**

```yaml
# Underlay routing protocol | Required.
underlay_routing_protocol: < isis-sr, isis-ldp, isis-sr-ldp, ospf-ldp | Default -> isis-sr >
overlay_routing_protocol: < ibgp | Default -> ibgp >

# Underlay ISIS parameters
isis_default_is_type: < level-1 | level-2 | level-1-2 | Default -> level-1-2 >
isis_default_circuit_type: < level-1 | level-2 | level-1-2 | Default -> level-1-2 >
isis_default_metric: < int >
isis_advertise_passive_only: < true | false | Default -> false >

#  Underlay ISIS TI-LFA parameters
isis_ti_lfa:
  enabled: < true | false | Default -> false >
  protection: < link | node | Default -> link >
  # Microloop protection delay in ms
  local_convergence_delay: < int | Default -> 10000 >

# Underlay IPv6 turns on ipv6 for the underlay, which requires loopback_ipv6_pool to be defined.
underlay_ipv6: < true | false | Default -> false >

# Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
bgp_mesh_pes: < true | false | Default -> false >

# BGP peer groups encrypted password
# MPLS_OVERLAY_PEERS | Required
# RR_OVERLAY_PEERS | Optional (Used to peer route reflectors in the same node-group (rr cluster) to each other)
# Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
# Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
bgp_peer_groups:
  MPLS_OVERLAY_PEERS:
    name: < name of peer group | default -> MPLS-OVERLAY-PEERS >
    password: "< encrypted password >"
  RR_OVERLAY_PEERS:
    name: < name of peer group | default -> RR-OVERLAY-PEERS >
    password: "< encrypted password >"
```

## Unsupported Fabric Variables

The following fabric variables or variable values are not supported with the mpls design.

```yaml
underlay_routing_protocol: < ebgp | isis | ospf >
overlay_routing_protocol: ebgp

# Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
# Unsupported because it requires "underlay_routing_protocol: EBGP"
underlay_rfc5549: < true | false | default -> false >

# IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1 | Optional
# Unsupported due to lack of vtep in mpls design.
vtep_vvtep_ip: < IPv4_address/Mask >

# EVPN ebgp-multihop
# Unsupported because ebgp in the overlay is not supported.
evpn_ebgp_multihop: < ebgp_multihop | default -> 3 >

# Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
# Unsupported due to lack of l2leaf node type in mpls design.
inband_management_subnet: < IPv4_network/Mask >
inband_management_vlan: < vlan_id >
```
