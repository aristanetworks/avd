<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# CloudVision Integration: Porting to `cv_deploy`

This guide provides a step-by-step process for updating your Ansible inventory and playbooks to ensure a smooth and successful transition from legacy roles `eos_config_deploy_cvp` and `cvp_configlet_upload` to `cv_deploy`.

## Requirements

The `cv_deploy` role is part of the `arista.avd` Ansible collection. The `arista.cvp` collection is no longer required for AVD-to-CloudVision integration using `cv_deploy`. For a complete look at requirements, please see the [installation guide](../installation/collection-installation.md).

<div class="grid" markdown>

=== "Old Requirements"

    ```yaml
    ---
    collections:
      - name: arista.avd
        version: 5.7.0
      - name: arista.cvp
        version: 3.12.0

    ```
=== "New Requirements"

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

=== "Old"

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

=== "New"

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

We recommend leveraging the `cv_server` and `cv_token` keys to specify the authentication to your CloudVision instance. The `cv_token` should be generated from a **service account** with the appropriate permissions in your workflows. You can find step-by-step instructions on creating service account tokens in the `cv_deploy` role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision).

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

=== "Old (Separate Tasks)"

    You would first deploy device configs and then upload the static configlets.

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

=== "New (Single, Unified Task)"

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

=== "Old (`cvp_configlet_upload` only)"

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

=== "New (Manifest-Only Mode)"

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

!!! note
    For a complete overview of all the updates and capabilities in the `cv_deploy` role, including how to manage configlets and configlet containers, please see the role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md)
