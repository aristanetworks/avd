<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# PyAVD

PyAVD is a Python package that serves as the foundation for the Arista AVD project and the `arista.avd` Ansible collection. PyAVD is maintained alongside the `arista.avd` Ansible collection and they are co-versioned.

PyAVD does not provide inventory or variable management, however it can serve as a component in a larger framework that provides this capability.

!!! note

    [AVD support](../support/support_overview.md) customers must leverage the Arista AVD project via the `arista.avd` Ansible collection.

Supported features:

- Validation of inputs based on the [AVD Design data models](../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md).
- Generation of "avd_facts" and "structured config" to be used in other PyAVD functions.
- Validation of "structured config" based on the [EOS Config data models](../../ansible_collections/arista/avd/roles/eos_cli_config_gen/docs/data-models.md).
- Generation of device configuration.
- Generation of device documentation.

Feedback is very welcome. Please use [GitHub discussions](https://github.com/aristanetworks/avd/discussions).

## Functions overview

![Arista AVD Overview](../_media/excalidraw/pyavd_functions.excalidraw)

## Known limitations

!!! warning

    Input data and "structured_configs" will be in-place updated by various PyAVD functions.
    Make sure to deep copy the data first if modifications are not allowed.

!!! warning

    `get_device_structured_config()`, `get_device_config()` and `get_device_doc()` are not thread-safe, so avoid running them for the same device across multiple threads.

!!! note

    - No support for inline Jinja2 or custom Jinja2 templates.
    - The logic uses the hostname as the unique identifier for each device, so overlapping hostnames will not work.
    - For `get_avd_facts()`, `fabric_name` is not used or verified and may differ between devices.
      All devices in the given inputs will be treated as one fabric.
    - `hostname` *must* be set in "structured_config" for each device. `hostname` *will* be set correctly when using `get_structured_config()`.

## Installation

Install the `pyavd` Python package:

```sh
pip install pyavd
```

Python dependencies are automatically installed with above command.

### Optional requirements

To install Ansible [AVD collection Python requirements](../installation/collection-installation.md#python-requirements-installation) install with extra `ansible`:

```sh
pip install pyavd[ansible]
```

## Reference

::: pyavd.validate_inputs
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_avd_facts
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_device_structured_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.validate_structured_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_fabric_documentation
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_device_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_device_doc
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.get_device_test_catalog
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.api.fabric_documentation
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.api.interface_descriptions
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.api.ip_addressing
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.api.pool_manager
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true

::: pyavd.api.validation
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
