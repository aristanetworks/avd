# OpenAVD — Open, Vendor-Agnostic Network Automation Framework

![License](https://img.shields.io/github/license/aristanetworks/avd)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Ansible](https://img.shields.io/badge/ansible-core%202.15%2B-red)

**OpenAVD** is a vendor-agnostic fork of [Arista's AVD (Architect, Validate, Deploy)](https://github.com/aristanetworks/avd) framework. Where AVD is purpose-built for Arista EOS, OpenAVD extends the same proven architecture — YAML-defined network designs compiled through Jinja2 templates and deployed via Ansible — to support **any network equipment vendor**.

Define your network once. Generate vendor-specific CLI configs for Arista EOS, Cisco IOS/NXOS, Juniper JunOS, or any other platform. Deploy them all through a single, unified Ansible workflow.

---

## How It Works

OpenAVD follows a three-phase pipeline:

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: Design                                                │
│  User-defined YAML  →  validate_inputs()  →  Fabric Facts      │
├─────────────────────────────────────────────────────────────────┤
│  Phase 2: Compile                                               │
│  Fabric Facts  →  get_device_structured_config()  →            │
│  Vendor-neutral structured config (Python objects / YAML)      │
├─────────────────────────────────────────────────────────────────┤
│  Phase 3: Render & Deploy                                       │
│  Structured Config  →  Jinja2 templates  →  Vendor CLI text    │
│  CLI text  →  Ansible role  →  Device                          │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 1 — Design (YAML → Fabric Facts)

You describe your network topology in YAML using a rich, high-level data model. A single inventory might look like:

```yaml
# group_vars/FABRIC.yml
fabric_name: my_fabric

bgp_as: 65000

spine_bgp_defaults:
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200

l3leaf:
  defaults:
    platform: generic
    bgp_as_range: 65001-65099
    uplink_interfaces: [Ethernet1, Ethernet2]
    uplink_switches: [spine1, spine2]
```

`validate_inputs()` parses this YAML against the **AVDDesign JSON schema**, catching type errors and missing fields before anything is deployed.

`get_avd_facts()` then processes the full fabric inventory — resolving relationships between devices, allocating BGP ASNs and IP addresses from pools, and computing MLAG pairs, VXLAN VNIs, uplink topology, and more.

### Phase 2 — Compile (Facts → Structured Config)

`get_device_structured_config()` runs ~108 structured-config generator modules, each responsible for one area of the network stack (underlay BGP, VXLAN overlay, MLAG, VLANs, management, etc.). The output is a **vendor-neutral structured config** object — a validated Python dataclass tree that fully describes what a device should look like, without containing any vendor-specific CLI syntax.

This is the critical abstraction layer: the same structured config can feed multiple vendor-specific rendering pipelines.

### Phase 3 — Render & Deploy (Structured Config → CLI → Device)

`get_device_config()` passes the structured config through a **Jinja2 template tree**. Each template handles one section of the device config. The templates are where vendor specificity lives — a Cisco IOS template for BGP neighbors looks different from an EOS template, but both receive the same structured-config input.

The rendered CLI text is written to flat files and then pushed to devices by an Ansible playbook.

---

## Repository Layout

```
OpenAVD/
├── ansible_collections/arista/avd/   # Ansible collection (roles, plugins)
│   ├── roles/
│   │   ├── eos_designs/              # Phase 1+2: design → structured config
│   │   ├── eos_cli_config_gen/       # Phase 3: structured config → EOS CLI
│   │   ├── eos_config_deploy_eapi/   # Deploy to EOS via eAPI
│   │   ├── eos_config_deploy_cvp/    # Deploy to EOS via CloudVision
│   │   └── eos_validate_state/       # Post-deployment validation
│   └── plugins/
│       ├── action/                   # Core action plugins (validate, facts, config gen)
│       └── filter/                   # Jinja2 filter plugins (shared with PyAVD)
│
└── python-avd/
    └── pyavd/                        # PyAVD — pure Python library
        ├── __init__.py               # Public API surface
        ├── templater.py              # Jinja2 environment + custom loader
        ├── j2filters/                # Custom Jinja2 filters
        ├── j2tests/                  # Custom Jinja2 test functions
        ├── _eos_designs/             # Phase 1+2 implementation
        │   ├── schema/               # AVDDesign YAML schema (80+ fragments)
        │   ├── eos_designs_facts/    # Fabric fact generators (BGP, VLAN, overlay…)
        │   └── structured_config/   # 108 structured-config generator modules
        ├── _eos_cli_config_gen/      # Phase 3 implementation (EOS-specific)
        │   ├── schema/               # EOSConfig YAML schema (380+ fragments)
        │   └── j2templates/          # Jinja2 templates → EOS CLI (210 files)
        ├── _schema/                  # Schema engine (validation, coercion, models)
        ├── _utils/                   # Shared utilities
        └── api/                      # Public API helpers (pool manager, IP addressing…)
```

---

## Quick Start

### Prerequisites

```bash
pip install pyavd ansible-core
ansible-galaxy collection install git+https://github.com/n3tpor/OpenAVD.git
```

### Pure Python (PyAVD)

```python
import pyavd

# 1. Load your design inputs (one dict per device)
inputs = {
    "spine1": { "type": "spine", "bgp_as": 65000, ... },
    "leaf1":  { "type": "l3leaf", "bgp_as": 65001, ... },
}

# 2. Validate inputs against the AVDDesign schema
validated = {hostname: pyavd.validate_inputs(vars) for hostname, vars in inputs.items()}

# 3. Generate fabric-wide facts (resolves topology, allocates IDs)
avd_facts = pyavd.get_avd_facts(validated)

# 4. Per device: compile structured config
for hostname in inputs:
    structured = pyavd.get_device_structured_config(hostname, validated[hostname], avd_facts)

    # 5. Render to vendor CLI
    cli_config = pyavd.get_device_config(structured)
    print(cli_config)  # Ready to push to the device

    # Optional: generate Markdown documentation
    doc = pyavd.get_device_doc(structured)
```

### Ansible

A minimal Ansible playbook that runs the full pipeline:

```yaml
# playbook.yml
- name: Build and deploy network configs
  hosts: FABRIC
  gather_facts: false
  tasks:

    - name: Generate EOS designs
      import_role:
        name: arista.avd.eos_designs

    - name: Generate device configs
      import_role:
        name: arista.avd.eos_cli_config_gen

    - name: Deploy via eAPI
      import_role:
        name: arista.avd.eos_config_deploy_eapi
```

Run with:
```bash
ansible-playbook playbook.yml -i inventory/
```

Configs are written to `intended/configs/<hostname>.cfg` and can be inspected before deployment.

---

## Key Concepts

| Concept | Description |
|---|---|
| **AVDDesign** | High-level vendor-neutral YAML schema describing fabric topology, protocols, and services |
| **Structured Config** | Intermediate Python object tree (validated, vendor-neutral) that describes device state |
| **Jinja2 Template Tree** | Vendor-specific rendering layer — swap templates to target a different OS |
| **Schema Fragments** | Modular YAML schema files assembled at runtime — easy to extend or override |
| **Action Plugins** | Ansible wrappers around PyAVD functions — the bridge between Ansible and the Python library |
| **Filter Plugins** | Custom Jinja2 filters (`range_expand`, `natural_sort`, `encrypt`, etc.) available in both Ansible and PyAVD |

---

## Vendor-Agnostic Roadmap

OpenAVD is currently in the process of being extended beyond EOS. Below is an honest assessment of what is already abstracted, what needs work, and what the path forward looks like.

### Already Abstracted ✅

- **Schema engine** (`_schema/`) — fully generic; validates any YAML structure
- **Templating engine** (`templater.py`) — vendor-neutral Jinja2 loader; template sets are swappable
- **PyAVD public API** — `validate_inputs`, `get_avd_facts`, `get_device_structured_config`, `get_device_config` are all generic function signatures
- **Filter/test plugins** — generic string, list, and crypto utilities with no EOS dependency
- **Schema fragment system** — modular YAML fragments can be added per-vendor without touching existing schemas

### Needs Work Before Full Vendor-Agnostic Support 🔧

#### 1. New vendor template sets (`_<vendor>_cli_config_gen/j2templates/`)
The EOS template tree (`_eos_cli_config_gen/j2templates/eos/`, 210 files) must be replicated for each target vendor. The structured config object is the input spec — templates only need to render it into the correct CLI syntax. This is the **primary implementation task** for adding a new vendor.

#### 2. Vendor-specific structured-config schema (`_<vendor>_cli_config_gen/schema/`)
The 380+ EOS CLI schema fragments define what fields are valid in a structured config. A new vendor schema must be created covering that vendor's feature set. Many fields (BGP peers, VLANs, interfaces, NTP, SNMP) map 1:1 — only the CLI rendering differs.

#### 3. Vendor selection in PyAVD and Ansible
Currently `get_device_config()` and the `eos_cli_config_gen` role are hardcoded to load EOS templates. A `vendor` parameter (e.g. `vendor: cisco_ios`) must be threaded through to select the correct template set at runtime.

#### 4. Rename / namespace Ansible roles and collection
The Ansible collection is namespaced `arista.avd`. For OpenAVD this should become a neutral namespace (e.g. `openavd.avd`). The `eos_*` role prefix should become `cli_config_gen`, `designs`, etc., with EOS remaining as the default/reference implementation.

#### 5. EOS-specific fact generators (`_eos_designs/eos_designs_facts/`)
Some fact generators (MLAG, short ESI, CloudVision tags) are EOS-specific. These should be moved into an `eos`-namespaced subdirectory and replaced with vendor-conditional dispatch so non-EOS flows skip them cleanly.

#### 6. CloudVision integration (`_cv/`)
The entire `_cv/` module is Arista-proprietary. It can be preserved as an optional EOS-only module but must not be required by vendor-neutral code paths.

### Suggested Development Order

1. Add `vendor` field to `AVDDesign` schema (defaults to `eos`)
2. Refactor `get_device_config()` to select template set from `vendor`
3. Create `openavd.avd` Ansible collection namespace alongside the existing `arista.avd`
4. Implement first non-EOS vendor template set (Cisco IOS-XE is recommended as the most widely deployed)
5. Move EOS-specific fact generators and CV integration behind `vendor == "eos"` guards
6. Add vendor-specific structured-config schema for new vendor
7. Write integration tests for each vendor using molecule

---

## Contributing

OpenAVD welcomes contributions — especially new vendor template sets. To add support for a new vendor:

1. Create `python-avd/pyavd/_<vendor>_cli_config_gen/` following the EOS reference structure
2. Add Jinja2 templates in `j2templates/<vendor>/`
3. Add schema fragments in `schema/schema_fragments/`
4. Add a molecule scenario in `ansible_collections/.../tests/`
5. Open a pull request with a working end-to-end example

Please open a discussion before starting large changes to agree on naming conventions and schema structure.

---

## License

This project is a fork of [Arista AVD](https://github.com/aristanetworks/avd), copyright 2019-2026 Arista Networks, Inc.

OpenAVD modifications are published under the same [Apache 2.0 License](LICENSE).
