# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging

from pyavd._utils.hash_dir import check_hash
from pyavd.constants import RUNNING_FROM_SRC

from .constants import (
    EOS_CLI_CONFIG_GEN_SCHEMA_DIR,
    # METASCHEMA_DIR,
    EOS_DESIGNS_SCHEMA_DIR,
)

LOGGER = logging.getLogger(__name__)


def check_schemas() -> None:
    """TODO.

    Schemas
    """
    if not RUNNING_FROM_SRC:
        return

    LOGGER.info("pyavd running from source detected, checking schemas for any changes...")

    # TODO: ok to import from here
    from schema_tools.build_schemas import build_schemas

    # eos_designs
    eos_designs_changed, eos_designs_new_hash = check_hash(EOS_DESIGNS_SCHEMA_DIR / "schema_fragments")
    eos_cli_config_gen_changed, eos_cli_config_gen_new_hash = check_hash(EOS_CLI_CONFIG_GEN_SCHEMA_DIR / "schema_fragments")
    if eos_designs_changed or eos_cli_config_gen_changed:
        LOGGER.info("Recompiling schemas...")
        build_schemas()
        with (EOS_DESIGNS_SCHEMA_DIR / "schema_fragments/.hash").open("w") as fd:
            fd.write(eos_designs_new_hash)
        with (EOS_CLI_CONFIG_GEN_SCHEMA_DIR / "schema_fragments/.hash").open("w") as fd:
            fd.write(eos_cli_config_gen_new_hash)
