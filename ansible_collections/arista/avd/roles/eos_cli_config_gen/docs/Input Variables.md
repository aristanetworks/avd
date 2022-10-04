!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

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

## Management Console

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_console</samp>](## "management_console") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_console.idle_timeout") | Integer |  |  | Max: 86400 |  |

### YAML

```yaml
management_console:
  idle_timeout: <int>
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
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_ssh.idle_timeout") | Integer |  |  | Max: 86400 | Idle timeout in minutes |
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
