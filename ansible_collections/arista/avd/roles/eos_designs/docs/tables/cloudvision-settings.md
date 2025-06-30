<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_settings</samp>](## "cv_settings") | Dictionary |  |  |  | Settings for CloudVision telemetry streaming and provisioning. |
    | [<samp>&nbsp;&nbsp;cvaas</samp>](## "cv_settings.cvaas") | Dictionary |  |  |  | State streaming to CloudVision-as-a-Service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cv_settings.cvaas.enabled") | Boolean | Required |  |  | Enable streaming to CVaaS.<br>When enabled it will stream to 'apiserver.arista.io:443' using the VRF obtained from `default_mgmt_method` unless overridden under `clusters`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;clusters</samp>](## "cv_settings.cvaas.clusters") | List, items: Dictionary |  | `[{'name': 'cvaas'}]` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_settings.cvaas.clusters.[].name") | String | Required, Unique |  | Pattern: `^[a-zA-Z1-9-_]+$` | Short name for the CVaaS cluster. Required here, but only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "cv_settings.cvaas.clusters.[].region") | String |  | `auto` | Valid Values:<br>- <code>auto</code><br>- <code>us-central1-a</code><br>- <code>us-central1-b</code><br>- <code>us-central1-c</code><br>- <code>apnortheast-1</code><br>- <code>euwest-2</code><br>- <code>ausoutheast-1</code><br>- <code>na-northeast1-b</code><br>- <code>uk-1</code><br>- <code>india-1</code><br>- <code>staging</code><br>- <code>dev</code><br>- <code>play</code> | Optionally set the region to stream to.<br>The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.<br>"staging", "dev" and "play" are for internal Arista use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings.cvaas.clusters.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The VRF used to connect to CloudVision.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings.cvaas.clusters.[].token_file") | String |  | `/tmp/cv-onboarding-token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings.cvaas.clusters.[].source_interface") | String |  |  |  | Source-interface used to connect to CloudVision.<br>If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`. |
    | [<samp>&nbsp;&nbsp;onprem_clusters</samp>](## "cv_settings.onprem_clusters") | List, items: Dictionary |  |  |  | On-premise CloudVision clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_settings.onprem_clusters.[].name") | String | Required, Unique |  | Pattern: `^[a-zA-Z1-9-_]+$` | Short name for the cluster. Required here, but only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "cv_settings.onprem_clusters.[].servers") | List, items: Dictionary | Required |  | Min Length: 1<br>Max Length: 3 | CloudVision servers that makes up one cluster. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_settings.onprem_clusters.[].servers.[].name") | String | Required, Unique |  |  | Server FQDN or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "cv_settings.onprem_clusters.[].servers.[].port") | Integer |  | `9910` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings.onprem_clusters.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The VRF used to connect to CloudVision.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the VRF set with `mgmt_interface_vrf` and configure the `mgmt_interface` as the source interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the VRF set with `inband_mgmt_vrf` and configure the `inband_mgmt_interface` as the source interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings.onprem_clusters.[].token_file") | String |  | `/tmp/token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings.onprem_clusters.[].source_interface") | String |  |  |  | Source-interface used to connect to CloudVision.<br>If not set, the source interface may be set automatically when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`. |
    | [<samp>&nbsp;&nbsp;terminattr</samp>](## "cv_settings.terminattr") | Dictionary |  |  |  | Specific settings for the TerminAttr daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ingestexclude</samp>](## "cv_settings.terminattr.ingestexclude") | String |  |  |  | Exclude paths from Sysdb on the ingest side.<br>e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;smashexcludes</samp>](## "cv_settings.terminattr.smashexcludes") | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  | Exclude paths from the shared memory table.<br>e.g. "ale,flexCounter,hardware,kni,pulse,strata"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disable_aaa</samp>](## "cv_settings.terminattr.disable_aaa") | Boolean |  | `False` |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization.<br> |
    | [<samp>&nbsp;&nbsp;set_source_interfaces</samp>](## "cv_settings.set_source_interfaces") | Boolean |  | `True` |  | Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>Can be set to `false` to avoid changes when migrating from old `cv_instances` model. |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") <span style="color:red">deprecated</span> | String |  |  |  | On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.<br>If not set, TerminAttr will be configured with certificate based authentication:<br>- On-premise using token onboarding. Default token path is '/tmp/token'.<br>- CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.<br>Token must be copied to the device first.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") <span style="color:red">removed</span> | String |  |  |  | IPv4 address or DNS name for CloudVision.<br>This variable only supports an on-premise single-node cluster or the DNS name of a CloudVision as a Service instance.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") <span style="color:red">deprecated</span> | List, items: String |  |  |  | List of IPv4 addresses or DNS names for CloudVision.<br>For on-premise CloudVision enter all the nodes of the cluster.<br>For CloudVision as a Service enter the DNS name of the instance.<br>`eos_designs` only supports one CloudVision cluster.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cvp_instance_ips.[]") | String |  |  |  | IPv4 address or DNS name for CloudVision |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") <span style="color:red">deprecated</span> | String |  |  |  | cvp_token_file is the path to the token file on the switch.<br>If not set the default locations for on-premise or CVaaS will be used.<br>See cvp_ingestauth_key for details.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") <span style="color:red">deprecated</span> | Boolean |  | `False` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") <span style="color:red">deprecated</span> | String |  | `/Sysdb/cell/1/agent,/Sysdb/cell/2/agent` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") <span style="color:red">deprecated</span> | Integer |  | `9910` |  | Port number used for Terminattr connection to an on-premise CloudVision cluster.<br>The port number is always 443 when using CloudVision as a Service, so this value is ignored.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") <span style="color:red">deprecated</span> | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cv_settings</samp> instead.</span> |

=== "YAML"

    ```yaml
    # Settings for CloudVision telemetry streaming and provisioning.
    cv_settings:

      # State streaming to CloudVision-as-a-Service.
      cvaas:

        # Enable streaming to CVaaS.
        # When enabled it will stream to 'apiserver.arista.io:443' using the VRF obtained from `default_mgmt_method` unless overridden under `clusters`.
        enabled: <bool; required>
        clusters: # default=[{'name': 'cvaas'}]

            # Short name for the CVaaS cluster. Required here, but only used when configuring multiple clusters.
          - name: <str; required; unique>

            # Optionally set the region to stream to.
            # The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.
            # "staging", "dev" and "play" are for internal Arista use.
            region: <str; "auto" | "us-central1-a" | "us-central1-b" | "us-central1-c" | "apnortheast-1" | "euwest-2" | "ausoutheast-1" | "na-northeast1-b" | "uk-1" | "india-1" | "staging" | "dev" | "play"; default="auto">

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

          # Short name for the cluster. Required here, but only used when configuring multiple clusters.
        - name: <str; required; unique>

          # CloudVision servers that makes up one cluster.
          servers: # 1-3 items; required

              # Server FQDN or IP address.
            - name: <str; required; unique>
              port: <int; default=9910>

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

      # Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
      # Can be set to `false` to avoid changes when migrating from old `cv_instances` model.
      set_source_interfaces: <bool; default=True>

    # On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.
    # If not set, TerminAttr will be configured with certificate based authentication:
    # - On-premise using token onboarding. Default token path is '/tmp/token'.
    # - CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.
    # Token must be copied to the device first.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    cvp_ingestauth_key: <str>

    # List of IPv4 addresses or DNS names for CloudVision.
    # For on-premise CloudVision enter all the nodes of the cluster.
    # For CloudVision as a Service enter the DNS name of the instance.
    # `eos_designs` only supports one CloudVision cluster.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    cvp_instance_ips:

        # IPv4 address or DNS name for CloudVision
      - <str>

    # cvp_token_file is the path to the token file on the switch.
    # If not set the default locations for on-premise or CVaaS will be used.
    # See cvp_ingestauth_key for details.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    cvp_token_file: <str>
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    terminattr_disable_aaa: <bool; default=False>
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    terminattr_ingestexclude: <str; default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent">

    # Port number used for Terminattr connection to an on-premise CloudVision cluster.
    # The port number is always 443 when using CloudVision as a Service, so this value is ignored.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    terminattr_ingestgrpcurl_port: <int; default=9910>
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `cv_settings` instead.
    terminattr_smashexcludes: <str; default="ale,flexCounter,hardware,kni,pulse,strata">
    ```
