=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  | SNMP settings<br>For SNMP local-interfaces see "source_interfaces.snmp"<br>Configuration of remote SNMP engine IDs are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | `False` |  | Set SNMP location. Formatted as "<fabric_name> <dc_name> <pod_name> <switch_rack> <inventory_hostname>". |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_settings.vrfs") | List, items: Dictionary |  |  |  | Enable/disable SNMP for one or more VRFs.<br>Can be used in combination with "enable_mgmt_interface_vrf" and "enable_inband_mgmt_vrf". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.vrfs.[].enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_mgmt_interface_vrf</samp>](## "snmp_settings.enable_mgmt_interface_vrf") | Boolean |  |  |  | Enable/disable SNMP for the VRF set with "mgmt_interface_vrf".<br>Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device.<br>Can be used in combination with "vrfs" and "enable_inband_mgmt_vrf". |
    | [<samp>&nbsp;&nbsp;enable_inband_mgmt_vrf</samp>](## "snmp_settings.enable_inband_mgmt_vrf") | Boolean |  |  |  | Enable/disable SNMP for the VRF set with "inband_mgmt_vrf".<br>Ignored if inband management is not configured for the device.<br>Can be used in combination with "vrfs" and "enable_mgmt_interface_vrf". |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | `False` |  | Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | `hostname_and_ip` | Valid Values:<br>- hostname_and_ip<br>- system_mac | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}.<br>- `system_mac` generate the switch default engine id for AVD usage.<br>  To use this, `system_mac_address` MUST be set for the device.<br>  The formula is f5717f + system_mac_address + 00.<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | `False` |  | Requires compute_local_engineid to be `true`.<br>If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.<br>The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  | Configuration of local SNMP users.<br>Configuration of remote SNMP users are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- md5<br>- sha<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- des<br>- aes<br>- aes192<br>- aes256 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_settings.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "snmp_settings.hosts.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.hosts.[].vrf") | String |  |  |  | VRF Name.<br>Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_mgmt_interface_vrf</samp>](## "snmp_settings.hosts.[].use_mgmt_interface_vrf") | Boolean |  |  |  | Configure the SNMP host under the VRF set with "mgmt_interface_vrf". Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_inband_mgmt_vrf</samp>](## "snmp_settings.hosts.[].use_inband_mgmt_vrf") | Boolean |  |  |  | Configure the SNMP host under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.hosts.[].version") | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_settings.hosts.[].community") | String |  |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_settings.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp>](## "snmp_settings.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_settings.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_settings.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.communities.[].name") | String | Required, Unique |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_settings.communities.[].access") | String |  |  | Valid Values:<br>- ro<br>- rw |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_settings.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_settings.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_settings.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_settings.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_settings.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_settings.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.views.[].name") | String |  |  |  | SNMP view name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_settings.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_settings.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_settings.views.[].MIB_family_name") <span style="color:red">deprecated</span> | String |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>mib_family_name</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_settings.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.groups.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_settings.groups.[].authentication") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_settings.groups.[].read") | String |  |  |  | Read view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_settings.groups.[].write") | String |  |  |  | Write view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_settings.groups.[].notify") | String |  |  |  | Notify view |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_settings.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.traps.enable") | Boolean |  | `False` |  | Enable or disable all snmp-traps<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_settings.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_settings.traps.snmp_traps.[].enabled") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    snmp_settings:
      contact: <str>
      location: <bool>
      vrfs:
        - name: <str>
          enable: <bool>
      enable_mgmt_interface_vrf: <bool>
      enable_inband_mgmt_vrf: <bool>
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
      hosts:
        - host: <str>
          vrf: <str>
          use_mgmt_interface_vrf: <bool>
          use_inband_mgmt_vrf: <bool>
          version: <str>
          community: <str>
          users:
            - username: <str>
              authentication_level: <str>
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
      traps:
        enable: <bool>
        snmp_traps:
          - name: <str>
            enabled: <bool>
    ```
