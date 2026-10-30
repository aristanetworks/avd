# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from ipaddress import IPv4Interface
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

from yaml import CSafeDumper, CSafeLoader, YAMLError, dump, load

from pyavd._errors import AristaAvdInvalidInputsError


@dataclass(frozen=True)
class Ipv4Allocation:
    """One persistent endpoint reservation, independent of node ID and interface name."""

    owner: str
    subnet: str
    vrf: str
    address: str


class Ipv4AllocationCollection:
    """Versioned IPv4 reservations. Unaccessed reservations are deliberately retained."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._snapshot = self._read()
        self.assignments: dict[str, Ipv4Allocation] = {}
        self._saved_assignments: dict[str, Ipv4Allocation] = {}
        if self._snapshot is None:
            return
        try:
            data = load(self._snapshot, Loader=CSafeLoader)
            if not isinstance(data, dict) or type(data.get("version")) is not int or data["version"] != 1 or not isinstance(data.get("allocations"), list):
                message = "Expected version: 1 and an allocations list."
                raise ValueError(message)  # noqa: TRY301
            for record in data["allocations"]:
                self._load_assignment(record)
        except (TypeError, ValueError, YAMLError) as error:
            msg = f"Invalid IPv4 allocation state '{path}': {error}"
            raise AristaAvdInvalidInputsError(msg) from error
        self._saved_assignments = self.assignments.copy()

    def _load_assignment(self, record: Any) -> None:
        if not isinstance(record, dict) or set(record) != {"owner", "subnet", "vrf", "address"}:
            message = "Each allocation must contain owner, subnet, vrf, and address."
            raise ValueError(message)
        if not all(isinstance(value, str) and value for value in record.values()):
            message = "Allocation fields must be nonempty strings."
            raise ValueError(message)
        allocation = Ipv4Allocation(**record)
        interface = IPv4Interface(allocation.address)
        if str(interface) != allocation.address or "/" not in allocation.address:
            message = f"Invalid canonical IPv4 address/prefix '{allocation.address}'."
            raise ValueError(message)
        if allocation.owner in self.assignments:
            message = f"Duplicate allocation owner '{allocation.owner}'."
            raise ValueError(message)
        self.assignments[allocation.owner] = allocation

    def _read(self) -> bytes | None:
        try:
            return self.path.read_bytes()
        except FileNotFoundError:
            return None

    def save_updates(self, dumper_cls: type = CSafeDumper) -> bool:
        """Atomically save changes, rejecting a writer based on outdated state."""
        if self.assignments == self._saved_assignments:
            return False
        self.path.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
        # Exclusive lock creation also works on platforms without POSIX advisory locks.
        lock_path = self.path.with_suffix(".yml.lock")
        try:
            lock_path.touch(exist_ok=False)
        except FileExistsError as error:
            msg = f"IPv4 allocation state '{self.path}' is locked by another writer. Re-run when that build completes."
            raise AristaAvdInvalidInputsError(msg) from error
        try:
            if self._read() != self._snapshot:
                msg = f"IPv4 allocation state '{self.path}' changed during this build. Re-run against the updated state."
                raise AristaAvdInvalidInputsError(msg)
            records = [asdict(self.assignments[owner]) for owner in sorted(self.assignments)]
            content = dump({"version": 1, "allocations": records}, Dumper=dumper_cls, sort_keys=False).encode()
            temporary_path: Path | None = None
            try:
                with NamedTemporaryFile(dir=self.path.parent, prefix=f".{self.path.name}.", delete=False) as temporary:
                    temporary_path = Path(temporary.name)
                    temporary.write(content)
                    temporary.flush()
                    os.fsync(temporary.fileno())
                temporary_path.replace(self.path)
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)
            self._snapshot = content
            self._saved_assignments = self.assignments.copy()
        finally:
            lock_path.unlink()
        return True
