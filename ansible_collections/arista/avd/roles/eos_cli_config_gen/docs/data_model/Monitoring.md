---
search:
  boost: 2
---

# Monitoring
## Daemon TerminAttr

=== "Daemon TerminAttr"

    You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
    Streaming to multiple clusters both on-prem and cloud service is supported.
    > Note For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
      which always contain the latest recommended versions and minimum required versions per EOS release.


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>daemon_terminattr</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;cvaddrs</samp> | List, items: String |  |  |  | Streaming address(es) for CloudVision single cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
    | <samp>&nbsp;&nbsp;clusters</samp> | List, items: Dictionary |  |  |  | Multiple CloudVision clusters<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Cluster Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvaddrs</samp> | List, items: String |  |  |  | Streaming address(es) for CloudVision cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvauth</samp> | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp> | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp> | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvobscurekeyfile</samp> | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvproxy</samp> | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvsourceip</samp> | String |  |  |  | Set source IP address in case of in-band managament<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvvrf</samp> | String |  |  |  | The VRF to use to connect to CloudVision<br> |
    | <samp>&nbsp;&nbsp;cvauth</samp> | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp> | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp> | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
    | <samp>&nbsp;&nbsp;cvobscurekeyfile</samp> | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
    | <samp>&nbsp;&nbsp;cvproxy</samp> | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
    | <samp>&nbsp;&nbsp;cvsourceip</samp> | String |  |  |  | Set source IP address in case of in-band managament<br> |
    | <samp>&nbsp;&nbsp;cvvrf</samp> | String |  |  |  | The VRF to use to connect to CloudVision<br> |
    | <samp>&nbsp;&nbsp;cvgnmi</samp> | Boolean |  |  |  | Stream states from EOS GNMI servers (Openconfig) to CloudVision. Available as of TerminAttr v1.13.1<br> |
    | <samp>&nbsp;&nbsp;disable_aaa</samp> | Boolean |  |  |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization<br> |
    | <samp>&nbsp;&nbsp;grpcaddr</samp> | String |  |  |  | Set the gRPC server address, the default is 127.0.0.1:6042<br>e.g. "MGMT/0.0.0.0:6042"<br> |
    | <samp>&nbsp;&nbsp;grpcreadonly</samp> | Boolean |  |  |  | gNMI read-only mode - Disable gnmi.Set()<br> |
    | <samp>&nbsp;&nbsp;ingestexclude</samp> | String |  |  |  | Exclude paths from Sysdb on the ingest side.<br>e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"<br> |
    | <samp>&nbsp;&nbsp;smashexcludes</samp> | String |  |  |  | Exclude paths from the shared memory table.<br>e.g. "ale,flexCounter,hardware,kni,pulse,strata"<br> |
    | <samp>&nbsp;&nbsp;taillogs</samp> | String |  |  |  | Enable log file collection; /var/log/messages is streamed by default if no path is set.<br>e.g. "/var/log/messages"<br> |
    | <samp>&nbsp;&nbsp;ecodhcpaddr</samp> | String |  |  |  | ECO DHCP Collector address or ECO DHCP Fingerprint listening address in standalone mode (default "127.0.0.1:67")<br> |
    | <samp>&nbsp;&nbsp;ipfix</samp> | Boolean |  |  |  | Enable IPFIX provider (TerminAttr default is true).<br>This flag is enabled by default and does not have to be added to the daemon configuration.<br> |
    | <samp>&nbsp;&nbsp;ipfixaddr</samp> | String |  |  |  | ECO IPFIX Collector address to listen on to receive IPFIX packets (TerminAttr default "127.0.0.1:4739").<br> |
    | <samp>&nbsp;&nbsp;sflow</samp> | Boolean |  |  |  | Enable sFlow provider (TerminAttr default is true).<br> |
    | <samp>&nbsp;&nbsp;sflowaddr</samp> | String |  |  |  | ECO sFlow Collector address to listen on to receive sFlow packets (TerminAttr default "127.0.0.1:6343").<br> |
    | <samp>&nbsp;&nbsp;cvconfig</samp> | Boolean |  |  |  | Subscribe to dynamic device configuration from CloudVision (TerminAttr default is false).<br> |
    | <samp>&nbsp;&nbsp;cvcompression</samp> | String |  |  |  | The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.<br>There is no need to change the compression scheme.<br> |
    | <samp>&nbsp;&nbsp;ingestauth_key</samp> | String |  |  |  | Deprecated key. Use `cvauth` instead.<br> |
    | <samp>&nbsp;&nbsp;ingestgrpcurl</samp> | Dictionary |  |  |  | Deprecated key. Use `cvaddrs` instead.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ips</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;ingestvrf</samp> | String |  |  |  | Deprecated key. Use `cvvrf` instead.<br> |

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
      cvconfig: <bool>
      cvcompression: <str>
      ingestauth_key: <str>
      ingestgrpcurl:
        ips:
          - <str>
        port: <int>
      ingestvrf: <str>
    ```
## Custom Daemons

=== "Custom Daemons"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>daemons</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Daemon Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp> | String | Required |  |  | command to run as a daemon<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    daemons:
      - name: <str>
        exec: <str>
        enabled: <bool>
    ```
