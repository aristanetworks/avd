# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: cv_workflow
version_added: "4.7.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Deploy various objects to CloudVision
description: |-
  The `arista.avd.cv_workflow` module is an Ansible Action Plugin providing the following capabilities:

  - Verify Devices are in the CloudVision inventory.
  - Verify Devices are in the Inventory & Topology Studio.
  - Update the Device hostname in the Inventory & Topology Studio as needed.
  - Create Workspace and build, submit, abandon as needed.
  - Deploy device-specific EOS configurations using Static Configuration Studio.
  - Deploy a full hierarchy of containers and configlets using Static Configuration Studio.
  - Create and associate Device and Interface Tags.
  - Approve, run, cancel Change Controls as needed.
options:
  cv_servers:
    description: List of hostnames or IP addresses for CloudVision instance to deploy to.
    type: list
    elements: str
    required: true
  cv_token:
    description: Service account token. It is strongly recommended to use Vault for this.
    type: str
    required: false
  cv_username:
    description: Username to use if `cv_token` is missing. Not supported for CVaaS.
    type: str
    required: false
  cv_password:
    description: Password to use if `cv_token` is missing. Not supported for CVaaS. It is strongly recommended to use Vault for this.
    type: str
    required: false
  cv_verify_certs:
    description: Verifies CloudVison server certificates.
    type: bool
    default: true
  proxy_host:
    description: FQDN/IP of the HTTP CONNECT proxy server.
    type: str
    required: false
  proxy_port:
    description: TCP port of the HTTP CONNECT proxy server.
    type: int
    default: 8080
  proxy_username:
    description: Authentication username for the HTTP CONNECT proxy server.
    type: str
    required: false
  proxy_password:
    description: Authentication password for the HTTP CONNECT proxy server. It is strongly recommended to use Vault for this.
    type: str
    required: false
  configuration_dir:
    description: Path to directory containing .cfg files with EOS configurations.
    required: true
    type: str
  structured_config_dir:
    description: |-
      Path to directory containing files with AVD structured configurations.
      If found, the `serial_number` or `system_mac_address` will be used to identify the Device on CloudVision.
      Any tags found in the structured configuration metadata will be applied to the Device and/or Interfaces.
    required: false
    type: str
  structured_config_suffix:
    description: File suffix for AVD structured configuration files.
    default: "yml"
    type: str
  device_list:
    description: List of devices to deploy. The names are used to find AVD structured configuration and EOS configuration files.
    type: list
    required: false
    elements: str
  strict_tags:
    description: If `true` other tags associated with the devices will get removed. Otherwise other tags will be left as-is.
    type: bool
    default: false
  skip_missing_devices:
    description: If `true` anything that can be deployed will get deployed. Otherwise the Workspace will be abandoned on any issue.
    type: bool
    default: false
  strict_system_mac_address:
    description: |-
      If `true`, raise an exception if the input data contains devices with a duplicated system_mac_address but unique serial_number values.
      Otherwise, just issue a warning.
    type: bool
    default: false
  configlet_name_template:
    description: Python String Template to use for creating the configlet name for each device configuration.
    type: str
    default: "AVD-${hostname}"
  static_config_manifest:
    description: Deploy a manifest of containers and configlets to CloudVision using the Static Configuration Studio.
    type: dict
    suboptions:
      configlets:
        description: |-
          A list of dictionaries defining configlets to be pushed to the Configlet Library.

          Each dictionary in the list must follow this data model:
          - **name** (`str`, required): Unique name for the configlet.
          - **file** (`str`, required): Filesystem path to the text file containing the configlet body. Relative to the current working directory.
        type: list
        elements: dict
      containers:
        description: |-
          A list of dictionaries defining the root containers in the hierarchy.

          Each dictionary in the list must follow this data model:
          - **name** (`str`, required): Name for the container. Sibling containers must have unique names.
          - **tag_query** (`str`, required): A query string used to match devices based on their assigned tags.
          - **description** (`str`, optional): An optional description for the container.
          - **match_policy** (`str`, optional, default: "match_all"): The match policy to determine how devices with a matching tag inherit
              a child container configlets. Valid choices are `match_all` or `match_first`.
          - **configlets** (`list` of `str`, optional): A list of configlet names to apply to this container. Must be defined in the `configlets` section.
          - **sub_containers** (`list` of `dict`, optional): A nested list of container dictionaries that follow this same data model,
              allowing for a full hierarchy.
        type: list
        elements: dict
  workspace:
    description: CloudVision Workspace to create or use for the deployment.
    type: dict
    suboptions:
      name:
        description: Optional name to use for the created Workspace. By default the name will be `AVD <timestamp>`.
        type: str
      description:
        description: Optional description to use for the created Workspace.
        type: str
      id:
        description: Optional ID to use for the created Workspace. If there is already a workspace with the same ID, it must be in the 'pending' state.
        type: str
      requested_state:
        description: |-
          The requested state for the Workspace.

          - `pending`: Leave the Workspace in pending state.
          - `built`: Build the Workspace but do not submit.
          - `submitted` (default): Build and submit the Workspace.
          - `abandoned`: Build and then abandon the Workspace.
              Used for dry-run where no changes will be committed to CloudVision.
          - `deleted`: Build, abort and then delete the Workspace.
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
        description: Optional name to use for the created Change Control. By default the name generated by CloudVision will be kept.
        type: str
      description:
        description: Optional description to use for the created Change Control.
        type: str
      requested_state:
        description: |-
          The requested state for the Change Control.

          - `pending approval` (default): Leave the Change Control in "pending approval" state.
          - `approved`: Approve the Change Control but do not start.
          - `running`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
          - `completed`: Approve and start the Change Control. Wait for the Change Control to be completed.
        type: str
        default: pending approval
        choices: ["pending approval", "approved", "running", "completed"]
  timeouts:
    description: Timeouts for long running operations. May need to be adjusted for large inventories.
    type: dict
    suboptions:
      workspace_build_timeout:
        description: Time to wait for Workspace build before failing.
        type: float
        default: 300.0
      change_control_creation_timeout:
        description: Time to wait for Change Control creation before failing.
        type: float
        default: 300.0
  return_details:
    description: |-
      If `true` all details will be returned to Ansible and can be registered.
      For large inventories this can affect performance, so it is disabled by default.
    type: bool
    default: false
