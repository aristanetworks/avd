<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dhcp_servers</samp>](## "dhcp_servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- disabled</samp>](## "dhcp_servers.[].disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "dhcp_servers.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_domain_name_ipv4</samp>](## "dhcp_servers.[].dns_domain_name_ipv4") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_domain_name_ipv6</samp>](## "dhcp_servers.[].dns_domain_name_ipv6") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_vendor_options</samp>](## "dhcp_servers.[].ipv4_vendor_options") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- vendor_id</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].vendor_id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_options</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- code</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].code") | Integer | Required, Unique |  | Min: 1<br>Max: 254 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].type") | String | Required |  | Valid Values:<br>- string<br>- ipv4-address<br>- array ipv4-address |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].data") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;subnets</samp>](## "dhcp_servers.[].subnets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- subnet</samp>](## "dhcp_servers.[].subnets.[].subnet") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "dhcp_servers.[].subnets.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_gateway</samp>](## "dhcp_servers.[].subnets.[].default_gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns_servers</samp>](## "dhcp_servers.[].subnets.[].dns_servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "dhcp_servers.[].subnets.[].dns_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ranges</samp>](## "dhcp_servers.[].subnets.[].ranges") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- start</samp>](## "dhcp_servers.[].subnets.[].ranges.[].start") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "dhcp_servers.[].subnets.[].ranges.[].end") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lease_time</samp>](## "dhcp_servers.[].subnets.[].lease_time") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;days</samp>](## "dhcp_servers.[].subnets.[].lease_time.days") | Integer | Required |  | Min: 0<br>Max: 2000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hours</samp>](## "dhcp_servers.[].subnets.[].lease_time.hours") | Integer | Required |  | Min: 0<br>Max: 23 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minutes</samp>](## "dhcp_servers.[].subnets.[].lease_time.minutes") | Integer | Required |  | Min: 0<br>Max: 59 |  |

=== "YAML"

    ```yaml
    dhcp_servers:
      - disabled: <bool>
        vrf: <str>
        dns_domain_name_ipv4: <str>
        dns_domain_name_ipv6: <str>
        ipv4_vendor_options:
          - vendor_id: <str>
            sub_options:
              - code: <int>
                type: <str>
                data: <str>
        subnets:
          - subnet: <str>
            name: <str>
            default_gateway: <str>
            dns_servers:
              - <str>
            ranges:
              - start: <str>
                end: <str>
            lease_time:
              days: <int>
              hours: <int>
              minutes: <int>
    ```
