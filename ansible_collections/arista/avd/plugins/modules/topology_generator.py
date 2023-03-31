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
