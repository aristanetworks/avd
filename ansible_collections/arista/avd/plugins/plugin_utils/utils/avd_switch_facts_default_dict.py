# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts

try:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


class AvdSwitchFactsDefaultDict(defaultdict[str, EosDesignsFacts]):
    avd_switch_facts: dict[str, dict]

    def __init__(self, avd_switch_facts: dict[str, dict]) -> None:
        if not HAS_PYAVD:
            msg = "The 'arista.avd' collection requires the 'pyavd' Python library."
            raise ImportError(msg)

        self.avd_switch_facts = avd_switch_facts

    def __contains__(self, key: object) -> bool:
        return key in self.avd_switch_facts

    def get(self, key: str, default: Any = None) -> EosDesignsFacts:
        if key in self.avd_switch_facts:
            # Trigger __missing__
            return self[key]

        return default

    def __missing__(self, key: str) -> EosDesignsFacts:
        self[key] = EosDesignsFacts._from_dict(self.avd_switch_facts[key])
        return self[key]

    def keys(self) -> Iterable[str]:
        return self.avd_switch_facts.keys()
