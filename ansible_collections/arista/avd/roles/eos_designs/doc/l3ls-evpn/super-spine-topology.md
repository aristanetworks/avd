# Role Enhancements for Super Spine Support

The enhancement listed below are required to support bigger deployments with super-spines (5 stage CLOS).
5 stage CLOS fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
The logic to deploy every leaf-spine POD fabric remains unchanged. The enhancement only adds logic required to provision spine-to-super-spine fabric.
Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

!!! warning
    Current AVD release supports single plane deployment only.

Only BGP underlay is supported for super-spine deployment. Spines in every POD must have unique AS per POD.

<div style="text-align:center">
  <img src="../../../media/topology.gif" />
</div>

!!! info
    This section gives enhancements to add super-spines and overlay controllers (Route servers) into your topology. For spines, L3Leaves, L2Leaves, please report to [this documentation](./leaf-spine-topology.md).

## Super Spine Deployment

This section provides additional settings to support super-spine in your l3ls-evpn topology

Defaults:

```yaml
max_spine_to_super_spine_links: 1  # number of parallel links between spines and super-spines
```

Assigned to the DC group:

```yaml
max_super_spines: 4  # maximum number of super-spines, changing this parameter affects address allocation

super_spine:
  platform: vEOS-LAB  # super-spine platform
  bgp_as: <super-spine BGP AS>

  nodes:
    SU-01:  # super-spine name
      id: 1
      mgmt_ip: 192.168.0.1/24
      # EVPN Role for Overlay BGP Peerings | Optional, default is none
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> none  >
      # Peer with these EVPN Route Servers / Route Reflectors | Optional
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname >]
    <-- etc. -->

# IP address range for loopbacks for all super-spines in the DC,
# assigned as /32s
# Assign range larger then total super-spines
super_spine_loopback_network_summary: 192.168.100.0/24

# additional lines for super-spine BGP config
super_spine_bgp_defaults:
  #  - update wait-for-convergence
  #  - update wait-install
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart
```

Assigned to Super Spine Group:

```yaml
type: super-spine  # identifies every host in the group as super-spine
```

Assigned to Every POD Group:

```yaml
spine:
  # list of spine interfaces used as uplinks to super-spines
  # taking `max_spine_to_super_spine_links` into account
  # for example: spine1, spine2, spine3, ...
  # or spine1, spine1, spine2, spine2, etc.
  uplinks_to_super_spine_interfaces: [ Ethernet10, Ethernet11, Ethernet12, Ethernet13 ]
  nodes:
    <spine-hostname>:
      # super-spine interfaces to spines
      # taking `max_spine_to_super_spine_links` into account
      # for example: super-spine1, super-spine2, super-spine3, ...
      # or super-spine1, super-spine1, super-spine2, super-spine2, etc.
      super_spine_interfaces: [ Ethernet1, Ethernet1, Ethernet1, Ethernet1 ]
    <-- etc. -->

# Point to Point Network Summary range, assigned as /31 for each
# uplink interfaces
# Assign range larger then total
# [ max_spines_in_a_POD * max_super_spines * max_spine_to_super_spine_links * 2 ]
super_spine_underlay_p2p_network_summary: 172.31.1.0/24
```

Following variables must be now defined on DC and not POD level:

- `p2p_uplinks_mtu`
- `bgp_peer_groups`

## Overlay Controllers Deployment

This section provides options to enable overlay-controller in your l3ls-evpn topology.

Defaults:
```yaml
# The maximum number of uplinks for each overlay_controller.
#This is used to calculate P2P Link IP addresses, and should not be changed after deployment.
max_overlay_controller_to_switch_links: 2
```

Assigned to the DC group:

```yaml
overlay_controller:
  platform: <platform>   # overlay-controller platform

  # All variables defined under `nodes` dictionary can be defined under the defaults key will be inherited by all overlay-controllers.
  # The variables defined under a specific node will take precedence over defaults.
  defaults:

  nodes:
    <inventory_hostname>:
      id: <number> # Starting from 1
      mgmt_ip: < IPv4_address/Mask >
      remote_switches_interfaces: [ <remote_switch_interface> , <remote_switch_interface> ] # Interfaces on remote switch

      remote_switches: [ <switch_inventory_hostname> , <switch_inventory_hostname> ] #Remote Switches connected to uplink interfaces
      uplink_to_remote_switches: [ <uplink_interface> , <uplink_interface> ]
      bgp_as: <BGP AS>

      # EVPN Role for Overlay BGP Peerings | Optional, default is none
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> none  >

      # Peer with these EVPN Route Servers / Route Reflectors | Optional
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname > ]

# Point to Point Network Summary range, assigned as /31 for each uplink interfaces
# Assign range larger than [ total overlay_controllers * max_overlay_controller_to_switch_links * 2]
overlay_controller_p2p_network_summary: < IPv4_network/Mask >
# IP address summary for BGP evpn overlay peering loopback for Overlay Controllers | Required
# Assigned as /32 to Loopback0
# Assign range larger then:
# [ total overlay_controllers ]
overlay_controller_loopback_network_summary: < IPv4_network/Mask >
# Enable BFD for p2p BGP sessions - useful if the overlay_controller is a VM | Optional
overlay_controller_p2p_bfd: < true | false | default -> false >
# additional lines for overlay-controller BGP config
overlay_controller_bgp_defaults:
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart
```

Assigned to Overlay Controller Group:

```yaml
type: overlay-controller # identifies every host in the group as overlay-controller
```
