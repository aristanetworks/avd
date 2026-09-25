<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dns_settings_profiles</samp>](## "dns_settings_profiles") | List, items: Dictionary |  |  |  | List of DNS settings profiles that can be applied to devices using `dns_settings_profile` under node definitions.<br>Profiles support inheritance using `parent_profile`, allowing common DNS settings to be shared and selectively overridden per profile. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "dns_settings_profiles.[].profile") | String | Required, Unique |  |  | DNS settings profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "dns_settings_profiles.[].parent_profile") | String |  | `` |  | Inherit settings from a parent profile defined under `dns_settings_profiles`.<br>The settings from this profile override settings inherited from the parent profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "dns_settings_profiles.[].servers") | List, items: Dictionary |  |  | Min Length: 1 | DNS servers for this profile.<br>If omitted, servers are inherited from `parent_profile` or from global `dns_settings.servers`.<br>At least one DNS server must be available after profile inheritance is resolved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vrf</samp>](## "dns_settings_profiles.[].servers.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the DNS server under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the DNS server under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. Remember to set the `dns_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dns_settings_profiles.[].servers.[].ip_address") | String | Required |  |  | IPv4 or IPv6 address for DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "dns_settings_profiles.[].servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "dns_settings_profiles.[].domain") | String |  |  |  | DNS domain name like 'fabric.local' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_list</samp>](## "dns_settings_profiles.[].domain_list") | List, items: String |  |  |  | Domain names to complete unqualified host names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dns_settings_profiles.[].domain_list.[]") | String |  |  |  | Domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "dns_settings_profiles.[].vrfs") | List, items: Dictionary |  |  |  | Per-VRF DNS lookup source-interface settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "dns_settings_profiles.[].vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "dns_settings_profiles.[].vrfs.[].source_interface") | String |  |  |  | Source interface to use for DNS lookups in this VRF.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;set_source_interfaces</samp>](## "dns_settings_profiles.[].set_source_interfaces") | Boolean |  | `True` |  | Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>Can be set to `false` to avoid changes when migrating from the old `name_servers` model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_hosts</samp>](## "dns_settings_profiles.[].ip_hosts") | List, items: Dictionary |  |  |  | Static hostname-to-IP address mappings to configure in the local host table. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "dns_settings_profiles.[].ip_hosts.[].hostname") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_addresses</samp>](## "dns_settings_profiles.[].ip_hosts.[].ipv4_addresses") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dns_settings_profiles.[].ip_hosts.[].ipv4_addresses.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # List of DNS settings profiles that can be applied to devices using `dns_settings_profile` under node definitions.
    # Profiles support inheritance using `parent_profile`, allowing common DNS settings to be shared and selectively overridden per profile.
    dns_settings_profiles:

        # DNS settings profile name.
      - profile: <str; required; unique>

        # Inherit settings from a parent profile defined under `dns_settings_profiles`.
        # The settings from this profile override settings inherited from the parent profile.
        parent_profile: <str; default="">

        # DNS servers for this profile.
        # If omitted, servers are inherited from `parent_profile` or from global `dns_settings.servers`.
        # At least one DNS server must be available after profile inheritance is resolved.
        servers: # >=1 items

            # The value of `vrf` will be interpreted according to these rules:
            # - `use_mgmt_interface_vrf` will configure the DNS server under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as DNS lookup source-interface.
            #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
            # - `use_inband_mgmt_vrf` will configure the DNS server under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as DNS lookup source-interface.
            #   An error will be raised if inband management is not configured for the device.
            # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
            # - Any other string will be used directly as the VRF name. Remember to set the `dns_settings.vrfs[].source_interface` if needed.
          - vrf: <str; default="use_default_mgmt_method_vrf">

            # IPv4 or IPv6 address for DNS server.
            ip_address: <str; required>

            # Priority value (lower is first).
            priority: <int; 0-4>

        # DNS domain name like 'fabric.local'
        domain: <str>

        # Domain names to complete unqualified host names.
        domain_list:

            # Domain name.
          - <str>

        # Per-VRF DNS lookup source-interface settings.
        vrfs:

            # VRF name.
          - name: <str; required; unique>

            # Source interface to use for DNS lookups in this VRF.
            # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
            source_interface: <str>

        # Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
        # Can be set to `false` to avoid changes when migrating from the old `name_servers` model.
        set_source_interfaces: <bool; default=True>

        # Static hostname-to-IP address mappings to configure in the local host table.
        ip_hosts:
          - hostname: <str; required; unique>
            ipv4_addresses: # >=1 items; required
              - <str>
    ```
