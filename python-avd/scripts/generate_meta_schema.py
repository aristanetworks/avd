#!/usr/bin/env python3
# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Generate avd_meta_schema.json from the Pydantic model.

This script generates the JSON schema file that is used to validate
AVD schema fragments in YAML files.
"""
import json
import logging
from pathlib import Path
from sys import argv, path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.metaschema.meta_schema_model import AristaAvdSchema

METASCHEMA_JSON_PATH = Path(__file__).parents[1].joinpath("pyavd/_schema/avd_meta_schema.json")

if __name__ == "__main__":
    log_level_str = argv[1].upper() if len(argv) > 1 else "INFO"
    log_level = logging.getLevelName(log_level_str)
    logging.basicConfig(level=log_level, format="[generate_meta_schema] - %(message)s")
    
    logger = logging.getLogger(__name__)
    
    logger.info("Generating avd_meta_schema.json from Pydantic model...")
    
    # Generate JSON schema from the Pydantic model
    json_schema = AristaAvdSchema.model_json_schema(
        by_alias=True,
        mode="validation",
    )
    
    # Write to file with pretty formatting
    with METASCHEMA_JSON_PATH.open(mode="w", encoding="UTF-8") as f:
        json.dump(json_schema, f, indent=2, ensure_ascii=False)
        f.write("\n")  # Add final newline
    
    logger.info(f"Successfully generated {METASCHEMA_JSON_PATH}")

