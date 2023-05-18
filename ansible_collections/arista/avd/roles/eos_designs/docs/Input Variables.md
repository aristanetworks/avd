---
search:
  boost: 2
---

# Input Variables

## AVD Data Conversion Mode

Conversion Mode for AVD input data conversion.
Input data conversion will perform type conversion of input variables as defined in the schema.
The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
"disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.
"info" will produce regular log messages.
"debug" will produce hidden debug messages viewable with -v.
"quiet" will not produce any messages

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_conversion_mode</samp>](## "avd_data_conversion_mode") | String |  | debug | Valid Values:<br>- disabled<br>- error<br>- warning<br>- info<br>- debug<br>- quiet |  |

=== "YAML"

    ```yaml
    avd_data_conversion_mode: <str>
    ```

## AVD Data Validation Mode

Validation Mode for AVD input data validation.
Input data validation will validate the input variables according to the schema.
During validation, messages will generated with information about the host(s) and key(s) which failed validation.
"disabled" means that validation will not run.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.
"info" will produce regular log messages.
"debug" will produce hidden debug messages viewable with -v.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_validation_mode</samp>](## "avd_data_validation_mode") | String |  | warning | Valid Values:<br>- disabled<br>- error<br>- warning<br>- info<br>- debug |  |

=== "YAML"

    ```yaml
    avd_data_validation_mode: <str>
    ```

## EOS Designs Custom Templates

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_custom_templates</samp>](## "eos_designs_custom_templates") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- template</samp>](## "eos_designs_custom_templates.[].template") | String | Required |  |  | Template file. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp>](## "eos_designs_custom_templates.[].options") | Dictionary |  |  |  | Template options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp>](## "eos_designs_custom_templates.[].options.list_merge") | String |  | append_rp |  | Merge strategy for lists |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp>](## "eos_designs_custom_templates.[].options.strip_empty_keys") | Boolean |  | True |  | Filter out keys from the generated output if value is null/none/undefined |

=== "YAML"

    ```yaml
    eos_designs_custom_templates:
      - template: <str>
        options:
          list_merge: <str>
          strip_empty_keys: <bool>
    ```

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

## EVPN Ebgp Gateway Inter Domain

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_inter_domain</samp>](## "evpn_ebgp_gateway_inter_domain") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_inter_domain: <bool>
    ```

## Hardware Counters

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsability of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "hardware_counters.features.[].name") | String |  |  | Valid Values:<br>- acl<br>- decap-group<br>- directflow<br>- ecn<br>- flow-spec<br>- gre tunnel interface<br>- ip<br>- mpls interface<br>- mpls lfib<br>- mpls tunnel<br>- multicast<br>- nexthop<br>- pbr<br>- pdp<br>- policing interface<br>- qos<br>- qos dual-rate-policer<br>- route<br>- routed-port<br>- subinterface<br>- tapagg<br>- traffic-class<br>- traffic-policy<br>- vlan<br>- vlan-interface<br>- vni decap<br>- vni encap<br>- vtep decap<br>- vtep encap |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- in<br>- out<br>- cpu | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- mac | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    hardware_counters:
      features:
        - name: <str>
          direction: <str>
          address_type: <str>
          layer3: <bool>
          vrf: <str>
          prefix: <str>
          units_packets: <bool>
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

## Management Destination Networks

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

## Management Gateway

OOB Management interface gateway in IPv4 format.
Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

=== "YAML"

    ```yaml
    mgmt_gateway: <str>
    ```

## Management Interface Description

Management interface description

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") | String |  | oob_management |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_description: <str>
    ```

## Management Interface VRF

OOB Management VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_vrf: <str>
    ```

## Management Interface

OOB Management interface.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

=== "YAML"

    ```yaml
    mgmt_interface: <str>
    ```

## Management VRF Routing

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
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | False |  | Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | hostname_and_ip | Valid Values:<br>- hostname_and_ip<br>- system_mac | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}<br>- `system_mac` generate the switch default engine id for AVD usage<br>  To use this, `system_mac_address` MUST be set for the device<br>  The formula is f5717f + system_mac_address + 00<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | False |  | Requires compute_local_engineid to be `true`.<br>If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.<br>The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  | Configuration of the SNMP User Groups are currently only possible using `structured_config`.<br> |
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

## System MAC Address

Set to the same MAC address as available in "show version" on the device.
"system_mac_address" can also be set under "Fabric Topology".
If both are set, the setting under "Fabric Topology" takes precedence.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  |  |

=== "YAML"

    ```yaml
    system_mac_address: <str>
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
