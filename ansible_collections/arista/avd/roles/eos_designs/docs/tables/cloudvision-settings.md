<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_settings</samp>](## "cv_settings") | Dictionary |  |  |  | Settings for configuring CloudVision telemetry streaming and provisioning.<br><br>`cv_settings` replaces the following deprecated keys, which are ignored when `cv_settings` is set:<br>- `cvp_ingestauth_key`<br>- `cvp_instance_ip`<br>- `cvp_instance_ips`<br>- `cvp_token_file`<br>- `terminattr_disable_aaa`<br>- `terminattr_ingestexclude`<br>- `terminattr_ingestgrpcurl_port`<br>- `terminattr_smashexcludes` |
    | [<samp>&nbsp;&nbsp;cvaas_clusters</samp>](## "cv_settings.cvaas_clusters") | List, items: Dictionary |  |  |  | CloudVision as a Service clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cv_settings.cvaas_clusters.[].name") | String | Required, Unique |  |  | Cluster Name.<br>Only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "cv_settings.cvaas_clusters.[].server") | String | Required |  | Pattern: ^[a-z1-9\.-]+\.arista\.io | CVaaS Server name like 'www.arista.io' or 'www.cv-prod-euwest-2.arista.io'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings.cvaas_clusters.[].vrf") | String |  |  |  | The VRF used to connect to CloudVision. Must be set in the absence of source_interface.<br>- `use_mgmt_interface_vrf` will use VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will use the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings.cvaas_clusters.[].source_interface") | String |  |  |  | The source interface used to connect to CloudVision.  Must be set in the absence of vrf.<br>- `use_mgmt_interface` will use interface set with `mgmt_interface`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_interface` will use the interface set with `inband_mgmt_interface`.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings.cvaas_clusters.[].token_file") | String |  | `/tmp/cv-onboarding-token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;onprem_clusters</samp>](## "cv_settings.onprem_clusters") | List, items: Dictionary |  |  |  | On-premise CloudVision clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cv_settings.onprem_clusters.[].name") | String | Required, Unique |  |  | Cluster Name.<br>Only used when configuring multiple clusters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "cv_settings.onprem_clusters.[].servers") | List, items: Dictionary | Required |  | Min Length: 1<br>Max Length: 3 | CloudVision servers that makes up one cluster. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cv_settings.onprem_clusters.[].servers.[].name") | String | Required, Unique |  |  | Server FQDN or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "cv_settings.onprem_clusters.[].servers.[].port") | Integer |  | `9910` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "cv_settings.onprem_clusters.[].vrf") | String |  |  |  | The VRF used to connect to CloudVision. Must be set in the absence of source_interface.<br>- `use_mgmt_interface_vrf` will use VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will use the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "cv_settings.onprem_clusters.[].source_interface") | String |  |  |  | The source interface used to connect to CloudVision.  Must be set in the absence of vrf.<br>- `use_mgmt_interface` will use interface set with `mgmt_interface`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_interface` will use the interface set with `inband_mgmt_interface`.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "cv_settings.onprem_clusters.[].key") | String |  |  |  | Key-based authentication is deprecated in CloudVision and is not supported starting from CloudVision 2023.1.0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "cv_settings.onprem_clusters.[].token_file") | String |  | `/tmp/token` |  | Path to the onboarding token used for certificate based authentication.<br>The path is on the EOS device and the token file must be copied to the device first. |
    | [<samp>&nbsp;&nbsp;terminattr_ingestexclude</samp>](## "cv_settings.terminattr_ingestexclude") | String |  | `/Sysdb/cell/1/agent,/Sysdb/cell/2/agent` |  | Exclude paths from Sysdb on the ingest side. |
    | [<samp>&nbsp;&nbsp;terminattr_smashexcludes</samp>](## "cv_settings.terminattr_smashexcludes") | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  | Exclude paths from the shared memory table. |
    | [<samp>&nbsp;&nbsp;terminattr_disable_aaa</samp>](## "cv_settings.terminattr_disable_aaa") | Boolean |  | `False` |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") <span style="color:red">deprecated</span> | String |  |  |  | On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.<br>If not set, TerminAttr will be configured with certificate based authentication:<br>- On-premise using token onboarding. Default token path is '/tmp/token'.<br>- CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.<br>Token must be copied to the device first.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.onprem_clusters[].key</samp> instead.</span> |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") <span style="color:red">deprecated</span> | String |  |  |  | IPv4 address or DNS name for CloudVision.<br>This variable only supports an on-premise single-node cluster or the DNS name of a CloudVision as a Service instance.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.onprem_clusters[].servers[].name or cv_settings.cvaas.server</samp> instead.</span> |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") <span style="color:red">deprecated</span> | List, items: String |  |  |  | List of IPv4 addresses or DNS names for CloudVision.<br>For on-premise CloudVision enter all the nodes of the cluster.<br>For CloudVision as a Service enter the DNS name of the instance.<br>`eos_designs` only supports one CloudVision cluster.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.onprem_clusters[].servers[].name or cv_settings.cvaas.server</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or DNS name for CloudVision |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") <span style="color:red">deprecated</span> | String |  |  |  | cvp_token_file is the path to the token file on the switch.<br>If not set the default locations for on-premise or CVaaS will be used.<br>See cvp_ingestauth_key for details.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.onprem_clusters[].token_file or cv_settings.cvaas.token_file</samp> instead.</span> |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") <span style="color:red">deprecated</span> | Boolean |  | `False` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.terminattr_disable_aaa</samp> instead.</span> |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") <span style="color:red">deprecated</span> | String |  | `/Sysdb/cell/1/agent,/Sysdb/cell/2/agent` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.terminattr_ingestexclude</samp> instead.</span> |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") <span style="color:red">deprecated</span> | Integer |  | `9910` |  | Port number used for Terminattr connection to an on-premise CloudVision cluster.<br>The port number is always 443 when using CloudVision as a Service, so this value is ignored.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.onprem_clusters[].servers[].port</samp> instead.</span> |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") <span style="color:red">deprecated</span> | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>cv_settings.terminattr_smashexcludes</samp> instead.</span> |

=== "YAML"

    ```yaml
    cv_settings:
      cvaas_clusters:
        - name: <str>
          server: <str>
          vrf: <str>
          source_interface: <str>
          token_file: <str>
      onprem_clusters:
        - name: <str>
          servers:
            - name: <str>
              port: <int>
          vrf: <str>
          source_interface: <str>
          key: <str>
          token_file: <str>
      terminattr_ingestexclude: <str>
      terminattr_smashexcludes: <str>
      terminattr_disable_aaa: <bool>
    cvp_ingestauth_key: <str>
    cvp_instance_ip: <str>
    cvp_instance_ips:
      - <str>
    cvp_token_file: <str>
    terminattr_disable_aaa: <bool>
    terminattr_ingestexclude: <str>
    terminattr_ingestgrpcurl_port: <int>
    terminattr_smashexcludes: <str>
    ```
