---
search:
  boost: 2
---

# Input Variables

## Event Handlers

Gives ability to monitor and react to Syslog messages provides a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event handler name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to run when handler is triggered |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |

=== "YAML"

    ```yaml
    event_handlers:
      - name: <str>
        action_type: <str>
        action: <str>
        delay: <int>
        trigger: <str>
        regex: <str>
        asynchronous: <bool>
    ```

## Inband Management Subnet

Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
SVI IP address will be assigned as follows:
virtual-router: <subnet> + 1
l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
l2leafs       : <subnet> + 3 + <l2leaf id>
GW on l2leafs : <subnet> + 1
Assign range larger than total l2leafs + 5

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>inband_management_subnet</samp>](## "inband_management_subnet") | String |  |  |  |  |

=== "YAML"

    ```yaml
    inband_management_subnet: <str>
    ```

## Inband Management VLAN

VLAN number assigned to Inband Management SVI on l2leafs in default VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>inband_management_vlan</samp>](## "inband_management_vlan") | Integer |  | 4092 |  |  |

=== "YAML"

    ```yaml
    inband_management_vlan: <int>
    ```

## Local Users

Dictionary of local users

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 1<br>Max: 15 | Initial privilege level with local EXEC authorization. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  | True |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  | SSH key string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If "disabled" is true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user. |

=== "YAML"

    ```yaml
    local_users:
      - name: <str>
        privilege: <int>
        role: <str>
        sha512_password: <str>
        no_password: <bool>
        ssh_key: <str>
        disabled: <bool>
    ```

## Management Eapi

Default is https management eAPI enabled.
The vrf is set to < mgmt_interface_vrf >

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    management_eapi:
      enable_http: <bool>
      enable_https: <bool>
      default_services: <bool>
    ```

## Mgmt Destination Networks

OOB mgmt interface destination networks - override default route

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_network/Mask |

=== "YAML"

    ```yaml
    mgmt_destination_networks:
      - <str>
    ```

## Mgmt Gateway

Management interface configuration and it is IPv4 address

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

=== "YAML"

    ```yaml
    mgmt_gateway: <str>
    ```

## Mgmt Interface VRF

Management interface configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_vrf: <str>
    ```

## Mgmt Interface

Management interface configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

=== "YAML"

    ```yaml
    mgmt_interface: <str>
    ```

## Mgmt VRF Routing

Management interface configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    mgmt_vrf_routing: <bool>
    ```

## Name Server

Only name_server from eos_ci_config_gen.
The variables will make it to the intended config.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>name_server</samp>](## "name_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |

=== "YAML"

    ```yaml
    name_server:
      source:
        vrf: <str>
      nodes:
        - <str>
    ```

## Name Servers

Only eos_designs name_servers variables

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_servers.[].&lt;str&gt;") | String |  |  |  | IPv4 address |

=== "YAML"

    ```yaml
    name_servers:
      - <str>
    ```

## Snmp Settings

Set SNMP settings. It is optional.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | False |  | SNMP location. Formatted as {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }} |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | False |  | Generate a local engineId for SNMP by hashing via SHA1 the string<br>generated via the concatenation of the hostname plus the management IP.<br>{{ inventory_hostname }} + {{ switch.mgmt_ip }}<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | False |  | Requires compute_local_engineid to be `true` if enabled, the SNMPv3<br>passphrases for auth and priv are transfromed using RFC 2574,<br>matching the value they would take in EOS cli the algorithm requires<br>a local engineId which is unknown to AVD hence the necessity to generate<br>one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- md5<br>- sha<br>- sha256<br>- sha384<br>- sha512 | It is optional |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Clear passphrase, requires auth, recommended to use vault |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- des<br>- aes<br>- aes192<br>- aes256 | It is optional |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Clear pasphrase, requires priv, recommended to use vault |

=== "YAML"

    ```yaml
    snmp_settings:
      contact: <str>
      location: <bool>
      compute_local_engineid: <bool>
      compute_v3_user_localized_key: <bool>
      users:
        - name: <str>
          group: <str>
          version: <str>
          auth: <str>
          auth_passphrase: <str>
          priv: <str>
          priv_passphrase: <str>
    ```

## Timezone

Clock timezone is optional

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  |  |

=== "YAML"

    ```yaml
    timezone: <str>
    ```
