# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Verify locked runtime assembly and the public artifact boundary."""

from __future__ import annotations

import base64
import hashlib
import importlib.util
import subprocess
from pathlib import Path
from typing import Any

import pytest

SPEC = importlib.util.spec_from_file_location("runtime_generate", Path(__file__).parents[1] / "generate.py")
assert SPEC is not None
assert SPEC.loader is not None
GENERATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATE)


def test_runtime_assembly_hashes_installed_bytes_and_only_publishes_allowlist(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A dependency change updates every integrity reference without publishing package internals."""
    monkeypatch.setattr(GENERATE.shutil, "which", lambda _: "/usr/bin/npm")

    def install(command: list[str], *, cwd: Path, check: bool) -> None:
        assert command[1:] == ["ci", "--engine-strict", "--omit=dev", "--ignore-scripts", "--no-audit", "--no-fund"]
        assert check
        assert (cwd / "package-lock.json").is_file()
        assert not cwd.is_relative_to(GENERATE.HERE)
        for source, _ in GENERATE.RUNTIME_ASSETS.values():
            target = cwd / "node_modules" / source
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"updated package bytes")
        fonts = cwd / "node_modules/bootstrap-icons/font/fonts"
        fonts.mkdir()
        for filename in GENERATE.ICON_FONTS:
            (fonts / filename).write_bytes(b"font")
        for filename in GENERATE.RUNTIME_LICENSES:
            (cwd / "node_modules" / filename).write_text("license")
        (cwd / "node_modules/private-package-metadata.json").write_text("not public")

    monkeypatch.setattr(GENERATE.subprocess, "run", install)
    stale = tmp_path / "vendor/stale.js"
    stale.parent.mkdir()
    stale.write_text("obsolete")
    GENERATE._copy_static_assets(tmp_path)
    expected_hash = "sha384-" + base64.b64encode(hashlib.sha384(b"updated package bytes").digest()).decode()
    for filename in ("index.html", "js/app.js"):
        content = (tmp_path / filename).read_text()
        assert expected_hash in content
        assert "_INTEGRITY__" not in content
    published = {str(path.relative_to(tmp_path / "vendor")) for path in (tmp_path / "vendor").rglob("*") if path.is_file()}
    expected = {destination for _, destination in GENERATE.RUNTIME_ASSETS.values()}
    expected.update(f"bootstrap-icons/font/fonts/{filename}" for filename in GENERATE.ICON_FONTS)
    expected.update(GENERATE.RUNTIME_LICENSES)
    assert published == expected


def test_missing_npm_fails_clearly(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(GENERATE.shutil, "which", lambda _: None)
    with pytest.raises(RuntimeError, match=r"requires Node\.js"):
        GENERATE._copy_static_assets(tmp_path)


def test_failed_install_stops_build(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(GENERATE.shutil, "which", lambda _: "/usr/bin/npm")

    def fail(*_args: Any, **_kwargs: Any) -> None:
        raise subprocess.CalledProcessError(1, "npm ci")

    monkeypatch.setattr(GENERATE.subprocess, "run", fail)
    with pytest.raises(subprocess.CalledProcessError):
        GENERATE._copy_static_assets(tmp_path)
