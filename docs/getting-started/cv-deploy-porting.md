<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# CloudVision Integration: Porting to `cv_deploy`

This guide provides a step-by-step process for updating your Ansible inventory and playbooks to ensure a smooth and successful transition from `eos_config_deploy_cvp` to `cv_deploy`.

## Requirements

The `cv_deploy` role is part of the `arista.avd` Ansible collection. `arista.cvp` collection is not required any more for AVD-to-CloudVision integration using `cv_deploy`. For a complete look at requirements, please see the [installation guide](../installation/collection-installation.md).

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

We recommend leveraging the `cv_server` and `cv_token` keys to specify the authentication to your CloudVision instance. The `cv_token` should be generated from a service account with the appropriate permissions in your workflows. You can find step-by-step instructions on creating service account tokens in the `cv_deploy` role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision).

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
    You may use the combination of `cv_username` and `cv_password` instead of `cv_token`, but this is only supported for on-prem CloudVision. CVaaS only supports token-based authentication.

## Provisioning

`cv_deploy` leverages the CloudVision Studios Workflows for network provisioning, specifically with the Static Configlet Studio. When running playbooks to provision a network, the change control will remain pending (similar to the previous `eos_config_deploy_cvp` role). We can override this default with the `cv_run_change_control` key.

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

!!! note
    For a complete overview of all the updates in the `cv_deploy` role, please see the role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision).
