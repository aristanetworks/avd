<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# pyavd

!!! warning
    pyavd is in beta phase. Please do not use for production. Everything is subject to change.

Pyavd is a python package providing some of the features from the `arista.avd` Ansible collection without requiring Ansible. Pyavd leverages the same logic as the Ansible collection, so the generated outputs should be exactly the same based on the same inputs.

Pyavd does not provide any inventory or variable management, so pyavd cannot replace a full Ansible based solution by itself. Pyavd could serve as an element in larger framework.

Supported features:

- Validation of inputs based on the [`eos_designs` input schema](../roles/eos_designs/docs/input-variables.md).
- Generation of "avd_facts" and "structured config" to be used in other pyavd functions.
- Validation of "structured config" based on the [`eos_cli_config_gen` input schema](../roles/eos_cli_config_gen/docs/input-variables.md).
- Generation of device configuration.
- Generation of device documentation.

Feedback is very welcome. Please use [GitHub discussions](https://github.com/aristanetworks/ansible-avd/discussions).

## Functions overview

![Arista AVD Overview](_media/pyavd_functions_dark.svg#only-dark)
![Arista AVD Overview](_media/pyavd_functions_light.svg#only-light)

## Known limitations

- No support for inline Jinja2 or custom Jinja2 templates.
- Input data and "structured_configs" will be in-place updated by various pyavd functions.
  Make sure to deep copy the data first if modifications are not allowed.
- The logic uses the hostname as the unique identifier for each device, so overlapping hostnames will not work.
- For `get_avd_facts()`, `fabric_name` is not used or verified and may differ between devices.
  All devices in the given inputs will be treated as one fabric.
- `hostname` must be set in "structured_config" for each device. `hostname` *will* be set correctly when using `get_structured_config()`.
- `get_device_structured_config()`, `get_device_config()` and `get_device_doc()` are not thread-safe, so avoid running them for the same device across multiple threads.

## Roadmap

!!! note
    Subject to change. No commitments implied.

- Add examples
- Add more tests (current coverage is 85%)
- Add network state validation similar to `eos_validate_state`.
- Add cloudvision tag integrations
- Make pyavd the source of AVD logic and use as a dependency for the `arista.avd` Ansible collection.
- Explore support for custom Jinja2 templates.

## Installation

Install `pyavd`:

```sh
pip3 install pyavd
```

Requirements (automatically installed with above command):

```ini
jinja2>=3.0
jsonschema>=4.5.1,<4.18
deepmerge>=1.1.0
```

### Optional requirements

For support of `get_device_doc(..., add_md_toc=True)` install with extra `mdtoc`:

```sh
pip3 install pyavd[mdtoc]
```

Optional `md-toc` requirement (automatically installed with above command):

```ini
md-toc>=8.1.8
```

## Reference

::: pyavd.validate_inputs
    options:
      show_root_toc_entry: false

::: pyavd.get_avd_facts
    options:
      show_root_toc_entry: false

::: pyavd.get_device_structured_config
    options:
      show_root_toc_entry: false

::: pyavd.validate_structured_config
    options:
      show_root_toc_entry: false

::: pyavd.get_device_config
    options:
      show_root_toc_entry: false

::: pyavd.get_device_doc
    options:
      show_root_toc_entry: false

::: pyavd.validation_result
    options:
      show_root_toc_entry: false

::: pool_manager.avdpoolmanager
    options:
      show_root_toc_entry: false
