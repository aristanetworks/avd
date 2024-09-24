<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mpls</samp>](## "mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ip</samp>](## "mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ldp</samp>](## "mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp>](## "mpls.ldp.interface_disabled_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "mpls.ldp.router_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.ldp.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp>](## "mpls.ldp.transport_address_interface") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;icmp</samp>](## "mpls.icmp") | Dictionary |  |  |  | Enables the LSRs to generate ICMP reply messages and deliver them to the originating host. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fragmentation_needed_tunneling</samp>](## "mpls.icmp.fragmentation_needed_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_exceeded_tunneling</samp>](## "mpls.icmp.ttl_exceeded_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of TTL exceeded ICMP replies. |

=== "YAML"

    ```yaml
    mpls:
      ip: <bool>
      ldp:
        interface_disabled_default: <bool>
        router_id: <str>
        shutdown: <bool>

        # Interface Name.
        transport_address_interface: <str>

      # Enables the LSRs to generate ICMP reply messages and deliver them to the originating host.
      icmp:

        # Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big).
        fragmentation_needed_tunneling: <bool>

        # Enables the MPLS tunneling of TTL exceeded ICMP replies.
        ttl_exceeded_tunneling: <bool>
    ```
