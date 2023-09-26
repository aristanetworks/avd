# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

# NOTE that this is supposed to be deprecated as per
# https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html#ansible-metadata-block
# But our doc Jinja2 template renders it as preview which is what we want
ANSIBLE_METADATA = {"metadata_version": "1.0", "status": ["preview"]}

DOCUMENTATION = r"""
---
module: eos_validate_state_runner
version_added: "4.4.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Leverage ANTA for eos_validate_state role
description:
  - The C(arista.avd.eos_validate_state_runner) module is an Ansible Action Plugin leveraging the ANTA test
    framework to validate that the generated structured configurations by AVD are applied to the devices and
    that the deployed network is working correctly.
  - This plugin expects that the structued_configs of each device is present in hostvars, otherwise no test will be generated.
  - |-
    The plugin provides the following capabilities:
        - Generate a per-device test catalog based on the structured_configs
        - Run the generated tests against each device and generate a report in Markdown and CSV format.
        - When using check_mode, only generate the test catalog and generate a report to preview what would tests be run against each device
        - Dumping the per-device catalog to a file.
        - Backward compatibility with existing ansible tags behavior for eos_validate_state to filter categories of tests.
options:
  logging_level:
    description: Controls the log level for the ANTA library. If unset, the Action plugin will set it to "WARNING"
    required: false
    type: str
    choices: ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
    default: "WARNING"
  save_catalog:
    description: A boolean to indicate whether or not the catalog should be saved for each device.
    type: bool
    default: false
  device_catalog_output_dir:
    description:
      - When C(save_catalog) is True, this is the directory where the device catalogs will be saved.
      - Required if I(save_catalog=True)
    type: str
  skipped_test:
    description:
      - A dictionary to indicate skipped tests.
    type: dict
seealso:
  - name: ANTA website
    description: ANTA documentation
    link: https://anta.ninja
notes:
  - C(check_mode) is supported for this module and allows to generate a Test Report without running the tests.
"""

EXAMPLES = r"""
- name: Run eos_validate_state_runner leveraging ANTA
  arista.avd.eos_validate_state_runner:
    logging_level: ERROR
    save_catalog: True
    eos_validate_state_dir: "/tmp"
    skipped_tests: {"BGP"}
  register: anta_results
"""
