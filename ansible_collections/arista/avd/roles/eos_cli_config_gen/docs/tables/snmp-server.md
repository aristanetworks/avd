<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_server</samp>](## "snmp_server") | Dictionary |  |  |  | SNMP settings |
    | [<samp>&nbsp;&nbsp;engine_ids</samp>](## "snmp_server.engine_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "snmp_server.engine_ids.local") | String |  |  |  | Engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp>](## "snmp_server.engine_ids.remotes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "snmp_server.engine_ids.remotes.[].id") | String |  |  |  | Remote engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "snmp_server.engine_ids.remotes.[].address") | String |  |  |  | Hostname or IP of remote engine<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.engine_ids.remotes.[].udp_port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_server.contact") | String |  |  |  | SNMP contact |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_server.location") | String |  |  |  | SNMP location |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_server.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.communities.[].name") | String | Required, Unique |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_server.communities.[].access") | String |  |  | Valid Values:<br>- ro<br>- rw |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_server.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_server.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_server.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_server.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_server.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "snmp_server.local_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.local_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.local_interfaces.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_server.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.views.[].name") | String |  |  |  | SNMP view name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_server.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_server.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_server.views.[].MIB_family_name") <span style="color:red">deprecated</span> | String |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>mib_family_name</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_server.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.groups.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_server.groups.[].authentication") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_server.groups.[].read") | String |  |  |  | Read view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_server.groups.[].write") | String |  |  |  | Write view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_server.groups.[].notify") | String |  |  |  | Notify view |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_server.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_server.users.[].group") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp>](## "snmp_server.users.[].remote_address") | String |  |  |  | Hostname or ip of remote engine<br>The remote_address and udp_port are used for remote users<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.users.[].udp_port") | Integer |  |  |  | udp_port will not be used if no remote_address is configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp>](## "snmp_server.users.[].localized") | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_server.users.[].auth") | String |  |  |  | Hash algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_server.users.[].auth_passphrase") | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_server.users.[].priv") | String |  |  |  | Encryption algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_server.users.[].priv_passphrase") | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase<br> |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_server.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "snmp_server.hosts.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.hosts.[].version") | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_server.hosts.[].community") | String |  |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_server.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp>](## "snmp_server.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_server.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_server.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.traps.enable") | Boolean |  | `False` |  | Enable or disable all snmp-traps<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_server.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_server.traps.snmp_traps.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_server.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.vrfs.[].enable") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    snmp_server:
      engine_ids:
        local: <str>
        remotes:
          - id: <str>
            address: <str>
            udp_port: <int>
      contact: <str>
      location: <str>
      communities:
        - name: <str>
          access: <str>
          access_list_ipv4:
            name: <str>
          access_list_ipv6:
            name: <str>
          view: <str>
      ipv4_acls:
        - name: <str>
          vrf: <str>
      ipv6_acls:
        - name: <str>
          vrf: <str>
      local_interfaces:
        - name: <str>
          vrf: <str>
      views:
        - name: <str>
          mib_family_name: <str>
          included: <bool>
          MIB_family_name: <str>
      groups:
        - name: <str>
          version: <str>
          authentication: <str>
          read: <str>
          write: <str>
          notify: <str>
      users:
        - name: <str>
          group: <str>
          remote_address: <str>
          udp_port: <int>
          version: <str>
          localized: <str>
          auth: <str>
          auth_passphrase: <str>
          priv: <str>
          priv_passphrase: <str>
      hosts:
        - host: <str>
          vrf: <str>
          version: <str>
          community: <str>
          users:
            - username: <str>
              authentication_level: <str>
      traps:
        enable: <bool>
        snmp_traps:
          - name: <str>
            enabled: <bool>
      vrfs:
        - name: <str>
          enable: <bool>
    ```
