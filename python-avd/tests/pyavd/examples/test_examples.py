# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from pathlib import Path


def test_simple_example() -> None:
    """
    Test running the simple example script.

    The script is written for direct execution so we just import it.
    We overwrite the script's path to sys.path so it can support relative imports.
    """
    import sys

    sys.path.insert(0, str(Path(__file__).parent / "simple"))

    import simple.avdbuild  # noqa: F401
