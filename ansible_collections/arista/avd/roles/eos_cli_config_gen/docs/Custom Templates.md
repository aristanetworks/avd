# Custom Templates

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
- It is recommended to use a `!` delimiter at the top of each custom template.

Add `custom_templates` to group/host variables:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_templates.[].&lt;str&gt;") | String |  |  |  | Template relative path below playbook directory |

### YAML

```yaml
custom_templates:
  - <str>
```
