<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# pyavd

!!! warning
    pyavd is still in the development phase. Please do not use.

## Functions overview

![Arista AVD Overview](_media/pyavd_functions_dark.svg#only-dark)
![Arista AVD Overview](_media/pyavd_functions_light.svg#only-light)

## Installation

```sh
pip3 install pyavd
```

Requirements (automatically installed with above command)

```ini
jinja2>=3.0
jsonschema>=4.5.1,<4.18
deepmerge>=1.1.0
```

## Reference

::: pyavd.validate_inputs
    options:
      show_root_toc_entry: false
      paths: ../../../../python-avd

::: pyavd.get_avd_facts
    options:
      show_root_toc_entry: false

::: pyavd.get_device_structured_config
    options:
      show_root_toc_entry: false

::: pyavd.validate_structured_config
    options:
      show_root_toc_entry: false
      paths: ../../../../python-avd

::: pyavd.get_device_config
    options:
      show_root_toc_entry: false

::: pyavd.get_device_doc
    options:
      show_root_toc_entry: false

::: pyavd.validation_result
    options:
      show_root_toc_entry: false
      paths: ../../../../python-avd
