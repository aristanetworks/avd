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

DOCUMENTATION = r'''
---
module: include_vars
version_added: "3.8.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Include Variables from files
description:
    This class is wrapping the builtin action plugin "include_vars" 1:1.
    We need this to avoid the Ansible behavior of injecting variables from
    "include_vars" with special precedence.

    Since Ansible uses the task name (fqcn) to detect if it is "include_vars"
    or some other module returning "ansible_facts", we only need to provide
    a different name, to avoid the builtin behavior.

    If we did not have this, we would have no way of overriding included_vars
    with structured_config or the automatic input variable conversion.

    Ref. https://github.com/ansible/ansible/blob/v2.13.3/lib/ansible/plugins/strategy/__init__.py#L738
'''

EXAMPLES = r'''
- arista.avd.include_vars:
    file: "{{ filename }}"
'''
