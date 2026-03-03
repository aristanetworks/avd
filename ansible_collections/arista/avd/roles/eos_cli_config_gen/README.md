---
# This title is used for search results
title: Ansible Collection Role eos_cli_config_gen
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_cli_config_gen

## Overview

**eos_cli_config_gen**, is a role that generates EOS CLI configuration and device documentation.

The **eos_cli_config_gen** role:

- Designed to generate the intended configuration offline, without relying on switch current state information.
- Facilitates the evaluation of the configuration post deployment with [anta_runner](../anta_runner/README.md) role.

## Role Inputs and Outputs

Figure 1 below provides a visualization of the roles inputs, and outputs and tasks in order executed by the role.

![Figure 1: Ansible Role eos_cli_config_gen](../../../../../docs/_media/excalidraw/exported/eos_cli_config_gen_dark.svg#only-dark)
![Figure 1: Ansible Role eos_cli_config_gen](../../../../../docs/_media/excalidraw/exported/eos_cli_config_gen_light.svg#only-light)

**Inputs:**

- [EOS Config](./docs/data-models.md) inputs according to supported data models.

**Outputs:**

- EOS configuration in CLI format.
- Device documentation in Markdown format.

**Tasks:**

1. Load and validate input variables according to the EOS Config schema.
2. Generate EOS configuration in CLI format.
3. Generate device documentation in Markdown format.

## Requirements

Requirements are located in the [collection installation guide](../../../../../docs/installation/collection-installation.md)

## Data models

The data models are documented in the [EOS Config data models](docs/data-models.md) section.

## Role Configuration

The role configuration variables are documented in the [Role Configuration](docs/role-configuration.md) section.

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## License

Project is published under [Apache 2.0 License](https://github.com/aristanetworks/avd/blob/devel/LICENSE)
