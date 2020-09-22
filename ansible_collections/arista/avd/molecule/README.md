# AVD Unit test

This section provides a list of AVD scenario executed during Continuous Integration to validate AVD integration.

- [AVD Unit test](#avd-unit-test)
  - [Ansible molecule](#ansible-molecule)
  - [Scenario](#scenario)
  - [Create Molecule scenario](#create-molecule-scenario)
    - [Create molecule structure](#create-molecule-structure)
    - [Configure Molecule](#configure-molecule)
    - [Ansible playbook for molecule](#ansible-playbook-for-molecule)
      - [Create playbook](#create-playbook)
      - [Converge playbook](#converge-playbook)
      - [Destroy playbook](#destroy-playbook)
      - [Verify playbook](#verify-playbook)
    - [Inventory creation](#inventory-creation)
  - [Manual execution](#manual-execution)
  - [Continuous Integration](#continuous-integration)

## Ansible molecule

Molecule provides support for testing with multiple instances, operating systems and distributions, virtualization providers, test frameworks and testing scenarios. Molecule encourages an approach that results in consistently developed roles that are well-written, easily understood and maintained.

## Scenario

Current molecule implementation provides following scenario:

- AVD-L3LS-EBGP
- AVD-L3LS-EBGP-JSON
- AVD-L3LS-ISIS
- EOS-CLI-CONFIG-GEN

## Create Molecule scenario

### Create molecule structure

First create new molecule scenario:

```shell
$ molecule init scenario test
--> Initializing new scenario test...
Initialized scenario in ./molecule/test successfully.
```

### Configure Molecule

Once, default structure is created by molecule itself, you can customize your molecule settings to define:

- Inventory
- Scenario execution
- Provisioner content
- Verifier content

First, let's define docker as molecule driver:

```yaml
# vim molecule.yml
dependency:
  name: galaxy
driver:
  name: docker
```

Define inventory for provisioner. This section will run a playbook to build AVD configurations

```yaml
# vim molecule.yml
provisioner:
  name: ansible
  env:
    # Path to access to collection. Usually root of the repository
    ANSIBLE_COLLECTIONS_PATHS: '../../../../../'
  # Replicate specific ansible.cfg settings
  config_options:
    defaults:
      jinja2_extensions: 'jinja2.ext.loopcontrols,jinja2.ext.do,jinja2.ext.i18n'
      gathering: explicit
      command_warnings: False
  # Define where inventory file is defined
  inventory:
    links:
      hosts: 'inventory/hosts'
      group_vars: 'inventory/group_vars/'
      host_vars: 'inventory/host_vars/'
  ansible_args:
    - --inventory=inventory/hosts
```

Then we should define a platform to run molecule testing. In AVD context, this platform should be a device part of testing inventory

```shell
platforms:
  - name: DC1-LEAF1A
    # Docker image to run for that host
    image: avdteam/base:3.6
    pre_build_image: true
    managed: false
    # Inventory group for this specific host.
    groups:
      - DC1_LEAF1
      - DC1_LEAFS
      - DC1_FABRIC
      - AVD_LAB
```

Then, configure sequence to run during molecule execution:

```yaml
scenario:
  test_sequence:
    - destroy
    - create
    - converge
    - idempotence
```

In this configuration, molecule will run playbooks in that specific order:

- destroy: `destroy.yml` playbook
- create: `create.yml` playbook
- converge: `converge.yml` playbook
- idempotency: `converge.yml` playbook with no change expected.

Molecule provides more sequences as explained in [documentation](https://molecule.readthedocs.io/en/latest/configuration.html#scenario)

### Ansible playbook for molecule

#### Create playbook

This playbook is a helper to prepare converge and test sequences. In AVD context, we leverage this playbook to build output directories:

```yaml
---
- name: Configure local folders
  hosts: all
  gather_facts: false
  connection: local
  tasks:
    - name: create local output folders
      delegate_to: 127.0.0.1
      import_role:
         name: arista.avd.build_output_folders
      run_once: true
```

#### Converge playbook

This playbook builds AVD content:

```yaml
---
- name: Converge
  hosts: all
  gather_facts: false
  connection: local
  tasks:

    - name: generate intented variables
      delegate_to: 127.0.0.1
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documention
      delegate_to: 127.0.0.1
      import_role:
         name: arista.avd.eos_cli_config_gen

```

This playbook will be run twice: first as __converge__ sequence and second as __idempotency__

#### Destroy playbook

Because we want to save content to CI, this sequence should not be added to the end of the scenario but only at the begining to cleanup pre-execution.

```yaml
---
- name: Remove output folders
  hosts: all
  gather_facts: false
  connection: local
  tasks:
    - name: delete local folders
      delegate_to: 127.0.0.1
      run_once: true
      file:
        path: "{{root_dir}}/{{ item }}"
        state: absent
      with_items:
        - documentation
        - intended
        - config_backup

```

#### Verify playbook

Not leverage in current implementation.

### Inventory creation

Inventory has no difference with [AVD documentation](https://aristanetworks.github.io/ansible-avd/roles/eos_l3ls_evpn/) provides:

- inventory/hosts has list of devices using `YAML` structure.
- inventory/group_vars has list of all AVD variables
- inventory/host_vars/all.yml configure a specific variable to save all AVD output outside of inventory fo CI purpose

```yaml
# inventory/host_vars/all.yml
---
root_dir: '{{playbook_dir}}'
```

## Manual execution

To manually run molecule testing, follow commands:

```shell
# Install development requirements
$ pip install -r development/requirements-dev.txt

# Move to AVD collection
$ ansible-avd/ansible_collections/arista/avd

# Run molecule for a given test
$ molecule test -s <scenario-name>

# Run molecule for all test
$ molecule test --all
```

## Continuous Integration

These scenario are all included in github actions and executed on `push` and `pull_request` when a file under `roles` and/or `molecule` is updated.

```yaml
name: Ansible Molecule
on:
  push:
  pull_request:
    paths:
      - 'ansible_collections/arista/avd/roles/**'
      - 'ansible_collections/arista/avd/molecules/**'
      - 'requirements.txt'
jobs:
  molecule:
    runs-on: ubuntu-latest
    env:
      PY_COLORS: 1 # allows molecule colors to be passed to GitHub Actions
      ANSIBLE_FORCE_COLOR: 1 # allows ansible colors to be passed to GitHub Actions
    strategy:
      fail-fast: true
      matrix:
        avd_scenario:
          - 'avd-l3ls-ebgp'
          - 'avd-l3ls-ebgp-json'
          - 'avd-l3ls-isis'
          - 'eos-cli-config-gen'
    steps:
      - uses: actions/checkout@v1
      - name: Set up Python 3
        uses: actions/setup-python@v1
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r development/requirements.txt
          pip install -r development/requirements-dev.txt

      - name: Execute molecule
        run: |
          cd ansible_collections/arista/avd
          molecule test --scenario-name ${{ matrix.avd_scenario }}

      - uses: actions/upload-artifact@v1
        with:
          name: molecule-results-${{ matrix.avd_scenario }}
          path: ansible_collections/arista/avd/molecule/${{ matrix.avd_scenario }}
```
