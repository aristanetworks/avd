<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_settings_profiles</samp>](## "cv_settings_profiles") | List, items: Dictionary |  |  |  | List of CloudVision settings profiles that can be applied to devices using `cv_settings_profile` under node definitions.<br>Profiles support inheritance using `parent_profile`, allowing common CloudVision settings to be shared and selectively overridden per profile. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "cv_settings_profiles.[].profile") | String | Required, Unique |  | Min Length: 1 | CloudVision settings profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "cv_settings_profiles.[].parent_profile") | String |  |  | Min Length: 1 | Inherit settings from a parent profile defined under `cv_settings_profiles`.<br>The settings from this profile override settings inherited from the parent profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cvaas</samp>](## "cv_settings_profiles.[].cvaas") | Dictionary |  |  |  | State streaming to CloudVision-as-a-Service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cv_settings_profiles.[].cvaas.enabled") | Boolean |  |  |  | Enable streaming to CVaaS.<br>When enabled it will stream to 'apiserver.arista.io:443' using the VRF obtained from `default_mgmt_method` unless overridden under `clusters`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clusters</samp>](## "cv_settings_profiles.[].cvaas.clusters") | List, items: Dictionary |  | `[{'name': 'cvaas'}]` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_settings_profiles.[].cvaas.clusters.[].name") | String | Required, Unique |  | Pattern: `[a-zA-Z0-9-_]+` | Short name for the CVaaS cluster. Required here, but only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "cv_settings_profiles.[].cvaas.clusters.[].region") | String |  | `auto` | Valid Values:<br>- <code>auto</code><br>- <code>us-central1-a</code><br>- <code>us-central1-b</code><br>- <code>us-central1-c</code><br>- <code>us-4</code><br>- <code>apnortheast-1</code><br>- <code>euwest-2</code><br>- <code>eu-3</code><br>- <code>ausoutheast-1</code><br>- <code>na-northeast1-b</code><br>- <code>uk-1</code><br>- <code>india-1</code><br>- <code>staging</code><br>- <code>dev</code><br>- <code>play</code> | Optionally set the region to stream to.<br>The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.<br>"staging", "dev" and "play" are for internal Arista use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings_profiles.[].cvaas.clusters.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The VRF used to connect to CloudVision.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings_profiles.[].cvaas.clusters.[].token_file") | String |  | `/tmp/cv-onboarding-token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings_profiles.[].cvaas.clusters.[].source_interface") | String |  |  |  | Source-interface used to connect to CloudVision.<br>If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;onprem_clusters</samp>](## "cv_settings_profiles.[].onprem_clusters") | List, items: Dictionary |  |  |  | On-premise CloudVision clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;servers</samp>](## "cv_settings_profiles.[].onprem_clusters.[].servers") | List, items: Dictionary |  |  | Min Length: 1<br>Max Length: 3 | CloudVision servers that make up one cluster.<br>May be omitted when inherited from a parent CloudVision settings profile or global `cv_settings`.<br>After resolving profile and global settings, each on-prem cluster must have at least one server.<br><br>Note: Servers from this profile are merged with servers for the same cluster from the parent profile and global<br>`cv_settings`, so the combined list must not exceed three servers.<br>If a server has the same `name` as an inherited server, values from this profile override the inherited values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_settings_profiles.[].onprem_clusters.[].servers.[].name") | String | Required, Unique |  |  | Server IP address or FQDN.<br>Note: It is currently recommended to use IP address because of limitations with Image transfers from CloudVision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "cv_settings_profiles.[].onprem_clusters.[].servers.[].port") | Integer |  | `9910` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "cv_settings_profiles.[].onprem_clusters.[].name") | String | Required, Unique |  | Pattern: `[a-zA-Z0-9-_]+` | Short name for the cluster. Required here, but only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings_profiles.[].onprem_clusters.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The VRF used to connect to CloudVision.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings_profiles.[].onprem_clusters.[].token_file") | String |  | `/tmp/token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings_profiles.[].onprem_clusters.[].source_interface") | String |  |  |  | Source-interface used to connect to CloudVision.<br>If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;terminattr</samp>](## "cv_settings_profiles.[].terminattr") | Dictionary |  |  |  | Specific settings for the TerminAttr daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingestexclude</samp>](## "cv_settings_profiles.[].terminattr.ingestexclude") | String |  |  |  | Exclude paths from Sysdb on the ingest side.<br>e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smashexcludes</samp>](## "cv_settings_profiles.[].terminattr.smashexcludes") | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  | Exclude paths from the shared memory table.<br>e.g. "ale,flexCounter,hardware,kni,pulse,strata"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disable_aaa</samp>](## "cv_settings_profiles.[].terminattr.disable_aaa") | Boolean |  | `False` |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvtargetconfigs</samp>](## "cv_settings_profiles.[].terminattr.cvtargetconfigs") | List, items: String |  |  | Min Length: 1 | Set the target configuration path(s) for dynamic device configuration from CloudVision.<br>Used for MSS (Multi-Domain Segmentation Service) integrations.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_settings_profiles.[].terminattr.cvtargetconfigs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flowdns</samp>](## "cv_settings_profiles.[].terminattr.flowdns") | Boolean |  |  |  | Enable DNS resolution for flow records (TerminAttr default is true).<br>Set to false to disable DNS lookups on sFlow/IPFIX flow records.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;custom_cv_options</samp>](## "cv_settings_profiles.[].terminattr.custom_cv_options") | List, items: Dictionary |  |  |  | TerminAttr CLI options not covered by the schema.<br>Each entry renders as `-<flag>=<value>` when `value` is set, or `-<flag>` when `value` is omitted.<br>Options are appended at the end of the TerminAttr exec command line after all other flags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;flag</samp>](## "cv_settings_profiles.[].terminattr.custom_cv_options.[].flag") | String | Required |  | Min Length: 1<br>Pattern: `^(?!-)(?!.*[\s=]).+$` | TerminAttr CLI flag name without the leading dash.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_settings_profiles.[].terminattr.custom_cv_options.[].value") | String |  |  |  | Flag value. If omitted, the flag is rendered without a value (e.g. `-someflag`).<br>If set, the flag is rendered as `-flag=value`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;set_source_interfaces</samp>](## "cv_settings_profiles.[].set_source_interfaces") | Boolean |  | `True` |  | Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>Can be set to `false` to avoid changes when migrating from the old `cv_instances` model. |

=== "YAML"

    ```yaml
    # List of CloudVision settings profiles that can be applied to devices using `cv_settings_profile` under node definitions.
    # Profiles support inheritance using `parent_profile`, allowing common CloudVision settings to be shared and selectively overridden per profile.
    cv_settings_profiles:

        # CloudVision settings profile name.
      - profile: <str; length >=1; required; unique>

        # Inherit settings from a parent profile defined under `cv_settings_profiles`.
        # The settings from this profile override settings inherited from the parent profile.
        parent_profile: <str; length >=1>

        # State streaming to CloudVision-as-a-Service.
        cvaas:

          # Enable streaming to CVaaS.
          # When enabled it will stream to 'apiserver.arista.io:443' using the VRF obtained from `default_mgmt_method` unless overridden under `clusters`.
          enabled: <bool>
          clusters: # default=[{'name': 'cvaas'}]

              # Short name for the CVaaS cluster. Required here, but only used when configuring multiple clusters.
            - name: <str; required; unique>

              # Optionally set the region to stream to.
              # The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.
              # "staging", "dev" and "play" are for internal Arista use.
              region: <str; "auto" | "us-central1-a" | "us-central1-b" | "us-central1-c" | "us-4" | "apnortheast-1" | "euwest-2" | "eu-3" | "ausoutheast-1" | "na-northeast1-b" | "uk-1" | "india-1" | "staging" | "dev" | "play"; default="auto">

              # The VRF used to connect to CloudVision.
              # The value will be interpreted according to these rules:
              # - `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.
              #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
              # - `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.
              #   An error will be raised if inband management is not configured for the device.
              # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
              # - Any other string will be used directly as the VRF name.
              vrf: <str; default="use_default_mgmt_method_vrf">

              # Path to the onboarding token used for certificate based authentication.
              # The path is on the EOS device and the token file must be copied to the device first.
              token_file: <str; default="/tmp/cv-onboarding-token">

              # Source-interface used to connect to CloudVision.
              # If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
              source_interface: <str>

        # On-premise CloudVision clusters.
        onprem_clusters:

            # CloudVision servers that make up one cluster.
            # May be omitted when inherited from a parent CloudVision settings profile or global `cv_settings`.
            # After resolving profile and global settings, each on-prem cluster must have at least one server.
            #
            # Note: Servers from this profile are merged with servers for the same cluster from the parent profile and global
            # `cv_settings`, so the combined list must not exceed three servers.
            # If a server has the same `name` as an inherited server, values from this profile override the inherited values.
          - servers: # 1-3 items

                # Server IP address or FQDN.
                # Note: It is currently recommended to use IP address because of limitations with Image transfers from CloudVision.
              - name: <str; required; unique>
                port: <int; default=9910>

            # Short name for the cluster. Required here, but only used when configuring multiple clusters.
            name: <str; required; unique>

            # The VRF used to connect to CloudVision.
            # The value will be interpreted according to these rules:
            # - `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.
            #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
            # - `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.
            #   An error will be raised if inband management is not configured for the device.
            # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
            # - Any other string will be used directly as the VRF name.
            vrf: <str; default="use_default_mgmt_method_vrf">

            # Path to the onboarding token used for certificate based authentication.
            # The path is on the EOS device and the token file must be copied to the device first.
            token_file: <str; default="/tmp/token">

            # Source-interface used to connect to CloudVision.
            # If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
            source_interface: <str>

        # Specific settings for the TerminAttr daemon.
        terminattr:

          # Exclude paths from Sysdb on the ingest side.
          # e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"
          ingestexclude: <str>

          # Exclude paths from the shared memory table.
          # e.g. "ale,flexCounter,hardware,kni,pulse,strata"
          smashexcludes: <str; default="ale,flexCounter,hardware,kni,pulse,strata">

          # Disable AAA authorization and accounting.
          # When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization.
          disable_aaa: <bool; default=False>

          # Set the target configuration path(s) for dynamic device configuration from CloudVision.
          # Used for MSS (Multi-Domain Segmentation Service) integrations.
          cvtargetconfigs: # >=1 items
            - <str>

          # Enable DNS resolution for flow records (TerminAttr default is true).
          # Set to false to disable DNS lookups on sFlow/IPFIX flow records.
          flowdns: <bool>

          # TerminAttr CLI options not covered by the schema.
          # Each entry renders as `-<flag>=<value>` when `value` is set, or `-<flag>` when `value` is omitted.
          # Options are appended at the end of the TerminAttr exec command line after all other flags.
          custom_cv_options:

              # TerminAttr CLI flag name without the leading dash.
            - flag: <str; length >=1; required>

              # Flag value. If omitted, the flag is rendered without a value (e.g. `-someflag`).
              # If set, the flag is rendered as `-flag=value`.
              value: <str>

        # Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
        # Can be set to `false` to avoid changes when migrating from the old `cv_instances` model.
        set_source_interfaces: <bool; default=True>
    ```
