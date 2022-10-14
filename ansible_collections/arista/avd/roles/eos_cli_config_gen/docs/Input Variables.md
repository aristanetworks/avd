!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## AAA Authentication

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_authentication</samp>](## "aaa_authentication") | Dictionary |  |  |  | AAA Authentication |
| [<samp>&nbsp;&nbsp;login</samp>](## "aaa_authentication.login") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.login.default") | String |  |  |  | Login authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_authentication.login.console") | String |  |  |  | Console authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
| [<samp>&nbsp;&nbsp;enable</samp>](## "aaa_authentication.enable") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.enable.default") | String |  |  |  | Enable authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
| [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_authentication.dot1x") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.dot1x.default") | String |  |  |  | 802.1x authentication method(s) as a string.<br>Examples:<br>- "group radius"<br>- "group MYGROUP group radius"<br> |
| [<samp>&nbsp;&nbsp;policies</samp>](## "aaa_authentication.policies") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp>](## "aaa_authentication.policies.on_failure_log") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp>](## "aaa_authentication.policies.on_success_log") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "aaa_authentication.policies.local") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp>](## "aaa_authentication.policies.local.allow_nopassword") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp>](## "aaa_authentication.policies.lockout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp>](## "aaa_authentication.policies.lockout.failure") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "aaa_authentication.policies.lockout.duration") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "aaa_authentication.policies.lockout.window") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |

### YAML

```yaml
aaa_authentication:
  login:
    default: <str>
    console: <str>
  enable:
    default: <str>
  dot1x:
    default: <str>
  policies:
    on_failure_log: <bool>
    on_success_log: <bool>
    local:
      allow_nopassword: <bool>
    lockout:
      failure: <int>
      duration: <int>
      window: <int>
```

## AAA Authorization

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_authorization</samp>](## "aaa_authorization") | Dictionary |  |  |  | AAA Authorization |
| [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_authorization.exec") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
| [<samp>&nbsp;&nbsp;config_commands</samp>](## "aaa_authorization.config_commands") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;serial_console</samp>](## "aaa_authorization.serial_console") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_authorization.commands") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- level</samp>](## "aaa_authorization.commands.privilege.[].level") | String |  |  |  | Privilege level(s) 0-15 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.commands.privilege.[].default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local" |

### YAML

```yaml
aaa_authorization:
  exec:
    default: <str>
  config_commands: <bool>
  serial_console: <bool>
  commands:
    all_default: <str>
    privilege:
      - level: <str>
        default: <str>
```

## AAA Root

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_root</samp>](## "aaa_root") | Dictionary |  |  |  | AAA Root |
| [<samp>&nbsp;&nbsp;secret</samp>](## "aaa_root.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_root.secret.sha512_password") | String |  |  |  |  |

### YAML

```yaml
aaa_root:
  secret:
    sha512_password: <str>
```

## IP Extended Access-Lists (legacy model)

### Description

AVD currently supports 2 different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>access_lists</samp>](## "access_lists") | List, items: Dictionary |  |  |  | IP Extended Access-Lists (legacy model) |
| [<samp>&nbsp;&nbsp;- name</samp>](## "access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## As Path

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>as_path</samp>](## "as_path") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;regex_mode</samp>](## "as_path.regex_mode") | String |  |  | Valid Values:<br>- asn<br>- string |  |
| [<samp>&nbsp;&nbsp;access_lists</samp>](## "as_path.access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "as_path.access_lists.[].name") | String |  |  |  | Access List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "as_path.access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "as_path.access_lists.[].entries.[].type") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "as_path.access_lists.[].entries.[].match") | String |  |  |  | Regex To Match |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin</samp>](## "as_path.access_lists.[].entries.[].origin") | String |  | any | Valid Values:<br>- any<br>- egp<br>- igp<br>- incomplete |  |

### YAML

```yaml
as_path:
  regex_mode: <str>
  access_lists:
    - name: <str>
      entries:
        - type: <str>
          match: <str>
          origin: <str>
```

## Banners

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>banners</samp>](## "banners") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;login</samp>](## "banners.login") | String |  |  |  | Multiline string ending with EOF on the last line |
| [<samp>&nbsp;&nbsp;motd</samp>](## "banners.motd") | String |  |  |  | Multiline string ending with EOF on the last line |

### YAML

```yaml
banners:
  login: <str>
  motd: <str>
```

## Bgp Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_groups</samp>](## "bgp_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "bgp_groups.[].name") | String | Required, Unique |  |  | Group Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "bgp_groups.[].vrf") | String |  |  |  | VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "bgp_groups.[].neighbors") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].neighbors.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "bgp_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Profile Name |

### YAML

```yaml
bgp_groups:
  - name: <str>
    vrf: <str>
    neighbors:
      - <str>
    bgp_maintenance_profiles:
      - <str>
```

## System Boot Settings

### Description

Set the Aboot password

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>boot</samp>](## "boot") | Dictionary |  |  |  | System Boot Settings |
| [<samp>&nbsp;&nbsp;secret</samp>](## "boot.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "boot.secret.hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "boot.secret.key") | String |  |  |  | Hashed Password |

### YAML

```yaml
boot:
  secret:
    hash_algorithm: <str>
    key: <str>
```

## QOS Class-maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>class_maps</samp>](## "class_maps") | Dictionary |  |  |  | QOS Class-maps |
| [<samp>&nbsp;&nbsp;pbr</samp>](## "class_maps.pbr") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.pbr.[].name") | String |  |  |  | Class-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.pbr.[].ip") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.pbr.[].ip.access_group") | String |  |  |  | Standard Access-List Name |
| [<samp>&nbsp;&nbsp;qos</samp>](## "class_maps.qos") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.qos.[].name") | String |  |  |  | Class-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "class_maps.qos.[].vlan") | Integer |  |  |  | VLAN value(s) or range(s) of VLAN values |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "class_maps.qos.[].cos") | Integer |  |  |  | CoS value(s) or range(s) of CoS values |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.qos.[].ip") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ip.access_group") | String |  |  |  | IPv4 Access-List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "class_maps.qos.[].ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ipv6.access_group") | String |  |  |  | IPv6 Access-List Name |

### YAML

```yaml
class_maps:
  pbr:
    - name: <str>
      ip:
        access_group: <str>
  qos:
    - name: <str>
      vlan: <int>
      cos: <int>
      ip:
        access_group: <str>
      ipv6:
        access_group: <str>
```

## Clock

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>clock</samp>](## "clock") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;timezone</samp>](## "clock.timezone") | String |  |  |  |  |

### YAML

```yaml
clock:
  timezone: <str>
```

## Community Lists (legacy model)

### Description

AVD supports 2 different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The legacy data model supports simplified community list definition that only allows a single action to be defined as string:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>community_lists</samp>](## "community_lists") | List, items: Dictionary |  |  |  | Community Lists (legacy model) |
| [<samp>&nbsp;&nbsp;- name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

### YAML

```yaml
community_lists:
  - name: <str>
    action: <str>
```

## Extensibility with Custom Templates

### Description

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommenended to use a `!` delimiter at the top of each custom template.

Add `custom_templates` to group/host variables:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  | Extensibility with Custom Templates |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_templates.[].&lt;str&gt;") | String |  |  |  | Template relative path below playbook directory |

### YAML

```yaml
custom_templates:
  - <str>
```

## Daemon TerminAttr

### Description

You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
Streaming to multiple clusters both on-prem and cloud service is supported.
> Note For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
  which always contain the latest recommended versions and minimum required versions per EOS release.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>daemon_terminattr</samp>](## "daemon_terminattr") | Dictionary |  |  |  | Daemon TerminAttr |
| [<samp>&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision single cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
| [<samp>&nbsp;&nbsp;clusters</samp>](## "daemon_terminattr.clusters") | List, items: Dictionary |  |  |  | Multiple CloudVision clusters<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "daemon_terminattr.clusters.[].name") | String | Required, Unique |  |  | Cluster Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.clusters.[].cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.clusters.[].cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.clusters.[].cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.clusters.[].cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.clusters.[].cvauth.key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.clusters.[].cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.clusters.[].cvobscurekeyfile") | Boolean |  |  |  | Obscure Key File<br>Encrypt the private key used for authentication to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.clusters.[].cvproxy") | String |  |  |  | Proxy URL<br>Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.clusters.[].cvsourceip") | String |  |  |  | Source IP Address<br>Set source IP address in case of in-band managament<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.clusters.[].cvvrf") | String |  |  |  | VRF<br>The VRF to use to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.cvauth.key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
| [<samp>&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.cvobscurekeyfile") | Boolean |  |  |  | Obscure Key File<br>Encrypt the private key used for authentication to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.cvproxy") | String |  |  |  | Proxy URL<br>Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
| [<samp>&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.cvsourceip") | String |  |  |  | Source IP Address<br>Set source IP address in case of in-band managament<br> |
| [<samp>&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.cvvrf") | String |  |  |  | VRF<br>The VRF to use to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvgnmi</samp>](## "daemon_terminattr.cvgnmi") | Boolean |  |  |  | Stream states from EOS GNMI servers (Openconfig) to CloudVision. Available as of TerminAttr v1.13.1<br> |
| [<samp>&nbsp;&nbsp;disable_aaa</samp>](## "daemon_terminattr.disable_aaa") | Boolean |  |  |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization<br> |
| [<samp>&nbsp;&nbsp;grpcaddr</samp>](## "daemon_terminattr.grpcaddr") | String |  |  |  | Set the gRPC server address, the default is 127.0.0.1:6042<br>e.g. "MGMT/0.0.0.0:6042"<br> |
| [<samp>&nbsp;&nbsp;grpcreadonly</samp>](## "daemon_terminattr.grpcreadonly") | Boolean |  |  |  | gNMI read-only mode - Disable gnmi.Set()<br> |
| [<samp>&nbsp;&nbsp;ingestexclude</samp>](## "daemon_terminattr.ingestexclude") | String |  |  |  | Exclude paths from Sysdb on the ingest side.<br>e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"<br> |
| [<samp>&nbsp;&nbsp;smashexcludes</samp>](## "daemon_terminattr.smashexcludes") | String |  |  |  | Exclude paths from the shared memory table.<br>e.g. "ale,flexCounter,hardware,kni,pulse,strata"<br> |
| [<samp>&nbsp;&nbsp;taillogs</samp>](## "daemon_terminattr.taillogs") | String |  |  |  | Enable log file collection; /var/log/messages is streamed by default if no path is set.<br>e.g. "/var/log/messages"<br> |
| [<samp>&nbsp;&nbsp;ecodhcpaddr</samp>](## "daemon_terminattr.ecodhcpaddr") | String |  |  |  | ECO DHCP Collector address or ECO DHCP Fingerprint listening address in standalone mode (default "127.0.0.1:67")<br> |
| [<samp>&nbsp;&nbsp;ipfix</samp>](## "daemon_terminattr.ipfix") | Boolean |  |  |  | Enable IPFIX provider (TerminAttr default is true).<br>This flag is enabled by default and does not have to be added to the daemon configuration.<br> |
| [<samp>&nbsp;&nbsp;ipfixaddr</samp>](## "daemon_terminattr.ipfixaddr") | String |  |  |  | ECO IPFIX Collector address to listen on to receive IPFIX packets (TerminAttr default "127.0.0.1:4739").<br> |
| [<samp>&nbsp;&nbsp;sflow</samp>](## "daemon_terminattr.sflow") | Boolean |  |  |  | Enable sFlow provider (TerminAttr default is true).<br> |
| [<samp>&nbsp;&nbsp;sflowaddr</samp>](## "daemon_terminattr.sflowaddr") | String |  |  |  | ECO sFlow Collector address to listen on to receive sFlow packets (TerminAttr default "127.0.0.1:6343").<br> |
| [<samp>&nbsp;&nbsp;cvcompression</samp>](## "daemon_terminattr.cvcompression") | String |  |  |  | The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.<br>There is no need to change the compression scheme.<br> |
| [<samp>&nbsp;&nbsp;ingestauth_key</samp>](## "daemon_terminattr.ingestauth_key") | String |  |  |  | Deprecated key. Use `cvauth` instead.<br> |
| [<samp>&nbsp;&nbsp;ingestgrpcurl</samp>](## "daemon_terminattr.ingestgrpcurl") | Dictionary |  |  |  | Deprecated key. Use `cvaddrs` instead.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ips</samp>](## "daemon_terminattr.ingestgrpcurl.ips") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.ingestgrpcurl.ips.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "daemon_terminattr.ingestgrpcurl.port") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;ingestvrf</samp>](## "daemon_terminattr.ingestvrf") | String |  |  |  | Deprecated key. Use `cvvrf` instead.<br> |

### YAML

```yaml
daemon_terminattr:
  cvaddrs:
    - <str>
  clusters:
    - name: <str>
      cvaddrs:
        - <str>
      cvauth:
        method: <str>
        key: <str>
        token_file: <str>
      cvobscurekeyfile: <bool>
      cvproxy: <str>
      cvsourceip: <str>
      cvvrf: <str>
  cvauth:
    method: <str>
    key: <str>
    token_file: <str>
  cvobscurekeyfile: <bool>
  cvproxy: <str>
  cvsourceip: <str>
  cvvrf: <str>
  cvgnmi: <bool>
  disable_aaa: <bool>
  grpcaddr: <str>
  grpcreadonly: <bool>
  ingestexclude: <str>
  smashexcludes: <str>
  taillogs: <str>
  ecodhcpaddr: <str>
  ipfix: <bool>
  ipfixaddr: <str>
  sflow: <bool>
  sflowaddr: <str>
  cvcompression: <str>
  ingestauth_key: <str>
  ingestgrpcurl:
    ips:
      - <str>
    port: <int>
  ingestvrf: <str>
```

## Custom Daemons

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>daemons</samp>](## "daemons") | List, items: Dictionary |  |  |  | Custom Daemons |
| [<samp>&nbsp;&nbsp;- name</samp>](## "daemons.[].name") | String | Required, Unique |  |  | Daemon Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "daemons.[].exec") | String | Required |  |  | command to run as a daemon<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "daemons.[].enabled") | Boolean |  | True |  |  |

### YAML

```yaml
daemons:
  - name: <str>
    exec: <str>
    enabled: <bool>
```

## DHCP Relay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dhcp_relay</samp>](## "dhcp_relay") | Dictionary |  |  |  | DHCP Relay |
| [<samp>&nbsp;&nbsp;servers</samp>](## "dhcp_relay.servers") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "dhcp_relay.servers.[].&lt;str&gt;") | String |  |  |  | Server IP or Hostname |
| [<samp>&nbsp;&nbsp;tunnel_requests_disabled</samp>](## "dhcp_relay.tunnel_requests_disabled") | Boolean |  |  |  |  |

### YAML

```yaml
dhcp_relay:
  servers:
    - <str>
  tunnel_requests_disabled: <bool>
```

## DNS Domain

### Description

Domain Name
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dns_domain</samp>](## "dns_domain") | String |  |  |  | DNS Domain |

### YAML

```yaml
dns_domain: <str>
```

## Domain List

### Description

Search list of DNS domains
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "domain_list.[].&lt;str&gt;") | String |  |  |  | Domain name |

### YAML

```yaml
domain_list:
  - <str>
```

## Global 802.1x Authentication

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  | Global 802.1x Authentication |
| [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  | Protocol LLDP Bypass |
| [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |

### YAML

```yaml
dot1x:
  system_auth_control: <bool>
  protocol_lldp_bypass: <bool>
  dynamic_authorization: <bool>
```

## Enable Password

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>enable_password</samp>](## "enable_password") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;hash_algorithm</samp>](## "enable_password.hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;key</samp>](## "enable_password.key") | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device. |

### YAML

```yaml
enable_password:
  hash_algorithm: <str>
  key: <str>
```

## EOS CLI

### Description

Multiline string with EOS CLI rendered directly on the root level of the final EOS configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>eos_cli</samp>](## "eos_cli") | String |  |  |  | EOS CLI |

### YAML

```yaml
eos_cli: <str>
```

## Event Handlers

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Event Handlers |
| [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String |  |  |  | Event Handler Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log | Action Type<br>Type of action<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |

### YAML

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

## Event Monitor

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_monitor</samp>](## "event_monitor") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "event_monitor.enabled") | Boolean |  |  |  |  |

### YAML

```yaml
event_monitor:
  enabled: <bool>
```

## Generate Default Config

### Description

The `generate_default_config` knob allows to omit default EOS configuration.
This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

The following commands will be omitted when `generate_default_config` is set to `false`:

- RANCID Content Type
- Hostname
- Default configuration for `aaa`
- Default configuration for `enable password`
- Transceiver qsfp default mode
- End of configuration delimiter
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>generate_default_config</samp>](## "generate_default_config") | Boolean |  | True |  |  |

### YAML

```yaml
generate_default_config: <bool>
```

## Generate Device Documentation

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>generate_device_documentation</samp>](## "generate_device_documentation") | Boolean |  | True |  |  |

### YAML

```yaml
generate_device_documentation: <bool>
```

## Interface Defaults

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_defaults</samp>](## "interface_defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ethernet</samp>](## "interface_defaults.ethernet") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "interface_defaults.ethernet.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;mtu</samp>](## "interface_defaults.mtu") | Integer |  |  |  |  |

### YAML

```yaml
interface_defaults:
  ethernet:
    shutdown: <bool>
  mtu: <int>
```

## Maintenance Interface Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_groups</samp>](## "interface_groups") | List, items: Dictionary |  |  |  | Maintenance Interface Groups |
| [<samp>&nbsp;&nbsp;- name</samp>](## "interface_groups.[].name") | String | Required, Unique |  |  | Interface-Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "interface_groups.[].interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "interface_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of BGP Maintenance Profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_maintenance_profiles</samp>](## "interface_groups.[].interface_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interface_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of Interface Maintenance Profile |

### YAML

```yaml
interface_groups:
  - name: <str>
    interfaces:
      - <str>
    bgp_maintenance_profiles:
      - <str>
    interface_maintenance_profiles:
      - <str>
```

## Interface Profiles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_profiles</samp>](## "interface_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "interface_profiles.[].name") | String | Required, Unique |  |  | Interface-Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "interface_profiles.[].commands") | List, items: String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_profiles.[].commands.[].&lt;str&gt;") | String |  |  |  | EOS CLI interface command<br>Example: "switchport mode access" |

### YAML

```yaml
interface_profiles:
  - name: <str>
    commands:
      - <str>
```

## IP Extended Access-Lists (improved model)

### Description

AVD currently supports 2 different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The improved data model has a more sophisticated design documented below:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_access_lists</samp>](## "ip_access_lists") | List, items: Dictionary |  |  |  | IP Extended Access-Lists (improved model) |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ip_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_access_lists.[].entries") | List, items: Dictionary |  |  |  | ACL Entries |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ip_access_lists.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ip_access_lists.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in acl entry will be ignored.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny | ACL action.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_access_lists.[].entries.[].protocol") | String |  |  |  | ip, tcp, udp, icmp or other protocol name or number.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ip_access_lists.[].entries.[].source") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ip_access_lists.[].entries.[].source_ports_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ip_access_lists.[].entries.[].source_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].source_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP source port name or number. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ip_access_lists.[].entries.[].destination") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ip_access_lists.[].entries.[].destination_ports_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ip_access_lists.[].entries.[].destination_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].destination_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP destination port name or number. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ip_access_lists.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].tcp_flags.[].&lt;str&gt;") | String |  |  |  | TCP Flag Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp>](## "ip_access_lists.[].entries.[].fragments") | Boolean |  |  |  | Match non-head fragment packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ip_access_lists.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "ip_access_lists.[].entries.[].ttl") | Integer |  |  | Min: 0<br>Max: 254 | TTL value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp>](## "ip_access_lists.[].entries.[].ttl_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ip_access_lists.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ip_access_lists.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ip_access_lists.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ip_access_lists.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ip_access_lists.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ip_access_lists.[].entries.[].vlan_number") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp>](## "ip_access_lists.[].entries.[].vlan_inner") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ip_access_lists.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |

### YAML

```yaml
ip_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    entries:
      - sequence: <int>
        remark: <str>
        action: <str>
        protocol: <str>
        source: <str>
        source_ports_match: <str>
        source_ports:
          - <str>
        destination: <str>
        destination_ports_match: <str>
        destination_ports:
          - <str>
        tcp_flags:
          - <str>
        fragments: <bool>
        log: <bool>
        ttl: <int>
        ttl_match: <str>
        icmp_type: <str>
        icmp_code: <str>
        nexthop_group: <str>
        tracked: <bool>
        dscp: <str>
        vlan_number: <int>
        vlan_inner: <bool>
        vlan_mask: <str>
```

## IP Community Lists

### Description

AVD supports 2 different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The improved data model has a better design documented below:

communities and regexp MUST not be configured together in the same entry
possible community strings are (case insensitive):
 - GSHUT
 - internet
 - local-as
 - no-advertise
 - no-export
 - <1-4294967040>
 - aa:nn

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  | IP Community Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_community_lists.[].name") | String | Required, Unique |  |  | IP Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_community_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- action</samp>](## "ip_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "ip_community_lists.[].entries.[].communities") | List, items: String |  |  |  | If defined, a standard community-list will be configured |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_community_lists.[].entries.[].communities.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression<br>If defined, a regex community-list will be configured |

### YAML

```yaml
ip_community_lists:
  - name: <str>
    entries:
      - action: <str>
        communities:
          - <str>
        regexp: <str>
```

## IP DHCP Relay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_dhcp_relay</samp>](## "ip_dhcp_relay") | Dictionary |  |  |  | IP DHCP Relay |
| [<samp>&nbsp;&nbsp;information_option</samp>](## "ip_dhcp_relay.information_option") | Boolean |  |  |  | Insert Option-82 information |

### YAML

```yaml
ip_dhcp_relay:
  information_option: <bool>
```

## Domain Lookup

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_domain_lookup</samp>](## "ip_domain_lookup") | Dictionary |  |  |  | Domain Lookup |
| [<samp>&nbsp;&nbsp;source_interfaces</samp>](## "ip_domain_lookup.source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_domain_lookup.source_interfaces.[].name") | String | Required, Unique |  |  | Source Interface<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_domain_lookup.source_interfaces.[].vrf") | String |  |  |  | VRF |

### YAML

```yaml
ip_domain_lookup:
  source_interfaces:
    - name: <str>
      vrf: <str>
```

## IP Extended Community Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists</samp>](## "ip_extcommunity_lists") | List, items: Dictionary |  |  |  | IP Extended Community Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extcommunities</samp>](## "ip_extcommunity_lists.[].entries.[].extcommunities") | String | Required |  |  | Communities as string<br>Example: "65000:65000" |

### YAML

```yaml
ip_extcommunity_lists:
  - name: <str>
    entries:
      - type: <str>
        extcommunities: <str>
```

## IP Extended Community Lists RegExp

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists_regexp</samp>](## "ip_extcommunity_lists_regexp") | List, items: Dictionary |  |  |  | IP Extended Community Lists RegExp |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists_regexp.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists_regexp.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].regexp") | String | Required |  |  | Regular Expression |

### YAML

```yaml
ip_extcommunity_lists_regexp:
  - name: <str>
    entries:
      - type: <str>
        regexp: <str>
```

## IP HTTP Client Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_http_client_source_interfaces</samp>](## "ip_http_client_source_interfaces") | List, items: Dictionary |  |  |  | IP HTTP Client Source Interfaces |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_http_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_http_client_source_interfaces.[].vrf") | String |  |  |  | VRF |

### YAML

```yaml
ip_http_client_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP ICMP Redirect

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_icmp_redirect</samp>](## "ip_icmp_redirect") | Boolean |  |  |  | IP ICMP Redirect |

### YAML

```yaml
ip_icmp_redirect: <bool>
```

## IP IGMP Snooping

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_igmp_snooping</samp>](## "ip_igmp_snooping") | Dictionary |  |  |  | IP IGMP Snooping |
| [<samp>&nbsp;&nbsp;globally_enabled</samp>](## "ip_igmp_snooping.globally_enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;robustness_variable</samp>](## "ip_igmp_snooping.robustness_variable") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;restart_query_interval</samp>](## "ip_igmp_snooping.restart_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;interface_restart_query</samp>](## "ip_igmp_snooping.interface_restart_query") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.proxy") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;vlans</samp>](## "ip_igmp_snooping.vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "ip_igmp_snooping.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.vlans.[].querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.vlans.[].querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.vlans.[].querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.vlans.[].querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_groups</samp>](## "ip_igmp_snooping.vlans.[].max_groups") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.vlans.[].fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.vlans.[].proxy") | Boolean |  |  |  | Global proxy settings should be enabled before enabling per-vlan |

### YAML

```yaml
ip_igmp_snooping:
  globally_enabled: <bool>
  robustness_variable: <int>
  restart_query_interval: <int>
  interface_restart_query: <int>
  fast_leave: <bool>
  querier:
    enabled: <bool>
    address: <str>
    query_interval: <int>
    max_response_time: <int>
    last_member_query_interval: <int>
    last_member_query_count: <int>
    startup_query_interval: <int>
    startup_query_count: <int>
    version: <int>
  proxy: <bool>
  vlans:
    - id: <int>
      enabled: <bool>
      querier:
        enabled: <bool>
        address: <str>
        query_interval: <int>
        max_response_time: <int>
        last_member_query_interval: <int>
        last_member_query_count: <int>
        startup_query_interval: <int>
        startup_query_count: <int>
        version: <int>
      max_groups: <int>
      fast_leave: <bool>
      proxy: <bool>
```

## IP RADIUS Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_radius_source_interfaces</samp>](## "ip_radius_source_interfaces") | List, items: Dictionary |  |  |  | IP RADIUS Source Interfaces |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_radius_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_radius_source_interfaces.[].vrf") | String |  |  |  | VRF Name |

### YAML

```yaml
ip_radius_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP Routing

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_routing</samp>](## "ip_routing") | Boolean |  |  |  | IP Routing |

### YAML

```yaml
ip_routing: <bool>
```

## IP Routing IPv6 Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_routing_ipv6_interfaces</samp>](## "ip_routing_ipv6_interfaces") | Boolean |  |  |  | IP Routing IPv6 Interfaces |

### YAML

```yaml
ip_routing_ipv6_interfaces: <bool>
```

## IP SSH Client Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_ssh_client_source_interfaces</samp>](## "ip_ssh_client_source_interfaces") | List, items: Dictionary |  |  |  | IP SSH Client Source Interfaces |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_ssh_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_ssh_client_source_interfaces.[].vrf") | String |  | default |  | VRF |

### YAML

```yaml
ip_ssh_client_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IPv6 Extended Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_access_lists</samp>](## "ipv6_access_lists") | List, items: Dictionary |  |  |  | IPv6 Extended Access-Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_access_lists.[].name") | String | Required, Unique |  |  | IPv6 Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

### YAML

```yaml
ipv6_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## IPv6 Hardware

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_hardware</samp>](## "ipv6_hardware") | Dictionary |  |  |  | IPv6 Hardware |
| [<samp>&nbsp;&nbsp;fib</samp>](## "ipv6_hardware.fib") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ipv6_hardware.fib.optimize") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ipv6_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ipv6_hardware.fib.optimize.prefixes.profile") | String |  |  |  | Pre-defined profile 'internet' or user-defined profile name |

### YAML

```yaml
ipv6_hardware:
  fib:
    optimize:
      prefixes:
        profile: <str>
```

## IPv6 ICMP Redirect

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_icmp_redirect</samp>](## "ipv6_icmp_redirect") | Boolean |  |  |  | IPv6 ICMP Redirect |

### YAML

```yaml
ipv6_icmp_redirect: <bool>
```

## IPv6 Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_prefix_lists</samp>](## "ipv6_prefix_lists") | List, items: Dictionary |  |  |  | IPv6 Prefix Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 1b11:3a00:22b0:0082::/64 eq 128" |

### YAML

```yaml
ipv6_prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## IPv6 Standard Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_standard_access_lists</samp>](## "ipv6_standard_access_lists") | List, items: Dictionary |  |  |  | IPv6 Standard Access-Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_standard_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

### YAML

```yaml
ipv6_standard_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## LACP

### Description

Set Link Aggregation Control Protocol (LACP) parameters.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>lacp</samp>](## "lacp") | Dictionary |  |  |  | LACP |
| [<samp>&nbsp;&nbsp;port_id</samp>](## "lacp.port_id") | Dictionary |  |  |  | LACP port-ID range configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp>](## "lacp.port_id.range") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;begin</samp>](## "lacp.port_id.range.begin") | Integer |  |  |  | Minimum LACP port-ID range. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "lacp.port_id.range.end") | Integer |  |  |  | Maximum LACP port-ID range. |
| [<samp>&nbsp;&nbsp;rate_limit</samp>](## "lacp.rate_limit") | Dictionary |  |  |  | Set LACPDU rate limit options. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "lacp.rate_limit.default") | Boolean |  |  |  | Enable LACPDU rate limiting by default on all ports. |
| [<samp>&nbsp;&nbsp;system_priority</samp>](## "lacp.system_priority") | Integer |  |  | Min: 0<br>Max: 65535 | Set local system LACP priority. |

### YAML

```yaml
lacp:
  port_id:
    range:
      begin: <int>
      end: <int>
  rate_limit:
    default: <bool>
  system_priority: <int>
```

## Load Interval

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>load_interval</samp>](## "load_interval") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;default</samp>](## "load_interval.default") | Integer |  |  |  | Default load interval in seconds |

### YAML

```yaml
load_interval:
  default: <int>
```

## Local Users

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 1<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  | SSH Key |

### YAML

```yaml
local_users:
  - name: <str>
    privilege: <int>
    role: <str>
    sha512_password: <str>
    no_password: <bool>
    ssh_key: <str>
```

## Mac Access Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_access_lists</samp>](## "mac_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "mac_access_lists.[].name") | String | Required, Unique |  |  | MAC Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "mac_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "mac_access_lists.[].entries.[].sequence") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_access_lists.[].entries.[].action") | String |  |  |  |  |

### YAML

```yaml
mac_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    entries:
      - sequence: <int>
        action: <str>
```

## MACsec

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_security</samp>](## "mac_security") | Dictionary |  |  |  | MACsec |
| [<samp>&nbsp;&nbsp;license</samp>](## "mac_security.license") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_name</samp>](## "mac_security.license.license_name") | String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_key</samp>](## "mac_security.license.license_key") | String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;fips_restrictions</samp>](## "mac_security.fips_restrictions") | Boolean | Required |  |  |  |
| [<samp>&nbsp;&nbsp;profiles</samp>](## "mac_security.profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "mac_security.profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher</samp>](## "mac_security.profiles.[].cipher") | String |  |  | Valid Values:<br>- aes128-gcm<br>- aes128-gcm-xpn<br>- aes256-gcm<br>- aes256-gcm-xpn |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_keys</samp>](## "mac_security.profiles.[].connection_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "mac_security.profiles.[].connection_keys.[].id") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypted_key</samp>](## "mac_security.profiles.[].connection_keys.[].encrypted_key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback</samp>](## "mac_security.profiles.[].connection_keys.[].fallback") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp>](## "mac_security.profiles.[].mka") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session</samp>](## "mac_security.profiles.[].mka.session") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rekey_period</samp>](## "mac_security.profiles.[].mka.session.rekey_period") | Integer |  |  | Min: 30<br>Max: 100000 | Rekey period in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sci</samp>](## "mac_security.profiles.[].sci") | Boolean |  |  |  |  |

### YAML

```yaml
mac_security:
  license:
    license_name: <str>
    license_key: <str>
  fips_restrictions: <bool>
  profiles:
    - name: <str>
      cipher: <str>
      connection_keys:
        - id: <str>
          encrypted_key: <str>
          fallback: <bool>
      mka:
        session:
          rekey_period: <int>
      sci: <bool>
```

## Maintenance Mode

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>maintenance</samp>](## "maintenance") | Dictionary |  |  |  | Maintenance Mode |
| [<samp>&nbsp;&nbsp;default_interface_profile</samp>](## "maintenance.default_interface_profile") | String |  |  |  | Name of default Interface Profile<br> |
| [<samp>&nbsp;&nbsp;default_bgp_profile</samp>](## "maintenance.default_bgp_profile") | String |  |  |  | Name of default BGP Profile<br> |
| [<samp>&nbsp;&nbsp;default_unit_profile</samp>](## "maintenance.default_unit_profile") | String |  |  |  | Name of default Unit Profile<br> |
| [<samp>&nbsp;&nbsp;interface_profiles</samp>](## "maintenance.interface_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.interface_profiles.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_monitoring</samp>](## "maintenance.interface_profiles.[].rate_monitoring") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "maintenance.interface_profiles.[].rate_monitoring.load_interval") | Integer |  |  |  | Load Interval in Seconds<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "maintenance.interface_profiles.[].rate_monitoring.threshold") | Integer |  |  |  | Threshold in kbps<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "maintenance.interface_profiles.[].shutdown") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_delay</samp>](## "maintenance.interface_profiles.[].shutdown.max_delay") | Integer |  |  |  | Max delay in seconds<br> |
| [<samp>&nbsp;&nbsp;bgp_profiles</samp>](## "maintenance.bgp_profiles") | List, items: Dictionary |  |  |  | BGP Profiles |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.bgp_profiles.[].name") | String | Required, Unique |  |  | BGP Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initiator</samp>](## "maintenance.bgp_profiles.[].initiator") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_inout</samp>](## "maintenance.bgp_profiles.[].initiator.route_map_inout") | String |  |  |  | Route Map |
| [<samp>&nbsp;&nbsp;unit_profiles</samp>](## "maintenance.unit_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.unit_profiles.[].name") | String | Required, Unique |  |  | Unit Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_boot</samp>](## "maintenance.unit_profiles.[].on_boot") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "maintenance.unit_profiles.[].on_boot.duration") | Integer |  |  | Min: 300<br>Max: 3600 | On-boot in seconds<br> |
| [<samp>&nbsp;&nbsp;units</samp>](## "maintenance.units") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.units.[].name") | String | Required, Unique |  |  | Unit Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiesce</samp>](## "maintenance.units.[].quiesce") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "maintenance.units.[].profile") | String | Required |  |  | Name of Unit Profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "maintenance.units.[].groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_groups</samp>](## "maintenance.units.[].groups.bgp_groups") | List, items: String |  |  |  | BGP Groups |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.bgp_groups.[].&lt;str&gt;") | String |  |  |  | Name of BGP Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_groups</samp>](## "maintenance.units.[].groups.interface_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.interface_groups.[].&lt;str&gt;") | String |  |  |  | Name of Interface Group |

### YAML

```yaml
maintenance:
  default_interface_profile: <str>
  default_bgp_profile: <str>
  default_unit_profile: <str>
  interface_profiles:
    - name: <str>
      rate_monitoring:
        load_interval: <int>
        threshold: <int>
      shutdown:
        max_delay: <int>
  bgp_profiles:
    - name: <str>
      initiator:
        route_map_inout: <str>
  unit_profiles:
    - name: <str>
      on_boot:
        duration: <int>
  units:
    - name: <str>
      quiesce: <bool>
      profile: <str>
      groups:
        bgp_groups:
          - <str>
        interface_groups:
          - <str>
```

## Management HTTP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_api_http</samp>](## "management_api_http") | Dictionary |  |  |  | Management HTTP |
| [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_api_http.enable_http") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_api_http.enable_https") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;https_ssl_profile</samp>](## "management_api_http.https_ssl_profile") | String |  |  |  | SSL Profile Name |
| [<samp>&nbsp;&nbsp;default_services</samp>](## "management_api_http.default_services") | Boolean |  |  |  | Enable default services: capi-doc and tapagg |
| [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_http.enable_vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_http.enable_vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "management_api_http.enable_vrfs.[].access_group") | String |  |  |  | Standard IPv4 ACL name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp>](## "management_api_http.enable_vrfs.[].ipv6_access_group") | String |  |  |  | Standard IPv6 ACL name |
| [<samp>&nbsp;&nbsp;protocol_https_certificate</samp>](## "management_api_http.protocol_https_certificate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_api_http.protocol_https_certificate.certificate") | String |  |  |  | Name of certificate; private key must also be specified |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_key</samp>](## "management_api_http.protocol_https_certificate.private_key") | String |  |  |  | Name of private key; certificate must also be specified |

### YAML

```yaml
management_api_http:
  enable_http: <bool>
  enable_https: <bool>
  https_ssl_profile: <str>
  default_services: <bool>
  enable_vrfs:
    - name: <str>
      access_group: <str>
      ipv6_access_group: <str>
  protocol_https_certificate:
    certificate: <str>
    private_key: <str>
```

## Management API Models

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_api_models</samp>](## "management_api_models") | Dictionary |  |  |  | Management API Models |
| [<samp>&nbsp;&nbsp;providers</samp>](## "management_api_models.providers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_models.providers.[].name") | String |  |  | Valid Values:<br>- sysdb<br>- smash |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.providers.[].paths") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- path</samp>](## "management_api_models.providers.[].paths.[].path") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.providers.[].paths.[].disabled") | Boolean |  | False |  |  |

### YAML

```yaml
management_api_models:
  providers:
    - name: <str>
      paths:
        - path: <str>
          disabled: <bool>
```

## Management Console

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_console</samp>](## "management_console") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_console.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 |  |

### YAML

```yaml
management_console:
  idle_timeout: <int>
```

## Management Defaults

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_defaults</samp>](## "management_defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;secret</samp>](## "management_defaults.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash</samp>](## "management_defaults.secret.hash") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |

### YAML

```yaml
management_defaults:
  secret:
    hash: <str>
```

## Management Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_interfaces</samp>](## "management_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "management_interfaces.[].name") | String | Required, Unique |  |  | Management Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "management_interfaces.[].description") | String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "management_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_interfaces.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "management_interfaces.[].ip_address") | String | Required |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "management_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_interfaces.[].type") | String |  | oob | Valid Values:<br>- oob<br>- inband | For documentation purposes only |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "management_interfaces.[].gateway") | String | Required |  |  | IPv4 address of default gateway in management VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_gateway</samp>](## "management_interfaces.[].ipv6_gateway") | String |  |  |  | IPv6 address of default gateway in management VRF |

### YAML

```yaml
management_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    mtu: <int>
    vrf: <str>
    ip_address: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    type: <str>
    gateway: <str>
    ipv6_gateway: <str>
```

## Management Security

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_security</samp>](## "management_security") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;entropy_source</samp>](## "management_security.entropy_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;password</samp>](## "management_security.password") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum_length</samp>](## "management_security.password.minimum_length") | Integer |  |  | Min: 1<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_key_common</samp>](## "management_security.password.encryption_key_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_reversible</samp>](## "management_security.password.encryption_reversible") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;ssl_profiles</samp>](## "management_security.ssl_profiles") | List, items: Dictionary |  |  |  | SSL Profiles |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_security.ssl_profiles.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp>](## "management_security.ssl_profiles.[].tls_versions") | String |  |  |  | TLS Versions<br>List of allowed TLS versions as string<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp>](## "management_security.ssl_profiles.[].cipher_list") | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_security.ssl_profiles.[].certificate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "management_security.ssl_profiles.[].certificate.file") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.ssl_profiles.[].certificate.key") | String |  |  |  |  |

### YAML

```yaml
management_security:
  entropy_source: <str>
  password:
    minimum_length: <int>
    encryption_key_common: <bool>
    encryption_reversible: <str>
  ssl_profiles:
    - name: <str>
      tls_versions: <str>
      cipher_list: <str>
      certificate:
        file: <str>
        key: <str>
```

## Management SSH

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_ssh</samp>](## "management_ssh") | Dictionary |  |  |  | Management SSH |
| [<samp>&nbsp;&nbsp;access_groups</samp>](## "management_ssh.access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.access_groups.[].name") | String |  |  |  | Standard ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.access_groups.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;ipv6_access_groups</samp>](## "management_ssh.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.ipv6_access_groups.[].name") | String |  |  |  | Standard ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.ipv6_access_groups.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_ssh.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes |
| [<samp>&nbsp;&nbsp;cipher</samp>](## "management_ssh.cipher") | List, items: String |  |  |  | Cryptographic ciphers for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.cipher.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;key_exchange</samp>](## "management_ssh.key_exchange") | List, items: String |  |  |  | Cryptographic key exchange methods for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.key_exchange.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;mac</samp>](## "management_ssh.mac") | List, items: String |  |  |  | Cryptographic MAC algorithms for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.mac.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;hostkey</samp>](## "management_ssh.hostkey") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "management_ssh.hostkey.server") | List, items: String |  |  |  | SSH host key settings |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.hostkey.server.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable</samp>](## "management_ssh.enable") | Boolean |  |  |  | Enable SSH daemon |
| [<samp>&nbsp;&nbsp;connection</samp>](## "management_ssh.connection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "management_ssh.connection.limit") | Integer |  |  | Min: 1<br>Max: 100 | Maximum total number of SSH sessions to device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;per_host</samp>](## "management_ssh.connection.per_host") | Integer |  |  | Min: 1<br>Max: 20 | Maximum number of SSH sessions to device from a single host |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_ssh.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_ssh.vrfs.[].enable") | Boolean |  |  |  | Enable SSH in VRF |
| [<samp>&nbsp;&nbsp;log_level</samp>](## "management_ssh.log_level") | String |  |  |  | SSH daemon log level |

### YAML

```yaml
management_ssh:
  access_groups:
    - name: <str>
      vrf: <str>
  ipv6_access_groups:
    - name: <str>
      vrf: <str>
  idle_timeout: <int>
  cipher:
    - <str>
  key_exchange:
    - <str>
  mac:
    - <str>
  hostkey:
    server:
      - <str>
  enable: <bool>
  connection:
    limit: <int>
    per_host: <int>
  vrfs:
    - name: <str>
      enable: <bool>
  log_level: <str>
```

## Match Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>match_list_input</samp>](## "match_list_input") | Dictionary |  |  |  | Match Lists |
| [<samp>&nbsp;&nbsp;string</samp>](## "match_list_input.string") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "match_list_input.string.[].name") | String | Required, Unique |  |  | Match-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "match_list_input.string.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "match_list_input.string.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_regex</samp>](## "match_list_input.string.[].sequence_numbers.[].match_regex") | String | Required |  |  | Regular Expression |

### YAML

```yaml
match_list_input:
  string:
    - name: <str>
      sequence_numbers:
        - sequence: <int>
          match_regex: <str>
```

## MCS Client

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mcs_client</samp>](## "mcs_client") | Dictionary |  |  |  | MCS Client |
| [<samp>&nbsp;&nbsp;shutdown</samp>](## "mcs_client.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;cvx_secondary</samp>](## "mcs_client.cvx_secondary") | Dictionary |  |  |  | CVX Secondary |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "mcs_client.cvx_secondary.name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mcs_client.cvx_secondary.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_hosts</samp>](## "mcs_client.cvx_secondary.server_hosts") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mcs_client.cvx_secondary.server_hosts.[].&lt;str&gt;") | String |  |  |  | IP or hostname |

### YAML

```yaml
mcs_client:
  shutdown: <bool>
  cvx_secondary:
    name: <str>
    shutdown: <bool>
    server_hosts:
      - <str>
```

## Monitor Connectivity

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>monitor_connectivity</samp>](## "monitor_connectivity") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;shutdown</samp>](## "monitor_connectivity.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;interval</samp>](## "monitor_connectivity.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.interface_sets") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.interface_sets.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.interface_sets.[].interfaces") | String |  |  |  | Interface range(s) should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interface ranges can be specified separated by ","<br> |
| [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.hosts.[].name") | String |  |  |  | Host Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.hosts.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.hosts.[].ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.hosts.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.hosts.[].url") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "monitor_connectivity.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.vrfs.[].interface_sets") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].hosts.[].name") | String |  |  |  | Host name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.vrfs.[].hosts.[].ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].hosts.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.vrfs.[].hosts.[].url") | String |  |  |  |  |

### YAML

```yaml
monitor_connectivity:
  shutdown: <bool>
  interval: <int>
  interface_sets:
    - name: <str>
      interfaces: <str>
  local_interfaces: <str>
  hosts:
    - name: <str>
      description: <str>
      ip: <str>
      local_interfaces: <str>
      url: <str>
  vrfs:
    - name: <str>
      description: <str>
      interface_sets:
        - name: <str>
          interfaces: <str>
      local_interfaces: <str>
      hosts:
        - name: <str>
          description: <str>
          ip: <str>
          local_interfaces: <str>
          url: <str>
```

## Monitor Sessions

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>monitor_sessions</samp>](## "monitor_sessions") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].name") | String | Required |  |  | Session Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sources</samp>](## "monitor_sessions.[].sources") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].sources.[].name") | String |  |  |  | Interface name, range or comma separated list |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "monitor_sessions.[].sources.[].direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].sources.[].access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].sources.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].sources.[].access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "monitor_sessions.[].sources.[].access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "monitor_sessions.[].destinations") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "monitor_sessions.[].destinations.[].&lt;str&gt;") | String |  |  |  | 'cpu' or interface name, range or comma separated list |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "monitor_sessions.[].encapsulation_gre_metadata_tx") | Boolean |  |  |  | Encapsulation GRE metadata TX |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "monitor_sessions.[].header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "monitor_sessions.[].rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "monitor_sessions.[].rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_sessions.[].sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "monitor_sessions.[].truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "monitor_sessions.[].truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "monitor_sessions.[].truncate.size") | Integer |  |  |  | Size in bytes |

### YAML

```yaml
monitor_sessions:
  - name: <str>
    sources:
      - name: <str>
        direction: <str>
        access_group:
          type: <str>
          name: <str>
          priority: <int>
    destinations:
      - <str>
    encapsulation_gre_metadata_tx: <bool>
    header_remove_size: <int>
    access_group:
      type: <str>
      name: <str>
    rate_limit_per_ingress_chip: <str>
    rate_limit_per_egress_chip: <str>
    sample: <int>
    truncate:
      enabled: <bool>
      size: <int>
```

## MPLS

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mpls</samp>](## "mpls") | Dictionary |  |  |  | MPLS |
| [<samp>&nbsp;&nbsp;ip</samp>](## "mpls.ip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;ldp</samp>](## "mpls.ldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp>](## "mpls.ldp.interface_disabled_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "mpls.ldp.router_id") | String |  |  |  | Router ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.ldp.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp>](## "mpls.ldp.transport_address_interface") | String |  |  |  | Interface Name |

### YAML

```yaml
mpls:
  ip: <bool>
  ldp:
    interface_disabled_default: <bool>
    router_id: <str>
    shutdown: <bool>
    transport_address_interface: <str>
```

## Name Server

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_server</samp>](## "name_server") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
name_server:
  source:
    vrf: <str>
  nodes:
    - <str>
```

## Peer Filters

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>peer_filters</samp>](## "peer_filters") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "peer_filters.[].name") | String | Required, Unique |  |  | Peer-filter Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "peer_filters.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "peer_filters.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "peer_filters.[].sequence_numbers.[].match") | String | Required |  |  | Match as string<br>Example: "as-range 1-100 result accept" |

### YAML

```yaml
peer_filters:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        match: <str>
```

## Platform

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform</samp>](## "platform") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;trident</samp>](## "platform.trident") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp>](## "platform.trident.forwarding_table_partition") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;sand</samp>](## "platform.sand") | Dictionary |  |  |  | Most of the platform sand options are hardware dependant and optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp>](## "platform.sand.qos_maps") | List, items: Dictionary |  |  |  | QOS Maps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- traffic_class</samp>](## "platform.sand.qos_maps.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp>](## "platform.sand.qos_maps.[].to_network_qos") | Integer |  |  | Min: 0<br>Max: 63 | To Network QOS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp>](## "platform.sand.lag") | Dictionary |  |  |  | LAG |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp>](## "platform.sand.lag.hardware_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sand.lag.mode") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp>](## "platform.sand.forwarding_mode") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp>](## "platform.sand.multicast_replication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "platform.sand.multicast_replication.default") | String |  |  | Valid Values:<br>- ingress<br>- egress |  |

### YAML

```yaml
platform:
  trident:
    forwarding_table_partition: <str>
  sand:
    qos_maps:
      - traffic_class: <int>
        to_network_qos: <int>
    lag:
      hardware_only: <bool>
      mode: <str>
    forwarding_mode: <str>
    multicast_replication:
      default: <str>
```

## Policy-Maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  | Policy-Maps |
| [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].name") | String |  |  |  | Policy-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].classes.[].name") | String |  |  |  | Class Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | Drop<br>'drop' and 'set' are mutually exclusive |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].name") | String |  |  |  | Policy-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].classes.[].name") | String |  |  |  | Class Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  | COS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  | DSCP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  | Traffic-class |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  | Drop-precedence |

### YAML

```yaml
policy_maps:
  pbr:
    - name: <str>
      classes:
        - name: <str>
          index: <int>
          drop: <bool>
          set:
            nexthop:
              ip_address: <str>
              recursive: <bool>
  qos:
    - name: <str>
      classes:
        - name: <str>
          set:
            cos: <int>
            dscp: <str>
            traffic_class: <int>
            drop_precedence: <int>
```

## Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>prefix_lists</samp>](## "prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 10.255.0.0/27 eq 32" |

### YAML

```yaml
prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Redundancy

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  |  | Redundancy Protocol |

### YAML

```yaml
redundancy:
  protocol: <str>
```

## Route Maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>route_maps</samp>](## "route_maps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "route_maps.[].name") | String | Required, Unique |  |  | Route-map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "route_maps.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "route_maps.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "route_maps.[].sequence_numbers.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "route_maps.[].sequence_numbers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "route_maps.[].sequence_numbers.[].match") | List, items: String |  |  |  | List of "match" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].match.[].&lt;str&gt;") | String |  |  |  | Match as string<br>Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "route_maps.[].sequence_numbers.[].set") | List, items: String |  |  |  | List of "set" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].set.[].&lt;str&gt;") | String |  |  |  | Set as string<br>Example: "origin incomplete"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_route_map</samp>](## "route_maps.[].sequence_numbers.[].sub_route_map") | String |  |  |  | Name of Sub-Route-map |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</samp>](## "route_maps.[].sequence_numbers.[].continue") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "route_maps.[].sequence_numbers.[].continue.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number</samp>](## "route_maps.[].sequence_numbers.[].continue.sequence_number") | Integer |  |  |  |  |

### YAML

```yaml
route_maps:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        type: <str>
        description: <str>
        match:
          - <str>
        set:
          - <str>
        sub_route_map: <str>
        continue:
          enabled: <bool>
          sequence_number: <int>
```

## Router General configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_general</samp>](## "router_general") | Dictionary |  |  |  | Router General configuration |
| [<samp>&nbsp;&nbsp;router_id</samp>](## "router_general.router_id") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_general.router_id.ipv4") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_general.router_id.ipv6") | String |  |  |  | IPv6 Address |
| [<samp>&nbsp;&nbsp;nexthop_fast_failover</samp>](## "router_general.nexthop_fast_failover") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_general.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].name") | String | Required, Unique |  |  | Destination-VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;leak_routes</samp>](## "router_general.vrfs.[].leak_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_vrf</samp>](## "router_general.vrfs.[].leak_routes.[].source_vrf") | String |  |  |  | Source-VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subscribe_policy</samp>](## "router_general.vrfs.[].leak_routes.[].subscribe_policy") | String |  |  |  | Route-Map Policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_general.vrfs.[].routes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_prefix_lists</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic Prefix List Name |

### YAML

```yaml
router_general:
  router_id:
    ipv4: <str>
    ipv6: <str>
  nexthop_fast_failover: <bool>
  vrfs:
    - name: <str>
      leak_routes:
        - source_vrf: <str>
          subscribe_policy: <str>
      routes:
        dynamic_prefix_lists:
          - name: <str>
```

## Router IGMP Configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_igmp</samp>](## "router_igmp") | Dictionary |  |  |  | Router IGMP Configuration |
| [<samp>&nbsp;&nbsp;ssm_aware</samp>](## "router_igmp.ssm_aware") | Boolean |  |  |  |  |

### YAML

```yaml
router_igmp:
  ssm_aware: <bool>
```

## Router L2 VPN

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_l2_vpn</samp>](## "router_l2_vpn") | Dictionary |  |  |  | Router L2 VPN |
| [<samp>&nbsp;&nbsp;nd_rs_flooding_disabled</samp>](## "router_l2_vpn.nd_rs_flooding_disabled") | Boolean |  |  |  | ND RS Flooding Disabled |
| [<samp>&nbsp;&nbsp;virtual_router_nd_ra_flooding_disabled</samp>](## "router_l2_vpn.virtual_router_nd_ra_flooding_disabled") | Boolean |  |  |  | Virtual Router ND RA Flooding Disabled |
| [<samp>&nbsp;&nbsp;arp_selective_install</samp>](## "router_l2_vpn.arp_selective_install") | Boolean |  |  |  | ARP Selective Install |
| [<samp>&nbsp;&nbsp;arp_proxy</samp>](## "router_l2_vpn.arp_proxy") | Dictionary |  |  |  | ARP Proxy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.arp_proxy.prefix_list") | String |  |  |  | Prefix-list Name |

### YAML

```yaml
router_l2_vpn:
  nd_rs_flooding_disabled: <bool>
  virtual_router_nd_ra_flooding_disabled: <bool>
  arp_selective_install: <bool>
  arp_proxy:
    prefix_list: <str>
```

## Routing PIM Sparse Mode

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_pim_sparse_mode</samp>](## "router_pim_sparse_mode") | Dictionary |  |  |  | Routing PIM Sparse Mode |
| [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.ipv4") | Dictionary |  |  |  | IPv4 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssm_range</samp>](## "router_pim_sparse_mode.ipv4.ssm_range") | String |  |  |  | IPv4 Prefix associated with SSM |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses") | List, items: Dictionary |  |  |  | RP Addresses |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].address") | String | Required, Unique |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;anycast_rps</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps") | List, items: Dictionary |  |  |  | Anycast RPs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].address") | String | Required, Unique |  |  | Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_anycast_rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses") | List, items: Dictionary |  |  |  | Other Anycast RP Addresses |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].address") | String | Required, Unique |  |  | Other Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register_count</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].register_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_pim_sparse_mode.vrfs") | List, items: Dictionary |  |  |  | VRFs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_pim_sparse_mode.vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses") | List, items: Dictionary |  |  |  | RP Addresses |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].address") | String |  |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
router_pim_sparse_mode:
  ipv4:
    ssm_range: <str>
    rp_addresses:
      - address: <str>
        groups:
          - <str>
    anycast_rps:
      - address: <str>
        other_anycast_rp_addresses:
          - address: <str>
            register_count: <int>
  vrfs:
    - name: <str>
      ipv4:
        rp_addresses:
          - address: <str>
            groups:
              - <str>
```

## Service Routing Protocols Model

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>service_routing_protocols_model</samp>](## "service_routing_protocols_model") | String |  |  | Valid Values:<br>- multi-agent<br>- ribd |  |

### YAML

```yaml
service_routing_protocols_model: <str>
```

## Sflow

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>sflow</samp>](## "sflow") | Dictionary |  |  |  | Sflow |
| [<samp>&nbsp;&nbsp;sample</samp>](## "sflow.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;dangerous</samp>](## "sflow.dangerous") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "sflow.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.vrfs.[].name") | String |  |  |  | VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "sflow.vrfs.[].destinations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.vrfs.[].destinations.[].destination") | String |  |  |  | Sflow Destination IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.vrfs.[].destinations.[].port") | Integer |  |  |  | Port Number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "sflow.vrfs.[].source_interface") | String |  |  |  | Source Interface |
| [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow.destinations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.destinations.[].destination") | String |  |  |  | Sflow Destination IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.destinations.[].port") | Integer |  |  |  | Port Number |
| [<samp>&nbsp;&nbsp;source_interface</samp>](## "sflow.source_interface") | String |  |  |  | Source Interface |
| [<samp>&nbsp;&nbsp;interface</samp>](## "sflow.interface") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disable</samp>](## "sflow.interface.disable") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "sflow.interface.disable.default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;run</samp>](## "sflow.run") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;hardware_acceleration</samp>](## "sflow.hardware_acceleration") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "sflow.hardware_acceleration.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;modules</samp>](## "sflow.hardware_acceleration.modules") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.hardware_acceleration.modules.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.modules.[].enabled") | Boolean |  | True |  |  |

### YAML

```yaml
sflow:
  sample: <int>
  dangerous: <bool>
  vrfs:
    - name: <str>
      destinations:
        - destination: <str>
          port: <int>
      source_interface: <str>
  destinations:
    - destination: <str>
      port: <int>
  source_interface: <str>
  interface:
    disable:
      default: <bool>
  run: <bool>
  hardware_acceleration:
    enabled: <bool>
    sample: <int>
    modules:
      - name: <str>
        enabled: <bool>
```

## Spanning Tree

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>spanning_tree</samp>](## "spanning_tree") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;root_super</samp>](## "spanning_tree.root_super") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;edge_port</samp>](## "spanning_tree.edge_port") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpdufilter_default</samp>](## "spanning_tree.edge_port.bpdufilter_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard_default</samp>](## "spanning_tree.edge_port.bpduguard_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "spanning_tree.mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;bpduguard_rate_limit</samp>](## "spanning_tree.bpduguard_rate_limit") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "spanning_tree.bpduguard_rate_limit.default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "spanning_tree.bpduguard_rate_limit.count") | Integer |  |  |  | Maximum number of BPDUs per timer interval |
| [<samp>&nbsp;&nbsp;rstp_priority</samp>](## "spanning_tree.rstp_priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;mst</samp>](## "spanning_tree.mst") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvst_border</samp>](## "spanning_tree.mst.pvst_border") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;configuration</samp>](## "spanning_tree.mst.configuration") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "spanning_tree.mst.configuration.name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revision</samp>](## "spanning_tree.mst.configuration.revision") | Integer |  |  |  | 0-65535 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;instances</samp>](## "spanning_tree.mst.configuration.instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst.configuration.instances.[].id") | Integer |  |  |  | Instance ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "spanning_tree.mst.configuration.instances.[].vlans") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18<br> |
| [<samp>&nbsp;&nbsp;mst_instances</samp>](## "spanning_tree.mst_instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst_instances.[].id") | String |  |  |  | Instance ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.mst_instances.[].priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;no_spanning_tree_vlan</samp>](## "spanning_tree.no_spanning_tree_vlan") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
| [<samp>&nbsp;&nbsp;rapid_pvst_instances</samp>](## "spanning_tree.rapid_pvst_instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.rapid_pvst_instances.[].id") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.rapid_pvst_instances.[].priority") | Integer |  |  |  |  |

### YAML

```yaml
spanning_tree:
  root_super: <bool>
  edge_port:
    bpdufilter_default: <bool>
    bpduguard_default: <bool>
  mode: <str>
  bpduguard_rate_limit:
    default: <bool>
    count: <int>
  rstp_priority: <int>
  mst:
    pvst_border: <bool>
    configuration:
      name: <str>
      revision: <int>
      instances:
        - id: <int>
          vlans: <str>
  mst_instances:
    - id: <str>
      priority: <int>
  no_spanning_tree_vlan: <str>
  rapid_pvst_instances:
    - id: <str>
      priority: <int>
```

## Standard Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>standard_access_lists</samp>](## "standard_access_lists") | List, items: Dictionary |  |  |  | Standard Access-Lists |
| [<samp>&nbsp;&nbsp;- name</samp>](## "standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "standard_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
standard_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Static Routes

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>static_routes</samp>](## "static_routes") | List, items: Dictionary |  |  |  | Static Routes |
| [<samp>&nbsp;&nbsp;- vrf</samp>](## "static_routes.[].vrf") | String |  |  |  | VRF Name<br>If vrf_name = default the route will be placed in the GRT |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_network/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "static_routes.[].gateway") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "static_routes.[].name") | String |  |  |  | Description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

### YAML

```yaml
static_routes:
  - vrf: <str>
    destination_address_prefix: <str>
    interface: <str>
    gateway: <str>
    distance: <int>
    tag: <int>
    name: <str>
    metric: <int>
```

## Switchport Default

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>switchport_default</samp>](## "switchport_default") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "switchport_default.mode") | String |  |  | Valid Values:<br>- routed<br>- access |  |
| [<samp>&nbsp;&nbsp;phone</samp>](## "switchport_default.phone") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "switchport_default.phone.cos") | Integer |  |  | Min: 0<br>Max: 7 | COS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "switchport_default.phone.trunk") | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "switchport_default.phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID |

### YAML

```yaml
switchport_default:
  mode: <str>
  phone:
    cos: <int>
    trunk: <str>
    vlan: <int>
```

## Hardware TCAM Profiles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>tcam_profile</samp>](## "tcam_profile") | Dictionary |  |  |  | Hardware TCAM Profiles |
| [<samp>&nbsp;&nbsp;system</samp>](## "tcam_profile.system") | String |  |  |  | TCAM profile name to activate<br> |
| [<samp>&nbsp;&nbsp;profiles</samp>](## "tcam_profile.profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "tcam_profile.profiles.[].name") | String | Required, Unique |  |  | Tcam-Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config</samp>](## "tcam_profile.profiles.[].config") | String | Required |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{lookup('file', '{{ root_dir }}/inventory/TCAM_TRAFFIC_POLICY.conf')}}" |

### YAML

```yaml
tcam_profile:
  system: <str>
  profiles:
    - name: <str>
      config: <str>
```

## Trackers

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>trackers</samp>](## "trackers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "trackers.[].name") | String | Required, Unique |  |  | Name of tracker object |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "trackers.[].interface") | String | Required |  |  | Name of tracked interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp>](## "trackers.[].tracked_property") | String |  | line-protocol |  | Property to track |

### YAML

```yaml
trackers:
  - name: <str>
    interface: <str>
    tracked_property: <str>
```

## Virtual Source NAT

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>virtual_source_nat_vrfs</samp>](## "virtual_source_nat_vrfs") | List, items: Dictionary |  |  |  | Virtual Source NAT |
| [<samp>&nbsp;&nbsp;- name</samp>](## "virtual_source_nat_vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "virtual_source_nat_vrfs.[].ip_address") | String |  |  |  | IPv4 Address |

### YAML

```yaml
virtual_source_nat_vrfs:
  - name: <str>
    ip_address: <str>
```

## Internal VLAN Order

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlan_internal_order</samp>](## "vlan_internal_order") | Dictionary |  |  |  | Internal VLAN Order |
| [<samp>&nbsp;&nbsp;allocation</samp>](## "vlan_internal_order.allocation") | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
| [<samp>&nbsp;&nbsp;range</samp>](## "vlan_internal_order.range") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "vlan_internal_order.range.beginning") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "vlan_internal_order.range.ending") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |

### YAML

```yaml
vlan_internal_order:
  allocation: <str>
  range:
    beginning: <int>
    ending: <int>
```

## VLANs

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlans</samp>](## "vlans") | List, items: Dictionary |  |  |  | VLANs |
| [<samp>&nbsp;&nbsp;- id</samp>](## "vlans.[].id") | Integer |  |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "vlans.[].name") | String |  |  |  | VLAN Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;state</samp>](## "vlans.[].state") | String |  |  | Valid Values:<br>- active<br>- suspend |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "vlans.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk Group Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "vlans.[].private_vlan") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlans.[].private_vlan.type") | String |  |  | Valid Values:<br>- community<br>- isolated |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_vlan</samp>](## "vlans.[].private_vlan.primary_vlan") | Integer |  |  |  | Primary VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

### YAML

```yaml
vlans:
  - id: <int>
    name: <str>
    state: <str>
    trunk_groups:
      - <str>
    private_vlan:
      type: <str>
      primary_vlan: <int>
    tenant: <str>
```

## VM Tracer Sessions

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vmtracer_sessions</samp>](## "vmtracer_sessions") | List, items: Dictionary |  |  |  | VM Tracer Sessions |
| [<samp>&nbsp;&nbsp;- name</samp>](## "vmtracer_sessions.[].name") | String | Required, Unique |  |  | Vmtracer Session Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "vmtracer_sessions.[].url") | String |  |  |  | URL |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "vmtracer_sessions.[].username") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "vmtracer_sessions.[].password") | String |  |  |  | Type 7 Password Hash |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;autovlan_disable</samp>](## "vmtracer_sessions.[].autovlan_disable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vmtracer_sessions.[].source_interface") | String |  |  |  |  |

### YAML

```yaml
vmtracer_sessions:
  - name: <str>
    url: <str>
    username: <str>
    password: <str>
    autovlan_disable: <bool>
    source_interface: <str>
```
