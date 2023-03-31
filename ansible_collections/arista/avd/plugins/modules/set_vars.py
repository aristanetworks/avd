# Copyright 2023 Arista Networks
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
module: set_vars
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set vars as ansible_facts.
description:
  - Set vars as ansible_facts.
  - Ansible will copy these into vars in the global namespace as well.
  - Arguments are treated as one dict so all arguments will be set as vars.
options: {}
"""

EXAMPLES = r"""
- name: Remove avd_switch_facts
  tags: [build, provision, facts, remove_avd_switch_facts]
  arista.avd.set_vars:
    avd_switch_facts: null
  run_once: true
  check_mode: false
"""
