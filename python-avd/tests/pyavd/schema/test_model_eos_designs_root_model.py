# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdModelDeprecationWarning


def test_warning_emited_for_eos_cli_config_gen_keys() -> None:
    """Verify that warnings are emitted when passing eos_cli_config_gen keys to _from_dict to create EosDesigns."""
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        EosDesigns._from_dict({"dns_domain": "this.should.warn.test", "dns_settings": {"servers": [{"ip_address": "8.8.8.8"}]}})
        # Ensure that the correct warning is emitted.
        assert len(w) == 1
        assert issubclass(w[-1].category, AristaAvdModelDeprecationWarning)
        assert "The direct usage of `eos_cli_config_gen` keys when running `eos_designs` is deprecated and will be disabled by default in AVD 6.0.0." in str(
            w[-1].message
        )
        assert "dns_domain" in str(w[-1].message)
