# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Publish the documentation index excluded by mkdocs-same-dir's root-file filter."""

import shutil
from pathlib import Path
from typing import Any


def on_post_build(config: dict[str, Any]) -> None:
    """Copy llms.txt after MkDocs has published the site's normal assets."""
    shutil.copyfile(Path(config["docs_dir"]) / "llms.txt", Path(config["site_dir"]) / "llms.txt")
