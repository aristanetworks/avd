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

DOCUMENTATION = r"""
---
module: topology_generator
version_added: "1.0.0"
author: EMEA AS Team (@aristanetworks)
short_description: Generate topology diagram from structure config
description:
  - Generate topology diagram from structure config
options:
  structured_config:
    description: Structured config directory path.
    required: true
    type: str
"""

EXAMPLES = r"""
- name: Generate topology diagram from structure config in svg file format
  topology_generator:
    structured_config: "base/main.j2"
  check_mode: no
  changed_when: False
"""
