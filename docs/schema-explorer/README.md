# AVD Schema Explorer

Browsable, searchable view of the AVD `eos_designs` and `eos_cli_config_gen`
schemas. Pure-static — runs entirely in the browser via
[sql.js](https://github.com/sql-js/sql.js) (WASM SQLite). No backend, no app
server, just files served from the same MkDocs bucket as the rest of the docs
site.

Tracked in `aristanetworks/avd-internal#503`.

## Layout

```
docs/schema-explorer/
├── index.html                      # SPA shell — sql.js loader + nav
├── js/app.js                       # Hash router + landing/module/var-detail views
├── css/style.css                   # Bootstrap overrides
├── categories.py                   # Category mapping (used by generate.py)
├── generate.py                     # CLI: avd schemas → schema.sqlite
└── data/<release>/schema.sqlite    # local-test only; gitignored
```

In production the `data/` prefix is the same-origin path served from the
MkDocs static bucket — change `SCHEMA_BASE` in `js/app.js` if it ever moves.

## Run locally

From this directory:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>.

The schema database is loaded once on first request and cached in memory for
subsequent navigation. Each fetch sends a conditional GET (`cache: "no-cache"`)
so a freshly regenerated SQLite is picked up on next page load without
needing a hard reload.

## Generate the SQLite

From the avd repo root:

```bash
python docs/schema-explorer/generate.py \
    --avd-root . \
    --release devel \
    --out docs/schema-explorer/data/devel/schema.sqlite
```

`generate.py` loads each schema through pyavd's `schema_tools` resolver so
that `dynamic_keys` placeholders (e.g. `<node_type_keys.key>`,
`<connected_endpoints_keys.key>`) and same-schema `$ref` blocks are fully
expanded. Cross-schema `$ref`s — primarily `eos_cli_config_gen#/...` from
inside `eos_designs` — are stripped before resolving and surfaced as a
`cross_ref` column on the leaf row, so the SQLite stays small (~7.5 MB)
instead of materializing the whole `eos_cli_config_gen` tree under every
`structured_config`.

Required Python packages: `pyyaml`, `referencing`, `deepmerge`, `pydantic`,
`jsonschema_rs`, plus `python-avd/` on `PYTHONPATH` (handled automatically
by `--avd-root`).

Repeat per supported AVD release (5.7+); the publish pipeline drops each
output under `docs/schema-explorer/data/<release>/schema.sqlite`.

## Architecture decisions

See aristanetworks/avd-internal#503 for the full thread. The short version:

- **MkDocs static + sql.js**, not App Engine — picked at the May 8th
  maintainers call. No managed-service patching, no LB URL map, no GCS bucket
  for data files; the SQLite ships under the docs bucket alongside everything
  else and the browser does the queries.
- **`schema_tools` resolver**, not raw `yaml.safe_load` — see issue
  aristanetworks/avd-internal#539. This closes the dynamic_keys hole (entire
  top-level subtrees like `<node_type_keys.key>` were missing) and the
  same-schema `$ref` hole, while keeping cross-schema refs as leaf annotations
  to bound the SQLite size.
