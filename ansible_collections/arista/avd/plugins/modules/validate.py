# Copyright 2022 Arista Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DOCUMENTATION = r"""
---
module: validate
version_added: "3.7.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Validate input data according to Schema
description:
  - The `arista.avd.validate` Action Plugin validates the input variables according to the supplied Schema
  - This is used in `arista.avd.eos_designs` and `arista.avd.eos_cli_config_gen`.
  - The Action Plugin supports different modes, to either block the playbook or just warn the user.
options:
  schema:
    description: Schema conforming to "AVD Meta Schema"
    required: True
    type: dict
  conversion_mode:
    description:
      - Run data conversion in either "warning", "info", "debug" or "disabled" mode.
      - Conversion will perform type conversion of input variables as defined in the schema.
      - Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
      - During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
      - conversion_mode:disabled means that conversion will not run.
      - conversion_mode:warning will produce warning messages.
      - conversion_mode:info will produce regular log messages.
      - conversion_mode:debug will produce hidden messages viewable with -v.
      - The converted data is set as facts which can be seen with -v, but is more readable with -vvv.
    required: False
    default: "debug"
    type: str
    choices: [ "warning", "info", "debug", "disabled" ]
  validation_mode:
    description:
      - Run validation in either "error", "warning", "info", "debug" or "disabled" mode.
      - Validation will validate the input variables according to the schema.
      - During validation, messages will generated with information about the host(s) and key(s) which failed validation.
      - validation_mode:disabled means that validation will not run.
      - validation_mode:error will produce error messages and fail the task.
      - validation_mode:warning will produce warning messages.
      - validation_mode:info will produce regular log messages.
      - validation_mode:debug will produce hidden messages viewable with -v.
    required: False
    default: "warning"
    type: str
    choices: [ "error", "warning", "info", "debug", "disabled" ]
"""

EXAMPLES = r"""
- name: Validate input vars according to AVD eos_designs schema
  tags: [validate]
  arista.avd.validate:
    schema: "{{ lookup('ansible.builtin.file', role_schema_path) | from_yaml }}"
    conversion_mode: "{{ avd_data_conversion_mode }}"
    validation_mode: "{{ avd_data_validation_mode }}"
  delegate_to: localhost
"""
