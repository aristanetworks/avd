---
search:
  boost: 2
---

# Monitoring

## Custom Daemons

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>daemons</samp>](## "daemons") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "daemons.[].name") | String | Required, Unique |  |  | Daemon Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "daemons.[].exec") | String | Required |  |  | command to run as a daemon<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "daemons.[].enabled") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    daemons:
      - name: <str>
        exec: <str>
        enabled: <bool>
    ```

## Daemon TerminAttr

You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
Streaming to multiple clusters both on-prem and cloud service is supported.

!!! note
    For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
    which always contain the latest recommended versions and minimum required versions per EOS release.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>daemon_terminattr</samp>](## "daemon_terminattr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision single cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
    | [<samp>&nbsp;&nbsp;clusters</samp>](## "daemon_terminattr.clusters") | List, items: Dictionary |  |  |  | Multiple CloudVision clusters<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "daemon_terminattr.clusters.[].name") | String | Required, Unique |  |  | Cluster Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.clusters.[].cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.clusters.[].cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.clusters.[].cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.clusters.[].cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key<br>- certs |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.clusters.[].cvauth.key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.clusters.[].cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cert_file</samp>](## "daemon_terminattr.clusters.[].cvauth.cert_file") | String |  |  |  | Client certificate file path<br>e.g. "/persist/secure/ssl/terminattr/primary/certs/client.crt"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ca_file</samp>](## "daemon_terminattr.clusters.[].cvauth.ca_file") | String |  |  |  | CA certificate file path (on-prem only)<br>e.g. "/persist/secure/ssl/terminattr/primary/certs/ca.crt"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_file</samp>](## "daemon_terminattr.clusters.[].cvauth.key_file") | String |  |  |  | Client certificate key file path<br>e.g. "/persist/secure/ssl/terminattr/primary/keys/client.key"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.clusters.[].cvobscurekeyfile") | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.clusters.[].cvproxy") | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: `http://arista:arista@10.83.12.78:3128`. Available as of TerminAttr v1.13.0<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.clusters.[].cvsourceip") | String |  |  |  | Set source IP address in case of in-band managament<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvsourceintf</samp>](## "daemon_terminattr.clusters.[].cvsourceintf") | String |  |  |  | Set source interface in case of in-band managament. Available as of TerminAttr v1.23.0<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.clusters.[].cvvrf") | String |  |  |  | The VRF to use to connect to CloudVision<br> |
    | [<samp>&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key<br>- certs |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.cvauth.key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cert_file</samp>](## "daemon_terminattr.cvauth.cert_file") | String |  |  |  | Client certificate file path<br>e.g. "/persist/secure/ssl/terminattr/primary/certs/client.crt"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ca_file</samp>](## "daemon_terminattr.cvauth.ca_file") | String |  |  |  | CA certificate file path (on-prem only)<br>e.g. "/persist/secure/ssl/terminattr/primary/certs/ca.crt"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_file</samp>](## "daemon_terminattr.cvauth.key_file") | String |  |  |  | Client certificate key file path<br>e.g. "/persist/secure/ssl/terminattr/primary/keys/client.key"<br> |
    | [<samp>&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.cvobscurekeyfile") | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
    | [<samp>&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.cvproxy") | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: `http://arista:arista@10.83.12.78:3128`. Available as of TerminAttr v1.13.0<br> |
    | [<samp>&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.cvsourceip") | String |  |  |  | Set source IP address in case of in-band managament<br> |
    | [<samp>&nbsp;&nbsp;cvsourceintf</samp>](## "daemon_terminattr.cvsourceintf") | String |  |  |  | Set source interface in case of in-band managament<br> |
    | [<samp>&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.cvvrf") | String |  |  |  | The VRF to use to connect to CloudVision<br> |
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
    | [<samp>&nbsp;&nbsp;cvconfig</samp>](## "daemon_terminattr.cvconfig") | Boolean |  |  |  | Subscribe to dynamic device configuration from CloudVision (TerminAttr default is false).<br> |
    | [<samp>&nbsp;&nbsp;cvcompression</samp>](## "daemon_terminattr.cvcompression") | String |  |  |  | The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.<br>There is no need to change the compression scheme.<br> |
    | [<samp>&nbsp;&nbsp;ingestauth_key</samp>](## "daemon_terminattr.ingestauth_key") | String |  |  |  | Deprecated key. Use `cvauth` instead.<br> |
    | [<samp>&nbsp;&nbsp;ingestgrpcurl</samp>](## "daemon_terminattr.ingestgrpcurl") | Dictionary |  |  |  | Deprecated key. Use `cvaddrs` instead.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ips</samp>](## "daemon_terminattr.ingestgrpcurl.ips") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.ingestgrpcurl.ips.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "daemon_terminattr.ingestgrpcurl.port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ingestvrf</samp>](## "daemon_terminattr.ingestvrf") | String |  |  |  | Deprecated key. Use `cvvrf` instead.<br> |

=== "YAML"

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
            cert_file: <str>
            ca_file: <str>
            key_file: <str>
          cvobscurekeyfile: <bool>
          cvproxy: <str>
          cvsourceip: <str>
          cvsourceintf: <str>
          cvvrf: <str>
      cvauth:
        method: <str>
        key: <str>
        token_file: <str>
        cert_file: <str>
        ca_file: <str>
        key_file: <str>
      cvobscurekeyfile: <bool>
      cvproxy: <str>
      cvsourceip: <str>
      cvsourceintf: <str>
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
      cvconfig: <bool>
      cvcompression: <str>
      ingestauth_key: <str>
      ingestgrpcurl:
        ips:
          - <str>
        port: <int>
      ingestvrf: <str>
    ```

## Event Handlers

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging<br>- on-startup-config | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |

=== "YAML"

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_monitor</samp>](## "event_monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "event_monitor.enabled") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    event_monitor:
      enabled: <bool>
    ```

## Load Interval

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>load_interval</samp>](## "load_interval") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;default</samp>](## "load_interval.default") | Integer |  |  |  | Default load interval in seconds |

=== "YAML"

    ```yaml
    load_interval:
      default: <int>
    ```

## Logging

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>logging</samp>](## "logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;console</samp>](## "logging.console") | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Console logging severity level<br> |
    | [<samp>&nbsp;&nbsp;monitor</samp>](## "logging.monitor") | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Monitor logging severity level<br> |
    | [<samp>&nbsp;&nbsp;buffered</samp>](## "logging.buffered") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "logging.buffered.size") | Integer |  |  | Min: 10<br>Max: 2147483647 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.buffered.level") | String |  |  | Valid Values:<br>- alerts<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- warnings<br>- disabled | Buffer logging severity level<br> |
    | [<samp>&nbsp;&nbsp;trap</samp>](## "logging.trap") | String |  |  | Valid Values:<br>- alerts<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- system<br>- warnings<br>- disabled | Trap logging severity level<br> |
    | [<samp>&nbsp;&nbsp;synchronous</samp>](## "logging.synchronous") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.synchronous.level") | String |  | critical | Valid Values:<br>- alerts<br>- all<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- warnings<br>- disabled | Synchronous logging severity level<br> |
    | [<samp>&nbsp;&nbsp;format</samp>](## "logging.format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "logging.format.timestamp") | String |  |  | Valid Values:<br>- high-resolution<br>- traditional<br>- traditional timezone<br>- traditional year<br>- traditional timezone year<br>- traditional year timezone | Timestamp format |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "logging.format.hostname") | String |  |  | Valid Values:<br>- fqdn<br>- ipv4 | Hostname format |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "logging.format.sequence_numbers") | Boolean |  |  |  | Add sequence numbers to log messages<br> |
    | [<samp>&nbsp;&nbsp;facility</samp>](## "logging.facility") | String |  |  | Valid Values:<br>- auth<br>- cron<br>- daemon<br>- kern<br>- local0<br>- local1<br>- local2<br>- local3<br>- local4<br>- local5<br>- local6<br>- local7<br>- lpr<br>- mail<br>- news<br>- sys9<br>- sys10<br>- sys11<br>- sys12<br>- sys13<br>- sys14<br>- syslog<br>- user<br>- uucp |  |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "logging.source_interface") | String |  |  |  | Source Interface Name |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "logging.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "logging.vrfs.[].source_interface") | String |  |  |  | Source interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "logging.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Syslog server name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "logging.vrfs.[].hosts.[].protocol") | String |  | udp | Valid Values:<br>- tcp<br>- udp |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "logging.vrfs.[].hosts.[].ports") | List, items: Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "logging.vrfs.[].hosts.[].ports.[].&lt;int&gt;") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy</samp>](## "logging.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "logging.policy.match") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_lists</samp>](## "logging.policy.match.match_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.policy.match.match_lists.[].name") | String | Required, Unique |  |  | Match list |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "logging.policy.match.match_lists.[].action") | String |  |  | Valid Values:<br>- discard |  |

=== "YAML"

    ```yaml
    logging:
      console: <str>
      monitor: <str>
      buffered:
        size: <int>
        level: <str>
      trap: <str>
      synchronous:
        level: <str>
      format:
        timestamp: <str>
        hostname: <str>
        sequence_numbers: <bool>
      facility: <str>
      source_interface: <str>
      vrfs:
        - name: <str>
          source_interface: <str>
          hosts:
            - name: <str>
              protocol: <str>
              ports:
                - <int>
      policy:
        match:
          match_lists:
            - name: <str>
              action: <str>
    ```

## Monitor Connectivity

=== "Table"

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

=== "YAML"

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

=== "Table"

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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "monitor_sessions.[].encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
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

=== "YAML"

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

## Sflow

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>sflow</samp>](## "sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample</samp>](## "sflow.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dangerous</samp>](## "sflow.dangerous") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;polling_interval</samp>](## "sflow.polling_interval") | Integer |  |  |  | Polling interval in seconds |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "sflow.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "sflow.vrfs.[].destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.vrfs.[].destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.vrfs.[].destinations.[].port") | Integer |  |  |  | Port Number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "sflow.vrfs.[].source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "sflow.vrfs.[].source_interface") | String |  |  |  | Source Interface |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow.destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.destinations.[].port") | Integer |  |  |  | Port Number |
    | [<samp>&nbsp;&nbsp;source</samp>](## "sflow.source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "sflow.source_interface") | String |  |  |  | Source Interface |
    | [<samp>&nbsp;&nbsp;extensions</samp>](## "sflow.extensions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.extensions.[].name") | String | Required, Unique |  |  | Extension Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.extensions.[].enabled") | Boolean | Required |  |  | Enable or Disable Extension |
    | [<samp>&nbsp;&nbsp;interface</samp>](## "sflow.interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disable</samp>](## "sflow.interface.disable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "sflow.interface.disable.default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;run</samp>](## "sflow.run") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hardware_acceleration</samp>](## "sflow.hardware_acceleration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "sflow.hardware_acceleration.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;modules</samp>](## "sflow.hardware_acceleration.modules") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.hardware_acceleration.modules.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.modules.[].enabled") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    sflow:
      sample: <int>
      dangerous: <bool>
      polling_interval: <int>
      vrfs:
        - name: <str>
          destinations:
            - destination: <str>
              port: <int>
          source: <str>
          source_interface: <str>
      destinations:
        - destination: <str>
          port: <int>
      source: <str>
      source_interface: <str>
      extensions:
        - name: <str>
          enabled: <bool>
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

## Snmp Server

SNMP settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_server</samp>](## "snmp_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;engine_ids</samp>](## "snmp_server.engine_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "snmp_server.engine_ids.local") | String |  |  |  | Engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp>](## "snmp_server.engine_ids.remotes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "snmp_server.engine_ids.remotes.[].id") | String |  |  |  | Remote engine ID in hexadecimal<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "snmp_server.engine_ids.remotes.[].address") | String |  |  |  | Hostname or IP of remote engine<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.engine_ids.remotes.[].udp_port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_server.contact") | String |  |  |  | SNMP contact |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_server.location") | String |  |  |  | SNMP location |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_server.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.communities.[].name") | String | Required, Unique |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_server.communities.[].access") | String |  |  | Valid Values:<br>- ro<br>- rw |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_server.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_server.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_server.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_server.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_server.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "snmp_server.local_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.local_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.local_interfaces.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_server.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.views.[].name") | String |  |  |  | SNMP view name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_server.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_server.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_server.views.[].MIB_family_name") <span style="color:red">deprecated</span> | String |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>mib_family_name</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_server.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.groups.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_server.groups.[].authentication") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_server.groups.[].read") | String |  |  |  | Read view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_server.groups.[].write") | String |  |  |  | Write view |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_server.groups.[].notify") | String |  |  |  | Notify view |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_server.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_server.users.[].group") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp>](## "snmp_server.users.[].remote_address") | String |  |  |  | Hostname or ip of remote engine<br>The remote_address and udp_port are used for remote users<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.users.[].udp_port") | Integer |  |  |  | udp_port will not be used if no remote_address is configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp>](## "snmp_server.users.[].localized") | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_server.users.[].auth") | String |  |  |  | Hash algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_server.users.[].auth_passphrase") | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_server.users.[].priv") | String |  |  |  | Encryption algorithm<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_server.users.[].priv_passphrase") | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase<br> |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_server.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "snmp_server.hosts.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.hosts.[].version") | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_server.hosts.[].community") | String |  |  |  | Community name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_server.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp>](## "snmp_server.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_server.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_server.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.traps.enable") | Boolean |  | False |  | Enable or disable all snmp-traps<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_server.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_server.traps.snmp_traps.[].enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_server.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.vrfs.[].name") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.vrfs.[].enable") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    snmp_server:
      engine_ids:
        local: <str>
        remotes:
          - id: <str>
            address: <str>
            udp_port: <int>
      contact: <str>
      location: <str>
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
      local_interfaces:
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
      users:
        - name: <str>
          group: <str>
          remote_address: <str>
          udp_port: <int>
          version: <str>
          localized: <str>
          auth: <str>
          auth_passphrase: <str>
          priv: <str>
          priv_passphrase: <str>
      hosts:
        - host: <str>
          vrf: <str>
          version: <str>
          community: <str>
          users:
            - username: <str>
              authentication_level: <str>
      traps:
        enable: <bool>
        snmp_traps:
          - name: <str>
            enabled: <bool>
      vrfs:
        - name: <str>
          enable: <bool>
    ```

## Tap Aggregation

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tap_aggregation</samp>](## "tap_aggregation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "tap_aggregation.mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclusive</samp>](## "tap_aggregation.mode.exclusive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "tap_aggregation.mode.exclusive.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tap_aggregation.mode.exclusive.profile") | String |  |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_errdisable</samp>](## "tap_aggregation.mode.exclusive.no_errdisable") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "tap_aggregation.mode.exclusive.no_errdisable.[].&lt;str&gt;") | String |  |  |  | Interface name e.g Ethernet1, Port-Channel1 |
    | [<samp>&nbsp;&nbsp;encapsulation_dot1br_strip</samp>](## "tap_aggregation.encapsulation_dot1br_strip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;encapsulation_vn_tag_strip</samp>](## "tap_aggregation.encapsulation_vn_tag_strip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_lldp_trap</samp>](## "tap_aggregation.protocol_lldp_trap") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;truncation_size</samp>](## "tap_aggregation.truncation_size") | Integer |  |  |  | Allowed truncation_size values vary depending on the platform<br> |
    | [<samp>&nbsp;&nbsp;mac</samp>](## "tap_aggregation.mac") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "tap_aggregation.mac.timestamp") | Dictionary |  |  |  | mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined, replace_source_mac takes precedence<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_source_mac</samp>](## "tap_aggregation.mac.timestamp.replace_source_mac") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "tap_aggregation.mac.timestamp.header") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "tap_aggregation.mac.timestamp.header.format") | String |  |  | Valid Values:<br>- 48-bit<br>- 64-bit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eth_type</samp>](## "tap_aggregation.mac.timestamp.header.eth_type") | Integer |  |  |  | EtherType |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_append</samp>](## "tap_aggregation.mac.fcs_append") | Boolean |  |  |  | mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_error</samp>](## "tap_aggregation.mac.fcs_error") | String |  |  | Valid Values:<br>- correct<br>- discard<br>- pass-through |  |

=== "YAML"

    ```yaml
    tap_aggregation:
      mode:
        exclusive:
          enabled: <bool>
          profile: <str>
          no_errdisable:
            - <str>
      encapsulation_dot1br_strip: <bool>
      encapsulation_vn_tag_strip: <bool>
      protocol_lldp_trap: <bool>
      truncation_size: <int>
      mac:
        timestamp:
          replace_source_mac: <bool>
          header:
            format: <str>
            eth_type: <int>
        fcs_append: <bool>
        fcs_error: <str>
    ```

## Trackers

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>trackers</samp>](## "trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "trackers.[].name") | String | Required, Unique |  |  | Name of tracker object |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "trackers.[].interface") | String | Required |  |  | Name of tracked interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp>](## "trackers.[].tracked_property") | String |  | line-protocol |  | Property to track |

=== "YAML"

    ```yaml
    trackers:
      - name: <str>
        interface: <str>
        tracked_property: <str>
    ```
