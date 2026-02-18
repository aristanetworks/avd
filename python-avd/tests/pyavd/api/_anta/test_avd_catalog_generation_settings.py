# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

import pytest

from pyavd.api.anta import AVDCatalogGenerationSettings


def test_post_init_valid_output_dir(tmp_path: Path) -> None:
    """Test that a valid, existing directory is accepted."""
    settings = AVDCatalogGenerationSettings(output_dir=tmp_path)
    assert settings.output_dir == tmp_path


def test_post_init_none_output_dir() -> None:
    """Test that None is accepted (default behavior)."""
    settings = AVDCatalogGenerationSettings(output_dir=None)
    assert settings.output_dir is None


def test_post_init_non_existent_dir() -> None:
    """Test validation fails if the directory does not exist."""
    invalid_path = Path("/path/that/definitely/does/not/exist")
    with pytest.raises(ValueError, match="does not exist or is not a directory"):
        AVDCatalogGenerationSettings(output_dir=invalid_path)


def test_post_init_file_as_dir(tmp_path: Path) -> None:
    """Test validation fails if the path is a file, not a directory."""
    file_path = tmp_path / "test_file.txt"
    file_path.touch()
    with pytest.raises(ValueError, match="does not exist or is not a directory"):
        AVDCatalogGenerationSettings(output_dir=file_path)
