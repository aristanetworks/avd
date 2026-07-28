<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Description Guidelines

This document defines how to write `description` fields in the AVD YAML schemas (`eos_designs`, `eos_cli_config_gen`, `cv_deploy`). These guidelines apply to all schema fragments under `python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments` and `python-avd/pyavd/_eos_designs/schema/schema_fragments`.

## Where descriptions are rendered

The same `description` text is rendered in multiple places:

- **Schema documentation** on [avd.arista.com](https://avd.arista.com) — shown as-is in tables and key documentation.
- **LSP hover tooltips** in VS Code and other editors — shown when hovering over a key in YAML.
- **UI forms** in CloudVision and other Arista tools — shown as field labels, help text, or tooltips.

Write every description so it reads correctly in all of these contexts without modification.

## Writing style

- Start with a capital letter, end with a period. Even fragments: `"BGP AS number."`
- Sentence fragments are preferred over full sentences: `"BGP AS number."` not `"This field defines the BGP AS number for the device."`.
- Present tense: `"Enables..."`, `"Overrides..."`. Not `"Will enable..."` or `"Used to enable..."`.
- Two sentences max. Longer explanations belong on the documentation site.
- Same concept, same words. If `"Enable BFD."` is used in one place, don't write `"Turns on BFD."` elsewhere.

- *Good Example*

  ```yaml
  description: Administrative distance for eBGP-learned routes.
  ```

- *Bad Example*

  ```yaml
  description: This is a string value that is used by eos_designs to set the administrative distance for routes learned via eBGP. Default is 200.
  ```

---

## Rules

### DESC-1 - No tool-specific language

AVD is consumed through Ansible, Python, UI, and other interfaces. Descriptions must not assume any specific tool.

**Do not use (when possible):**

- `hostvars`, `inventory`, `inventory_hostname`, `playbook`, `role`, `vars files`
- `ansible_host`, `ansible_password`, `ansible_facts`
- Ansible module, plugin, or collection path references
- `group_vars`, `host_vars`

**Replace with:**

| Instead of | Write |
|---|---|
| `hostvars` | `input variables` |
| `inventory_hostname` | `hostname` |
| `inventory host` | `device` or `node` |
| `using Ansible Vault` | `stored securely (e.g. using a vault)` |

!!! note
    URLs pointing to AVD documentation (e.g. `avd.arista.com`) are documentation content, not tool-specific language. Keep them.

- *Good Examples*

  ```yaml
  description: Overrides the password for CloudVision authentication.
  description: Read structured configuration from input variables.
  description: Relative path to the template.
  ```

- *Bad Examples*

  ```yaml
  description: Will override ansible_password on inventory host.
  description: Read structured configuration from hostvars.
  description: Template relative path below playbook directory.
  ```

### DESC-2 - Don't prefix list descriptions with "List of"

The schema type already declares `type: list`. All consumers render this information separately. Don't repeat it in the description.

- *Good Examples*

  ```yaml
  type: list
  description: BGP peer entries.

  type: list
  description: Tenant definitions for network services.
  ```

- *Bad Examples*

  ```yaml
  type: list
  description: List of BGP peer entries.

  type: list
  description: List of tenant definitions for network services.
  ```

- *Exception — "Ordered list of"*

  Keep "Ordered list of" when ordering is semantically important (ACL entries, route-map sequences, accounting methods). "Ordered" adds information the schema type does not convey.

  ```yaml
  # KEEP - ordering matters
  description: Ordered list of access-list entries identified by sequence number.
  description: Ordered list of accounting methods for EXEC session activity.
  ```

- *Exception — Comma-separated string fields*

  When "list" describes a string format (not a YAML list), keep the concept but normalize the wording:

  ```yaml
  # BAD
  type: str
  description: Comma separated list of prefixes (IPv4 address/Mask).

  # GOOD
  type: str
  description: Comma-separated prefixes (IPv4 address/Mask).
  ```

### DESC-3 - Don't repeat valid values or ranges

Valid values are defined in the schema via `enum`, `valid_values`, `min`, `max`. Each consumer renders them separately (dropdown, table, detail block). Repeating them in the description doubles the maintenance — when values change, the description goes stale.

- *Good Examples*

  ```yaml
  valid_values: ["ascending", "descending"]
  description: Allocation setting.

  min: 1
  max: 16777215
  description: Value in microseconds.
  ```

- *Bad Examples*

  ```yaml
  description: "Allocation setting. Valid values: ascending, descending."
  description: "Valid values are 1-16777215 microseconds."
  ```

### DESC-4 - Don't restate the type

The schema already declares `type: str`, `type: int`, `type: bool`, etc. Don't echo it in the description.

- *Good Examples*

  ```yaml
  type: str
  description: Device hostname.

  type: bool
  description: Enable BFD.
  ```

- *Bad Examples*

  ```yaml
  type: str
  description: String that defines the hostname.

  type: bool
  description: Boolean to enable BFD.
  ```

### DESC-5 - Describe what, not how

A description explains **what a setting is** and **what it controls**. Leave out:

- How AVD processes the value internally
- Workflow steps (`"Add to group_vars"`, `"Run the playbook"`)
- Information the schema already provides (type, default, required)

- *Good Examples*

  ```yaml
  description: BGP AS number for this node.
  description: Enable the feature.
  ```

- *Bad Examples*

  ```yaml
  description: >-
    This key is used by eos_designs to generate the final structured config
    that is then fed into eos_cli_config_gen.
  description: "Set this to true to enable the feature. Default is false."
  ```

---

## Checklist to review schema description changes

- [ ] No Ansible-specific language (`hostvars`, `inventory`, `playbook`, `ansible_*`, `group_vars`).
- [ ] No "List of" prefix on list-type fields (except "Ordered list of" where order matters).
- [ ] No valid values or ranges repeated from schema constraints.
- [ ] No type restated from schema declaration.
- [ ] Descriptions are concise — two sentences max.
- [ ] All descriptions start with a capital letter and end with a period.
