---
search:
  boost: 2
---

# Management Settings

## Cloudvision Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  | On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.<br>If not set, TerminAttr will be configured with certificate based authentication using token-secure onboarding.<br>Token must be copied to the device first. |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  | IPv4 address.<br>CloudVision - Telemetry Agent (TerminAttr) configuration is optional<br>You can either provide a list of IPs to target on-premise CloudVision cluster or<br>use DNS name for your CloudVision as a Service instance. If you have both on-prem and<br>CVaaS defined, only on-prem is going to be configured. |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  | You can either provide a list of IPs to target on-premise CloudVision cluster or<br>use DNS name for your CloudVision as a Service instance. If you have both on-prem and<br>CVaaS defined, only on-prem is going to be configured.<br> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or CV as a Service hostname |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  | /tmp/cv-onboarding-token |  | cvp_token_file is the path to the token file on the switch. |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  | Port number for Terminattr ingest GRPC |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

=== "YAML"

    ```yaml
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
