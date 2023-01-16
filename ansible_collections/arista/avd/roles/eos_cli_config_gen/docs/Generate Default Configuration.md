# Generate Default Configuration

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
