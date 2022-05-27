# BETA Feature

The MPLS design feature is in BETA until the release of AVD 4.0.0. Changes to data models and default behavior for the MPLS design should be expected.

# Network Services Variables for MPLS Design - VRFs/VLANs

- The MPLS design supports any network services variables already supported by l3ls-evpn, barring the exceptions outlined in this document.
- The MPLS design additionally supports several new network services variables that are outlined in this document.
- The network services variables provide an abstracted model to create L2 and L3 network services across the fabric.
- The network services are grouped by tenants. The definition of a tenant may vary between organizations.
  - e.g. Tenants can be organizations or departments.
- The tenant shares a common vni range for mac vrf assignment.
- The filtering model allows for granular deployment of network service to the fabric leveraging the tenant name and tags applied to the service definition.
  - This allows for the re-use of SVIs and VLANs across the fabric.

## New Variables and Options

```yaml
# Dictionary of tenants, to define network services: L3 VRFs and L2 VLANS.

tenants:

  # Specify a tenant name. | Required
  # Tenant provide a construct to group L3 VRFs and L2 VLANs.
  # Networks services can be filtered by tenant name.
  - name: < tenant_a >

    # Pseudowire rt base, used to generate route targets for vpws services. Avoid overlapping route target spaces between different services.
    pseudowire_rt_base: < int >

    # Define point to point services (pseudowires) as a list of dictionaries.
    point_to_point_services:

        # L1 service pseudowire name
      - name: < name >

        # L1 service type, currently only vpws-pseudowire is supported.
        type: < vpws-pseudowire >

        # Subinterfaces will create subinterfaces and additional pseudowires/patch panel config
        subinterfaces:
          - number: < subif1 number >
          - number: < subif2 number >

        # Pseudowire terminating endpoints.
        endpoints:
          - id: < id A-side >
            # With ESI multihoming we support 2 nodes per pseudowire endpoint
            nodes: [ < node1 >, < node2 > ]
            # Interfaces patched to the pseudowire on side A
            interfaces: [ < node1 interface >, < node2 interface > ]
            port_channel:
              mode: < active | on >
              short_esi: < short ESI value >

          - id: < id B-side >
            nodes: [ < node3 >, < node4 >]
            # Interfaces patched to the pseudowire on side B
            interfaces: [ < node3 interface >, < node4 interface > ]
            port_channel:
              mode: < active | on >
              short_esi: < short ESI value >

        # Whether to disable lldp rx/tx on port mode pseudowire services
        lldp_disable: true
```

## Examples

```yaml
tenants:
  - name: Tenant_A
    pseudowire_rt_base: 1000
    point_to_point_services:
      # simple p2p pseudowire, no redundancy, port-based
      - name: TEN_A_site2_site5_eline_port_based
        type: vpws-pseudowire
        endpoints: # Or alternative name: "termination"
          - id: 26
            nodes: ["pe2"]
            interfaces: ["Ethernet6"]
          - id: 57
            nodes: ["pe5"]
            interfaces: ["Ethernet7"]
        lldp_disable: true
      # pw with ESI active-active port channel on one side, single interface on other side.
      # multiple subinterfaces will be created, own pw on each, IDs generated from endpoint.id + subif number.
      - name: TEN_A_site3_site5_eline_vlan_based
        type: vpws-pseudowire
        subinterfaces:
          - number: 1000
          - number: 1001
          - number: 1002
          - number: 1003
        endpoints:
          - id: 10000
            nodes: ["pe1", "pe2"]
            interfaces: ["Ethernet5", "Ethernet5"]
            port_channel:
              mode: active
              short_esi: 0303:0202:0101
          - id: 58000
            port_channel:
              mode: active
            nodes: ["pe5", "pe5"]
            interfaces: ["Ethernet8", "Ethernet9"]
```

## Unsupported Variables

The following variables used with l3ls-evpn are not supported with the MPLS design:

```yaml
# MLAG is currently not supported with MPLS-EVPN.
mlag_ibgp_peering_vrfs:
  base_vlan: < vlan >

tenants:
  - name: < tenant_a >
    # MLAG is not supported with MPLS-EVPN topologies.
    enable_mlag_ibgp_peering_vrfs: < true | false >
    vrfs:
      - name: < vrf name >
        # Replaced by vrf_id
        vrf_vni: < vni >
        # MLAG is not supported with MPLS-EVPN topologies.
        enable_mlag_ibgp_peering_vrfs: < true | false >
        mlag_ibgp_peering_vlan: <1-4096>
        svis:
          - id: < 1-4096 >
            # Replaced by rt_override
            vni_override: < 1-16777215 >
            # Not relevant for MPLS
            vxlan: < true | false | default -> true >
    l2vlans:
      - id: < vlan id >
        # Replaced by rt_override
        vni_override: < 1-16777215 >
```
