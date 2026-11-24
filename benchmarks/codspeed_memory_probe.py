# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Observe CodSpeed profiling outside measurement and retain completed artifacts."""

from __future__ import annotations

import json
import os
import shutil
import sys
import sysconfig
from importlib.metadata import version
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator

OUTPUT = Path(os.environ.get("MEMORY_DIAGNOSTIC_OUTPUT", "/tmp/avd-memory-diagnostic"))  # noqa: S108


def record_state(stage: str, nodeid: str | None = None) -> None:
    """Record profiling state without enabling profiling or wrapping measured code."""
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pid = os.getpid()
    perf_map = Path(f"/tmp/perf-{pid}.map")  # noqa: S108
    lines = perf_map.read_text().splitlines() if perf_map.exists() else []
    checker = getattr(sys, "is_stack_trampoline_active", None)
    task_dir = Path(f"/proc/{pid}/task")
    children_file = task_dir / str(pid) / "children"
    state = {
        "stage": stage,
        "nodeid": nodeid,
        "pid": pid,
        "python": sys.version,
        "pytest_codspeed": version("pytest-codspeed"),
        "supports_perf_trampoline": sysconfig.get_config_var("PY_HAVE_PERF_TRAMPOLINE"),
        "stack_trampoline_active": checker() if checker else None,  # pylint: disable=using-constant-test
        "loaded_benchmark_modules": sorted(name for name in sys.modules if name.startswith("benchmarks.test_")),
        "perf_map": str(perf_map),
        "perf_map_exists": perf_map.exists(),
        "perf_map_lines": len(lines),
        "perf_map_benchmark_examples": [line for line in lines if "benchmarks/test_" in line][:5],
        "children": children_file.read_text().strip() if children_file.exists() else None,
        "thread_count": len(list(task_dir.iterdir())) if task_dir.is_dir() else None,
        "environment": {
            key: os.environ.get(key)
            for key in (
                "CODSPEED_ENV",
                "CODSPEED_RUNNER_MODE",
                "CODSPEED_PROFILE_FOLDER",
                "PYTHONPERFSUPPORT",
                "PYTHON_PERF_JIT_SUPPORT",
                "PYTHONMALLOC",
                "BENCHMARK_TARGETS",
            )
        },
    }
    with (OUTPUT / "states.jsonl").open("a") as stream:
        stream.write(json.dumps(state) + "\n")
    print("MEMORY_DIAGNOSTIC " + json.dumps(state), flush=True)  # noqa: T201
    if profile_folder := os.environ.get("CODSPEED_PROFILE_FOLDER"):
        (OUTPUT / "profile-folder.txt").write_text(profile_folder)
    if perf_map.exists():
        shutil.copy2(perf_map, OUTPUT / perf_map.name)


@pytest.hookimpl(trylast=True)
def pytest_sessionstart() -> None:
    """Observe the state after pytest-codspeed configures its instrument."""
    record_state("session_start")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item: pytest.Item) -> Iterator[None]:
    """Observe each case after the measured callback and fixture teardown."""
    try:
        yield
    finally:
        record_state("after_test", item.nodeid)


def pytest_sessionfinish() -> None:
    """Preserve the Python symbol map before the process exits."""
    record_state("session_finish")


def collect_artifacts() -> None:
    """Copy the completed profile after the CodSpeed action, including failed runs."""
    profile_file = OUTPUT / "profile-folder.txt"
    if not profile_file.exists():
        msg = "No CodSpeed profile directory was recorded; check whether pytest and the diagnostic plugin started."
        raise FileNotFoundError(msg)
    source = Path(profile_file.read_text().strip())
    if not source.is_dir():
        msg = f"Recorded CodSpeed profile directory is missing: {source}"
        raise FileNotFoundError(msg)
    if OUTPUT.resolve().is_relative_to(source.resolve()):
        msg = f"Diagnostic output {OUTPUT} must be outside the CodSpeed profile directory {source}."
        raise ValueError(msg)
    shutil.copytree(source, OUTPUT / "runner-profile", dirs_exist_ok=True)
    inventory = [{"path": str(path.relative_to(source)), "bytes": path.stat().st_size} for path in sorted(source.rglob("*")) if path.is_file()]
    (OUTPUT / "profile-inventory.json").write_text(json.dumps(inventory, indent=2))
    print(f"Retained {len(inventory)} profile files from {source}", flush=True)  # noqa: T201


if __name__ == "__main__":
    collect_artifacts()
