<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Jinja2 Decision Backlog

This domain covers template responsibilities, compilation, rendering order, and extension boundaries. Syntax and formatting rules remain in the
contributor style guide.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `jinja2/0001` | Use Jinja2 only for deterministic presentation | Keep domain calculations reusable, typed, and independently testable in Python. |
| `jinja2/0002` | Treat source templates as canonical and compiled modules as ephemeral | Retain packaged performance without committing environment-dependent generated artifacts. |
| `jinja2/0003` | Define EOS output order with explicit root includes | Make semantically important configuration ordering auditable rather than filesystem-dependent. |
| `jinja2/0004` | Fail on undefined template data | Prevent missing values from silently removing configuration. |
| `jinja2/0005` | Separate CLI and documentation renderers over shared models | Support different formats and stability promises without duplicating calculations. |
| `jinja2/0006` | Append custom templates after built-ins through an explicit extension boundary | Preserve customization while making ordering, collisions, and precedence predictable. |
