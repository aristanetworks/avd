<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_multicast</samp>](## "router_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_multicast.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "router_multicast.ipv4.counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_period_decay</samp>](## "router_multicast.ipv4.counters.rate_period_decay") | Integer |  |  | Min: 0<br>Max: 600 | Rate in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.ipv4.routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multipath</samp>](## "router_multicast.ipv4.multipath") | String |  |  | Valid Values:<br>- none<br>- deterministic<br>- deterministic color<br>- deterministic router-id |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;software_forwarding</samp>](## "router_multicast.ipv4.software_forwarding") | String |  |  | Valid Values:<br>- kernel<br>- sfe |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rpf</samp>](## "router_multicast.ipv4.rpf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_multicast.ipv4.rpf.routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_multicast.ipv4.rpf.routes.[].source_prefix") | String | Required |  |  | Source address A.B.C.D or Source prefix A.B.C.D/E |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nexthop</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].nexthop") | String | Required |  |  | Next-hop IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for this route |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_multicast.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_multicast.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_multicast.vrfs.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.vrfs.[].ipv4.routing") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_multicast:
      ipv4:
        counters:
          rate_period_decay: <int>
        routing: <bool>
        multipath: <str>
        software_forwarding: <str>
        rpf:
          routes:
            - source_prefix: <str>
              destinations:
                - nexthop: <str>
                  distance: <int>
      vrfs:
        - name: <str>
          ipv4:
            routing: <bool>
    ```
