<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Code Decision Backlog

This domain covers Python architecture and authoring boundaries, not formatting or general code style. The following qualified identifiers and titles
form the initial backlog; each requires its own decision review before it becomes authoritative.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `code/0001` | Place reusable domain logic in PyAVD | Prevent behavior from diverging between direct Python and Ansible entry points. |
| `code/0002` | Mark public and internal Python APIs | Give users a useful SemVer surface without freezing every implementation module. |
| `code/0003` | Use generated typed schema models in the core | Align Python data semantics with schema validation and enable static analysis. |
| `code/0004` | Compose structured configuration with feature generators | Scale feature ownership while detecting conflicts instead of silently overwriting data. |
| `code/0005` | Make generation deterministic and side-effect bounded | Keep generated artifacts reproducible and reviewable. |
| `code/0006` | Separate generated and handwritten Python | Preserve clear source ownership and reproducible code generation. |