## Event Handlers

=== "Event Handlers"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>event_handlers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Event Handler Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp> | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  |  | Command to execute<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp> | Integer |  |  |  | Event-handler delay in seconds<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp> | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp> | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp> | Boolean |  | False |  | Set the action to be non-blocking. |

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

=== "Event Monitor"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>event_monitor</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    event_monitor:
      enabled: <bool>
    ```
## Load Interval

=== "Load Interval"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>load_interval</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;default</samp> | Integer |  |  |  | Default load interval in seconds |

=== "YAML"

    ```yaml
    load_interval:
      default: <int>
    ```
## Logging

=== "Logging"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>logging</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;console</samp> | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Console logging severity level<br> |
    | <samp>&nbsp;&nbsp;monitor</samp> | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Monitor logging severity level<br> |
    | <samp>&nbsp;&nbsp;buffered</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp> | Integer |  |  | Min: 10<br>Max: 2147483647 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Buffer logging severity level<br> |
    | <samp>&nbsp;&nbsp;trap</samp> | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Trap logging severity level<br> |
    | <samp>&nbsp;&nbsp;synchronous</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | String |  | critical | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Synchronous logging severity level<br> |
    | <samp>&nbsp;&nbsp;format</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp> | String |  |  | Valid Values:<br>- high-resolution<br>- traditional<br>- traditional timezone<br>- traditional year<br>- traditional timezone year<br>- traditional year timezone | Timestamp format |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp> | String |  |  | Valid Values:<br>- fqdn<br>- ipv4 | Hostname format |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | Boolean |  |  |  | Add sequence numbers to log messages<br> |
    | <samp>&nbsp;&nbsp;facility</samp> | String |  |  | Valid Values:<br>- auth<br>- cron<br>- daemon<br>- kern<br>- local0<br>- local1<br>- local2<br>- local3<br>- local4<br>- local5<br>- local6<br>- local7<br>- lpr<br>- mail<br>- news<br>- sys9<br>- sys10<br>- sys11<br>- sys12<br>- sys13<br>- sys14<br>- syslog<br>- user<br>- uucp |  |
    | <samp>&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source Interface Name |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Syslog server name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp> | String |  | udp | Valid Values:<br>- tcp<br>- udp |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp> | List, items: Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;match</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Match list |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  | Valid Values:<br>- discard |  |

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

=== "Monitor Connectivity"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>monitor_connectivity</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;interface_sets</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp> | String |  |  |  | Interface range(s) should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interface ranges can be specified separated by ","<br> |
    | <samp>&nbsp;&nbsp;local_interfaces</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;hosts</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Host Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Host name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp> | String |  |  |  |  |

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

=== "Monitor Sessions"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>monitor_sessions</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required |  |  | Session Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sources</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Interface name, range or comma separated list |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | ACL Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | 'cpu' or interface name, range or comma separated list |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp> | Integer |  |  |  | Number of bytes to remove from header |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | ACL Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp> | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp> | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp> | Integer |  |  |  | Size in bytes |

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

=== "Sflow"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>sflow</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;sample</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;dangerous</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;polling_interval</samp> | Integer |  |  |  | Polling interval in seconds |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp> | String | Required, Unique |  |  | Sflow Destination IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp> | Integer |  |  |  | Port Number |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp> | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source Interface |
    | <samp>&nbsp;&nbsp;destinations</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp> | String | Required, Unique |  |  | Sflow Destination IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp> | Integer |  |  |  | Port Number |
    | <samp>&nbsp;&nbsp;source</samp> | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | <samp>&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source Interface |
    | <samp>&nbsp;&nbsp;extensions</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Extension Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean | Required |  |  | Enable or Disable Extension |
    | <samp>&nbsp;&nbsp;interface</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;disable</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;run</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;hardware_acceleration</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;modules</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  | True |  |  |

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

=== "Snmp Server"

    SNMP settings

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>snmp_server</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;engine_ids</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp> | String |  |  |  | Engine ID in hexadecimal<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String |  |  |  | Remote engine ID in hexadecimal<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp> | String |  |  |  | Hostname or IP of remote engine<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;contact</samp> | String |  |  |  | SNMP contact |
    | <samp>&nbsp;&nbsp;location</samp> | String |  |  |  | SNMP location |
    | <samp>&nbsp;&nbsp;communities</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Community name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp> | String |  |  | Valid Values:<br>- ro<br>- rw |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | IPv4 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;ipv4_acls</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | IPv4 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;ipv6_acls</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;local_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;views</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | SNMP view name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp> | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp> | String |  |  |  | Read view |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp> | String |  |  |  | Write view |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp> | String |  |  |  | Notify view |
    | <samp>&nbsp;&nbsp;users</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Username |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp> | String |  |  |  | Hostname or ip of remote engine<br>The remote_address and udp_port are used for remote users<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp> | Integer |  |  |  | udp_port will not be used if no remote_address is configured<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp> | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp> | String |  |  |  | Hash algorithm<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp> | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp> | String |  |  |  | Encryption algorithm<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp> | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase<br> |
    | <samp>&nbsp;&nbsp;hosts</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp> | String |  |  |  | Host IP address or name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp> | String |  |  |  | Community name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp> | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
    | <samp>&nbsp;&nbsp;traps</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  | False |  | Enable or disable all snmp-traps<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  | True |  |  |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |

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
          MIB_family_name: <str>
          included: <bool>
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

=== "Tap Aggregation"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>tap_aggregation</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;mode</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;exclusive</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String |  |  |  | Profile Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_errdisable</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Interface name e.g Ethernet1, Port-Channel1 |
    | <samp>&nbsp;&nbsp;encapsulation_dot1br_strip</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;encapsulation_vn_tag_strip</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;protocol_lldp_trap</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;truncation_size</samp> | Integer |  |  |  | Allowed truncation_size values vary depending on the platform<br> |
    | <samp>&nbsp;&nbsp;mac</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp> | Dictionary |  |  |  | mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined, replace_source_mac takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_source_mac</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp> | String |  |  | Valid Values:<br>- 48-bit<br>- 64-bit |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eth_type</samp> | Integer |  |  |  | EtherType |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_append</samp> | Boolean |  |  |  | mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_error</samp> | String |  |  | Valid Values:<br>- correct<br>- discard<br>- pass-through |  |

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

=== "Trackers"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>trackers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Name of tracker object |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | String | Required |  |  | Name of tracked interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp> | String |  | line-protocol |  | Property to track |

=== "YAML"

    ```yaml
    trackers:
      - name: <str>
        interface: <str>
        tracked_property: <str>
    ```
