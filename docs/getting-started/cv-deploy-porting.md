<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# CVP Integration. Porting to `cv_deploy`

This guide provides a step-by-step process for updating your Ansible inventory and playbooks to ensure a smooth and successful transition from `eos_config_deploy_cvp` to `cv_deploy`.

## Requirements

The `cv_deploy` role is now part of the `arista.avd` Ansible collection. This will now remove the requirement of the `arista.cvp` collection. If you have the `arista.cvp` collection listed in your `requirements.yml` file, it may be removed.

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

In `eos_config_deploy_cvp`, we targeted the definition of a CloudVision host as the target node. In `cv_deploy`, we now target the intended devices and set parameters for the URL of the CloudVision instance and the token to be used for authentication. You may also create a `cloudvision` host as before and the name is configurable by leveraging the key `cv_inventory_hostname` in your deployment. Please note, the `cloudvision` host is only leveraged to pickup the `ansible_host` and `ansible_password` to connect to CloudVision. This means `ansible_password` should still be a token from the service account.

<div class="grid" markdown>

=== "Old Playbook"

    ```yaml
    ---
    - name: Deploy Configurations
      hosts: cloudvision
      gather_facts: false

    ```

=== "Old Inventory"

    ```yaml
    all:
      children:
        cloudvision:
          hosts:
            cv_server01:
            ansible_host: 10.83.28.164
            ansible_user: ansible
            ansible_password: ansible
            ansible_connection: httpapi
            ansible_httpapi_use_ssl: true
            ansible_httpapi_validate_certs: false
            ansible_network_os: eos
            ansible_httpapi_port: 443
    ```

=== "New Playbook"

    ```yaml
    ---
    - name: Deploy Configurations
      hosts: FABRIC
      gather_facts: false

    ```

=== "New Inventory"

    ```yaml
    all:
      hosts:
        cloudvision:
          ansible_host: <hostname or IP address of CloudVision host. Ex. "www.arista.io" for CVaaS>
          ansible_password: <service account token as defined on CloudVision. This value should be using Ansible Vault>

    ```

</div>

Since we are now targeting the appropriate hosts in the playbook. You may have had a `device_filter` when leveraging `eos_config_deploy_cvp`. This can now be removed. We also no longer require building out a container hierarchy to associate devices to configurations, therefore `container_root` can also be removed.

<div class="grid" markdown>

=== "Old Playbook"

    ```yaml
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

=== "New Playbook"

    ```yaml
    tasks:
      - name: Deploy configurations to CloudVision
        ansible.builtin.import_role:
          name: arista.avd.cv_deploy

    ```

</div>

## Authentication

The `cv_deploy` role has support for username and password combinations for authentication. Although, we recommend you leverage a service account with the appropriate permissions in your workflows. You can find step-by-step instructions on creating service account tokens in the `cv_deploy` role [documentation](../../ansible_collections/arista/avd/roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision). Please note, you do not have to define `cv_server` and `cv_token` if you have created a `cloudvision` host as mentioned in the previous section.

!!! warning

    The use of username and password combinations is not supported on CloudVision as a Service (CVaaS).

<div class="grid" markdown>

=== "Manual override within the playbook"

    ```yaml
    tasks:
      - name: Deploy configurations to CloudVision
        ansible.builtin.import_role:
          name: arista.avd.cv_deploy
        vars:
          cv_server: www.arista.io
          cv_token: <insert service_account token here - use Ansible Vault>
          # Optional with username and password instead of cv_token
          cv_username: arista
          cv_password: <use Ansible Vault>
    ```

=== "Overrides within FABRIC variables"

    ```yaml
    cv_server: www.arista.io
    cv_token: <insert service_account token here - use Ansible Vault>
    # Optional with username and password instead of cv_token
    cv_username: arista
    cv_password: <use Ansible Vault>

    ```

</div>

## Topology View with Tags - Preview

There is newer data-models that can automatically generate CloudVision tags. The topology view generation with tags is geared towards Campus deployments at the time of this writing.

```yaml
generate_cv_tags:
  topology_hints: true
  campus_fabric: true
```

## Provisioning
