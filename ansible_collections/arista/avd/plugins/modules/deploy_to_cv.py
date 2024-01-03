# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: deploy_to_cv
version_added: "4.6.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Deploy various objects to CloudVision
description: |-
  The `arista.avd.deploy_to_cv` module is an Ansible Action Plugin providing the following capabilities:

  - Verify Devices are in the CloudVision inventory.
  - Verify Devices are in the Inventory & Topology Studio.
  - Update the Device hostname in the Inventory & Topology Studio as needed.
  - Create Workspace and build, submit, abandon as needed.
  - Deploy EOS configurations using "Static Configlet Studio".
  - Create and associate Device and Interface Tags.
  - Approve, run, cancel Change Controls as needed.
options:
  configuration_dir:
    description: Path to directory containing .cfg files with EOS configurations.
    required: true
    type: str
  structured_config_dir:
    description: |-
      Path to directory containing files with AVD structured configurations.
      If found, the `serial_number` or `system_mac_address` will be used to identify the Device on CloudVision.
      Any tags found in the structured configuration metadata will be applied to the Device and/or Interfaces.
    required: true
    type: str
  structured_config_suffix:
    description: File suffix for AVD structured configuration files.
    default: "yml"
    type: str
  device_list:
    description: List of devices to deploy. The names are used to find AVD structured configuration and EOS configuration files.
    type: list
    required: true
    elements: str
  strict_tags:
    description: If `True` other tags associated with the devices will get removed. Otherwise other tags will be left as-is.
    type: bool
    default: false
  skip_missing_devices:
    description: If `True` anything that can be deployed will get deployed. Otherwise the Workspace will be abandoned on any issue.
    type: bool
    default: false
  configlet_name_template:
    description: Python String Template to use for creating the configlet name for each device configuration.
    type: str
    default: "AVD-${hostname}"
  cloudvision:
    description: CloudVision instance to deploy to.
    required: true
    type: dict
    suboptions:
      servers:
        description: List of hostnames or IP addresses for all CloudVision servers in one CloudVision cluster.
        type: list
        elements: str
        required: true
      token:
        type: str
        secret: true
        required: true
      verify_certs:
        type: bool
        default: true
  workspace:
    description: CloudVision Workspace to create or use for the deployment. If the Workspace already exists, it must be in 'pending' state.
    type: dict
    suboptions:
      name:
        type: str
      description:
        type: str
      id:
        type: str
      requested_state:
        description: |-
          The requested state for the Workspace.

          - `"pending"`: Leave the Workspace in pending state.
          - `"built"`: Build the Workspace but do not submit.
          - `"submitted"` (default): Build and submit the Workspace.
          - `"abandoned"`: Build and then abandon the Workspace.
              Used for dry-run where no changes will be committed to CloudVision.
          - `"deleted"`: Build, abort and then delete the Workspace.
              Used for dry-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid "clutter".
        type: str
        default: built
        choices: ["pending", "built", "submitted", "abandoned", "deleted"]
      force:
        description: Force submit the workspace even if some devices are not actively streaming to CloudVision.
        type: bool
        default: false
  change_control:
    description: CloudVision Change Control to create for the deployment.
    type: dict
    suboptions:
      name:
        type: str
      description:
        type: str
      requested_state:
        description: |-
          The requested state for the Change Control.

          - `"pending approval"` (default): Leave the Change Control in "pending approval" state.
          - `"approved"`: Approve the Change Control but do not start.
          - `"running"`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
          - `"completed"`: Approve and start the Change Control. Wait for the Change Control to be completed.
        type: str
        default: pending approval
        choices: ["pending approval", "approved", "running", "completed"]
  timeouts:
    type: dict
    suboptions:
      workspace_build_timeout:
        type: float
        default: 300.0
      change_control_creation_timeout:
        type: float
        default: 300.0
  return_details:
    type: bool
    default: false
"""

EXAMPLES = r"""
---
- name: Configuration deployment with CVP
  hosts: FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Provision CVP with AVD configuration
      run_once: true
      delegate_to: localhost
      arista.avd.deploy_to_cv:
        configuration_dir: "{{ inventory_dir }}/intended/configs"
        structured_config_dir: "{{ inventory_dir }}/intended/structured_configs"
        # structured_config_suffix: "yml"
        device_list: "{{ ansible_play_hosts }}"
        # strict_tags: false
        # skip_missing_devices: false
        # configlet_name_template: "AVD-${hostname}"
        cloudvision:
          servers: [ "www.arista.io" ]
          token: "<insert vaulted service account token here>"
          # verify_certs: True
        workspace:
        #   name:
        #   description:
        #   id: <uuid or similar>
          requested_state: submitted
          force: True
        change_control:
        #   name:
        #   description:
          requested_state: "approved"
        # timeouts:
        #   workspace_build_timeout: 300.0
        #   change_control_creation_timeout: 300.0
        # return_details: false
"""

# TODO: RETURNS
