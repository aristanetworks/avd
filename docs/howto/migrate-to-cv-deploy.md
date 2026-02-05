<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Migrate to `cv_deploy`

This guide provides a step-by-step process for updating your Ansible inventory and playbooks to ensure a smooth and successful transition from legacy roles `eos_config_deploy_cvp` and `cvp_configlet_upload` to `cv_deploy`.

## Requirements

The `cv_deploy` role is part of the `arista.avd` Ansible collection. The `arista.cvp` collection is no longer required for AVD-to-CloudVision integration using `cv_deploy`. For a complete look at requirements, please see the [installation guide](../installation/collection-installation.md).

<div class="grid" markdown>

=== "Previous Requirements"

    ```yaml
    ---
    collections:
      - name: arista.avd
        version: 5.7.0
      - name: arista.cvp
        version: 3.12.0

    ```
=== "cv_deploy Requirements"

    ```yaml
    ---
    collections:
      - name: arista.avd
        version: 5.7.0

    ```

</div>

## Target Host

In `eos_config_deploy_cvp`, we targeted the definition of a CloudVision host as the target node. In `cv_deploy`, we now target the intended devices and set parameters for the URL of the CloudVision instance and the token to be used for authentication.

<div class="grid" markdown>

=== "eos_config_deploy_cvp"

    Inventory

    ```yaml
    ---
    all:
      children:
        cloudvision:
          hosts:
            <CloudVision node>:
              ansible_host: <CloudVision address>
              ansible_user: <CloudVision username>
              ansible_password: <CloudVision password>
              ansible_connection: httpapi
              ansible_httpapi_use_ssl: true
              ansible_httpapi_validate_certs: false
              ansible_network_os: eos
              ansible_httpapi_port: 443
    ```

    Playbook

    ```yaml hl_lines="3"
    ---
    - name: Deploy Configurations
      hosts: cloudvision # Set to CloudVision instance
      gather_facts: false

      tasks:
        - name: Deploy configurations to CloudVision
          ansible.builtin.import_role:
            name: arista.avd.eos_config_deploy_cvp
          vars:
            container_root: 'DC1_FABRIC'
            configlets_prefix: 'DC1-AVD'
            device_filter: 'DC1'
            state: present

    ```

=== "cv_deploy"

    !!! note
        Defining the CloudVision host in the Ansible inventory is no longer required.

    Playbook

    ```yaml hl_lines="3"
    ---
    - name: Deploy Configurations
      hosts: FABRIC # Now set to specific group
      gather_facts: false

      tasks:
        - name: Deploy configurations to CloudVision
          ansible.builtin.import_role:
            name: arista.avd.cv_deploy
          vars:
            cv_server: <hostname or IP address of CloudVision host>
            cv_token: <insert service_account token here - use Ansible Vault>

    ```

</div>

## Authentication

We recommend using the `cv_server` and `cv_token` keys for CloudVision authentication. Generate the `cv_token` from a service account with the required permissions. Refer to the `cv_deploy` role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision) for step-by-step instructions on creating these tokens.

```yaml hl_lines="6 7 9 10"
  tasks:
    - name: Deploy configurations to CloudVision
      ansible.builtin.import_role:
        name: arista.avd.cv_deploy
      vars:
        cv_server: <hostname or IP address of CloudVision host>
        cv_token: <insert service_account token here - use Ansible Vault>
```

!!! info
    You may use the combination of `cv_username` and `cv_password` instead of `cv_token`, but this is only supported for on-prem CloudVision. **CVaaS only supports token-based authentication.**

## Provisioning

`cv_deploy` leverages the CloudVision Studios Workflows for network provisioning, specifically with the Static Configuration Studio. When running playbooks to provision a network, the change control will remain pending (similar to the previous `eos_config_deploy_cvp` role). We can override this default with the `cv_run_change_control` key.

```yaml hl_lines="13"
---
- name: Deploy Configurations
  hosts: FABRIC
  gather_facts: false

  tasks:
    - name: Deploy configurations to CloudVision
      ansible.builtin.import_role:
        name: arista.avd.cv_deploy
      vars:
        cv_server: <hostname or IP address of CloudVision host>
        cv_token: <insert service_account token here - use Ansible Vault>
        cv_run_change_control: true

```

## Migration Scenarios for Static Configlets

The `cv_deploy` role replaces `cvp_configlet_upload` by managing configlets in the CloudVision **Static Configuration Studio**. Depending on your workflow, you can either deploy static configlets alongside device configurations or manage them exclusively.

Below are the two common migration scenarios.

### Scenario 1: Adding Static Configlets to a Device Deployment

Use this approach when your playbook deploys AVD-generated configurations to CloudVision but you also need to upload additional static configlets.

<div class="grid" markdown>

=== "Previous (Separate Tasks)"

    You first deploy device configs with `eos_config_deploy_cvp` and then upload the static configlets with `cvp_configlet_upload`.

    ```yaml
    ---
    - name: Deploy to CloudVision
      hosts: cloudvision
      gather_facts: false

      tasks:
        # Task 1
        - name: Deploy Device Configurations
          ansible.builtin.import_role:
            name: arista.avd.eos_config_deploy_cvp
          vars:
            container_root: 'DC1_FABRIC'
            configlets_prefix: 'DC1-AVD'
            device_filter: 'DC1'
            state: present

        # Task 2
        - name: Deploy Static Configlets
          ansible.builtin.import_role:
            name: arista.avd.cvp_configlet_upload
          vars:
            configlet_directory: "configlets/"
            file_extension: "txt"
            configlets_cvp_prefix: "DC1-AVD"
    ```

