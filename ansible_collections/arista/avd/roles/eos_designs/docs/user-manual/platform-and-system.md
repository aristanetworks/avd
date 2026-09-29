---
# This title is used for search results
title: AVD Design data models for platform and system settings
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Platform and system

Platform-specific hardware behavior, reload timing, system settings, and EOS features that apply outside a single design area.

## Platform settings

Set platform specific settings like TCAM profile and reload delay.

If the platform is not defined, it will load parameters from the platform tagged `default`.

Management interface is modified for specific platforms like modular platforms with dual supervisor support and container EOS.

!!! note
    The reload delay values should be reviewed and tuned to the specific environment.

!!! note
    The default values will be overridden if `platform_settings` is defined.
    If you need to replace all the default platforms, it is recommended to copy the defaults and modify them.
    If you need to add custom platforms, create them under `custom_platform_settings`; if named identically to default `platform_settings` entries, custom entries will replace the equivalent default entry.

### Platform

--8<--
schemas/avd_design/docs/tables/platform-settings.md
--8<--

### Custom platform

--8<--
schemas/avd_design/docs/tables/custom-platform-settings.md
--8<--

### Platform speed groups

--8<--
schemas/avd_design/docs/tables/platform-speed-groups.md
--8<--

### TCAM profiles

--8<--
schemas/avd_design/docs/tables/tcam-profiles.md
--8<--

## System settings

--8<--
schemas/avd_design/docs/tables/system-settings.md
--8<--
