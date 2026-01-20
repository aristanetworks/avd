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
  The `arista.avd.validate_inputs` module is an Ansible Action Plugin designed to validate device variables against Arista AVD schemas.

  The plugin performs two phases:

  1. **Templating Phase**: Resolves Ansible hostvars and writes them as JSON files. This phase is skipped if `input_dir` is provided
     or pre-templated files already exist in the AVD temporary directory (e.g., from `eos_designs_structured_config`).
  2. **Validation Phase**: Validates the data against the specified AVD schema using `pyavd-utils`.

  The plugin uses multiprocessing for templating (CPU-bound) and multithreading for validation (I/O-bound with GIL released by Rust).
options:
  schema_name:
    description:
      - The AVD schema to validate against.
      - If set to `eos_designs`, the plugin will validate the inputs for the entire fabric (requiring `fabric_name` to be set).
      - If set to `eos_cli_config_gen`, the plugin will validate the inputs for the devices in the current play.
    type: str
    default: "eos_designs"
    choices: ["eos_designs", "eos_cli_config_gen"]
  input_dir:
    description:
      - Optional path to a directory containing input files to validate directly.
      - If provided, the templating phase is skipped and files are read from this directory.
      - Files must be named `<device_name>.<input_suffix>`.
    type: str
    required: false
  input_suffix:
    description:
      - File suffix for files located in `input_dir`.
      - Only used when `input_dir` is provided.
    type: str
    default: "json"
    choices: ["yml", "yaml", "json"]
  fail_on_validation_errors:
    description:
      - If `true`, the task will fail if any validation errors are detected.
      - If `false`, errors will be reported but the task will succeed.
    type: bool
    default: true
  batch_size:
    description:
      - The number of devices to process per child process during the templating phase.
    type: int
    default: 10
"""

EXAMPLES = r"""
---
- name: Validate eos_designs inputs for the fabric
  arista.avd.validate_inputs:
    schema_name: eos_designs
    fail_on_validation_errors: true

- name: Validate eos_cli_config_gen inputs from structured config files
  arista.avd.validate_inputs:
    schema_name: eos_cli_config_gen
    input_dir: "{{ inventory_dir }}/intended/structured_configs"
    input_suffix: "yml"
    fail_on_validation_errors: false
"""
