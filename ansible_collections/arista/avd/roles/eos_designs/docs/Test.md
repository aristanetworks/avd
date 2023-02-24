---
search:
  boost: 2
---

# Test

## Management Protocols

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_protocols</samp>](## "management_protocols") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;snmp</samp>](## "management_protocols.snmp") | Dictionary |  |  |  | SNMP settings |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;engine_ids</samp>](## "management_protocols.snmp.engine_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "management_protocols.snmp.engine_ids.local") | String |  |  |  | Engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp>](## "management_protocols.snmp.engine_ids.remotes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "management_protocols.snmp.engine_ids.remotes.[].id") | String |  |  |  | Remote engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "management_protocols.snmp.engine_ids.remotes.[].address") | String |  |  |  | Hostname or IP of remote engine<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "management_protocols.snmp.engine_ids.remotes.[].udp_port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;contact</samp>](## "management_protocols.snmp.contact") | String |  |  |  | SNMP contact |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "management_protocols.snmp.location") | String |  |  |  | SNMP location |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "management_protocols.snmp.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.communities.[].name") | String | Required, Unique |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "management_protocols.snmp.communities.[].access") | String |  |  | Valid Values:<br>- ro<br>- rw |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "management_protocols.snmp.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "management_protocols.snmp.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "management_protocols.snmp.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "management_protocols.snmp.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "management_protocols.snmp.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acls</samp>](## "management_protocols.snmp.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_protocols.snmp.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acls</samp>](## "management_protocols.snmp.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_protocols.snmp.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "management_protocols.snmp.local_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.local_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_protocols.snmp.local_interfaces.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;views</samp>](## "management_protocols.snmp.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.views.[].name") | String |  |  |  | SNMP view name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "management_protocols.snmp.views.[].MIB_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "management_protocols.snmp.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "management_protocols.snmp.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "management_protocols.snmp.groups.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "management_protocols.snmp.groups.[].authentication") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "management_protocols.snmp.groups.[].read") | String |  |  |  | Read view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "management_protocols.snmp.groups.[].write") | String |  |  |  | Write view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "management_protocols.snmp.groups.[].notify") | String |  |  |  | Notify view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "management_protocols.snmp.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "management_protocols.snmp.users.[].group") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp>](## "management_protocols.snmp.users.[].remote_address") | String |  |  |  | Hostname or ip of remote engine<br>The remote_address and udp_port are used for remote users<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "management_protocols.snmp.users.[].udp_port") | Integer |  |  |  | udp_port will not be used if no remote_address is configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "management_protocols.snmp.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp>](## "management_protocols.snmp.users.[].localized") | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "management_protocols.snmp.users.[].auth") | String |  |  |  | Hash algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "management_protocols.snmp.users.[].auth_passphrase") | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "management_protocols.snmp.users.[].priv") | String |  |  |  | Encryption algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "management_protocols.snmp.users.[].priv_passphrase") | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "management_protocols.snmp.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "management_protocols.snmp.hosts.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_protocols.snmp.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "management_protocols.snmp.hosts.[].version") | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "management_protocols.snmp.hosts.[].community") | String |  |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "management_protocols.snmp.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp>](## "management_protocols.snmp.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "management_protocols.snmp.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traps</samp>](## "management_protocols.snmp.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_protocols.snmp.traps.enable") | Boolean |  | False |  | Enable or disable all snmp-traps<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "management_protocols.snmp.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "management_protocols.snmp.traps.snmp_traps.[].enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "management_protocols.snmp.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_protocols.snmp.vrfs.[].name") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_protocols.snmp.vrfs.[].enable") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    management_protocols:
      snmp:
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
            MIB_family_name: <str>
            included: <bool>
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
