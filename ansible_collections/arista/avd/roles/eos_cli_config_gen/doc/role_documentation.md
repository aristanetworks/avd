# arista.avd.eos_cli_config_gen

## Data Model

### IP Extended Access-Lists

```yaml
access_lists:
  # Access-List Name | Required
- name: <str (unique)>
  # List of ACL Lines | Required
  sequence_numbers:
    # Sequence ID | Required
  - sequence: <int (unique)>
    # Action as string | Required
    action: <str>
```
