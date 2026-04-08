<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# CloudVision Deployment

## Introduction

**CloudVision Deployment** provides an end-to-end workflow for pushing AVD-generated device configurations to Arista CloudVision using the `cv_deploy` role. Instead of deploying configurations directly to devices via eAPI, `cv_deploy` creates a CloudVision Workspace, deploys configurations through the Static Configuration Studio, and manages Change Controls for controlled rollouts.

This guide covers the complete workflow: configuring TerminAttr for device streaming, setting up the `cv_deploy` role, and managing workspaces and change controls.

### When to Use CloudVision Deployment

- **Centralized configuration management**: Deploy and audit all device configurations from a single platform
- **Change control workflows**: Require approval gates before configurations are pushed to devices
- **Configuration compliance**: Leverage CloudVision's config diff and validation before deployment
- **Tag-based automation**: Assign device and interface tags for CloudVision Studios and dashboards

## Concepts

**Workspace**: A staging area in CloudVision where configuration changes are prepared, validated, and reviewed before being applied. Workspaces go through states: `pending` -> `built` -> `submitted`.

**Change Control**: Created automatically when a workspace is submitted. Provides approval workflows and controlled execution of configuration changes. States: `pending approval` -> `approved` -> `running` -> `completed`.

**Static Configuration Studio**: The CloudVision feature that manages device configurations deployed by `cv_deploy`. Each device gets a configlet (named `AVD-<hostname>` by default) containing its full running configuration.

**TerminAttr**: The EOS daemon that streams device state to CloudVision. Devices must be streaming to CloudVision before `cv_deploy` can manage them.

**Service Account Token**: The authentication method used to connect to CloudVision. Username/password authentication is not supported for CVaaS.

## Configuring TerminAttr

Before deploying configurations with `cv_deploy`, devices must be streaming to CloudVision via TerminAttr. AVD generates the TerminAttr configuration automatically using the `cv_settings` variable.

### CVaaS Configuration

```yaml title="CloudVision Settings"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTCD/fabric.yml
--8<--
```

