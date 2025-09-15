# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from pathlib import Path

import pytest

from ansible_collections.arista.avd.plugins.modules.configlet_build_config import get_configlet

CONFIGLETS_DIR = str(Path(__file__).parents[2] / "inventory/intended/configs")

CONFIGLETS_DATA = {
    "valid_source": {"src_folder": CONFIGLETS_DIR, "prefix": "AVD"},
    "default_prefix": {"src_folder": CONFIGLETS_DIR},
    "non_default_prefix": {"src_folder": CONFIGLETS_DIR, "prefix": "CFG"},
}


class TestConfigletBuildConfig:
    def verify_configlets(self, src_folder: str, prefix: str, extension: str, output: dict) -> None:
        """Verify that the configlets are correct."""
        suffixes = [f".{extension}"]
        for file_path in Path(src_folder).rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.suffix in suffixes:
                key = file_path.stem if not prefix else f"{prefix}_{file_path.stem}"
                assert key in output

                # Compare contents of each file
                with file_path.open(encoding="utf8") as f:
                    assert f.read() == output[key]

    @pytest.mark.parametrize("data", CONFIGLETS_DATA.values(), ids=CONFIGLETS_DATA.keys())
    def test_get_configlet(self, data: dict) -> None:
        prefix = data.get("prefix")
        extension = data.get("extension", "cfg")
        src_folder = data["src_folder"]

        if prefix:
            output = get_configlet(src_folder=src_folder, prefix=prefix, extension=extension)
        else:
            output = get_configlet(src_folder=src_folder, extension=extension)
            prefix = "AVD"
        assert isinstance(output, dict)
        self.verify_configlets(src_folder, prefix, extension, output)

    def test_get_configlet_invalid_source(self) -> None:
        output = get_configlet()
        assert output == {}

    def test_get_configlet_none_prefix(self) -> None:
        extension = "cfg"
        output = get_configlet(src_folder=CONFIGLETS_DIR, prefix="none")
        assert isinstance(output, dict)
        self.verify_configlets(CONFIGLETS_DIR, "", extension, output)
