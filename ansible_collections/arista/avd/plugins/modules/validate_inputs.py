# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
DOCUMENTATION = r"""
---
module: validate_inputs
version_added: "6.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Validate variables against AVD schemas
description: |-
  The `arista.avd.validate_inputs` module is an Ansible Action Plugin designed to validate host variables against Arista AVD schemas.

  The plugin offers the following capabilities:

  - **Templating Phase**: Resolves Ansible host variables (and optionally loads data from an external directory).
  - **Validation Phase**: Validates the templated data against the specified AVD schema (e.g., `eos_designs` or `eos_cli_config_gen`) using `pyavd-utils`.
options:
  schema_name:
    description:
      - The AVD schema to validate against.
      - If set to `eos_designs`, the plugin will validate the inputs for the entire fabric (requiring `fabric_name` to be set).
      - If set to `eos_cli_config_gen`, the plugin will validate the inputs for the hosts in the current play.
    type: str
    default: "eos_designs"
    choices: ["eos_designs", "eos_cli_config_gen"]
  template_inputs:
    description:
      - If `true`, the plugin will run the templating phase to resolve host variables.
      - If `false`, it assumes inputs are already available.
    type: bool
    default: true
  input_dir:
    description:
      - Optional path to a directory containing additional host variables files.
      - If provided, these files are loaded and overlaid onto the host variables during the templating phase.
    type: str
    required: false
  input_suffix:
    description:
      - File suffix for files located in `input_dir`.
    type: str
    default: "yml"
    choices: ["yml", "yaml", "json"]
  fail_on_validation_errors:
    description:
      - If `true`, the task will fail if any validation errors are detected.
      - If `false`, errors will be reported but the task will succeed.
    type: bool
    default: true
  batch_size:
    description:
      - The number of hosts to process in a single batch during the templating phase.
    type: int
    default: 10
"""

EXAMPLES = r"""
---
- name: Validate eos_designs inputs for the fabric
  arista.avd.validate_inputs:
    schema_name: eos_designs
    template_inputs: true
    fail_on_validation_errors: true

- name: Validate eos_cli_config_gen inputs
  arista.avd.validate_inputs:
    schema_name: eos_cli_config_gen
    input_dir: "{{ inventory_dir }}/intended/structured_configs"
    input_suffix: "yml"
    template_inputs: true
    fail_on_validation_errors: false
"""
