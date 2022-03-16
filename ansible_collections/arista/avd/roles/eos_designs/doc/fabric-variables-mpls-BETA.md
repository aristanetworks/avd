# BETA Feature

The MPLS design feature is in BETA until the release of AVD 4.0.0. Changes to data models and default behavior for the MPLS design should be expected.

# Fabric Variables for MPLS Design

- The MPLS design supports any fabric variables already supported by l3ls-evpn, barring the exceptions outlined in this document.
- Additionally the MPLS design supports several new fabric variables that are outlined in this document.
- The fabric underlay and overlay topology variables, define the elements related to build the L3 Leaf and Spine fabric.
- The following underlay routing protocols are supported:
  - ISIS-SR (default)
  - ISIS + LDP
  - ISIS-SR + LDP
  - OSPF + LDP
- The following overlay routing protocols are supported:
  - IBGP (default)
- Only summary network addresses need to be defined. IP addresses are then assigned to each node, based on its unique device id.
  - To view IP address allocation and consumption, a summary is provided in the auto-generated fabric documentation in Markdown and CSV format.
- The variables described in this document should be applied to all devices in the fabric.

## New Variables and Options

```yaml
# Fabric Name | Required
# Required to match an Ansible Group name covering all devices in the Fabric
fabric_name: < Fabric_Name >

# Underlay routing protocol | Required.
underlay_routing_protocol: < isis-sr | isis-ldp | isis-sr-ldp | ospf-ldp | default -> isis-sr >
overlay_routing_protocol: < ibgp | default -> ibgp >

# Underlay ISIS parameters
isis_default_is_type: < level-1 | level-2 | level-1-2 | default -> level-1-2 >
isis_default_circuit_type: < level-1 | level-2 | level-1-2 | default -> level-1-2 >
isis_default_metric: < int >
isis_advertise_passive_only: < true | false | default -> false >

# Underlay ISIS TI-LFA parameters
isis_ti_lfa:
  enabled: < true | false | default -> false >
  protection: < link | node | default -> link >
  # Microloop protection delay in ms
  local_convergence_delay: < int | default -> 10000 >

# Underlay IPv6 turns on ipv6 for the underlay, which requires loopback_ipv6_pool to be defined.
underlay_ipv6: < true | false | default -> false >

# Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
bgp_mesh_pes: < true | false | default -> false >

# BGP peer groups encrypted password
# mpls_overlay_peers | Required
# rr_overlay_peers | Optional (Used to peer route reflectors in the same node-group (rr cluster) to each other)
# Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
# Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
bgp_peer_groups:
  mpls_overlay_peers:
    name: < name of peer group | default -> MPLS-OVERLAY-PEERS >
    password: "< encrypted password >"
  rr_overlay_peers:
    name: < name of peer group | default -> RR-OVERLAY-PEERS >
    password: "< encrypted password >"
```

## Unsupported Fabric Variables

The following fabric variables or variable values are not supported with the MPLS design.

```yaml
underlay_routing_protocol: < ebgp | isis | ospf >
overlay_routing_protocol: ebgp
underlay_rfc5549: < true | false | default -> false >
vtep_vvtep_ip: < IPv4_address/Mask >
evpn_ebgp_multihop: < ebgp_multihop | default -> 3 >
inband_management_subnet: < IPv4_network/Mask >
inband_management_vlan: < vlan_id >
```
