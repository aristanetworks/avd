# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RenderConfiguration:
    """Common render configuration for eos_cli_config_gen output."""

    hide_passwords: bool | None = None
    """Replace sensitive values with '<removed>' when rendering output."""


@dataclass(frozen=True)
class ConfigRenderConfiguration(RenderConfiguration):
    """Render configuration for device EOS configurations."""


@dataclass(frozen=True)
class DocRenderConfiguration(RenderConfiguration):
    """Render configuration for device Markdown documentation."""


__all__ = ["ConfigRenderConfiguration", "DocRenderConfiguration", "RenderConfiguration"]
