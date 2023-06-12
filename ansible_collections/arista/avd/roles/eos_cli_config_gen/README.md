# eos_cli_config_gen

## Overview

**eos_cli_config_gen**, is a role that generates eos cli syntax and device documentation.

The **eos_cli_config_gen** role:

- Designed to generate the intended configuration offline, without relying on switch current state information.
- Facilitates the evaluation of the configuration prior to deployment with tools like [Batfish](https://www.batfish.org/)
- Facilitates the evaluation of the configuration post deployment with [eos_validate_state](../eos_validate_state) role.

## Role Inputs and Outputs

Figure 1 below provides a visualization of the roles inputs, and outputs and tasks in order executed by the role.

![Figure 1: Ansible Role eos_cli_config_gen](../../docs/_media/eos_cli_config_gen_dark.svg#only-dark)
![Figure 1: Ansible Role eos_cli_config_gen](../../docs/_media/eos_cli_config_gen_light.svg#only-light)

**Inputs:**

- Structured EOS configuration according to supported data models.

**Outputs:**

- EOS configuration in CLI format.
- Device Documentation in Markdown format.

**Tasks:**

1. Import device structured configuration from YAML file unless `structured_config` flag is set by `eos_designs`.
2. Generate EOS configuration in CLI format.
3. Generate Device Documentation in Markdown format.

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## Input Variables

- The input variables are documented in the [Input Variables](docs/Input Variables.md) section.
- Available features and variables may vary by platforms, refer to documentation on arista.com for specifics.
- All values are optional.

## License

Project is published under [Apache 2.0 License](../../LICENSE)
