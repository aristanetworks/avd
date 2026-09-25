# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# /// script
# dependencies = [
#   "pyavd[ansible] @ file:///${PROJECT_ROOT}/python-avd",
#   "gitpython>=3.1.57"
# ]
# requires-python = ">=3.11"
# [tool.uv]
# reinstall-package = ["pyavd"]
# ///
"""Command-line entry point for the AVD end-to-end test tool."""

from __future__ import annotations

import sys

from e2e_test_avd import main

if __name__ == "__main__":
    sys.exit(main())
