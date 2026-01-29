# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [E](#e)
- [H](#h)
- [I](#i)
- [L](#l)
- [N](#n)
- [P](#p)
- [R](#r)
- [S](#s)

## A

### action

**Type**: String  
**Path**: `router_bgp.peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.neighbors.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.neighbors.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### address_family

**Type**: String  
**Path**: `router_bgp.vrfs.[].default_route_exports.[].address_family`  
**Valid Values**: `evpn`, `vpn-ipv4`, `vpn-ipv6`  
---

### algorithm

**Type**: String  
**Path**: `router_bgp.vrfs.[].evpn_multicast_gateway_dr_election.algorithm`  
**Valid Values**: `hrw`, `modulus`, `preference`  

DR election algorithms:
  hrw: Default selection based on highest random weight.
  modulus: Selection based on VLAN ID modulo number of candidates.
  preference: Selection based on a configured preference value.

---

### ASN Notation

**Type**: String  
**Path**: `router_bgp.as_notation`  
**Valid Values**: `asdot`, `asplain`  

BGP AS can be deplayed in the asplain <1-4294967295> or asdot notation "<1-65535>.<0-65535>". This flag indicates which mode is preferred - asplain is the default.

---

## D

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].rd_evpn_domain.domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].rd_evpn_domain.domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.import_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.address_family_evpn.evpn_ethernet_segment.[].domain`  
**Valid Values**: `all`, `local`, `remote`  
---

## E

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbor_default.encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for neighbor.

---

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbors.[].encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for the neighbor.

---

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.peer_groups.[].encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for the peer-group.

---

## H

### hash_algorithm

**Type**: String  
**Path**: `router_bgp.peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `router_bgp.neighbors.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

## I

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_evpn.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_vpn_ipv4.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_vpn_ipv6.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

### isis_level

**Type**: String  
**Path**: `router_bgp.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

## L

### label_local_termination

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.label_local_termination`  
**Valid Values**: `explicit-null`, `implicit-null`  
---

## N

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

## P

### password_type

**Type**: String  
**Path**: `router_bgp.peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `router_bgp.neighbors.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `router_bgp.vrfs.[].neighbors.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### protocol

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.tunnel_source_protocols.[].protocol`  
**Valid Values**: `isis segment-routing`, `ldp`  
---

## R

### rib_type

**Type**: String  
**Path**: `router_bgp.address_family_evpn.next_hop_mpls_resolution_ribs.[].rib_type`  
**Valid Values**: `system-connected`, `tunnel-rib-colored`, `tunnel-rib`  

Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.

---

### rib_type

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.next_hop_resolution_ribs.[].rib_type`  
**Valid Values**: `system-connected`, `tunnel-rib-colored`, `tunnel-rib`  

Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.

---

## S

### send

**Type**: String  
**Path**: `router_bgp.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send_community

**Type**: String  
**Path**: `router_bgp.neighbor_default.send_community`  
**Valid Values**: `all`, `large`, `extended`, `standard`, `extended large`, `standard large`, `standard extended`, `standard extended large`  
---
