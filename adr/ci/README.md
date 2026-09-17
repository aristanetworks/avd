<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# CI Decision Backlog

This domain covers CI structure and quality gates that preserve architectural properties. Individual commands and workflow implementation details do
not require ADRs.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `ci/0001` | Fan out CI by changed paths | Keep monorepo feedback practical while preserving relevant required checks. |
| `ci/0002` | Test at the narrowest effective layer | Choose consistently between unit, direct PyAVD E2E, Molecule, and `ansible-test`. |
| `ci/0003` | Use generated artifacts as behavioral golden contracts | Make configuration changes explicit even when generation tools capture errors outside the exit status. |
| `ci/0004` | Test minimum and representative supported versions | Ensure declared Python, Ansible, and dependency ranges describe configurations that actually work. |
| `ci/0005` | Combine unit and E2E coverage | Measure the layered generation paths that neither test family covers alone. |
| `ci/0006` | Validate release-shaped collection artifacts | Detect Galaxy metadata, inclusion, and packaging failures that source tests cannot see. |
