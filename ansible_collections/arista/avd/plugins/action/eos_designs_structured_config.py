# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from collections import ChainMap
from typing import TYPE_CHECKING, Any

import yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

from ansible_collections.arista.avd.plugins.plugin_utils.constants import ANSIBLE_ABOVE_2_19
from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    AVDFileHandler,
    AvdSwitchFactsDefaultDict,
    AVDVaultHandler,
    cprofile,
    get_eos_designs_facts_path,
    get_templar,
    get_tmp_paths,
    write_file,
)
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AVDActionPlugin, AVDLoggingConfig

if TYPE_CHECKING:
    from pyavd._eos_designs.structured_config import get_structured_config
    from pyavd._schema.avdschema import AvdSchema
    from pyavd._utils import merge, strip_null_from_data
    from pyavd._utils import template as templater
    from pyavd.api.schemas import AVDDesign

try:
    from pyavd._eos_designs.structured_config import get_structured_config
    from pyavd._schema.avdschema import AvdSchema
    from pyavd._utils import merge, strip_null_from_data
    from pyavd._utils import template as templater
    from pyavd.api.schemas import AVDDesign

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


class ActionModule(AVDActionPlugin):
    _logging_config = AVDLoggingConfig(add_hostname_context=True)
    tmp_dir: str

    @cprofile()
    def main(self, task_vars: dict[str, Any]) -> None:
        if not HAS_PYAVD:
            msg = "The 'arista.avd.eos_designs_structured_config' plugin requires the 'pyavd' Python library. Got import error"
            raise ImportError(msg)

        hostname = task_vars["inventory_hostname"]

        if self._task.args.get("structured_config") is False:
            # Not creating structured config
            return

        eos_designs_custom_templates = self._task.args.get("eos_designs_custom_templates", [])
        filename = str(self._task.args.get("dest", ""))
        file_mode = str(self._task.args.get("mode", "0o664"))

        # Only template output on ansible versions < 2.19.
        template_output = bool(self._task.args.get("template_output", False)) and not ANSIBLE_ABOVE_2_19

        digital_twin = self._task.args.get("digital_twin", False)
        return_structured_config = self._task.args.get("return_structured_config", False)
        self.tmp_dir = self._task.args.get("tmp_dir")

        # Get updated templar instance to be passed along to our simplified "templater"
        self.templar = get_templar(self, task_vars)

        avd_design, host_hostvars = self.load_validated_inputs(hostname)

        all_facts = self.load_facts(hostname)

        # Get Structured Config from modules in PyAVD using internal api so we can supply our own templar
        structured_config = get_structured_config(
            hostname=hostname,
            inputs=avd_design,
            all_facts=all_facts,
            hostvars=host_hostvars,
            templar=self.templar,
            digital_twin=digital_twin,
        )

        output = structured_config._as_dict()

        # We use ChainMap to avoid copying large amounts of data around, mapping in
        #  - output (containing structured_config at this point)
        #  - templated, converted and validated version of all other vars
        # Any var assignments will end up in output, so all other objects are protected.
        template_vars = ChainMap(output, host_hostvars)

        # eos_designs_custom_templates can contain a list of jinja templates to run after PyAVD
        if eos_designs_custom_templates:
            # Load output schema used by merger on output of custom templates
            output_schema = AvdSchema(schema_id="eos_cli_config_gen")

            for template_item in eos_designs_custom_templates:
                template_options = template_item.get("options", {})
                list_merge = template_options.get("list_merge", "append_rp")
                strip_empty_keys = template_options.get("strip_empty_keys", True)
                template = template_item["template"]

                # Here we parse the template, expecting the result to be a YAML formatted string
                # self.templar is an AVDTemplar instance which already contains loader and searchpath
                template_result = templater(template, template_vars, self.templar)

                # Skip if template result is None or empty string
                if not template_result:
                    continue

                # Load data from the template result.
                template_result_data = yaml.safe_load(template_result)

                # If the argument 'strip_empty_keys' is set, remove keys with value of null / None from the resulting dict (recursively).
                if strip_empty_keys:
                    template_result_data = strip_null_from_data(template_result_data)

                if not template_result_data:
                    continue

                # If there is any data produced by the template, convert and merge it on top of previous output.
                # Some templates return a list of dicts, others only return a dict. Here we normalize to list.
                if not isinstance(template_result_data, list):
                    template_result_data = [template_result_data]

                merge(output, *template_result_data, list_merge=list_merge, schema=output_schema)

        # If the argument 'template_output' is set, run the output data through another jinja2 rendering.
        # This is to resolve any input values with inline jinja using variables/facts set by the input templates.
        if template_output:
            with self._templar.set_temporary_context(available_variables=template_vars):
                output = self._templar.template(output, fail_on_undefined=False)

        # If the argument 'dest' (filename) is set, write the output data to a file.
        if filename:
            # Depending on the file suffix of 'filename' (default: 'json') we will format the data to yaml or just write the output data directly.
            if filename.endswith((".yml", ".yaml")):
                self.result["changed"] = write_file(
                    content=yaml.dump(output, Dumper=AnsibleDumper, indent=2, sort_keys=False, width=130),
                    filename=filename,
                    file_mode=file_mode,
                )
            else:
                self.result["changed"] = write_file(
                    content=json.dumps(output),
                    filename=filename,
                    file_mode=file_mode,
                )

        # If 'dest' (filename) is not set, hardcode 'changed' to true, since we don't know if something changed and later tasks may depend on this.
        else:
            self.result["changed"] = True

        if return_structured_config:
            self.result["ansible_facts"] = output

    def load_validated_inputs(self, hostname: str) -> tuple[AVDDesign, dict[str, Any]]:
        """
        Load validated hostvars from the temporary file for the host and load them into AVDDesign class.

        Args:
            hostname: Inventory hostname.

        Returns:
            Tuple of an AVDDesign instance loaded from the host hostvars and a dict with the raw hostvars.
        """
        _templated_path, validated_path = get_tmp_paths(self.tmp_dir)
        file_path = validated_path / f"{hostname}.json"
        if not file_path.exists():
            msg = (
                f"Missing validated inputs for host '{hostname}'. "
                "Ensure the 'arista.avd.validate_inputs' task ran successfully for this host and that no validation errors occurred."
            )
            raise FileNotFoundError(msg)

        # Read, unvault, and parse the JSON file
        vault_handler = AVDVaultHandler(self._loader)
        file_handler = AVDFileHandler(vault_handler)
        host_hostvars = file_handler.load_json(file_path)

        # Load host hostvars into the AVDDesign data class.
        avd_design = AVDDesign._from_dict(host_hostvars)

        return avd_design, host_hostvars

    def load_facts(self, hostname: str) -> AvdSwitchFactsDefaultDict:
        """
        Load facts from the temporary file and load them into AvdSwitchFactsDefaultDict class.

        Args:
            hostname: Inventory hostname.

        Returns:
            AvdSwitchFactsDefaultDict instance loaded from facts.
        """
        file_path = get_eos_designs_facts_path(self.tmp_dir)

        if not file_path.exists():
            msg = f"Missing AVD eos_designs facts for host '{hostname}' ({file_path}). Ensure the 'arista.avd.eos_designs_facts' task ran successfully."
            raise FileNotFoundError(msg)

        with file_path.open(mode="r", encoding="utf-8") as f:
            avd_switch_facts = json.load(f)

        return AvdSwitchFactsDefaultDict(avd_switch_facts)
