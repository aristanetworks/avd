<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  | SNMP settings.<br>Configuration of remote SNMP engine IDs are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | `False` |  | Enables SNMP location using `location_template` value. |
    | [<samp>&nbsp;&nbsp;location_template</samp>](## "snmp_settings.location_template") | String |  | `{fabric_name} {dc_name?> }{pod_name?> }{rack?> }{hostname}` |  | Customize the SNMP location description.<br>The available template fields are:<br>  - fabric_name: The logical name of the fabric.<br>  - dc_name: The name of the data center associated with the fabric.<br>  - pod_name: The pod or cluster grouping within the data center.<br>  - rack: Physical rack location of switch.<br>  - hostname: Hostname used in inventory. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the SNMP ACL under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the SNMP ACL under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the SNMP ACL under the VRF for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.vrfs.[].enable") | Boolean |  |  |  | Enable/disable SNMP for this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "snmp_settings.vrfs.[].source_interface") | String |  |  |  | Source interface to use for SNMP hosts in this VRF.<br>If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "snmp_settings.vrfs.[].ipv4_acl") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "snmp_settings.vrfs.[].ipv6_acl") | String |  |  |  | IPv6 access-list name. |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | `False` |  | Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | `hostname_and_ip` | Valid Values:<br>- <code>hostname_and_ip</code><br>- <code>system_mac</code> | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}.<br>- `system_mac` generate the switch default engine id for AVD usage.<br>  To use this, `system_mac_address` MUST be set for the device.<br>  The formula is f5717f + system_mac_address + 00.<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | `False` |  | Requires compute_local_engineid to be `true`.<br>If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.<br>The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  | Configuration of local SNMP users.<br>Configuration of remote SNMP users are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- <code>des</code><br>- <code>aes</code><br>- <code>aes192</code><br>- <code>aes256</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_settings.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "snmp_settings.hosts.[].host") | String |  |  |  | Host IP address or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.hosts.[].vrf") | String |  |  |  | VRF Name.<br>The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the SNMP host under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as SNMP source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the SNMP host under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as SNMP source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the SNMP host under the VRF and set the source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. Remember to set the `snmp_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_mgmt_interface_vrf</samp>](## "snmp_settings.hosts.[].use_mgmt_interface_vrf") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrf: "use_mgmt_interface_vrf"</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_inband_mgmt_vrf</samp>](## "snmp_settings.hosts.[].use_inband_mgmt_vrf") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrf: "use_inband_mgmt_vrf"</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.hosts.[].version") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>2c</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_settings.hosts.[].community") | String |  |  |  | Community name. Required with version "1" or "2c". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_settings.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;username</samp>](## "snmp_settings.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_settings.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_settings.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.communities.[].name") | String | Required, Unique |  |  | Community name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_settings.communities.[].access") | String |  |  | Valid Values:<br>- <code>ro</code><br>- <code>rw</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_settings.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_settings.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_settings.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_settings.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.views.[].name") | String |  |  |  | SNMP view name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_settings.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_settings.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_settings.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.groups.[].name") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.groups.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_settings.groups.[].authentication") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_settings.groups.[].read") | String |  |  |  | Read view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_settings.groups.[].write") | String |  |  |  | Write view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_settings.groups.[].notify") | String |  |  |  | Notify view. |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_settings.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.traps.enable") | Boolean |  |  |  | Enable or disable all snmp-traps.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_settings.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps.<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_settings.traps.snmp_traps.[].enabled") | Boolean |  |  |  | The trap is enabled unless this is set to false. |
    | [<samp>&nbsp;&nbsp;enable_mgmt_interface_vrf</samp>](## "snmp_settings.enable_mgmt_interface_vrf") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrfs[name="use_mgmt_interface_vrf"].enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;enable_inband_mgmt_vrf</samp>](## "snmp_settings.enable_inband_mgmt_vrf") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrfs[name="use_inband_mgmt_vrf"].enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_settings.ipv4_acls") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrfs[].ipv4_acl</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_settings.ipv6_acls") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>vrfs[].ipv6_acl</samp> instead.</span> |

=== "YAML"

    ```yaml
    # SNMP settings.
    # Configuration of remote SNMP engine IDs are currently only possible using `structured_config`.
    snmp_settings:

      # SNMP contact.
      contact: <str>

      # Enables SNMP location using `location_template` value.
      location: <bool; default=False>

      # Customize the SNMP location description.
      # The available template fields are:
      #   - fabric_name: The logical name of the fabric.
      #   - dc_name: The name of the data center associated with the fabric.
      #   - pod_name: The pod or cluster grouping within the data center.
      #   - rack: Physical rack location of switch.
      #   - hostname: Hostname used in inventory.
      location_template: <str; default="{fabric_name} {dc_name?> }{pod_name?> }{rack?> }{hostname}">
      vrfs:

          # VRF name.
          # The value will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the SNMP ACL under the VRF set with `mgmt_interface_vrf`.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the SNMP ACL under the VRF set with `inband_mgmt_vrf`.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the SNMP ACL under the VRF for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name.
        - name: <str; required; unique>

          # Enable/disable SNMP for this VRF.
          enable: <bool>

          # Source interface to use for SNMP hosts in this VRF.
          # If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
          # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
          source_interface: <str>

          # IPv4 access-list name.
          ipv4_acl: <str>

          # IPv6 access-list name.
          ipv6_acl: <str>

      # Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.
      compute_local_engineid: <bool; default=False>

      # `compute_local_engineid_source` supports:
      # - `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1
      #   the string generated via the concatenation of the hostname plus the management IP.
      #   {{ inventory_hostname }} + {{ switch.mgmt_ip }}.
      # - `system_mac` generate the switch default engine id for AVD usage.
      #   To use this, `system_mac_address` MUST be set for the device.
      #   The formula is f5717f + system_mac_address + 00.
      compute_local_engineid_source: <str; "hostname_and_ip" | "system_mac"; default="hostname_and_ip">

      # Requires compute_local_engineid to be `true`.
      # If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.
      # The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.
      compute_v3_user_localized_key: <bool; default=False>

      # Configuration of local SNMP users.
      # Configuration of remote SNMP users are currently only possible using `structured_config`.
      users:

          # Username.
        - name: <str>

          # Group name.
          group: <str>
          version: <str; "v1" | "v2c" | "v3">
          auth: <str; "md5" | "sha" | "sha256" | "sha384" | "sha512">

          # Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set.
          auth_passphrase: <str>
          priv: <str; "des" | "aes" | "aes192" | "aes256">

          # Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set.
          priv_passphrase: <str>
      hosts:

          # Host IP address or name.
        - host: <str>

          # VRF Name.
          # The value of `vrf` will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the SNMP host under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as SNMP source-interface.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the SNMP host under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as SNMP source-interface.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the SNMP host under the VRF and set the source-interface for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name. Remember to set the `snmp_settings.vrfs[].source_interface` if needed.
          vrf: <str>
          version: <str; "1" | "2c" | "3">

          # Community name. Required with version "1" or "2c".
          community: <str>
          users:
            - username: <str>
              authentication_level: <str; "auth" | "noauth" | "priv">
      communities:

          # Community name.
        - name: <str; required; unique>
          access: <str; "ro" | "rw">
          access_list_ipv4:

            # IPv4 access list name.
            name: <str>
          access_list_ipv6:

            # IPv6 access list name.
            name: <str>
          view: <str>
      views:

          # SNMP view name.
        - name: <str>
          mib_family_name: <str>
          included: <bool>
      groups:

          # Group name.
        - name: <str>
          version: <str; "v1" | "v2c" | "v3">
          authentication: <str; "auth" | "noauth" | "priv">

          # Read view.
          read: <str>

          # Write view.
          write: <str>

          # Notify view.
          notify: <str>
      traps:

        # Enable or disable all snmp-traps.
        enable: <bool>
        snmp_traps:

            # Enable or disable specific snmp-traps and their sub_traps.
            # Examples:
            # - "bgp"
            # - "bgp established"
          - name: <str>

            # The trap is enabled unless this is set to false.
            enabled: <bool>
    ```