1. Fabric name shared by all devices in the topology
2. eBGP underlay routing protocol
3. eBGP overlay routing protocol
4. The `cv_settings` key configures TerminAttr on all devices in the fabric
5. Enable CloudVision-as-a-Service connectivity
6. Cluster name used in the TerminAttr `-cvopt` flags
7. CVaaS region - must match the region where your tenant is deployed. See the [regional URLs](#cvaas-regional-urls) table below
8. Sysdb paths excluded from streaming to reduce load
9. When `false` (default), TerminAttr uses AAA authorization and accounting

### Generated TerminAttr Configuration

AVD generates the following `daemon TerminAttr` configuration on each device:

=== "Leaf"

    ```cli title="htcd-leaf1a TerminAttr"
    --8<--
    docs/howto/cloudvision_deployment/artifacts/htcd-leaf1a-terminattr.cfg
    --8<--
    ```

=== "Spine"

    ```cli title="htcd-spine1 TerminAttr"
    --8<--
    docs/howto/cloudvision_deployment/artifacts/htcd-spine1-terminattr.cfg
    --8<--
    ```

The `-cvaddr` flag points to the CVaaS regional API server. The `-cvauth=token-secure` method uses a token file at `/tmp/cv-onboarding-token` that must be provisioned on each device before TerminAttr can connect.

### Management Interface

TerminAttr streams over the management interface in VRF `MGMT`:

```cli title="htcd-leaf1a Management"
--8<--
docs/howto/cloudvision_deployment/artifacts/htcd-leaf1a-management.cfg
--8<--
```

### On-Premises CloudVision

For on-premises CloudVision clusters, use `onprem_clusters` instead of `cvaas`:

```yaml title="On-Premises cv_settings"
cv_settings:
  onprem_clusters:
    - name: primary
      servers:
        - name: 192.168.1.12 # (1)!
          port: 9910 # (2)!
      token_file: /tmp/token # (3)!
  terminattr:
    smashexcludes: "ale,flexCounter,hardware,kni,pulse,strata"
    disable_aaa: false
```

1. CloudVision server IP address (IP is recommended over FQDN for image transfers)
2. gRPC port (default: 9910)
3. Path to the authentication token file on the device

### CVaaS Regional URLs

| Region | URL |
| -------------- | --------------------------------------- |
| United States 1a | `www.arista.io` |
| United States 1b | `www.cv-prod-us-central1-b.arista.io` |
| United States 1c | `www.cv-prod-us-central1-c.arista.io` |
| Canada | `www.cv-prod-na-northeast1-b.arista.io` |
| Europe West 2 | `www.cv-prod-euwest-2.arista.io` |
| Japan | `www.cv-prod-apnortheast-1.arista.io` |
| Australia | `www.cv-prod-ausoutheast-1.arista.io` |
| United Kingdom | `www.cv-prod-uk-1.arista.io` |

!!! warning
    URLs **must** include the `www` prefix. For example, use `www.arista.io`, not `arista.io`.

## Deploying with cv_deploy

### Basic Deployment Playbook

The deployment workflow uses two plays: one to generate configurations, and one to deploy them to CloudVision.

```yaml title="playbooks/deploy.yml"
---
- name: Build device configurations
  hosts: FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Generate structured variables
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate device configurations and documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

- name: Deploy configurations to CloudVision
  hosts: FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Deploy configurations and tags to CloudVision
      ansible.builtin.import_role:
        name: arista.avd.cv_deploy
      vars:
        cv_server: www.arista.io # (1)!
        cv_token: "{{ lookup('file', '~/.cloudvision/token') }}" # (2)!
```

1. CVaaS regional URL matching your tenant's region
2. Service account token - use Ansible Vault or a file lookup to avoid storing secrets in plain text

!!! tip
    Deploy a subset of devices using the `--limit` flag:

    ```bash
    ansible-playbook playbooks/deploy.yml --limit htcd-leaf1a,htcd-leaf1b
    ```

### Authentication Setup

`cv_deploy` requires a service account token for authentication. To create one:

1. In CloudVision, navigate to **Settings** -> **Service Accounts**
2. Create a new service account with appropriate permissions
3. Generate a token and save it securely
4. Reference the token in your playbook using Ansible Vault:

```yaml title="group_vars/FABRIC/cv_deploy.yml"
cv_server: www.arista.io
cv_token: "{{ vault_cv_token }}" # (1)!
cv_verify_certs: true # (2)!
```

1. Reference to an Ansible Vault-encrypted variable
2. Always use valid certificates in production (default: `true`)

## Workspace Management

By default, `cv_deploy` creates a workspace, builds it, and submits it. The resulting change control is left in `pending approval` state.

### Workspace Options

```yaml title="Workspace configuration"
cv_workspace_name: "AVD Deployment - Sprint 42" # (1)!
cv_workspace_description: "Deploying MLAG pair htcd-leaf1a/1b" # (2)!
cv_submit_workspace: true # (3)!
cv_submit_workspace_force: false # (4)!
cv_workspace_build_timeout: 300 # (5)!
```

1. Custom workspace name (default: `AVD <timestamp>`)
2. Description shown in the CloudVision UI
3. Submit the workspace after building (default: `true`)
4. Force submission even if some devices are not streaming (default: `false`)
5. Timeout in seconds for the workspace build phase (default: 300)

### Workspace States

For advanced workflows, control the workspace state directly:

```yaml title="Stop at built state for manual review"
cv_workspace_requested_state: built # (1)!
```

1. Accepted values: `pending`, `built`, `submitted`, `abandoned`, `deleted`

!!! note
    When `cv_workspace_requested_state` is set, it overrides `cv_submit_workspace` entirely.

## Change Control Management

Change controls are created automatically when a workspace is submitted. By default, they are left in `pending approval` state for manual review.

### Auto-Approve and Execute

```yaml title="Automatic change control execution"
cv_run_change_control: true # (1)!
cv_change_control_name: "Sprint 42 - Leaf pair deployment" # (2)!
cv_change_control_description: "Deploy updated BGP config to htcd-leaf1a/1b" # (3)!
```

1. Automatically approve, start, and wait for the change control to complete
2. Custom name for the change control
3. Description shown in the CloudVision UI

### Change Control States

For fine-grained control:

```yaml title="Direct state control"
cv_change_control_requested_state: approved # (1)!
```

1. Accepted values: `pending approval`, `approved`, `running`, `completed`. Overrides `cv_run_change_control`

## CloudVision Tags

Tags in CloudVision provide metadata for devices and interfaces. AVD automatically generates tags from the fabric topology (e.g., device role, DC name). Additional tags can be defined in the structured configuration.

When `cv_deploy` runs, it assigns the tags to devices and interfaces in CloudVision. By default, any existing tags with the same label but different values are removed to keep tags consistent with the AVD source of truth.

!!! warning
    Setting `cv_strict_tags: true` removes **all** tags not defined by AVD, including tags used by other Studios. This is not recommended for most deployments.

## Best Practices

1. **Use Ansible Vault for tokens**: Never store service account tokens in plain text. Use `ansible-vault encrypt_string` or reference a vault-encrypted vars file.

2. **Match CVaaS region to your tenant**: Using the wrong regional URL will cause connection failures. Verify your tenant's region in the CVaaS portal.

3. **Start with manual change controls**: Leave `cv_run_change_control: false` (the default) until you are confident in your deployment workflow. Review diffs in CloudVision before approving.

4. **Use `--limit` for incremental deployments**: Deploy to a subset of devices first, verify in CloudVision, then deploy to the full fabric.

5. **Set meaningful workspace names**: Include context like sprint number, ticket ID, or change description so that CloudVision audit trails are useful.

6. **Keep `cv_verify_certs: true` in production**: Only disable certificate verification in lab environments.

## Troubleshooting

### Devices not found in CloudVision

**Issue**: `cv_deploy` fails with "device not found" errors.

**Solution**:

- Verify TerminAttr is running and streaming on the device (`show daemon TerminAttr`)
- Check the device appears in CloudVision's Inventory
- Ensure the device hostname in the AVD inventory matches CloudVision exactly (case-sensitive)
- Set `cv_skip_missing_devices: true` to continue with available devices

### Workspace build fails

**Issue**: The workspace build phase reports errors.

**Solution**:

- Check the workspace in the CloudVision UI for detailed error messages
- Verify the generated EOS configurations are valid (`show running-config diffs` style)
- Increase `cv_workspace_build_timeout` for large deployments
- Use `cv_submit_workspace_force: true` if non-streaming devices are expected

### Authentication failures

**Issue**: Connection to CloudVision fails with authentication errors.

**Solution**:

- Verify the service account token is valid and not expired
- For CVaaS, ensure the URL includes the `www` prefix
- Check that `cv_verify_certs` matches your certificate setup
- Ensure the service account has sufficient permissions in CloudVision

### TerminAttr not connecting

**Issue**: Devices show TerminAttr running but not connected to CloudVision.

**Solution**:

- Verify DNS resolution for the CVaaS API server from the device's management VRF
- Check that the onboarding token file exists at the configured path (default: `/tmp/cv-onboarding-token`)
- Confirm the CVaaS region in `cv_settings` matches your tenant
- Verify network connectivity from the management VRF to the CloudVision server

## Reference

For complete details on all available properties, see:

- [CloudVision Settings (eos_designs)](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#cloudvision-settings)
- [cv_deploy Role Documentation](../../../ansible_collections/arista/avd/roles/cv_deploy/README.md)