notes:
  - |-
    When interacting with CVaaS the regional URL where the tenant is deployed should be used, e.g:
    `cv_servers: [ www.cv-prod-euwest-2.arista.io ]`
    To see the full list of regional URLs, please visit the
    [cv_deploy](../../../ansible_collections/arista/avd/roles/cv_deploy/README.md#overview)
    role documentation.
  - |-
    To generate service accounts check
    [cv_deploy](../../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision)
    role documentation or the CloudVision Help Center.
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
      arista.avd.cv_workflow:
        cv_servers: [ "www.arista.io" ]
        cv_token: "<insert vaulted service account token here>"
        # cv_verify_certs: true
        # proxy_host: "proxy.local.domain"
        # proxy_port: "8080"
        # proxy_username: "avd_user"
        # proxy_password: "avd_password"
        configuration_dir: "{{ inventory_dir }}/intended/configs"
        structured_config_dir: "{{ inventory_dir }}/intended/structured_configs"
        # structured_config_suffix: "yml"
        device_list: "{{ ansible_play_hosts }}"
        # strict_tags: false
        # skip_missing_devices: false
        # strict_system_mac_address: false
        # configlet_name_template: "AVD-${hostname}"
        # static_config_manifest:
        #   configlets:
        #     - name: "GLOBAL_NTP_SERVERS"
        #       file: "configlets/global_ntp.txt"
        #     - name: "CORP_BANNER"
        #       file: "configlets/corp_banner.txt"
        #   containers:
        #     - name: "Global"
        #       tag_query: "device:*"
        #       match_policy: "match_all"
        #       configlets:
        #         - name: "GLOBAL_NTP_SERVERS"
        #       sub_containers:
        #         - name: "Data Centers"
        #           tag_query: "topology_network_type:datacenter"
        #           configlets:
        #             - name: "CORP_BANNER"
        workspace:
        #   name:
        #   description:
        #   id: <uuid or similar>
          requested_state: submitted
          force: true
        change_control:
        #   name:
        #   description:
          requested_state: "approved"
        # timeouts:
        #   workspace_build_timeout: 300.0
        #   change_control_creation_timeout: 300.0
        # return_details: false
"""

# TODO: RETURN
