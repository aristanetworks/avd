<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>daemon_terminattr</samp>](## "daemon_terminattr") | Dictionary |  |  |  | You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.<br>Streaming to multiple clusters both on-prem and cloud service is supported.<br><br>!!! note<br>    For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes<br>    which always contain the latest recommended versions and minimum required versions per EOS release.<br> |
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
    | [<samp>&nbsp;&nbsp;cvgnmi</samp>](## "daemon_terminattr.cvgnmi") | Boolean |  |  |  | Stream states from EOS gNMI servers (Openconfig) to CloudVision. Available as of TerminAttr v1.13.1<br> |
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
    | [<samp>&nbsp;&nbsp;cvcompression</samp>](## "daemon_terminattr.cvcompression") | String |  |  |  | The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.<br>There is no need to change the compression scheme. |

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
    ```
