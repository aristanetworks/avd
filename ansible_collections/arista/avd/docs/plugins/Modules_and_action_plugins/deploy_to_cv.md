---
# This title is used for search results
title: arista.avd.deploy_to_cv
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# deploy_to_cv

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.deploy_to_cv` when using this plugin.

Deploy various objects to CloudVision

## Synopsis

The \`arista.avd.deploy\_to\_cv\` module is an Ansible Action Plugin providing the following capabilities\:

\- Verify Devices are in the CloudVision inventory.
\- Verify Devices are in the Inventory \& Topology Studio.
\- Update the Device hostname in the Inventory \& Topology Studio as needed.
\- Create Workspace and build, submit, abandon as needed.
\- Deploy EOS configurations using \"Static Configlet Studio\".
\- Create and associate Device and Interface Tags.
\- Approve, run, cancel Change Controls as needed.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| configuration_dir | str | True | None |  | Path to directory containing .cfg files with EOS configurations. |
| structured_config_dir | str | True | None |  | Path to directory containing files with AVD structured configurations.
If found, the \`serial\_number\` or \`system\_mac\_address\` will be used to identify the Device on CloudVision.
Any tags found in the structured configuration metadata will be applied to the Device and/or Interfaces. |
| structured_config_suffix | str | optional | yml |  | File suffix for AVD structured configuration files. |
| device_list | list | True | None |  | List of devices to deploy. The names are used to find AVD structured configuration and EOS configuration files. |
| strict_tags | bool | optional | False |  | If \`True\` other tags associated with the devices will get removed. Otherwise other tags will be left as\-is. |
| skip_missing_devices | bool | optional | False |  | If \`True\` anything that can be deployed will get deployed. Otherwise the Workspace will be abandoned on any issue. |
| configlet_name_template | str | optional | AVD-${hostname} |  | Python String Template to use for creating the configlet name for each device configuration. |
| cloudvision | dict | True | None |  | CloudVision instance to deploy to. |
|     servers | list | True | None |  | List of hostnames or IP addresses for all CloudVision servers in one CloudVision cluster. |
|     token | str | True | None |  |  |
|     verify_certs | bool | optional | True |  |  |
| workspace | dict | optional | None |  | CloudVision Workspace to create or use for the deployment. If the Workspace already exists, it must be in \'pending\' state. |
|     name | str | optional | None |  |  |
|     description | str | optional | None |  |  |
|     id | str | optional | None |  |  |
|     requested_state | str | optional | built | Valid values:<br>- <code>pending</code><br>- <code>built</code><br>- <code>submitted</code><br>- <code>abandoned</code><br>- <code>deleted</code> | The requested state for the Workspace.

\- \`\"pending\"\`\: Leave the Workspace in pending state.
\- \`\"built\"\`\: Build the Workspace but do not submit.
\- \`\"submitted\"\` \(default\)\: Build and submit the Workspace.
\- \`\"abandoned\"\`\: Build and then abandon the Workspace.
    Used for dry\-run where no changes will be committed to CloudVision.
\- \`\"deleted\"\`\: Build, abort and then delete the Workspace.
    Used for dry\-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid \"clutter\". |
|     force | bool | optional | False |  | Force submit the workspace even if some devices are not actively streaming to CloudVision. |
| change_control | dict | optional | None |  | CloudVision Change Control to create for the deployment. |
|     name | str | optional | None |  |  |
|     description | str | optional | None |  |  |
|     requested_state | str | optional | pending approval | Valid values:<br>- <code>pending approval</code><br>- <code>approved</code><br>- <code>running</code><br>- <code>completed</code> | The requested state for the Change Control.

\- \`\"pending approval\"\` \(default\)\: Leave the Change Control in \"pending approval\" state.
\- \`\"approved\"\`\: Approve the Change Control but do not start.
\- \`\"running\"\`\: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
\- \`\"completed\"\`\: Approve and start the Change Control. Wait for the Change Control to be completed. |
| timeouts | dict | optional | None |  |  |
|     workspace_build_timeout | float | optional | 300.0 |  |  |
|     change_control_creation_timeout | float | optional | 300.0 |  |  |
| return_details | bool | optional | False |  |  |

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
