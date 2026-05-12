# AVD Schema Explorer — source

Source for the static, sql.js-based browser of the AVD `eos_designs` and
`eos_cli_config_gen` schemas. Built into `docs/schema-explorer/` for the
MkDocs site (no application code lives under `docs/`).

Tracked in `aristanetworks/avd-internal#503`.

## Layout

```
tools/schema-explorer/
├── generate.py          # CLI: schemas → SQLite + copies static assets to --site-dir
├── categories.py        # Category mapping for the sidebar classifier
├── README.md            # this file
└── static/              # SPA source — copied verbatim into <site-dir>
    ├── index.html       # SPA shell — sql.js loader + nav
    ├── css/style.css    # Bootstrap overrides + dark-mode rules
    └── js/app.js        # Hash router + landing/module/var-detail views
```

## Build

From the repo root:

```bash
make schema-explorer-build
# or directly:
python tools/schema-explorer/generate.py \
    --avd-root . --release devel --site-dir docs/schema-explorer
```

Output:

```
docs/schema-explorer/                    # gitignored — built artifact
├── index.html
├── css/style.css
├── js/app.js
└── data/devel/schema.sqlite             # generated; ~7.5 MB
```

The MkDocs wrapper page `docs/schema-explorer.md` references this built path.

`make docs-serve` runs the build before `mkdocs serve`. The webdoc container
(`docker compose -f development/docker-compose.yml up`) does the same via
`development/entrypoint.sh`, with an mtime guard so restarts are fast.

## What `generate.py` does

Loads each schema through pyavd's `schema_tools` resolver so:

- `dynamic_keys` placeholders (`<node_type_keys.key>`,
  `<connected_endpoints_keys.key>`, …) are fully expanded.
- Same-schema `$ref` blocks are resolved.
- Cross-schema `$ref` (e.g. `eos_cli_config_gen#/...` from inside
  `eos_designs`) is stripped before resolution and surfaced as a `cross_ref`
  column on the leaf row, so the SQLite stays ~7.5 MB instead of materializing
  the whole `eos_cli_config_gen` tree under every `structured_config`.

Required Python packages (already in the `doc` dependency group of
`pyproject.toml`): `pyyaml`, `referencing`, `deepmerge`, `pydantic`,
`jsonschema_rs`. `--avd-root` puts `python-avd/` on `PYTHONPATH`
automatically.

Repeat per supported AVD release (5.7+); the publish pipeline drops each
output under `docs/schema-explorer/data/<release>/schema.sqlite`.

## Architecture decisions

See aristanetworks/avd-internal#503 for the full thread. Short version:

- **MkDocs static + sql.js**, not App Engine — picked at the May 8th
  maintainers call. No managed-service patching, no LB URL map, no GCS bucket
  for data files; the SQLite ships under the docs bucket alongside everything
  else and the browser does the queries.
- **`schema_tools` resolver**, not raw `yaml.safe_load` — see
  aristanetworks/avd-internal#539. Closes the dynamic_keys hole (entire
  top-level subtrees like `<node_type_keys.key>` were missing) and the
  same-schema `$ref` hole, while keeping cross-schema refs as leaf
  annotations to bound the SQLite size.
- **Source under `tools/`**, build artifacts under `docs/` — keeps `docs/`
  to documentation only. (See PR thread for the four locations considered.)
