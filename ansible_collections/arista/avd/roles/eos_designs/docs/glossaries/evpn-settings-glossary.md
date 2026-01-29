# Glossary

## Table of Contents

- [E](#e)
- [F](#f)

## E

### evpn_ebgp_gateway_multihop

**Type**: Integer  
**Path**: `evpn_ebgp_gateway_multihop`  
**Default**: `15`  

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.


---

### evpn_ebgp_multihop

**Type**: Integer  
**Path**: `evpn_ebgp_multihop`  
**Default**: `3`  

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.


---

### evpn_import_pruning

**Type**: Boolean  
**Path**: `evpn_import_pruning`  
**Default**: `False`  

Enable VPN import pruning (Min. EOS 4.24.2F).
The Route Target extended communities carried by incoming VPN paths will be examined.
If none of those Route Targets have been configured for import, the path will be immediately discarded.


---

### evpn_multicast

**Type**: Boolean  
**Path**: `evpn_multicast`  
**Default**: `False`  

General Configuration required for EVPN Multicast. "evpn_l2_multicast" or "evpn_l3_multicast" must also be configured under the Network Services (tenants).
Requires `underlay_multicast_pim_sm: true` and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP.
  The Following default platform setting will be configured on 7050X3 and 7300X3: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  The Following default platform setting will be configured on 720XP: "flexible exact-match 16000 l2-shared 18000 l3-shared 22000"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overriding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

---

### evpn_overlay_bgp_rtc

**Type**: Boolean  
**Path**: `evpn_overlay_bgp_rtc`  
**Default**: `False`  

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F).
Requires use eBGP as overlay protocol.


---

### evpn_prevent_readvertise_to_server

**Type**: Boolean  
**Path**: `evpn_prevent_readvertise_to_server`  
**Default**: `False`  

Prevent sending EVPN BGP updates to the route-server if they came from or passed through the route-server already.
Refer to `evpn_prevent_readvertise_to_server_mode` to control which configuration style to use.
This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.


---

### evpn_prevent_readvertise_to_server_mode

**Type**: String  
**Path**: `evpn_prevent_readvertise_to_server_mode`  
**Default**: `as_path_acl`  
**Valid Values**: `source_peer_asn`, `as_path_acl`  

`evpn_prevent_readvertise_to_server_mode` controls the method of identifying EVPN routes that should not be advertised to the EVPN route-servers.
Only used when `evpn_prevent_readvertise_to_server` is set to `true`.
`source_peer_asn` mode configures an outbound route-map towards EVPN route-servers which filter out BGP updates learned directly from the ASN of the route-server. This mode will still allow routes learned via any other peer, even if they have the route-server's ASN in the AS-path.
`as_path_acl` mode configures an outbound route-map and as-path access-list which filters out BGP updates with the route-server ASN anywhere in the AS-path.


---

### evpn_short_esi_prefix

**Type**: String  
**Path**: `evpn_short_esi_prefix`  
**Default**: `0000:0000:`  

Configure prefix for "short_esi" values.

---

### evpn_vlan_aware_bundles

**Type**: Boolean  
**Path**: `evpn_vlan_aware_bundles`  
**Default**: `False`  

Enable VLAN aware bundles for every EVPN MAC-VRF.
If set to `true` all SVIs in a VRF are configured in a vlan-aware-bundle using the VRF name as the bundle name. `l2vlans` are bundled in vlan-aware-bundles using the VLAN name as the bundle name.

The `evpn_vlan_bundle` option under SVI, L2VLAN, VRF or tenant level takes precedence and overrides this behavior. Per SVI/L2VLAN `evpn_vlan_bundle` also works when this setting is disabled which allow mixing vlan-aware-bundles with regular MAC-VRFs.

---

## F

### fabric_evpn_encapsulation

**Type**: String  
**Path**: `fabric_evpn_encapsulation`  
**Valid Values**: `vxlan`, `mpls`  

Should be set to mpls for evpn-mpls scenario. This overrides the evpn_encapsulation setting under node_type_keys.

---