=== "cv_deploy (Single Task)"

    With `cv_deploy`, you define a **"manifest"** using `cv_static_config_manifest` within the same task that deploys your device configurations.

    ```yaml hl_lines="15-20"
    ---
    - name: Deploy to CloudVision
      hosts: FABRIC
      gather_facts: false

      tasks:
        - name: Deploy Device Configurations and Static Configlets
          ansible.builtin.import_role:
            name: arista.avd.cv_deploy
          vars:
            cv_server: <hostname or IP address of CloudVision host>
            cv_token: <insert service_account token here - use Ansible Vault>

            # The manifest is deployed alongside device configurations in the Static Configuration Studio
            cv_static_config_manifest:
              configlets:
                - name: "DC1-AVD_access_lists"
                  file: "configlets/access_lists.txt"
                - name: "DC1-AVD_ntp_servers"
                  file: "configlets/ntp_servers.txt"
    ```

</div>

### Scenario 2: Managing Only Static Configlets

Use this approach to replace a playbook whose **only** job was to upload configlets using `cvp_configlet_upload`. This requires running `cv_deploy` in **"manifest-only" mode**.

<div class="grid" markdown>

=== "cvp_configlet_upload"

    The playbook has a single purpose: to scan a directory and upload configlets.

    ```yaml
    ---
    - name: Deploy to CloudVision
      hosts: cloudvision
      gather_facts: false

      tasks:
        - name: Deploy Static Configlets
          ansible.builtin.import_role:
            name: arista.avd.cvp_configlet_upload
          vars:
            configlet_directory: "configlets/"
            file_extension: "txt"
            configlets_cvp_prefix: "DC1-AVD"
    ```

=== "cv_deploy"

    By setting `cv_devices: []`, it instructs the role to skip all device-specific operations and only process the manifest.

    ```yaml hl_lines="14-15"
    ---
    - name: Deploy to CloudVision
      hosts: FABRIC
      gather_facts: false

      tasks:
        - name: Deploy Static Configlets
          ansible.builtin.import_role:
            name: arista.avd.cv_deploy
          vars:
            cv_server: <hostname or IP address of CloudVision host>
            cv_token: <insert service_account token here - use Ansible Vault>

            # Enable manifest-only mode
            cv_devices: []

            cv_static_config_manifest:
              configlets:
                - name: "DC1-AVD_access_lists"
                  file: "configlets/access_lists.txt"
                - name: "DC1-AVD_ntp_servers"
                  file: "configlets/ntp_servers.txt"
    ```

</div>

### Migration considerations for CloudVision

When migrating from `cvp_configlet_upload` to `cv_deploy` role, the EOS devices should be removed from CloudVision `Network Provisioning` to avoid multiple config sources and configuration overlap.

Omitting to clean up Network Provisioning configlets mapping will result in configuration not being removed from device configuration when removing it from the static configlet studios because it would still be defined in the Network Provisioning configlet.

Devices can be removed manually in the CloudVision Portal user interface or pragramatically with an ansible playbook.

<div class="grid" markdown>

=== "Manual (single device)"

    Under the `Provisioning / Network Provisioning` menu, right click the device and select `Remove` and save.

=== "Manual (multiple devices)"

    Under the `Provisioning / Network Provisioning` menu, right click a container, select `Manage / Device` and tick the box next the the devices you want to remove from network provisioning, click the trash bin icon on the top right corner and save.

    !!! note
        The box next to `Name` field in the blue bar on top can be used to select all devices.

=== "Ansible"

    The example playbook below gathers the required data from CVP and removes the devices from CVP Network Provisioning.

    ```yaml
    ---
    - name: "Trigger a provisioning reset on EOS devices"
      hosts: all
      connection: local
      gather_facts: false
      vars:
        EOS_targets:  # set to a group or device in the inventory you want to reset
        CVP_target:   # set to cloudvision portal host in the inventory file
      tasks:
        - name: build the reset list
          ansible.builtin.set_fact:
            cvp_devices: "{{ cvp_devices | arista.avd.default([]) + [ {'fqdn': item, 'parentContainerName': '' } ] }}"
          loop: "{{ groups[EOS_targets] }}"
          run_once: true

        - name: "Remove devices from Network Provisioning"
          arista.cvp.cv_device_v3:
            devices: "{{ cvp_devices }}"
            state: provisioning_reset
            search_key: hostname
          delegate_to: "{{ CVP_target }}"
          run_once: true
    ```

    !!! note
        For more details, refer to the full Ansible collection cv_device_v3 module [documentation](https://galaxy.ansible.com/ui/repo/published/arista/cvp/content/module/cv_device_v3/).

</div>

!!! note
    For a complete overview of all the updates and capabilities in the `cv_deploy` role, including how to manage configlets and configlet containers, please see the role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md)
