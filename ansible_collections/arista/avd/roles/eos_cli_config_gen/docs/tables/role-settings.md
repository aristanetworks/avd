<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_structured_config_file_format</samp>](## "avd_structured_config_file_format") | String |  | `yml` | Valid Values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | The file format to use when loading structured configuration files.<br> |
    | [<samp>avd_vault_id</samp>](## "avd_vault_id") | String |  |  |  | Vault identity to use for encrypting temporary files when Ansible Vault is configured.<br><br>When Ansible Vault is configured (via `--vault-password-file`, `--vault-id`, or `vault_identity_list` in ansible.cfg),<br>AVD encrypts temporary files containing templated and validated data to prevent sensitive information<br>from being exposed in logs or temporary directories.<br><br>**Default Behavior** (when `avd_vault_id` is not specified):<br>  - If Ansible Vault is configured, AVD uses the *first* vault identity in the list for encryption.<br>  - This is the standard Ansible behavior when no vault ID is explicitly specified.<br>  - Files encrypted this way can only be decrypted with the password of the first vault identity.<br><br>**Advanced Use Case** (when `avd_vault_id` is specified):<br>  - AVD uses the specified vault identity for encryption.<br>  - This is useful when multiple vault identities are configured and you want to control which one is used.<br>  - The specified vault identity must exist in the configured vault identities.<br><br>**Examples**:<br>  - Single vault password: `avd_vault_id` is not needed, the single vault password is used automatically.<br>  - Multiple vault identities via `vault_identity_list = dev@.vault_dev, prod@.vault_prod`:<br>    - Without `avd_vault_id`: Uses 'dev' (first in list) for encryption.<br>    - With `avd_vault_id: 'prod'`: Uses 'prod' for encryption.<br>  - Multiple vault identities via `--vault-id dev@.vault_dev --vault-id prod@.vault_prod`:<br>    - Without `avd_vault_id`: Uses 'dev' (first specified) for encryption.<br>    - With `avd_vault_id: 'prod'`: Uses 'prod' for encryption.<br><br>**Note**: If Ansible Vault is not configured, this parameter has no effect and files are written as plain JSON. |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_configuration.enable") | Boolean |  | `True` |  | Generate device EOS configurations. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | `False` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.<br> |
    | [<samp>eos_cli_config_gen_documentation</samp>](## "eos_cli_config_gen_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_documentation.enable") | Boolean |  | `True` |  | Generate device Markdown documentation. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_documentation.hide_passwords") | Boolean |  | `True` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.<br> |
    | [<samp>&nbsp;&nbsp;toc</samp>](## "eos_cli_config_gen_documentation.toc") | Boolean |  | `True` |  | Generate the table of content(TOC) on device documentation. |
    | [<samp>eos_cli_config_gen_validate_inputs_batch_size</samp>](## "eos_cli_config_gen_validate_inputs_batch_size") | Integer |  | `10` |  | The number of hosts to process in each batch when validating inputs.<br>Depending on your inventory size and the available resources, you may want to adjust this number. |
    | [<samp>generate_default_config</samp>](## "generate_default_config") <span style="color:red">removed</span> | Boolean |  | `False` |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#default-eos-configuration-is-no-longer-automatically-generated) for details.</span> |
    | [<samp>generate_device_documentation</samp>](## "generate_device_documentation") <span style="color:red">removed</span> | Boolean |  | `True` |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>eos_cli_config_gen_documentation.enable</samp> instead.</span> |
    | [<samp>read_structured_config_from_file</samp>](## "read_structured_config_from_file") | Boolean |  | `True` |  | Read structured configuration from files in `structured_dir` (default directory also used by the `eos_designs` role).<br>If set to false, `eos_cli_config_gen` will read structured configuration from hostvars.<br> |

=== "YAML"

    ```yaml
    # The file format to use when loading structured configuration files.
    avd_structured_config_file_format: <str; "yml" | "yaml" | "json"; default="yml">

    # Vault identity to use for encrypting temporary files when Ansible Vault is configured.
    #
    # When Ansible Vault is configured (via `--vault-password-file`, `--vault-id`, or `vault_identity_list` in ansible.cfg),
    # AVD encrypts temporary files containing templated and validated data to prevent sensitive information
    # from being exposed in logs or temporary directories.
    #
    # **Default Behavior** (when `avd_vault_id` is not specified):
    #   - If Ansible Vault is configured, AVD uses the *first* vault identity in the list for encryption.
    #   - This is the standard Ansible behavior when no vault ID is explicitly specified.
    #   - Files encrypted this way can only be decrypted with the password of the first vault identity.
    #
    # **Advanced Use Case** (when `avd_vault_id` is specified):
    #   - AVD uses the specified vault identity for encryption.
    #   - This is useful when multiple vault identities are configured and you want to control which one is used.
    #   - The specified vault identity must exist in the configured vault identities.
    #
    # **Examples**:
    #   - Single vault password: `avd_vault_id` is not needed, the single vault password is used automatically.
    #   - Multiple vault identities via `vault_identity_list = dev@.vault_dev, prod@.vault_prod`:
    #     - Without `avd_vault_id`: Uses 'dev' (first in list) for encryption.
    #     - With `avd_vault_id: 'prod'`: Uses 'prod' for encryption.
    #   - Multiple vault identities via `--vault-id dev@.vault_dev --vault-id prod@.vault_prod`:
    #     - Without `avd_vault_id`: Uses 'dev' (first specified) for encryption.
    #     - With `avd_vault_id: 'prod'`: Uses 'prod' for encryption.
    #
    # **Note**: If Ansible Vault is not configured, this parameter has no effect and files are written as plain JSON.
    avd_vault_id: <str>
    eos_cli_config_gen_configuration:

      # Generate device EOS configurations.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.
      hide_passwords: <bool; default=False>
    eos_cli_config_gen_documentation:

      # Generate device Markdown documentation.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.
      hide_passwords: <bool; default=True>

      # Generate the table of content(TOC) on device documentation.
      toc: <bool; default=True>

    # The number of hosts to process in each batch when validating inputs.
    # Depending on your inventory size and the available resources, you may want to adjust this number.
    eos_cli_config_gen_validate_inputs_batch_size: <int; default=10>

    # Read structured configuration from files in `structured_dir` (default directory also used by the `eos_designs` role).
    # If set to false, `eos_cli_config_gen` will read structured configuration from hostvars.
    read_structured_config_from_file: <bool; default=True>
    ```
