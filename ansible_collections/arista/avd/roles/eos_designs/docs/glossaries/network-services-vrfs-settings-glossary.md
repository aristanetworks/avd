# Glossary

## Table of Contents

- [M](#m)
- [N](#n)
- [T](#t)

## M

### mlag_ibgp_peering_vrfs

**Type**: Dictionary  
**Path**: `mlag_ibgp_peering_vrfs`  

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology).
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1.
Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is reused across all iBGP peerings.


---

## N

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

## T

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].type`  
**Valid Values**: `import`, `export`  
---
