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
module: verify_requirements
version_added: "3.8.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Verify Python requirements when running AVD
description:
  - The `arista.avd.verify_requirements` module is an Ansible Action Plugin providing the following capabilities
  - Given a list of python requirements, verify if the installed libraries match these requirements
options:
  dependencies:
    description: |
      - List of strings of dependencies with pip file syntax
    required: True
    type: list
"""

EXAMPLES = r"""
- name: Verify python requirements
  arista.avd.verify_requirements:
    dependencies:
      - Jinja2 >= 2.9
      - paramiko == 2.7.1
  check_mode: False
  run_once: True
"""
