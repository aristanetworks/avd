---
search:
  boost: 2
---

# Input Variables

## Event Handlers

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging<br>- on-startup-config | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
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

## Local Users

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- /bin/bash<br>- /bin/sh<br>- /sbin/nologin | Specify shell for the user<br> |

=== "YAML"

    ```yaml
    local_users:
      - name: <str>
        disabled: <bool>
        privilege: <int>
        role: <str>
        sha512_password: <str>
        no_password: <bool>
        ssh_key: <str>
        shell: <str>
    ```

## Management Eapi

Default is HTTPS management eAPI enabled.
The VRF is set to < mgmt_interface_vrf >.

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

List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
Replaces the default route.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |

=== "YAML"

    ```yaml
    mgmt_destination_networks:
      - <str>
    ```

## Mgmt Gateway

OOB Management interface gateway in IPv4 format.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

=== "YAML"

    ```yaml
    mgmt_gateway: <str>
    ```

## Mgmt Interface VRF

OOB Management VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_vrf: <str>
    ```

## Mgmt Interface

OOB Management interface.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

=== "YAML"

    ```yaml
    mgmt_interface: <str>
    ```

## Mgmt VRF Routing

Configure IP routing for the OOB Management VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    mgmt_vrf_routing: <bool>
    ```

## Name Servers

List of DNS servers. The VRF is set to < mgmt_interface_vrf >.

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

Set SNMP settings (optional).

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | False |  | Set SNMP location. Formatted as {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }}. |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | False |  | Generate a local engineId for SNMP by hashing via SHA1, the string<br>generated via the concatenation of the hostname plus the management IP.<br>{{ inventory_hostname }} + {{ switch.mgmt_ip }}<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | hostname_and_ip | Valid Values:<br>- hostname_and_ip<br>- system_mac | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}<br>- `system_mac` generate the switch default engine id for AVD usage<br>  To use this, `system_mac_address` MUST be set for the device<br>  The formula is f5717f + system_mac_address + 00<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | False |  | Requires compute_local_engineid to be `true`. If enabled, the SNMPv3<br>passphrases for auth and priv are transformed using RFC 2574,<br>matching the value they would take in EOS CLI. The algorithm requires<br>a local engineId, which is unknown to AVD, hence the necessity to generate<br>one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- md5<br>- sha<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- des<br>- aes<br>- aes192<br>- aes256 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set. |

=== "YAML"

    ```yaml
    snmp_settings:
      contact: <str>
      location: <bool>
      compute_local_engineid: <bool>
      compute_local_engineid_source: <str>
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

Clock timezone like "CET" or "US/Pacific".

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  |  |

=== "YAML"

    ```yaml
    timezone: <str>
    ```
