<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_settings</samp>](## "aaa_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_password</samp>](## "aaa_settings.enable_password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "aaa_settings.enable_password.password") | String |  |  |  | SHA512 hashed password.<br>Takes precedence over `cleartext_password`.<br>This variable is sensitive and SHOULD be configured using some vault. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cleartext_password</samp>](## "aaa_settings.enable_password.cleartext_password") | String |  |  |  | Cleartext enable password.<br>Encrypted using `password_type` by AVD.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "aaa_settings.enable_password.password_type") | String |  | `sha512` | Valid Values:<br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;tacacs</samp>](## "aaa_settings.tacacs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_settings.tacacs.servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "aaa_settings.tacacs.servers.[].host") | String | Required |  |  | Host IP address or name.<br>Combination of `host` and `vrf` should be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "aaa_settings.tacacs.servers.[].groups") | List, items: String |  |  | Min Length: 1 | List of Tacacs group names.<br>The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "aaa_settings.tacacs.servers.[].groups.[]") | String |  |  | Pattern: `(?!radius$|tacacs\+$|ldap$).+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_settings.tacacs.servers.[].vrf") | String |  |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the TACACS host under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the TACACS host under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "aaa_settings.tacacs.servers.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "aaa_settings.tacacs.servers.[].key") | String |  |  |  | Encrypted Type 7 key.<br>Takes precedence over `cleartext_key` if both are provided.<br>Either `key` or `cleartext_key` must be set to render the configuration;<br>otherwise, an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "aaa_settings.tacacs.servers.[].cleartext_key") | String |  |  |  | Plaintext password that will be encrypted to Type 7 by AVD.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar.<br>Either `key` or `cleartext_key` must be set to render the configuration;<br>otherwise, an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "aaa_settings.tacacs.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_settings.tacacs.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "aaa_settings.tacacs.vrfs.[].source_interface") | String |  |  |  | Source interface to use for TACACS hosts in this VRF.<br>If not set, the source interface may be set automatically when the TACACS server VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "aaa_settings.tacacs.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignore_unknown_mandatory_attribute</samp>](## "aaa_settings.tacacs.policy.ignore_unknown_mandatory_attribute") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;radius</samp>](## "aaa_settings.radius") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_settings.radius.servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "aaa_settings.radius.servers.[].host") | String | Required |  |  | Host IP address or name.<br>Multiple servers with the same hostname/IP address can be configured for TLS and no TLS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "aaa_settings.radius.servers.[].groups") | List, items: String |  |  | Min Length: 1 | List of Radius group names.<br>The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "aaa_settings.radius.servers.[].groups.[]") | String |  |  | Pattern: `(?!radius$|tacacs\+$|ldap$).+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_settings.radius.servers.[].vrf") | String |  |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the Radius host under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the Radius host under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "aaa_settings.radius.servers.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;retransmit</samp>](## "aaa_settings.radius.servers.[].retransmit") | Integer |  |  | Min: 0<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "aaa_settings.radius.servers.[].key") | String |  |  |  | Encrypted type-7 key.<br>Takes precedence over `cleartext_key`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "aaa_settings.radius.servers.[].cleartext_key") | String |  |  |  | Cleartext password.<br>Encrypted to Type 7 by AVD.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls</samp>](## "aaa_settings.radius.servers.[].tls") | Dictionary |  |  |  | When TLS is configured, `key` and `cleartext_key` are ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "aaa_settings.radius.servers.[].tls.enabled") | Boolean |  |  |  | Enable TLS for radius-server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "aaa_settings.radius.servers.[].tls.ssl_profile") | String |  |  |  | Name of TLS profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "aaa_settings.radius.servers.[].tls.port") | Integer |  |  | Min: 0<br>Max: 65535 | TCP Port used for TLS. EOS default is 2083. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "aaa_settings.authentication.policies") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp>](## "aaa_settings.authentication.policies.on_failure_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp>](## "aaa_settings.authentication.policies.on_success_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "aaa_settings.authentication.policies.local") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp>](## "aaa_settings.authentication.policies.local.allow_nopassword") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp>](## "aaa_settings.authentication.policies.lockout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp>](## "aaa_settings.authentication.policies.lockout.failure") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "aaa_settings.authentication.policies.lockout.duration") | Integer | Required |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "aaa_settings.authentication.policies.lockout.window") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;authorization</samp>](## "aaa_settings.authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "aaa_settings.authorization.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_default_role</samp>](## "aaa_settings.authorization.policy.local_default_role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "aaa_settings.authorization.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;config_commands</samp>](## "aaa_settings.authorization.config_commands") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_console</samp>](## "aaa_settings.authorization.serial_console") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "aaa_settings.authorization.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_settings.authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_settings.authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;level</samp>](## "aaa_settings.authorization.commands.privilege.[].level") | String | Required |  |  | Privilege level(s) 0-15. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.authorization.commands.privilege.[].default") | String | Required |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;accounting</samp>](## "aaa_settings.accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "aaa_settings.accounting.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_settings.accounting.exec.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.exec.console.type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.exec.console.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.exec.console.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.console.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.console.group") <span style="color:red">removed</span> | String |  |  |  | Group Name.<span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.exec.console.logging") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.exec.default.type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.exec.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.exec.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.exec.default.group") <span style="color:red">removed</span> | String |  |  |  | Group Name.<span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.exec.default.logging") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system</samp>](## "aaa_settings.accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.system.default.type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.system.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.system.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.system.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.system.default.group") <span style="color:red">removed</span> | String |  |  |  | Group Name.<span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "aaa_settings.accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_settings.accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_settings.accounting.commands.console.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.commands.console.[].type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.commands.console.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.commands.console.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.console.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.console.[].group") <span style="color:red">removed</span> | String |  |  |  | Group Name.<span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.commands.console.[].logging") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_settings.accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_settings.accounting.commands.default.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_settings.accounting.commands.default.[].type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_settings.accounting.commands.default.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_settings.accounting.commands.default.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.default.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_settings.accounting.commands.default.[].group") <span style="color:red">removed</span> | String |  |  |  | Group Name.<span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_settings.accounting.commands.default.[].logging") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;root_login</samp>](## "aaa_settings.root_login") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "aaa_settings.root_login.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_settings.root_login.sha512_password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_users</samp>](## "aaa_settings.local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sha512_password</samp>](## "aaa_settings.local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password.<br>Takes precedence over `cleartext_password`.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_password</samp>](## "aaa_settings.local_users.[].cleartext_password") | String |  |  |  | Cleartext user password.<br>Encrypted using `password_type` by AVD.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "aaa_settings.local_users.[].password_type") | String |  | `sha512` | Valid Values:<br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "aaa_settings.local_users.[].name") | String | Required, Unique |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "aaa_settings.local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_settings.local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "aaa_settings.local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "aaa_settings.local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "aaa_settings.local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary_ssh_key</samp>](## "aaa_settings.local_users.[].secondary_ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "aaa_settings.local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user.<br> |

=== "YAML"

    ```yaml
    aaa_settings:
      enable_password:

        # SHA512 hashed password.
        # Takes precedence over `cleartext_password`.
        # This variable is sensitive and SHOULD be configured using some vault.
        password: <str>

        # Cleartext enable password.
        # Encrypted using `password_type` by AVD.
        # This variable is sensitive and SHOULD be configured using some vault mechanism.
        cleartext_password: <str>
        password_type: <str; "sha512"; default="sha512">
      tacacs:
        servers:

            # Host IP address or name.
            # Combination of `host` and `vrf` should be unique.
          - host: <str; required>

            # List of Tacacs group names.
            # The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used.
            groups: # >=1 items
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

            # Timeout in seconds.
            timeout: <int; 1-1000>

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
            # Multiple servers with the same hostname/IP address can be configured for TLS and no TLS.
          - host: <str; required>

            # List of Radius group names.
            # The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used.
            groups: # >=1 items
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
            timeout: <int; 1-1000>
            retransmit: <int; 0-100>

            # Encrypted type-7 key.
            # Takes precedence over `cleartext_key`.
            key: <str>

            # Cleartext password.
            # Encrypted to Type 7 by AVD.
            # To protect the password at rest it is strongly recommended to make use of a vault or similar.
            cleartext_key: <str>

            # When TLS is configured, `key` and `cleartext_key` are ignored.
            tls:

              # Enable TLS for radius-server.
              enabled: <bool>

              # Name of TLS profile.
              ssl_profile: <str>

              # TCP Port used for TLS. EOS default is 2083.
              port: <int; 0-65535>
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
        policies:
          on_failure_log: <bool>
          on_success_log: <bool>
          local:
            allow_nopassword: <bool>
          lockout:
            failure: <int; 1-255; required>
            duration: <int; 1-4294967295; required>
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
        commands:

          # Command authorization method(s) as a string.
          # Examples:
          # - "group tacacs+ local"
          # - "group MYGROUP none"
          # - "group tacacs+ group MYGROUP local
          all_default: <str>
          privilege:

              # Privilege level(s) 0-15.
            - level: <str; required>

              # Command authorization method(s) as a string.
              # Examples:
              # - "group tacacs+ local"
              # - "group MYGROUP none"
              # - "group tacacs+ group MYGROUP local"
              default: <str; required>
      accounting:
        exec:
          console:
            type: <str; "none" | "start-stop" | "stop-only"; required>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
          default:
            type: <str; "none" | "start-stop" | "stop-only"; required>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        system:
          default:
            type: <str; "none" | "start-stop" | "stop-only"; required>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        commands:
          console:

              # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
            - commands: <str>
              type: <str; "none" | "start-stop" | "stop-only"; required>
              methods: # >=1 items
                - method: <str; "logging" | "group"; required>

                  # Specify the server group to be used.
                  # This option is applicable only when the `method` key is explicitly set to `group`.
                  group: <str>
          default:

              # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
            - commands: <str>
              type: <str; "none" | "start-stop" | "stop-only"; required>
              methods: # >=1 items
                - method: <str; "logging" | "group"; required>

                  # Specify the server group to be used.
                  # This option is applicable only when the `method` key is explicitly set to `group`.
                  group: <str>
      root_login:
        enabled: <bool; default=False>
        sha512_password: <str>
      local_users:

          # SHA512 Hash of Password.
          # Takes precedence over `cleartext_password`.
          # This variable is sensitive and SHOULD be configured using some vault mechanism.
        - sha512_password: <str>

          # Cleartext user password.
          # Encrypted using `password_type` by AVD.
          # This variable is sensitive and SHOULD be configured using some vault mechanism.
          cleartext_password: <str>
          password_type: <str; "sha512"; default="sha512">

          # Username.
          name: <str; required; unique>

          # If true, the user will be removed and all other settings are ignored.
          # Useful for removing the default "admin" user.
          disabled: <bool>

          # Initial privilege level with local EXEC authorization.
          privilege: <int; 0-15>

          # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".
          role: <str>

          # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
          no_password: <bool>
          ssh_key: <str>
          secondary_ssh_key: <str>

          # Specify shell for the user.
          shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">
    ```
