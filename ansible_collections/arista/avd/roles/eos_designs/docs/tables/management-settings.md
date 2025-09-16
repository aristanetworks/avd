<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_settings</samp>](## "aaa_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_password</samp>](## "aaa_settings.enable_password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "aaa_settings.enable_password.password") | String |  |  |  | SHA512 hashed password. |
    | [<samp>&nbsp;&nbsp;tacacs</samp>](## "aaa_settings.tacacs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_settings.tacacs.servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "aaa_settings.tacacs.servers.[].host") | String | Required |  |  | Host IP address or name.<br>Combination of `host` and `vrf` should be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "aaa_settings.tacacs.servers.[].groups") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "aaa_settings.tacacs.servers.[].groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_settings.tacacs.servers.[].vrf") | String |  |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the TACACS host under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the TACACS host under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "aaa_settings.tacacs.servers.[].key") | String |  |  |  | Encrypted Type 7 key.<br>Takes precedence over `cleartext_key` if both are provided.<br>Either `key` or `cleartext_key` must be set to render the configuration;<br>otherwise, an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "aaa_settings.tacacs.servers.[].cleartext_key") | String |  |  |  | Plaintext password that will be encrypted to Type 7 by AVD.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar.<br>Either `key` or `cleartext_key` must be set to render the configuration;<br>otherwise, an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "aaa_settings.tacacs.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_settings.tacacs.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "aaa_settings.tacacs.vrfs.[].source_interface") | String |  |  |  | Source interface to use for TACACS hosts in this VRF.<br>If not set, the source interface may be set automatically when the TACACS server VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "aaa_settings.tacacs.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignore_unknown_mandatory_attribute</samp>](## "aaa_settings.tacacs.policy.ignore_unknown_mandatory_attribute") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;radius</samp>](## "aaa_settings.radius") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_settings.radius.servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "aaa_settings.radius.servers.[].host") | String | Required |  |  | Host IP address or name.<br>Combination of `host` and `vrf` should be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "aaa_settings.radius.servers.[].groups") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "aaa_settings.radius.servers.[].groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_settings.radius.servers.[].vrf") | String |  |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the Radius host under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the Radius host under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "aaa_settings.radius.servers.[].key") | String |  |  |  | Encrypted type-7 key.<br>Takes precedence over `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "aaa_settings.radius.servers.[].cleartext_key") | String |  |  |  | Cleartext password.<br>Encrypted to Type 7 by AVD.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "aaa_settings.radius.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_settings.radius.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "aaa_settings.radius.vrfs.[].source_interface") | String |  |  |  | Source interface to use for RADIUS hosts in this VRF.<br>If not set, the source interface may be set automatically when the RADIUS server VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;authentication</samp>](## "aaa_settings.authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;login</samp>](## "aaa_settings.authentication.login") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authentication.login.default") | String |  |  |  | Login authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command_api</samp>](## "aaa_settings.authentication.login.command_api") | String |  |  |  | Command-API authentication method(s) as a string.<br>This feature is not yet visible in EOS.<br>This feature only supports local authentication at the moment.<br>Examples:<br>- "local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_settings.authentication.login.console") | String |  |  |  | Console authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "aaa_settings.authentication.enable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authentication.enable.default") | String |  |  |  | Enable authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "aaa_settings.authentication.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authentication.dot1x.default") | String |  |  |  | 802.1x authentication method(s) as a string.<br>Examples:<br>- "group radius"<br>- "group MYGROUP group radius"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "aaa_settings.authentication.policies") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp>](## "aaa_settings.authentication.policies.on_failure_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp>](## "aaa_settings.authentication.policies.on_success_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "aaa_settings.authentication.policies.local") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp>](## "aaa_settings.authentication.policies.local.allow_nopassword") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp>](## "aaa_settings.authentication.policies.lockout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp>](## "aaa_settings.authentication.policies.lockout.failure") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "aaa_settings.authentication.policies.lockout.duration") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "aaa_settings.authentication.policies.lockout.window") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;authorization</samp>](## "aaa_settings.authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "aaa_settings.authorization.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_default_role</samp>](## "aaa_settings.authorization.policy.local_default_role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "aaa_settings.authorization.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;config_commands</samp>](## "aaa_settings.authorization.config_commands") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_console</samp>](## "aaa_settings.authorization.serial_console") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "aaa_settings.authorization.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1x_additional_groups</samp>](## "aaa_settings.authorization.dynamic.dot1x_additional_groups") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "aaa_settings.authorization.dynamic.dot1x_additional_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "aaa_settings.authorization.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_settings.authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_settings.authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;level</samp>](## "aaa_settings.authorization.commands.privilege.[].level") | String |  |  |  | Privilege level(s) 0-15. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authorization.commands.privilege.[].default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;accounting</samp>](## "aaa_settings.accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "aaa_settings.accounting.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_settings.accounting.exec.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.exec.console.type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.console.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.exec.console.logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.exec.console.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.exec.console.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.console.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.exec.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.exec.default.logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.exec.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.exec.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system</samp>](## "aaa_settings.accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.system.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.system.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.system.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.system.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.system.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "aaa_settings.accounting.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.dot1x.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.dot1x.default.type") | String |  |  | Valid Values:<br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.dot1x.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.dot1x.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;multicast</samp>](## "aaa_settings.accounting.dot1x.default.methods.[].multicast") | Boolean |  |  |  | Forward accounting packets to all servers within the specified group.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "aaa_settings.accounting.dot1x.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.dot1x.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "aaa_settings.accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_settings.accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_settings.accounting.commands.console.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.commands.console.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.console.[].group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.commands.console.[].logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.commands.console.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.commands.console.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.console.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_settings.accounting.commands.default.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.commands.default.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.default.[].group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.commands.default.[].logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.commands.default.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.commands.default.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.default.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;root_login</samp>](## "aaa_settings.root_login") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "aaa_settings.root_login.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_settings.root_login.sha512_password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_users</samp>](## "aaa_settings.local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_settings.local_users.[].name") | String | Required, Unique |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "aaa_settings.local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_settings.local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "aaa_settings.local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_settings.local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password.<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "aaa_settings.local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "aaa_settings.local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary_ssh_key</samp>](## "aaa_settings.local_users.[].secondary_ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "aaa_settings.local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user.<br> |
    | [<samp>dns_settings</samp>](## "dns_settings") | Dictionary |  |  |  | DNS settings |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "dns_settings.domain") | String |  |  |  | DNS domain name like 'fabric.local' |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "dns_settings.servers") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vrf</samp>](## "dns_settings.servers.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the DNS server under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the DNS server under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. Remember to set the `dns_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dns_settings.servers.[].ip_address") | String | Required |  |  | IPv4 or IPv6 address for DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "dns_settings.servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first). |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "dns_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "dns_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "dns_settings.vrfs.[].source_interface") | String |  |  |  | Source interface to use for DNS lookups in this VRF.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;set_source_interfaces</samp>](## "dns_settings.set_source_interfaces") | Boolean |  | `True` |  | Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>Can be set to `false` to avoid changes when migrating from the old `name_servers` model. |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;actions</samp>](## "event_handlers.[].actions") | Dictionary |  |  |  | Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash_command</samp>](## "event_handlers.[].actions.bash_command") | String |  |  |  | Define BASH command action. Command could be multiline also. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "event_handlers.[].actions.log") | Boolean |  |  |  | Log a message when the event is triggered. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increment_device_health_metric</samp>](## "event_handlers.[].actions.increment_device_health_metric") | String |  |  |  | Name of device-health metric. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-counters</code><br>- <code>on-intf</code><br>- <code>on-logging</code><br>- <code>on-maintenance</code><br>- <code>on-startup-config</code><br>- <code>vm-tracer vm</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_counters</samp>](## "event_handlers.[].trigger_on_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;condition</samp>](## "event_handlers.[].trigger_on_counters.condition") | String |  |  |  | Set the logical expression to evaluate. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;granularity_per_source</samp>](## "event_handlers.[].trigger_on_counters.granularity_per_source") | Boolean |  |  |  | Set the granularity of event counting for a wildcarded condition.<br>Example -<br>  condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>  [* wildcard is used here] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_counters.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_logging</samp>](## "event_handlers.[].trigger_on_logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_logging.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].trigger_on_logging.regex") | String |  |  |  | Regular expression to use for searching log messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_intf</samp>](## "event_handlers.[].trigger_on_intf") | Dictionary |  |  |  | Trigger condition occurs on specified interface changes.<br>Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_intf.interface") | String | Required |  |  | Interface name.<br>Example - Ethernet4<br>          Loopback4-6<br>          Port-channel4,7 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "event_handlers.[].trigger_on_intf.ip") | Boolean |  |  |  | Action is triggered upon changes to interface IP address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "event_handlers.[].trigger_on_intf.ipv6") | Boolean |  |  |  | Action is triggered upon changes to interface ipv6 address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operstatus</samp>](## "event_handlers.[].trigger_on_intf.operstatus") | Boolean |  |  |  | Action is triggered upon changes to interface operStatus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_maintenance</samp>](## "event_handlers.[].trigger_on_maintenance") | Dictionary |  |  |  | Settings required for trigger 'on-maintenance'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operation</samp>](## "event_handlers.[].trigger_on_maintenance.operation") | String | Required |  | Valid Values:<br>- <code>enter</code><br>- <code>exit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer</samp>](## "event_handlers.[].trigger_on_maintenance.bgp_peer") | String |  |  |  | Ipv4/Ipv6 address or peer group name.<br>Trigger condition occurs on maintenance operation of specified BGP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].trigger_on_maintenance.action") | String | Required |  | Valid Values:<br>- <code>after</code><br>- <code>before</code><br>- <code>all</code><br>- <code>begin</code><br>- <code>end</code> | Action for maintenance operation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stage</samp>](## "event_handlers.[].trigger_on_maintenance.stage") | String |  |  | Valid Values:<br>- <code>bgp</code><br>- <code>linkdown</code><br>- <code>mlag</code><br>- <code>ratemon</code> | Action is triggered after/before specified stage. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "event_handlers.[].trigger_on_maintenance.vrf") | String |  |  |  | VRF name. VRF can be defined for "bgp_peer" only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_maintenance.interface") | String |  |  |  | Trigger condition occurs on maintenance operation of specified interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "event_handlers.[].trigger_on_maintenance.unit") | String |  |  |  | Name of unit. Trigger condition occurs on maintenance operation of specified unit |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking.<br> |
    | [<samp>inband_ztp_bootstrap_file</samp>](## "inband_ztp_bootstrap_file") | String |  |  |  | Bootstrap URL configured in DHCP to use for inband ZTP.<br>If not set and `cvp_instance_ips` is set then the bootstrap value will be set to:<br>    `https://{cvp_instance_ips[0]}/ztp/bootstrap`<br>Otherwise no value will be configured. |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.<br> |
    | [<samp>local_users</samp>](## "local_users") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>aaa_settings.local_users</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password.<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;secondary_ssh_key</samp>](## "local_users.[].secondary_ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user.<br> |
    | [<samp>logging_settings</samp>](## "logging_settings") | Dictionary |  |  |  | Logging settings |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "logging_settings.hosts") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging_settings.hosts.[].name") | String | Required |  |  | Syslog server name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "logging_settings.hosts.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the logging destination under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as logging source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the logging destination under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as logging source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. Remember to set the `logging_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "logging_settings.hosts.[].protocol") | String |  | `udp` | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code><br>- <code>tls</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "logging_settings.hosts.[].ports") | List, items: Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;int&gt;</samp>](## "logging_settings.hosts.[].ports.[]") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "logging_settings.hosts.[].ssl_profile") | String |  |  |  | Used when host protocol is 'tls'. Profiles are defined under `management_security.ssl_profiles`. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "logging_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "logging_settings.vrfs.[].source_interface") | String |  |  |  | Source interface to use for logging destinations in this VRF.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;console</samp>](## "logging_settings.console") | String |  |  | Valid Values:<br>- <code>debugging</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>errors</code><br>- <code>critical</code><br>- <code>alerts</code><br>- <code>emergencies</code><br>- <code>disabled</code> | Console logging severity level. |
    | [<samp>&nbsp;&nbsp;monitor</samp>](## "logging_settings.monitor") | String |  |  | Valid Values:<br>- <code>debugging</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>errors</code><br>- <code>critical</code><br>- <code>alerts</code><br>- <code>emergencies</code><br>- <code>disabled</code> | Monitor logging severity level. |
    | [<samp>&nbsp;&nbsp;buffered</samp>](## "logging_settings.buffered") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "logging_settings.buffered.size") | Integer |  |  | Min: 10<br>Max: 2147483647 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging_settings.buffered.level") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>disabled</code> | Buffer logging severity level. |
    | [<samp>&nbsp;&nbsp;repeat_messages</samp>](## "logging_settings.repeat_messages") | Boolean |  |  |  | Summarize concurrent repeat messages. |
    | [<samp>&nbsp;&nbsp;trap</samp>](## "logging_settings.trap") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>system</code><br>- <code>warnings</code><br>- <code>disabled</code> | Trap logging severity level. |
    | [<samp>&nbsp;&nbsp;synchronous</samp>](## "logging_settings.synchronous") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging_settings.synchronous.level") | String |  | `critical` | Valid Values:<br>- <code>alerts</code><br>- <code>all</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>disabled</code> | Synchronous logging severity level. |
    | [<samp>&nbsp;&nbsp;format</samp>](## "logging_settings.format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "logging_settings.format.timestamp") | String |  |  | Valid Values:<br>- <code>high-resolution</code><br>- <code>traditional</code><br>- <code>traditional timezone</code><br>- <code>traditional year</code><br>- <code>traditional timezone year</code><br>- <code>traditional year timezone</code> | Timestamp format. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "logging_settings.format.hostname") | String |  |  | Valid Values:<br>- <code>fqdn</code><br>- <code>ipv4</code> | Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "logging_settings.format.sequence_numbers") | Boolean |  |  |  | Add sequence numbers to log messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rfc5424</samp>](## "logging_settings.format.rfc5424") | Boolean |  |  |  | Forward logs in RFC5424 format. |
    | [<samp>&nbsp;&nbsp;facility</samp>](## "logging_settings.facility") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>cron</code><br>- <code>daemon</code><br>- <code>kern</code><br>- <code>local0</code><br>- <code>local1</code><br>- <code>local2</code><br>- <code>local3</code><br>- <code>local4</code><br>- <code>local5</code><br>- <code>local6</code><br>- <code>local7</code><br>- <code>lpr</code><br>- <code>mail</code><br>- <code>news</code><br>- <code>sys9</code><br>- <code>sys10</code><br>- <code>sys11</code><br>- <code>sys12</code><br>- <code>sys13</code><br>- <code>sys14</code><br>- <code>syslog</code><br>- <code>user</code><br>- <code>uucp</code> |  |
    | [<samp>&nbsp;&nbsp;policy</samp>](## "logging_settings.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "logging_settings.policy.match") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_lists</samp>](## "logging_settings.policy.match.match_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging_settings.policy.match.match_lists.[].name") | String | Required, Unique |  |  | Match list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "logging_settings.policy.match.match_lists.[].action") | String |  |  | Valid Values:<br>- <code>discard</code> |  |
    | [<samp>&nbsp;&nbsp;event</samp>](## "logging_settings.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops_interval</samp>](## "logging_settings.event.congestion_drops_interval") | Integer |  |  | Min: 1<br>Max: 65535 | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;global_link_status</samp>](## "logging_settings.event.global_link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "logging_settings.event.storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;discards</samp>](## "logging_settings.event.storm_control.discards") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;global</samp>](## "logging_settings.event.storm_control.discards.global") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "logging_settings.event.storm_control.discards.interval") | Integer |  |  | Min: 10<br>Max: 65535 | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;level</samp>](## "logging_settings.level") | List, items: Dictionary |  |  |  | Configure logging severity. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;facility</samp>](## "logging_settings.level.[].facility") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</samp>](## "logging_settings.level.[].severity") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>0</code><br>- <code>1</code><br>- <code>2</code><br>- <code>3</code><br>- <code>4</code><br>- <code>5</code><br>- <code>6</code><br>- <code>7</code> | Severity of facility. Below are the supported severities.<br>emergencies    System is unusable                (severity=0)<br>alerts         Immediate action needed           (severity=1)<br>critical       Critical conditions               (severity=2)<br>errors         Error conditions                  (severity=3)<br>warnings       Warning conditions                (severity=4)<br>notifications  Normal but significant conditions (severity=5)<br>informational  Informational messages            (severity=6)<br>debugging      Debugging messages                (severity=7)<br><0-7>          Severity level value |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  | Default is HTTPS management eAPI enabled.<br> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "management_eapi.enabled") | Boolean |  | `True` |  | Enable/Disable api http-commands. |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_eapi.vrfs") | List, items: Dictionary |  | See (+) on YAML tab |  | Note: For backward compatibility, `mgmt_ip` presence is not enforced when `vrfs` is **not** configured and the default value of `use_mgmt_interface_vrf` is used.<br>To enforce the presence of `mgmt_ip` for the VRF defined by `mgmt_interface_vrf`, explicitly define an entry in `vrfs` using `name: use_mgmt_interface_vrf`.<br>This behavior will be removed in AVD 6.0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_eapi.vrfs.[].name") | String | Required, Unique |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the eAPI under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the eAPI under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the eAPI under VRF for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "management_eapi.vrfs.[].enabled") | Boolean | Required |  |  | Enable/disable Management eAPI for this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "management_eapi.vrfs.[].ipv4_acl") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "management_eapi.vrfs.[].ipv6_acl") | String |  |  |  | IPv6 access-list name. |
    | [<samp>name_servers</samp>](## "name_servers") <span style="color:red">deprecated</span> | List, items: String |  |  |  | List of DNS servers. The VRF is set to < mgmt_interface_vrf >.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>dns_settings.servers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "name_servers.[]") | String |  |  |  | IPv4 or IPv6 address. |
    | [<samp>ntp_settings</samp>](## "ntp_settings") | Dictionary |  |  |  | NTP settings |
    | [<samp>&nbsp;&nbsp;server_vrf</samp>](## "ntp_settings.server_vrf") | String |  |  |  | EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.<br>- `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.<br>If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`. |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "ntp_settings.servers") | List, items: Dictionary |  |  |  | The first server is always set as "preferred". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ntp_settings.servers.[].name") | String |  |  |  | IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp_settings.servers.[].burst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp_settings.servers.[].iburst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp_settings.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp_settings.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp_settings.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp_settings.authenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp_settings.authenticate_servers_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp_settings.authentication_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;key</samp>](## "ntp_settings.authentication_keys.[].key") | String |  |  |  | Authentication provided using the `key_type` format.<br>Will be rendered as such.<br>Takes precedence over `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "ntp_settings.authentication_keys.[].cleartext_key") | String |  |  |  | Cleartext key for the NTP authentication key. Encrypted to Type 7 by AVD.<br>`key_type` does not influence this key.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp_settings.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Key type of the `key`.<br>Does not have any influence on `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "ntp_settings.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp_settings.authentication_keys.[].hash_algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code> |  |
    | [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp_settings.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15. |
    | [<samp>ssh_settings</samp>](## "ssh_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ssh_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ssh_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure SSH for the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure SSH for the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ssh_settings.vrfs.[].enabled") | Boolean | Required |  |  | Enable SSH in VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "ssh_settings.vrfs.[].ipv4_acl") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "ssh_settings.vrfs.[].ipv6_acl") | String |  |  |  | IPv6 access-list name. |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "ssh_settings.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes. |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  | Clock timezone like "CET" or "US/Pacific". |

=== "YAML"

    ```yaml
    aaa_settings:
      enable_password:

        # SHA512 hashed password.
        password: <str>
      tacacs:
        servers:

            # Host IP address or name.
            # Combination of `host` and `vrf` should be unique.
          - host: <str; required>
            groups: # >=1 items; required
              - <str>

            # VRF name.
            # The value will be interpreted according to these rules:
            # - `use_mgmt_interface_vrf` will configure the TACACS host under the VRF set with `mgmt_interface_vrf`.
            #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
            # - `use_inband_mgmt_vrf` will configure the TACACS host under the VRF set with `inband_mgmt_vrf`.
            #   An error will be raised if inband management is not configured for the device.
            # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
            # - Any other string will be used directly as the VRF name.
            vrf: <str>

            # Encrypted Type 7 key.
            # Takes precedence over `cleartext_key` if both are provided.
            # Either `key` or `cleartext_key` must be set to render the configuration;
            # otherwise, an error will be raised.
            key: <str>

            # Plaintext password that will be encrypted to Type 7 by AVD.
            # To protect the password at rest it is strongly recommended to make use of a vault or similar.
            # Either `key` or `cleartext_key` must be set to render the configuration;
            # otherwise, an error will be raised.
            cleartext_key: <str>
        vrfs:

            # VRF Name.
          - name: <str; required; unique>

            # Source interface to use for TACACS hosts in this VRF.
            # If not set, the source interface may be set automatically when the TACACS server VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
            # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
            source_interface: <str>
        policy:
          ignore_unknown_mandatory_attribute: <bool; default=False>
      radius:
        servers:

            # Host IP address or name.
            # Combination of `host` and `vrf` should be unique.
          - host: <str; required>
            groups: # >=1 items; required
              - <str>

            # VRF name.
            # The value will be interpreted according to these rules:
            # - `use_mgmt_interface_vrf` will configure the Radius host under the VRF set with `mgmt_interface_vrf`.
            #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
            # - `use_inband_mgmt_vrf` will configure the Radius host under the VRF set with `inband_mgmt_vrf`.
            #   An error will be raised if inband management is not configured for the device.
            # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
            # - Any other string will be used directly as the VRF name.
            vrf: <str>

            # Encrypted type-7 key.
            # Takes precedence over `cleartext_key`.
            key: <str>

            # Cleartext password.
            # Encrypted to Type 7 by AVD.
            # To protect the password at rest it is strongly recommended to make use of a vault or similar.
            cleartext_key: <str>
        vrfs:

            # VRF Name.
          - name: <str; required; unique>

            # Source interface to use for RADIUS hosts in this VRF.
            # If not set, the source interface may be set automatically when the RADIUS server VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
            # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
            source_interface: <str>
      authentication:
        login:

          # Login authentication method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group radius group MYGROUP local"
          default: <str>

          # Command-API authentication method(s) as a string.
          # This feature is not yet visible in EOS.
          # This feature only supports local authentication at the moment.
          # Examples:
          # - "local"
          command_api: <str>

          # Console authentication method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group radius group MYGROUP local"
          console: <str>
        enable:

          # Enable authentication method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group radius group MYGROUP local"
          default: <str>
        dot1x:

          # 802.1x authentication method(s) as a string.
          # Examples:
          # - "group radius"
          # - "group MYGROUP group radius"
          default: <str>
        policies:
          on_failure_log: <bool>
          on_success_log: <bool>
          local:
            allow_nopassword: <bool>
          lockout:
            failure: <int; 1-255>
            duration: <int; 1-4294967295>
            window: <int; 1-4294967295>
      authorization:
        policy:
          local_default_role: <str>
        exec:

          # Exec authorization method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group radius group MYGROUP local"
          default: <str>
        config_commands: <bool>
        serial_console: <bool>
        dynamic:
          dot1x_additional_groups: # >=1 items
            - <str>
        commands:

          # Command authorization method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group tacacs+ group MYGROUP local
          all_default: <str>
          privilege:

              # Privilege level(s) 0-15.
            - level: <str>

              # Command authorization method(s) as a string.
              # Examples:
              # - "group tacacs+ local"
              # - "group MYGROUP none"
              # - "group tacacs+ group MYGROUP local"
              default: <str>
      accounting:
        exec:
          console:
            type: <str; "none" | "start-stop" | "stop-only"; required>

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.group` instead.
            group: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.method` instead.
            logging: <bool>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
          default:
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.group` instead.
            group: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.method` instead.
            logging: <bool>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        system:
          default:
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.group` instead.
            group: <str>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        dot1x:
          default:
            type: <str; "start-stop" | "stop-only">

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use `methods.group` instead.
            group: <str>
            methods: # >=1 items

                # Forward accounting packets to all servers within the specified group.
                # This option is applicable only when the `method` key is explicitly set to `group`.
              - multicast: <bool>
                method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        commands:
          console:

              # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
            - commands: <str>
              type: <str; "none" | "start-stop" | "stop-only">

              # Group Name.
              # This key is deprecated.
              # Support will be removed in AVD version 6.0.0.
              # Use `methods.group` instead.
              group: <str>
              # This key is deprecated.
              # Support will be removed in AVD version 6.0.0.
              # Use `methods.method` instead.
              logging: <bool>
              methods: # >=1 items
                - method: <str; "logging" | "group"; required>

                  # Specify the server group to be used.
                  # This option is applicable only when the `method` key is explicitly set to `group`.
                  group: <str>
          default:

              # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
            - commands: <str>
              type: <str; "none" | "start-stop" | "stop-only">

              # Group Name.
              # This key is deprecated.
              # Support will be removed in AVD version 6.0.0.
              # Use `methods.group` instead.
              group: <str>
              # This key is deprecated.
              # Support will be removed in AVD version 6.0.0.
              # Use `methods.method` instead.
              logging: <bool>
              methods: # >=1 items
                - method: <str; "logging" | "group"; required>

                  # Specify the server group to be used.
                  # This option is applicable only when the `method` key is explicitly set to `group`.
                  group: <str>
      root_login:
        enabled: <bool; default=False>
        sha512_password: <str>
      local_users:

          # Username.
        - name: <str; required; unique>

          # If true, the user will be removed and all other settings are ignored.
          # Useful for removing the default "admin" user.
          disabled: <bool>

          # Initial privilege level with local EXEC authorization.
          privilege: <int; 0-15>

          # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".
          role: <str>

          # SHA512 Hash of Password.
          # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
          sha512_password: <str>

          # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
          no_password: <bool>
          ssh_key: <str>
          secondary_ssh_key: <str>

          # Specify shell for the user.
          shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">

    # DNS settings
    dns_settings:

      # DNS domain name like 'fabric.local'
      domain: <str>
      servers: # >=1 items; required

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
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Source interface to use for DNS lookups in this VRF.
          # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
          source_interface: <str>

      # Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
      # Can be set to `false` to avoid changes when migrating from the old `name_servers` model.
      set_source_interfaces: <bool; default=True>

    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name.
      - name: <str; required; unique>

        # Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`.
        actions:

          # Define BASH command action. Command could be multiline also.
          bash_command: <str>

          # Log a message when the event is triggered.
          log: <bool>

          # Name of device-health metric.
          increment_device_health_metric: <str>

        # Event-handler delay in seconds.
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-counters" | "on-intf" | "on-logging" | "on-maintenance" | "on-startup-config" | "vm-tracer vm">
        trigger_on_counters:

          # Set the logical expression to evaluate.
          condition: <str>

          # Set the granularity of event counting for a wildcarded condition.
          # Example -
          #   condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
          #   [* wildcard is used here]
          granularity_per_source: <bool>

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>
        trigger_on_logging:

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>

          # Regular expression to use for searching log messages.
          regex: <str>

        # Trigger condition occurs on specified interface changes.
        # Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`.
        trigger_on_intf:

          # Interface name.
          # Example - Ethernet4
          #           Loopback4-6
          #           Port-channel4,7
          interface: <str; required>

          # Action is triggered upon changes to interface IP address assignment.
          ip: <bool>

          # Action is triggered upon changes to interface ipv6 address assignment.
          ipv6: <bool>

          # Action is triggered upon changes to interface operStatus.
          operstatus: <bool>

        # Settings required for trigger 'on-maintenance'.
        trigger_on_maintenance:
          operation: <str; "enter" | "exit"; required>

          # Ipv4/Ipv6 address or peer group name.
          # Trigger condition occurs on maintenance operation of specified BGP peer.
          bgp_peer: <str>

          # Action for maintenance operation.
          action: <str; "after" | "before" | "all" | "begin" | "end"; required>

          # Action is triggered after/before specified stage.
          stage: <str; "bgp" | "linkdown" | "mlag" | "ratemon">

          # VRF name. VRF can be defined for "bgp_peer" only.
          vrf: <str>

          # Trigger condition occurs on maintenance operation of specified interface.
          interface: <str>

          # Name of unit. Trigger condition occurs on maintenance operation of specified unit
          unit: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>

    # Bootstrap URL configured in DHCP to use for inband ZTP.
    # If not set and `cvp_instance_ips` is set then the bootstrap value will be set to:
    #     `https://{cvp_instance_ips[0]}/ztp/bootstrap`
    # Otherwise no value will be configured.
    inband_ztp_bootstrap_file: <str>

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `aaa_settings.local_users` instead.
    local_users:

        # Username.
      - name: <str; required; unique>

        # If true, the user will be removed and all other settings are ignored.
        # Useful for removing the default "admin" user.
        disabled: <bool>

        # Initial privilege level with local EXEC authorization.
        privilege: <int; 0-15>

        # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".
        role: <str>

        # SHA512 Hash of Password.
        # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
        sha512_password: <str>

        # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
        no_password: <bool>
        ssh_key: <str>
        secondary_ssh_key: <str>

        # Specify shell for the user.
        shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">

    # Logging settings
    logging_settings:
      hosts: # >=1 items; required

          # Syslog server name.
        - name: <str; required>

          # The value of `vrf` will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the logging destination under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as logging source-interface.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the logging destination under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as logging source-interface.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name. Remember to set the `logging_settings.vrfs[].source_interface` if needed.
          vrf: <str; default="use_default_mgmt_method_vrf">
          protocol: <str; "tcp" | "udp" | "tls"; default="udp">
          ports:
            - <int>

          # Used when host protocol is 'tls'. Profiles are defined under `management_security.ssl_profiles`.
          ssl_profile: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Source interface to use for logging destinations in this VRF.
          # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
          source_interface: <str>

      # Console logging severity level.
      console: <str; "debugging" | "informational" | "notifications" | "warnings" | "errors" | "critical" | "alerts" | "emergencies" | "disabled">

      # Monitor logging severity level.
      monitor: <str; "debugging" | "informational" | "notifications" | "warnings" | "errors" | "critical" | "alerts" | "emergencies" | "disabled">
      buffered:
        size: <int; 10-2147483647>

        # Buffer logging severity level.
        level: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "disabled">

      # Summarize concurrent repeat messages.
      repeat_messages: <bool>

      # Trap logging severity level.
      trap: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "system" | "warnings" | "disabled">
      synchronous:

        # Synchronous logging severity level.
        level: <str; "alerts" | "all" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "disabled"; default="critical">
      format:

        # Timestamp format.
        timestamp: <str; "high-resolution" | "traditional" | "traditional timezone" | "traditional year" | "traditional timezone year" | "traditional year timezone">

        # Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).
        hostname: <str; "fqdn" | "ipv4">

        # Add sequence numbers to log messages.
        sequence_numbers: <bool>

        # Forward logs in RFC5424 format.
        rfc5424: <bool>
      facility: <str; "auth" | "cron" | "daemon" | "kern" | "local0" | "local1" | "local2" | "local3" | "local4" | "local5" | "local6" | "local7" | "lpr" | "mail" | "news" | "sys9" | "sys10" | "sys11" | "sys12" | "sys13" | "sys14" | "syslog" | "user" | "uucp">
      policy:
        match:
          match_lists:

              # Match list.
            - name: <str; required; unique>
              action: <str; "discard">
      event:

        # Logging interval in seconds.
        congestion_drops_interval: <int; 1-65535>
        global_link_status: <bool>
        storm_control:
          discards:
            global: <bool>

            # Logging interval in seconds.
            interval: <int; 10-65535>

      # Configure logging severity.
      level:
        - facility: <str; required; unique>

          # Severity of facility. Below are the supported severities.
          # emergencies    System is unusable                (severity=0)
          # alerts         Immediate action needed           (severity=1)
          # critical       Critical conditions               (severity=2)
          # errors         Error conditions                  (severity=3)
          # warnings       Warning conditions                (severity=4)
          # notifications  Normal but significant conditions (severity=5)
          # informational  Informational messages            (severity=6)
          # debugging      Debugging messages                (severity=7)
          # <0-7>          Severity level value
          severity: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7">

    # Default is HTTPS management eAPI enabled.
    management_eapi:

      # Enable/Disable api http-commands.
      enabled: <bool; default=True>
      enable_http: <bool>
      enable_https: <bool; default=True>
      default_services: <bool>

      # Note: For backward compatibility, `mgmt_ip` presence is not enforced when `vrfs` is **not** configured and the default value of `use_mgmt_interface_vrf` is used.
      # To enforce the presence of `mgmt_ip` for the VRF defined by `mgmt_interface_vrf`, explicitly define an entry in `vrfs` using `name: use_mgmt_interface_vrf`.
      # This behavior will be removed in AVD 6.0.
      vrfs: # (1)!

          # VRF name.
          # The value will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the eAPI under the VRF set with `mgmt_interface_vrf`.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the eAPI under the VRF set with `inband_mgmt_vrf`.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the eAPI under VRF for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name.
        - name: <str; required; unique>

          # Enable/disable Management eAPI for this VRF.
          enabled: <bool; required>

          # IPv4 access-list name.
          ipv4_acl: <str>

          # IPv6 access-list name.
          ipv6_acl: <str>

    # List of DNS servers. The VRF is set to < mgmt_interface_vrf >.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `dns_settings.servers` instead.
    name_servers:

        # IPv4 or IPv6 address.
      - <str>

    # NTP settings
    ntp_settings:

      # EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.
      # - `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.
      #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
      # - `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.
      #   An error will be raised if inband management is not configured for the device.
      # - Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.
      # If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.
      server_vrf: <str>

      # The first server is always set as "preferred".
      servers:

          # IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org.
        - name: <str>
          burst: <bool>
          iburst: <bool>
          key: <int; 1-65535>

          # Value of maxpoll between 3 - 17 (Logarithmic).
          maxpoll: <int; 3-17>

          # Value of minpoll between 3 - 17 (Logarithmic).
          minpoll: <int; 3-17>
          version: <int; 1-4>
      authenticate: <bool>
      authenticate_servers_only: <bool>
      authentication_keys:

          # Authentication provided using the `key_type` format.
          # Will be rendered as such.
          # Takes precedence over `cleartext_key`.
        - key: <str>

          # Cleartext key for the NTP authentication key. Encrypted to Type 7 by AVD.
          # `key_type` does not influence this key.
          # To protect the password at rest it is strongly recommended to make use of a vault or similar.
          cleartext_key: <str>

          # Key type of the `key`.
          # Does not have any influence on `cleartext_key`.
          key_type: <str; "0" | "7" | "8a">

          # Key identifier.
          id: <int; 1-65534; required; unique>
          hash_algorithm: <str; "md5" | "sha1"; required>

      # List of trusted-keys as string ex. 10-12,15.
      trusted_keys: <str>
    ssh_settings:
      vrfs:

          # VRF name.
          # The value will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure SSH for the VRF set with `mgmt_interface_vrf`.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure SSH for the VRF set with `inband_mgmt_vrf`.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the VRF for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name.
        - name: <str; required; unique>

          # Enable SSH in VRF.
          enabled: <bool; required>

          # IPv4 access-list name.
          ipv4_acl: <str>

          # IPv6 access-list name.
          ipv6_acl: <str>

      # Idle timeout in minutes.
      idle_timeout: <int; 0-86400>

    # Clock timezone like "CET" or "US/Pacific".
    timezone: <str>
    ```

    1. Default Value

        ```yaml
        vrfs:
        - enabled: true
          name: use_mgmt_interface_vrf
        ```
