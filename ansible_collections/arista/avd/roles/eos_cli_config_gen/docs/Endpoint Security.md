# Endpoint Security

## Global 802.1x Authentication

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |

### YAML

```yaml
dot1x:
  system_auth_control: <bool>
  protocol_lldp_bypass: <bool>
  dynamic_authorization: <bool>
```
