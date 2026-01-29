# Glossary

## Table of Contents

- [B](#b)

## B

### bgp_as

**Type**: String  
**Path**: `bgp_as`  

BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>" to use to configure overlay when "overlay_routing_protocol" == ibgp.
For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.

---

### bgp_as_notation

**Type**: String  
**Path**: `bgp_as_notation`  
**Default**: `auto`  
**Valid Values**: `auto`, `asdot`, `asplain`  

AS number representation.
asdot - AS number representation in asdot format (Ex. 123.12).
asplain - AS number representation in asplain format (Ex. 12312).
auto - Will look at the configured ASN and if there is a dot in it,
       it will use asdot otherwise asplain.

---

### bgp_default_ipv4_unicast

**Type**: Boolean  
**Path**: `bgp_default_ipv4_unicast`  
**Default**: `False`  

Default activation of IPv4 unicast address-family on all IPv4 neighbors.
It is best practice to disable activation.


---

### bgp_ecmp

**Type**: Integer  
**Path**: `bgp_ecmp`  

Maximum ECMP for BGP multi-path.

---

### bgp_graceful_restart

**Type**: Dictionary  
**Path**: `bgp_graceful_restart`  

BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.
Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.


---

### bgp_maximum_paths

**Type**: Integer  
**Path**: `bgp_maximum_paths`  

Maximum Paths for BGP multi-path.
The default value is 4 except for WAN Routers where the default value is 16.

---

### bgp_peer_groups

**Type**: Dictionary  
**Path**: `bgp_peer_groups`  

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.


---

### bgp_update_wait_for_convergence

**Type**: Boolean  
**Path**: `bgp_update_wait_for_convergence`  
**Default**: `False`  

Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.


---

### bgp_update_wait_install

**Type**: Boolean  
**Path**: `bgp_update_wait_install`  
**Default**: `True`  

Do not advertise reachability to a prefix until that prefix has been installed in hardware.
This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.


---
