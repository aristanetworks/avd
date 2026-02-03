<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

```diff title="avdbuild.py"
#!/usr/bin/env python3
# Copyright (c) 2026 Arista Networks, Inc.

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from pyavd import (
    get_avd_facts,
    get_device_config,
    get_device_doc,
    get_device_structured_config,
    validate_inputs,
-    validate_structured_config,
)

if TYPE_CHECKING:
    # Importing internal objects only for type hinting to improve script readability.
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
-    from pyavd import ValidationResult
+    from pyavd.api.schemas import EOSConfig
+    from pyavd.api.validation import ValidatedDataResult

# 'generate_inventory' is a module which generates a test inventory.
# This should be replaced with something that reads a proper inventory like the Ansible inventory.
from generate_inventory import generate_hostvars

def main() -> None:
    # Prepare output directories
    config_dir = Path(__file__).parent / "configs"
    config_dir.mkdir(exist_ok=True)
    [file.unlink() for file in config_dir.glob("*")]
    docs_dir = Path(__file__).parent / "docs"
    docs_dir.mkdir(exist_ok=True)
    [file.unlink() for file in docs_dir.glob("*")]

    inventory: dict[str, dict[str, Any]] = generate_hostvars(spine_count=2, l3leaf_count=2, l2leaf_count=2, vrf_count=2, per_vrf_svi_count=2)

-   # Validating and inplace update with coerced types
+   # Validating and get back the validated inputs with coerced types
    for device, hostvars in inventory.items():
-       validation_result: ValidationResult = validate_inputs(inputs=hostvars)
+       validated_data_result: ValidatedDataResult = validate_inputs(inputs=hostvars)
-       if validation_result.failed:
+       if validated_data_result.validated_data is None:
-           msg: str = f"Validation of hostvars failed for {device}: {validation_result.validation_errors}"
+           msg: str = f"Validation of hostvars failed for {device}: {validated_data_result.validation_result.violations}"
            raise ValueError(msg)
+
+       inventory[device] = validated_data_result.validated_data

    # Get AVD Facts
-   avd_facts: dict[str, EosDesignsFacts] = get_avd_facts(all_inputs=inventory)
+    # We may be using custom Python modules for IP addressing or Descriptions, so we need to pass the hostvars as well since they can be used there.
+   avd_facts: dict[str, EosDesignsFacts] = get_avd_facts(all_inputs=inventory, all_hostvars=inventory)

    # Get Device Structured Configs
    for device, hostvars in inventory.items():
-       structured_config: dict = get_device_structured_config(hostname=device, inputs=hostvars, avd_facts=avd_facts)
+       # We may be using custom Python modules for IP addressing or Descriptions, so we need to pass the hostvars as well since they can be used there.
+       structured_config: EOSConfig = get_device_structured_config(hostname=device, inputs=hostvars, hostvars=hostvars, avd_facts=avd_facts)
-       # Validating and inplace update with coerced types
-       validation_result: ValidationResult = validate_structured_config(structured_config=structured_config)
-       if validation_result.failed:
-           msg: str = f"Validation of structured config failed for {device}: {validation_result.validation_errors}"
-           raise ValueError(msg)

        # Get Device Configs
        config: str = get_device_config(structured_config=structured_config)
        config_dir.joinpath(f"{device}.cfg").write_text(data=config)

        # Get Device Documentation
        documentation: str = get_device_doc(structured_config=structured_config)
        docs_dir.joinpath(f"{device}.md").write_text(data=documentation)

        print(".", end="", flush=True)
    print("")

if __name__ == "__main__":
    main()
```
