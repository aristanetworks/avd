# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import runpy
import sys
from pathlib import Path

from pyavd._schema.constants import (
    EOS_CLI_CONFIG_GEN_SCHEMA_DIR,
    # METASCHEMA_DIR,
    EOS_DESIGNS_SCHEMA_DIR,
)
from pyavd.constants import EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH, EOS_DESIGNS_JINJA2_TEMPLATE_PATH, RUNNING_FROM_SRC

from .hash_dir import check_hash

LOGGER = logging.getLogger(__name__)


def check_running_from_source() -> None:
    """TODO."""
    if not RUNNING_FROM_SRC:
        return

    LOGGER.info("pyavd running from source detected, checking schemas and templates...")

    # Schemas
    BUILD_SCHEMAS_SCRIPT = Path(__file__).parents[2] / "scripts/build_schemas.py"

    # eos_designs
    eos_designs_changed, eos_designs_new_hash = check_hash(EOS_DESIGNS_SCHEMA_DIR / "schema_fragments")
    eos_cli_config_gen_changed, eos_cli_config_gen_new_hash = check_hash(EOS_CLI_CONFIG_GEN_SCHEMA_DIR / "schema_fragments")
    if eos_designs_changed or eos_cli_config_gen_changed:
        LOGGER.info("Recompiling schemas...")
        # TODO: this works but meh
        sys.argv = ["debug", "debug"]
        runpy.run_path(str(BUILD_SCHEMAS_SCRIPT), run_name="__main__")
        with (EOS_DESIGNS_SCHEMA_DIR / "schema_fragments/.hash").open("w") as fd:
            fd.write(eos_designs_new_hash)
        with (EOS_CLI_CONFIG_GEN_SCHEMA_DIR / "schema_fragments/.hash").open("w") as fd:
            fd.write(eos_cli_config_gen_new_hash)

    # Templates
    COMPILE_TEMPLATES_SCRIPT = Path(__file__).parents[2] / "scripts/compile_templates.py"

    changed, new_hash = check_hash(EOS_DESIGNS_JINJA2_TEMPLATE_PATH)
    if changed:
        LOGGER.info("Recompiling eos_designs templates...")
        runpy.run_path(str(COMPILE_TEMPLATES_SCRIPT), run_name="__main__")
        with (EOS_DESIGNS_JINJA2_TEMPLATE_PATH / ".hash").open("w") as fd:
            fd.write(new_hash)

    # eos_cli_config_gen
    changed, new_hash = check_hash(EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH)
    if changed:
        LOGGER.info("Recompiling eos_cli_config_gen templates...")
        runpy.run_path(str(COMPILE_TEMPLATES_SCRIPT), run_name="__main__")
        with (EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH / ".hash").open("w") as fd:
            fd.write(new_hash)
