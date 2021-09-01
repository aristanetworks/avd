# Connected Endpoints for mpls design

- The mpls design supports all connected endpoint variables already supported by l3ls-evpn barring the exceptions outlined in this document.
- The connected endpoints variables, define endpoints that connect to the fabric on pe interface(s).
- The connected endpoints are leveraged to define any device that connects to a pe switch ports, i.e.: servers, firewalls, routers, load balancers, and storage arrays.
- Connected endpoints key/value pairs are designed to be extended for your own needs and leveraged to configure the endpoint itself.

## Unsupported variables

Since MLAG is not supported with mpls-evpn topologies, it is necessary to use the EVPN A/A data model if a dual-homed port-channel configuration is desired. As such, the following data model will not render a functional configuration:

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC3B ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
```

The short_esi variable is mandatory in order to have a functional multihomed port-channel:

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC4A ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
          short_esi: 0303:0202:0101
```
