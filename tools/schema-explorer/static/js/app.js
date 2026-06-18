/* AVD Schema Explorer — static / sql.js variant.
 *
 * Loads schema.sqlite into the browser via sql.js (WASM), then renders
 * landing / module-browse / var-detail views via hash routing. No backend.
 */

// Split a key_path on "." while treating `<...>` placeholders as atomic, so
// `<connected_endpoints_keys.key>.foo.bar` → ["<connected_endpoints_keys.key>", "foo", "bar"]
// instead of the naive split's ["<connected_endpoints_keys", "key>", "foo", "bar"].
function splitKeyPath(keyPath) {
  const out = [];
  let buf = "";
  let depth = 0;
  for (const c of keyPath) {
    if (c === "<") { depth++; buf += c; }
    else if (c === ">") { depth = Math.max(0, depth - 1); buf += c; }
    else if (c === "." && depth === 0) { out.push(buf); buf = ""; }
    else { buf += c; }
  }
  if (buf || out.length === 0) out.push(buf);
  return out;
}
function rootSegment(keyPath) {
  return stripPlaceholderBrackets(splitKeyPath(keyPath)[0].replace("[]", ""));
}
function leafSegment(keyPath) {
  return stripPlaceholderBrackets(splitKeyPath(keyPath).pop());
}
function dynamicKeySource(keyPath) {
  const match = String(keyPath).match(/^<([^>]+)>/);
  return match ? match[1] : "";
}
// Pyavd's docs convention wraps dynamic_keys placeholders in `<...>`
// (e.g. <connected_endpoints_keys.key>). Brackets are noise once the user is
// inside the explorer — strip them for display only. URL hashes and DB
// lookups still use the canonical bracketed form.
function stripPlaceholderBrackets(s) {
  return String(s).replace(/^<(.+)>$/, "$1");
}
function displayPath(keyPath) {
  return splitKeyPath(keyPath).map(stripPlaceholderBrackets).join(".");
}
function formatDefaultSummary(parsed, raw) {
  if (Array.isArray(parsed)) return `list, ${parsed.length} item${parsed.length === 1 ? "" : "s"}`;
  if (parsed && typeof parsed === "object") {
    const count = Object.keys(parsed).length;
    return `dict, ${count} key${count === 1 ? "" : "s"}`;
  }
  return raw.length > 160 ? "large default" : raw;
}
function defaultValueParts(value, noneLabel = "-") {
  if (!value) return { hasValue: false, summary: noneLabel, full: noneLabel, large: false };
  const raw = String(value);
  let parsed = null;
  let parseOk = false;
  try {
    parsed = JSON.parse(raw);
    parseOk = true;
  } catch {
    // Keep non-JSON defaults as plain text.
  }
  const full = parseOk ? JSON.stringify(parsed, null, 2) : raw;
  const large = raw.length > 160 || full.length > 240 || full.includes("\n");
  return {
    hasValue: true,
    summary: large ? formatDefaultSummary(parseOk ? parsed : null, raw) : raw,
    full,
    large,
  };
}
function renderDefaultValue(value, options = {}) {
  const parts = defaultValueParts(value, options.noneLabel || "-");
  if (!parts.hasValue || !parts.large) return `<code>${escapeHtml(parts.summary)}</code>`;
  if (options.compact) return `<code class="schema-default-compact" title="${escapeAttr(parts.summary)}">${escapeHtml(parts.summary)}</code>`;
  const openAttr = options.open ? " open" : "";
  return `
    <details class="schema-default-details"${openAttr}>
      <summary class="schema-default-summary"><code>${escapeHtml(parts.summary)}</code></summary>
      <pre class="schema-default-full"><code>${escapeHtml(parts.full)}</code></pre>
    </details>`;
}
function rowModule(row, currentModule) {
  return currentModule === "all" ? row.module : currentModule;
}
function treeRowId(row, currentModule) {
  return `${rowModule(row, currentModule)}:${row.key_path}`;
}
function treeParentId(row, currentModule) {
  return row.parent_path ? `${rowModule(row, currentModule)}:${row.parent_path}` : "";
}
function treeGroupId(row, currentModule) {
  const root = rootSegment(row.key_path);
  return currentModule === "all" ? `${rowModule(row, currentModule)}:${root}` : root;
}

// Where the SPA fetches `schema.sqlite` from. Resolution order:
//   1. `window.SCHEMA_BASE_OVERRIDE` — explicit opt-out for hosts that already
//      know exactly where the data lives.
//   2. The directory containing this script, with `/data` appended. Works for
//      both the standalone `_assets/schema-explorer/index.html` page (script
//      lives under `_assets/schema-explorer/js/app.js`) and arbitrary MkDocs
//      pages that embed `<schema-explorer>` — fetches must be absolute since
//      the page URL is unrelated to the asset location.
//   3. Plain `data/` — last-resort relative path, kept for hand-rolled hosts.
function inferSchemaBase() {
  if (typeof window !== "undefined" && window.SCHEMA_BASE_OVERRIDE) return window.SCHEMA_BASE_OVERRIDE;
  const scripts = document.getElementsByTagName("script");
  for (const s of scripts) {
    if (s.src && /\/schema-explorer\/js\/app\.js(\?|$)/.test(s.src)) {
      return s.src.replace(/\/js\/app\.js.*$/, "/data");
    }
  }
  return "data";
}
const SCHEMA_BASE = inferSchemaBase();
const DEFAULT_RELEASE = "devel";

// SCHEMA_MODULES keys are the canonical module IDs stored in SQLite and used
// in URL hashes; `name` is the user-visible label rendered in the UI.
const SCHEMA_MODULES = {
  eos_designs: {
    name: "AVD Design",
    icon: "bi-diagram-3",
    description: "Fabric design data model — topology, addressing, network services, connected endpoints, and tenants.",
  },
  eos_cli_config_gen: {
    name: "EOS Config",
    icon: "bi-file-earmark-code",
    description: "Device configuration data model — interfaces, routing, ACLs, AAA, management, and platform settings.",
  },
};

const dbCache = new Map();    // release -> sql.js Database
let SQL = null;
const app = document.getElementById("app");

// ── boot ─────────────────────────────────────────────────────────────────────
//
// Two mount modes share this script:
//
//   * **Standalone**: a page declares `<main id="app">` + `<select id="release-select">`
//     (the SPA's own `index.html` at `/_assets/schema-explorer/index.html`).
//     Uses the URL hash for routing — landing / module / var-detail views.
//
//   * **Embed**: any docs page drops one or more `<schema-explorer>` custom
//     elements. Each embed is self-contained, scoped to a (release, module,
//     root) tuple via data attributes, and never touches `location.hash`.
//     Multiple embeds on the same page share `dbCache`.
//
// Both modes can coexist — embeds work even when `#app` is also present.

// CDN dependencies are lazy-loaded so docs pages that never host an embed
// do not pay for the extra script/font requests. Do not inject Bootstrap CSS
// here: it contains global element rules for headings, links, body line-height,
// etc. that leak into Material chrome. The standalone SPA owns the whole page
// and loads Bootstrap CSS directly from static/index.html.
const CDN_DEPS = {
  css: [
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
  ],
  js: [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
    "https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/sql-wasm.js",
  ],
};

function _hasTagWithUrl(selector, attr, url) {
  for (const el of document.querySelectorAll(selector)) {
    if (el.getAttribute(attr) === url) return true;
  }
  return false;
}

function _loadCss(href) {
  if (_hasTagWithUrl("link[rel='stylesheet']", "href", href)) return Promise.resolve();
  return new Promise((resolve, reject) => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    link.onload = resolve;
    link.onerror = () => reject(new Error(`Failed to load ${href}`));
    document.head.appendChild(link);
  });
}

function _loadScript(src) {
  if (_hasTagWithUrl("script", "src", src)) return Promise.resolve();
  return new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = src;
    s.onload = resolve;
    s.onerror = () => reject(new Error(`Failed to load ${src}`));
    document.head.appendChild(s);
  });
}

async function ensureDeps() {
  await Promise.all(CDN_DEPS.css.map(_loadCss));
  // Scripts must load in order — Bootstrap before sql.js doesn't strictly
  // matter, but doing them sequentially makes ordering predictable.
  for (const src of CDN_DEPS.js) await _loadScript(src);
}

async function ensureSqlJs() {
  if (SQL) return SQL;
  await ensureDeps();
  SQL = await initSqlJs({
    locateFile: f => `https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/${f}`,
  });
  return SQL;
}

// Delegated handler for tree-row chevron clicks. Lives at document level so
// it survives every renderResults innerHTML refresh and works across multiple
// embed roots on the same page.
document.addEventListener("click", e => {
  const icon = e.target.closest(".tree-toggle-icon");
  if (!icon) return;
  e.preventDefault();
  e.stopPropagation();
  const row = icon.closest("tr.schema-tree-row");
  if (!row) return;
  const wasExpanded = row.dataset.expanded === "1";
  row.dataset.expanded = wasExpanded ? "0" : "1";
  icon.classList.toggle("bi-chevron-right", wasExpanded);
  icon.classList.toggle("bi-chevron-down", !wasExpanded);
  applyTreeVisibility(row.closest(".schema-group"));
});

(async function boot() {
  const embeds = document.querySelectorAll("schema-explorer");
  const hasStandalone = !!app;
  if (!embeds.length && !hasStandalone) return;   // page doesn't host the explorer

  await ensureSqlJs();

  if (hasStandalone) {
    window.addEventListener("hashchange", route);
    const releaseSelect = document.getElementById("release-select");
    if (releaseSelect) {
      releaseSelect.addEventListener("change", e => {
        const path = location.hash.slice(1) || "/";
        location.hash = path + (path.includes("?") ? "&" : "?") + "release=" + encodeURIComponent(e.target.value);
      });
    }
    await route();
  }

  for (const el of embeds) {
    try { await mountEmbed(el); }
    catch (err) { failEmbed(el, err.message); }
  }
})().catch(err => {
  if (app) fail("Failed to initialise: " + err.message);
  else console.error("Schema Explorer init failed:", err);
});

// Per-group tree visibility — a row is shown iff every ancestor along its
// parent_path chain has data-expanded="1". Used by the chevron handler and
// by the group-level Expand/Collapse all buttons.
function applyTreeVisibility(groupEl) {
  if (!groupEl) return;
  const rows = groupEl.querySelectorAll("tr.schema-tree-row");
  const byPath = new Map();
  for (const r of rows) byPath.set(r.dataset.rowId, r);
  for (const r of rows) {
    const depth = parseInt(r.dataset.depth, 10);
    if (depth === 1) { r.style.display = ""; continue; }
    let p = r.dataset.parentId;
    let visible = true;
    while (p) {
      const parentRow = byPath.get(p);
      if (!parentRow || parentRow.dataset.expanded !== "1") { visible = false; break; }
      p = parentRow.dataset.parentId;
    }
    r.style.display = visible ? "" : "none";
  }
}

// ── hash router ──────────────────────────────────────────────────────────────

function parseHash() {
  const raw = location.hash.slice(1) || "/";
  const [pathPart, queryPart] = raw.split("?");
  const params = new URLSearchParams(queryPart || "");
  // Decode each segment so a key_path like `aaa_accounting.commands.default[].commands`
  // (which sits in the URL as `aaa_accounting.commands.default%5B%5D.commands`)
  // matches the literal value stored in SQLite.
  const segments = pathPart.split("/").filter(Boolean).map(s => {
    try { return decodeURIComponent(s); } catch { return s; }
  });
  return { segments, params };
}

async function route() {
  const { segments, params } = parseHash();
  const release = params.get("release") || DEFAULT_RELEASE;
  document.getElementById("release-select").value = release;
  try {
    const db = await getDb(release);
    if (segments.length === 0)             return renderLanding(db, release);
    if (segments.length === 1)             return renderModule(db, release, segments[0]);
    return renderVarDetail(db, release, segments[0], segments.slice(1).join("/"));
  } catch (err) {
    fail(err.message);
  }
}

function fail(msg) {
  app.innerHTML = `<div class="alert alert-danger m-3"><i class="bi bi-exclamation-triangle me-2"></i>${escapeHtml(msg)}</div>`;
}

// ── sqlite loader ────────────────────────────────────────────────────────────

async function getDb(release) {
  if (dbCache.has(release)) return dbCache.get(release);
  if (app) {
    app.innerHTML = `<div class="text-center py-5 text-muted">
      <span class="spinner-border spinner-border-sm"></span>
      <span class="ms-2 small">Loading ${release} schema…</span>
    </div>`;
  }
  const url = `${SCHEMA_BASE}/${release}/schema.sqlite`;
  // cache: "no-cache" forces a conditional GET so the browser revalidates
  // against the server's Last-Modified / ETag every page load. Keeps the
  // bytes cached locally when nothing changed (304), but picks up a freshly
  // regenerated SQLite immediately without a hard reload.
  const buf = await fetch(url, { cache: "no-cache" }).then(r => {
    if (!r.ok) throw new Error(`Could not load ${url} (${r.status})`);
    return r.arrayBuffer();
  });
  const db = new SQL.Database(new Uint8Array(buf));
  dbCache.set(release, db);
  return db;
}

// ── query helpers ────────────────────────────────────────────────────────────

function rows(db, sql, params = []) {
  const stmt = db.prepare(sql);
  stmt.bind(params);
  const out = [];
  while (stmt.step()) out.push(stmt.getAsObject());
  stmt.free();
  return out;
}

function getStats(db, release) {
  return rows(db, "SELECT module, var_count, loaded_at FROM schema_meta WHERE release = ?", [release]);
}

function getCategoryCounts(db, release, module) {
  if (module === "all") {
    return rows(db, "SELECT category, COUNT(*) AS count FROM schema_vars WHERE release = ? GROUP BY category ORDER BY category", [release]);
  }
  return rows(db, "SELECT category, COUNT(*) AS count FROM schema_vars WHERE release = ? AND module = ? GROUP BY category ORDER BY category", [release, module]);
}

function searchVars(db, release, module, opts = {}) {
  const conds = ["release = ?"];
  const ps = [release];
  if (module !== "all") { conds.push("module = ?"); ps.push(module); }
  if (opts.q) { conds.push("(key_path LIKE ? OR description LIKE ?)"); ps.push(`%${opts.q}%`, `%${opts.q}%`); }
  if (opts.requiredOnly) conds.push("required = 1");
  if (opts.showDeprecated && opts.showRemoved) conds.push("(deprecated = 1 OR removed = 1)");
  else if (opts.showDeprecated) conds.push("deprecated = 1");
  else if (opts.showRemoved) conds.push("removed = 1");
  if (opts.category) { conds.push("category = ?"); ps.push(opts.category); }
  if (opts.docTable) { conds.push("doc_table = ?"); ps.push(opts.docTable); }
  const sql = `SELECT * FROM schema_vars WHERE ${conds.join(" AND ")} ORDER BY key_path LIMIT ${opts.limit || 500}`;
  return rows(db, sql, ps);
}

function getDocTableCounts(db, release, module) {
  if (module === "all") {
    return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars WHERE release = ? GROUP BY doc_table ORDER BY doc_table", [release]);
  }
  return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars WHERE release = ? AND module = ? GROUP BY doc_table ORDER BY doc_table", [release, module]);
}

function isFilterActive(state) {
  return !!(state.q || state.requiredOnly || state.showDeprecated || state.showRemoved || state.category || state.docTable);
}

function lifecycleBadge(v) {
  if (v.removed) return `<span class="badge bg-danger">removed</span>`;
  if (v.deprecated) return `<span class="badge bg-warning text-dark">deprecated</span>`;
  return `<span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "-")}</span>`;
}

function getVar(db, release, module, key_path) {
  const r = rows(db, "SELECT * FROM schema_vars WHERE release = ? AND module = ? AND key_path = ?", [release, module, key_path]);
  return r[0] || null;
}

function getChildren(db, release, module, parent_path) {
  return rows(db, "SELECT * FROM schema_vars WHERE release = ? AND module = ? AND parent_path = ? ORDER BY key_path", [release, module, parent_path]);
}

function getSiblings(db, release, module, parent_path, exclude_key) {
  return rows(db, "SELECT key_path, var_type FROM schema_vars WHERE release = ? AND module = ? AND parent_path = ? AND key_path != ? ORDER BY key_path", [release, module, parent_path, exclude_key]);
}

// ── views ────────────────────────────────────────────────────────────────────

function renderLanding(db, release) {
  const stats = Object.fromEntries(getStats(db, release).map(s => [s.module, s]));
  const cards = Object.entries(SCHEMA_MODULES).map(([id, mod]) => {
    const s = stats[id] || {};
    const count = s.var_count || 0;
    return `
      <div class="col">
        <a href="#/${id}?release=${release}" class="text-decoration-none d-block h-100">
          <div class="card h-100 border-0 shadow-sm module-card">
            <div class="card-body d-flex flex-column">
              <div class="d-flex align-items-start mb-2">
                <span class="fs-3 me-2 brand-color"><i class="bi ${mod.icon}"></i></span>
                <div class="me-auto">
                  <h6 class="mb-0 fw-semibold">${escapeHtml(mod.name)}</h6>
                  <div class="text-muted" style="font-size:0.7rem;"><code>${id}</code></div>
                  <span class="badge mt-1" style="background-color:#198754; font-size:0.65rem;">${count} variables</span>
                </div>
              </div>
              <p class="text-muted small mb-0">${escapeHtml(mod.description)}</p>
            </div>
          </div>
        </a>
      </div>`;
  }).join("");

  app.innerHTML = `
    <div class="d-flex align-items-center mb-3">
      <h4 class="fw-bold mb-0 brand-color"><i class="bi bi-search me-2"></i>Schema Explorer</h4>
      <span class="badge ms-2" style="background-color: #16325B;">aristanetworks/avd</span>
    </div>
    <p class="text-muted small mb-3">
      Browse the AVD data model schemas. Select a module to explore variables, search by key path, and view detailed documentation.
    </p>
    <div class="row row-cols-1 row-cols-md-2 g-3 mb-4">${cards}</div>
    <div class="row mb-4"><div class="col">
      <a href="#/all?release=${release}" class="text-decoration-none d-block">
        <div class="card border-0 shadow-sm module-card">
          <div class="card-body d-flex align-items-center">
            <span class="fs-3 me-3 brand-color"><i class="bi bi-search"></i></span>
            <div>
              <h6 class="mb-0 fw-semibold">Search All Modules</h6>
              <p class="text-muted small mb-0">Search across both AVD Design and EOS Config schemas</p>
            </div>
          </div>
        </div>
      </a>
    </div></div>`;
}

function renderModule(db, release, module) {
  const isAll = module === "all";
  if (!isAll && !SCHEMA_MODULES[module]) return fail(`Module not found: ${module}`);

  const stats = getStats(db, release);
  const moduleStats = isAll
    ? { var_count: stats.reduce((s, x) => s + x.var_count, 0) }
    : stats.find(s => s.module === module) || {};
  const info = isAll
    ? { name: "All Modules", icon: "bi-search", description: "Search across both AVD Design and EOS Config schemas." }
    : SCHEMA_MODULES[module];

  const categories = getCategoryCounts(db, release, module);
  const docTables = getDocTableCounts(db, release, module);
  const total = moduleStats.var_count || 0;

  app.innerHTML = `
    <div class="d-flex align-items-center mb-3">
      <a href="#/?release=${release}" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>
      <div>
        <h4 class="mb-1 fw-bold brand-color"><i class="bi ${info.icon} me-2"></i>${escapeHtml(info.name)}${isAll ? "" : ` <small class="text-muted fw-normal" style="font-size:0.6em;"><code>${escapeHtml(module)}</code></small>`}</h4>
        ${total ? `<span class="badge" style="background-color:#198754; font-size:0.65rem;">${total} variables</span>` : ""}
      </div>
    </div>
    <p class="text-muted small mb-3">${info.description}</p>

    <form id="filter-form" class="mb-3 schema-filter-sticky" onsubmit="return false">
      <div class="d-flex flex-wrap align-items-center gap-3">
        <div class="flex-grow-1" style="min-width: 200px;">
          <div class="input-group input-group-sm">
            <span class="input-group-text"><i class="bi bi-search"></i></span>
            <input type="search" class="form-control" id="q" placeholder="Search key paths or descriptions…">
          </div>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="req">
          <label class="form-check-label small" for="req">Required only</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="dep">
          <label class="form-check-label small" for="dep">Deprecated</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="rem">
          <label class="form-check-label small" for="rem">Removed</label>
        </div>
        <div class="btn-group btn-group-sm" role="group" aria-label="View mode">
          <button type="button" class="btn btn-outline-secondary active" id="btn-view-tree" title="Tree view"><i class="bi bi-diagram-3"></i></button>
          <button type="button" class="btn btn-outline-secondary" id="btn-view-flat" title="Flat view"><i class="bi bi-list-ul"></i></button>
        </div>
      </div>
    </form>

    <div class="row g-3 schema-module-layout">
      <div class="col-lg-3 col-xl-2">
        <div class="card border-0 shadow-sm" style="position: sticky; top: 1rem;">
          <div class="card-header bg-light py-2 d-flex justify-content-between align-items-center">
            <span class="fw-semibold small brand-color"><i class="bi bi-tag me-1"></i>Browse by</span>
            <div class="btn-group btn-group-sm" role="group" aria-label="Classifier mode">
              <button type="button" class="btn btn-outline-secondary active" id="btn-classifier-category" title="Rule-based categories">Categories</button>
              <button type="button" class="btn btn-outline-secondary" id="btn-classifier-doc-table" title="documentation_options.table from schema">Tables</button>
            </div>
          </div>
          <div class="list-group list-group-flush" id="category-list" data-classifier-pane="category" style="max-height: 70vh; overflow-y: auto;">
            <a href="#" class="list-group-item list-group-item-action d-flex justify-content-between active" data-classifier="category" data-value="">
              <span>All</span><span class="badge bg-secondary rounded-pill">${total}</span>
            </a>
            ${categories.map(c => `
              <a href="#" class="list-group-item list-group-item-action d-flex justify-content-between" data-classifier="category" data-value="${escapeAttr(c.category || "")}">
                <span>${escapeHtml(c.category || "(none)")}</span><span class="badge bg-secondary rounded-pill">${c.count}</span>
              </a>`).join("")}
          </div>
          <div class="list-group list-group-flush" id="doc-table-list" data-classifier-pane="doc_table" style="max-height: 70vh; overflow-y: auto; display: none;">
            <a href="#" class="list-group-item list-group-item-action d-flex justify-content-between active" data-classifier="doc_table" data-value="">
              <span>All</span><span class="badge bg-secondary rounded-pill">${total}</span>
            </a>
            ${docTables.map(t => `
              <a href="#" class="list-group-item list-group-item-action d-flex justify-content-between" data-classifier="doc_table" data-value="${escapeAttr(t.doc_table || "")}">
                <span>${escapeHtml(t.doc_table || "(none)")}</span><span class="badge bg-secondary rounded-pill">${t.count}</span>
              </a>`).join("")}
          </div>
        </div>
      </div>
      <div class="col-lg-9 col-xl-10">
        <div class="card border-0 shadow-sm"><div id="results"></div></div>
      </div>
    </div>`;

  const state = {
    q: "", requiredOnly: false, showDeprecated: false, showRemoved: false,
    category: "", docTable: "", view: "tree", classifier: "category",
  };
  const refresh = debounce(() => renderResults(db, release, module, state), 250);

  document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; refresh(); });
  document.getElementById("req").addEventListener("change", e => { state.requiredOnly = e.target.checked; refresh(); });
  document.getElementById("dep").addEventListener("change", e => { state.showDeprecated = e.target.checked; refresh(); });
  document.getElementById("rem").addEventListener("change", e => { state.showRemoved = e.target.checked; refresh(); });

  const btnTree = document.getElementById("btn-view-tree");
  const btnFlat = document.getElementById("btn-view-flat");
  btnTree.addEventListener("click", () => { state.view = "tree"; btnTree.classList.add("active"); btnFlat.classList.remove("active"); refresh(); });
  btnFlat.addEventListener("click", () => { state.view = "flat"; btnFlat.classList.add("active"); btnTree.classList.remove("active"); refresh(); });

  function highlightActive() {
    app.querySelectorAll(`[data-classifier="${state.classifier}"]`).forEach(el => {
      const value = state.classifier === "category" ? state.category : state.docTable;
      el.classList.toggle("active", (el.dataset.value || "") === (value || ""));
    });
  }

  const classifierContainer = document.getElementById("category-list").parentElement;
  classifierContainer.addEventListener("click", e => {
    const item = e.target.closest("[data-classifier]");
    if (!item || item.dataset.classifier !== state.classifier || !classifierContainer.contains(item)) return;
    if (item.tagName === "A") e.preventDefault();
    if (state.classifier === "category") { state.category = item.dataset.value || ""; state.docTable = ""; }
    else { state.docTable = item.dataset.value || ""; state.category = ""; }
    highlightActive();
    refresh();
  });

  const btnCatMode = document.getElementById("btn-classifier-category");
  const btnTabMode = document.getElementById("btn-classifier-doc-table");
  function setClassifierMode(mode) {
    state.classifier = mode;
    btnCatMode.classList.toggle("active", mode === "category");
    btnTabMode.classList.toggle("active", mode === "doc_table");
    app.querySelectorAll("[data-classifier-pane]").forEach(p => {
      p.style.display = p.dataset.classifierPane === mode ? "" : "none";
    });
    state.category = "";
    state.docTable = "";
    highlightActive();
    refresh();
  }
  btnCatMode.addEventListener("click", () => setClassifierMode("category"));
  btnTabMode.addEventListener("click", () => setClassifierMode("doc_table"));

  renderResults(db, release, module, state);
}

function renderResults(db, release, module, state) {
  const target = document.getElementById("results");
  // Tree view needs every row in the active scope so the hierarchy is
  // complete — anything dropped at the SQL boundary disappears from the tree
  // entirely (eos_cli_config_gen has 6.4k rows; "all modules" hits ~12.6k).
  // Flat list view caps at 500 since users only consume the head visibly.
  const limit = state.view === "tree" ? 20000 : 500;
  const results = searchVars(db, release, module, { ...state, limit });
  if (!results.length) {
    target.innerHTML = `<div class="text-center py-5 text-muted"><i class="bi bi-inbox fs-3 d-block mb-2"></i><span class="small">No variables match.</span></div>`;
    return;
  }
  if (state.view === "tree") return renderTreeResults(target, db, release, module, state, results);
  const isAll = module === "all";
  const rowsHtml = results.map(v => {
    const mod = isAll ? v.module : module;
    const link = `#/${mod}/${encodeURI(v.key_path)}?release=${release}`;
    const modBadge = isAll ? `<td><span class="badge ${v.module === "eos_designs" ? "bg-primary" : "bg-success"}">${escapeHtml(SCHEMA_MODULES[v.module]?.name || v.module)}</span></td>` : "";
    return `
      <tr>
        ${modBadge}
        <td class="px-3"><a href="${link}" class="link-brand text-decoration-none"><code class="fw-bold" style="font-size: 0.82rem;">${highlight(displayPath(v.key_path), state.q)}</code></a></td>
        <td>${lifecycleBadge(v)}</td>
        <td class="text-muted small">${renderDefaultValue(v.default_value, { compact: true })}</td>
        <td class="text-center">${v.required ? `<i class="bi bi-check-circle-fill text-success"></i>` : ""}</td>
        <td class="text-muted small">${highlight(v.description || "-", state.q)}</td>
      </tr>`;
  }).join("");
  target.innerHTML = `
    <div class="px-3 py-2 text-muted small border-bottom">${results.length} variable${results.length === 1 ? "" : "s"} ${results.length >= 500 ? "(showing first 500)" : "found"}</div>
    <div class="table-responsive">
      <table class="table table-sm table-hover align-middle mb-0">
        <thead class="table-light"><tr>
          ${isAll ? `<th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Module</th>` : ""}
          <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key Path</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Default</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem; width: 30px;">Req</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
        </tr></thead>
        <tbody>${rowsHtml}</tbody>
      </table>
    </div>`;
}

let _treeRenderSeq = 0;

function renderTreeResults(target, db, release, module, state, matches) {
  const isAll = module === "all";
  const filtered = isFilterActive(state);
  // Per-render id prefix so multiple trees (e.g. several embeds on one page)
  // don't collide on Bootstrap collapse `data-bs-target` lookups.
  const idPrefix = `t${++_treeRenderSeq}`;

  // When a filter is active, walk parent chains via the parent_path column
  // and emit ancestor rows (tagged is_context) so the hierarchical structure
  // stays intact. Fetched in batched DB queries — the previous "load up to
  // 5000 vars and filter in JS" approach silently dropped any group whose
  // root sorts past the 5000th alphabetical key (e.g. `vlan_interfaces` in
  // eos_cli_config_gen).
  let rowsForGroups;
  if (filtered && matches.length) {
    const knownByPath = new Map(matches.map(v => [treeRowId(v, module), v]));
    const ancestorRows = [];
    let toFetch = [];
    for (const v of matches) {
      const parentId = treeParentId(v, module);
      if (v.parent_path && !knownByPath.has(parentId)) toFetch.push({ module: rowModule(v, module), keyPath: v.parent_path });
    }
    toFetch = [...new Map(toFetch.map(v => [`${v.module}:${v.keyPath}`, v])).values()];
    while (toFetch.length) {
      const fetched = [];
      const fetchByModule = new Map();
      for (const item of toFetch) {
        if (!fetchByModule.has(item.module)) fetchByModule.set(item.module, []);
        fetchByModule.get(item.module).push(item.keyPath);
      }
      for (const [fetchModule, keyPaths] of fetchByModule.entries()) {
        const placeholders = keyPaths.map(() => "?").join(",");
        fetched.push(...rows(db, `SELECT * FROM schema_vars WHERE release = ? AND module = ? AND key_path IN (${placeholders})`, [release, fetchModule, ...keyPaths]));
      }
      ancestorRows.push(...fetched);
      const next = [];
      for (const a of fetched) {
        knownByPath.set(treeRowId(a, module), a);
        const parentId = treeParentId(a, module);
        if (a.parent_path && !knownByPath.has(parentId)) next.push({ module: rowModule(a, module), keyPath: a.parent_path });
      }
      toFetch = [...new Map(next.map(v => [`${v.module}:${v.keyPath}`, v])).values()];
    }
    rowsForGroups = [
      ...matches.map(v => ({ ...v, is_context: false })),
      ...ancestorRows.map(v => ({ ...v, is_context: true })),
    ];
  } else {
    rowsForGroups = matches.map(v => ({ ...v, is_context: false }));
  }

  const groups = new Map();
  const matchCounts = new Map();
  for (const v of rowsForGroups) {
    const groupId = treeGroupId(v, module);
    const root = rootSegment(v.key_path);
    if (!groups.has(groupId)) groups.set(groupId, { root, module: rowModule(v, module), vars: [] });
    groups.get(groupId).vars.push(v);
    if (!v.is_context) matchCounts.set(groupId, (matchCounts.get(groupId) || 0) + 1);
  }
  const sorted = [...groups.entries()].sort(([, a], [, b]) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`));
  const total = matches.length;

  const groupsHtml = sorted.map(([groupId, group], idx) => {
    const { root, vars } = group;
    vars.sort((a, b) => `${rowModule(a, module)}:${a.key_path}`.localeCompare(`${rowModule(b, module)}:${b.key_path}`));
    const id = `${idPrefix}-group-${idx}`;
    const cat = vars[0].category;
    // Pre-compute which paths have children inside this group, so we know
    // which rows should render a chevron and which are leaves.
    const childCount = new Map();
    for (const v of vars) {
      const parentId = treeParentId(v, module);
      if (parentId) childCount.set(parentId, (childCount.get(parentId) || 0) + 1);
    }
    // Render rows in parent-first order, including ancestor context rows
    // fetched after filter matches.
    const rowsHtml = vars.map(v => {
      const mod = isAll ? v.module : module;
      const link = `#/${mod}/${encodeURI(v.key_path)}?release=${release}`;
      const leaf = leafSegment(v.key_path);
      const depth = v.depth || 1;
      const indent = (depth - 1) * 1.25;
      const modBadge = isAll ? `<td><span class="badge ${v.module === "eos_designs" ? "bg-primary" : "bg-success"}">${escapeHtml(SCHEMA_MODULES[v.module]?.name || v.module)}</span></td>` : "";
      const rowId = treeRowId(v, module);
      const parentId = treeParentId(v, module);
      const isBranch = (childCount.get(rowId) || 0) > 0;
      // Context rows (ancestors of matches when a filter is active) start
      // expanded so the matched descendants are visible by default.
      const initiallyExpanded = v.is_context;
      const chevron = isBranch
        ? `<i class="bi ${initiallyExpanded ? "bi-chevron-down" : "bi-chevron-right"} tree-toggle-icon" style="cursor: pointer; width: 1rem; display: inline-block; margin-right: 0.15rem;"></i>`
        : `<span style="display: inline-block; width: 1.15rem;"></span>`;
      const styleAttr = v.is_context
        ? ` style="opacity: 0.55;"`
        : (depth > 1 ? ` style="display: none;"` : "");
      return `
        <tr class="schema-tree-row${v.is_context ? " schema-row-context" : ""}"
            data-row-id="${escapeAttr(rowId)}"
            data-parent-id="${escapeAttr(parentId)}"
            data-is-branch="${isBranch ? "1" : "0"}"
            data-depth="${depth}"
            data-expanded="${initiallyExpanded ? "1" : "0"}"${styleAttr}>
          ${modBadge}
          <td class="px-3">
            <span class="schema-tree-indent" style="padding-left: ${indent}rem;">${chevron}<a href="${link}" class="link-brand text-decoration-none" title="${escapeAttr(v.key_path)}"><code class="fw-bold" style="font-size: 0.82rem;">${highlight(leaf, state.q)}</code></a></span>
          </td>
          <td>${lifecycleBadge(v)}</td>
          <td class="text-muted small">${renderDefaultValue(v.default_value, { compact: true })}</td>
          <td class="text-center">${v.required ? `<i class="bi bi-check-circle-fill text-success"></i>` : ""}</td>
          <td class="text-muted small">${highlight(v.description || "-", state.q)}</td>
        </tr>`;
    }).join("");
    const groupCount = matchCounts.get(groupId) ?? vars.length;
    const groupModuleBadge = isAll ? `<span class="badge ${group.module === "eos_designs" ? "bg-primary" : "bg-success"} ms-1" style="font-size: 0.6rem;">${escapeHtml(SCHEMA_MODULES[group.module]?.name || group.module)}</span>` : "";
    return `
      <div class="schema-group" data-group-id="${id}">
        <div class="schema-group-header" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="false" aria-controls="${id}">
          <i class="bi bi-chevron-right collapse-icon"></i>
          <code class="fw-bold" style="font-size: 0.88rem;">${highlight(root, state.q)}</code>
          ${groupModuleBadge}
          <span class="badge bg-secondary ms-1" style="font-size: 0.6rem;">${groupCount}</span>
          ${cat ? `<span class="badge schema-category-badge ms-1">${escapeHtml(cat)}</span>` : ""}
        </div>
        <div class="collapse" id="${id}">
          <div class="table-responsive">
            <table class="table table-sm table-hover align-middle mb-0" style="table-layout: fixed; width: 100%;">
              <colgroup>
                ${isAll ? `<col style="width: 9rem;">` : ""}
                <col>
                <col style="width: 7rem;">
                <col style="width: 8rem;">
                <col style="width: 3rem;">
                <col style="width: 38%;">
              </colgroup>
              <thead class="table-light"><tr>
                ${isAll ? `<th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Module</th>` : ""}
                <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key</th>
                <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
                <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Default</th>
                <th class="text-muted small text-uppercase text-center" style="font-size: 0.72rem;">Req</th>
                <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
              </tr></thead>
              <tbody>${rowsHtml}</tbody>
            </table>
          </div>
        </div>
      </div>`;
  }).join("");

  target.innerHTML = `
    <div class="px-3 py-2 d-flex align-items-center justify-content-between border-bottom">
      <span class="text-muted small">${total} variable${total === 1 ? "" : "s"} in ${sorted.length} group${sorted.length === 1 ? "" : "s"}</span>
      <div>
        <button type="button" class="btn btn-sm btn-link text-muted p-0 me-2" data-tree-action="expand-all"><i class="bi bi-arrows-expand"></i> <span class="small">Expand all</span></button>
        <button type="button" class="btn btn-sm btn-link text-muted p-0" data-tree-action="collapse-all"><i class="bi bi-arrows-collapse"></i> <span class="small">Collapse all</span></button>
      </div>
    </div>
    ${groupsHtml}`;

  function setAllTreeRows(expanded) {
    target.querySelectorAll("tr.schema-tree-row").forEach(r => {
      if (r.dataset.isBranch === "1") {
        r.dataset.expanded = expanded ? "1" : "0";
        const icon = r.querySelector(".tree-toggle-icon");
        if (icon) {
          icon.classList.toggle("bi-chevron-right", !expanded);
          icon.classList.toggle("bi-chevron-down", expanded);
        }
      }
    });
    target.querySelectorAll(".schema-group").forEach(applyTreeVisibility);
  }

  target.querySelector("[data-tree-action='expand-all']")?.addEventListener("click", () => {
    target.querySelectorAll(".collapse").forEach(el => bootstrap.Collapse.getOrCreateInstance(el, { toggle: false }).show());
    target.querySelectorAll(".schema-group-header").forEach(el => el.setAttribute("aria-expanded", "true"));
    setAllTreeRows(true);
  });
  target.querySelector("[data-tree-action='collapse-all']")?.addEventListener("click", () => {
    target.querySelectorAll(".collapse").forEach(el => bootstrap.Collapse.getOrCreateInstance(el, { toggle: false }).hide());
    target.querySelectorAll(".schema-group-header").forEach(el => el.setAttribute("aria-expanded", "false"));
    setAllTreeRows(false);
  });
}

function renderVarDetail(db, release, module, key_path) {
  if (!SCHEMA_MODULES[module]) return fail(`Module not found: ${module}`);
  const v = getVar(db, release, module, key_path);
  if (!v) return fail(`Variable not found: ${module}/${key_path}`);

  const constraints = v.constraints ? JSON.parse(v.constraints) : {};
  const children = getChildren(db, release, module, key_path);
  const siblings = getSiblings(db, release, module, v.parent_path || "", key_path);
  const dynamicSource = dynamicKeySource(v.key_path);
  const siblingsTitle = v.parent_path
    ? "Sibling keys"
    : dynamicSource
      ? "Other dynamic root keys"
      : "Other root keys";
  const siblingsHelp = v.parent_path
    ? "Keys with the same parent."
    : dynamicSource
      ? "Other schema branches generated from configurable key names."
      : "Other top-level schema keys.";

  const validValuesHtml = constraints.valid_values ? `
    <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Valid Values</h5>
    <div class="card border-0 shadow-sm mb-4"><div class="card-body p-0">
      ${constraints.valid_values.map((val, i, arr) => `
        <div class="d-flex align-items-start px-3 py-2 ${i < arr.length - 1 ? "border-bottom" : ""}">
          <div class="me-3" style="min-width: 3.5rem;"><code class="schema-valid-value">${escapeHtml(String(val))}</code></div>
        </div>`).join("")}
    </div></div>` : "";

  const otherCons = ["min", "max", "min_length", "max_length", "pattern", "format"]
    .filter(k => constraints[k] !== undefined)
    .map(k => `<tr><td class="px-3 fw-semibold small text-muted" style="width:140px;">${k}</td><td><code>${escapeHtml(String(constraints[k]))}</code></td></tr>`)
    .join("");

  const childrenHtml = children.length ? `
    <h5 class="fw-bold brand-color mb-2"><i class="bi bi-diagram-2 me-2"></i>Child Variables
      <span class="badge bg-secondary ms-1" style="font-size: 0.65rem; vertical-align: middle;">${children.length}</span>
    </h5>
    <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
      <table class="table table-sm table-hover align-middle mb-0">
        <thead class="table-light"><tr>
          <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Req</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
        </tr></thead>
        <tbody>${children.map(c => `
          <tr>
            <td class="px-3"><a href="#/${module}/${encodeURI(c.key_path)}?release=${release}" class="link-brand text-decoration-none"><code class="fw-bold" style="font-size:0.82rem;">${escapeHtml(leafSegment(c.key_path))}</code></a></td>
            <td>${lifecycleBadge(c)}</td>
            <td class="text-center">${c.required ? `<i class="bi bi-check-circle-fill text-success"></i>` : ""}</td>
            <td class="text-muted small">${escapeHtml(c.description || "-")}</td>
          </tr>`).join("")}</tbody>
      </table>
    </div></div>` : "";

  const lifecycleHeader = v.removed
    ? `<span class="badge bg-danger ms-1">removed</span>`
    : v.deprecated
      ? `<span class="badge bg-warning text-dark ms-1">deprecated</span>`
      : "";
  app.innerHTML = `
    <div class="d-flex align-items-center mb-4">
      <a href="#/${module}?release=${release}" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>
      <div>
        <h4 class="mb-1 fw-bold brand-color"><code>${escapeHtml(displayPath(v.key_path))}</code></h4>
        <span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "unknown")}</span>
        ${lifecycleHeader}
        <span class="text-muted small ms-2">${escapeHtml(SCHEMA_MODULES[module]?.name || module)}</span>
      </div>
    </div>
    <div class="row g-3">
      <div class="col-lg-8">
        ${v.description ? `
          <h5 class="fw-bold brand-color mb-2"><i class="bi bi-info-circle me-2"></i>Description</h5>
          <div class="card border-0 shadow-sm mb-4"><div class="card-body"><p class="mb-0">${escapeHtml(v.description)}</p></div></div>` : ""}

        <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Properties</h5>
        <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
          <table class="table table-sm align-middle mb-0"><tbody>
            <tr><td class="px-3 fw-semibold small text-muted" style="width:140px;">Type</td><td><span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "-")}</span></td></tr>
            ${(v.removed || v.deprecated) ? `<tr><td class="px-3 fw-semibold small text-muted">Status</td><td>${v.removed ? `<span class="badge bg-danger">removed</span>` : `<span class="badge bg-warning text-dark">deprecated</span>`}</td></tr>` : ""}
            <tr><td class="px-3 fw-semibold small text-muted">Default</td><td>${renderDefaultValue(v.default_value, { noneLabel: "none", open: true })}</td></tr>
            <tr><td class="px-3 fw-semibold small text-muted">Required</td><td>${v.required ? `<span class="text-success"><i class="bi bi-check-circle-fill me-1"></i>Yes</span>` : `<span class="text-muted">No</span>`}</td></tr>
            ${v.category ? `<tr><td class="px-3 fw-semibold small text-muted">Category</td><td><span class="badge schema-category-badge">${escapeHtml(v.category)}</span></td></tr>` : ""}
            ${v.doc_table ? `<tr><td class="px-3 fw-semibold small text-muted">Doc table</td><td><span class="badge schema-category-badge" title="documentation_options.table from the AVD schema">${escapeHtml(v.doc_table)}</span></td></tr>` : ""}
            ${v.cross_ref ? renderCrossRefRow(v.cross_ref, release) : ""}
            ${v.parent_path ? `<tr><td class="px-3 fw-semibold small text-muted">Parent</td><td><a href="#/${module}/${encodeURI(v.parent_path)}?release=${release}" class="link-brand"><code>${escapeHtml(displayPath(v.parent_path))}</code></a></td></tr>` : ""}
          </tbody></table>
        </div></div>

        ${validValuesHtml}
        ${otherCons ? `<h5 class="fw-bold brand-color mb-2"><i class="bi bi-check2-square me-2"></i>Constraints</h5>
          <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
            <table class="table table-sm align-middle mb-0"><tbody>${otherCons}</tbody></table>
          </div></div>` : ""}
        ${childrenHtml}
      </div>

      <div class="col-lg-4">
        ${dynamicSource ? `
        <div class="card border-0 shadow-sm mb-3">
          <div class="card-header bg-light py-2"><span class="fw-semibold brand-color small"><i class="bi bi-braces me-1"></i>Dynamic key</span></div>
          <div class="card-body">
            <div class="text-muted small mb-2">This branch represents input keys named by:</div>
            <code class="small">${escapeHtml(dynamicSource)}</code>
          </div>
        </div>` : ""}
        ${siblings.length ? `
        <div class="card border-0 shadow-sm mb-3">
          <div class="card-header bg-light py-2">
            <div class="fw-semibold brand-color small"><i class="bi bi-collection me-1"></i>${siblingsTitle}</div>
            <div class="text-muted" style="font-size:0.7rem;">${siblingsHelp}</div>
          </div>
          <ul class="list-group list-group-flush" style="max-height: 300px; overflow-y: auto;">
            ${siblings.map(s => `
              <li class="list-group-item px-3 py-2 border-0 border-bottom">
                <a href="#/${module}/${encodeURI(s.key_path)}?release=${release}" class="link-brand small text-decoration-none">
                  <code>${escapeHtml(displayPath(s.key_path))}</code>
                </a>
                <span class="badge bg-light text-dark border ms-1" style="font-size:0.6rem;">${escapeHtml(s.var_type || "-")}</span>
              </li>`).join("")}
          </ul>
        </div>` : ""}
      </div>
    </div>`;
}

// ── cross-schema reference helper ───────────────────────────────────────────
// Schema $ref strings look like "eos_cli_config_gen#/keys/foo/keys/bar".
// Convert into a SchemaExplorer hash link to the equivalent flattened key_path
// in the target module so users can jump straight there.
function renderCrossRefRow(ref, release) {
  const [target, jsonPointer] = String(ref).split("#", 2);
  if (!target || !jsonPointer) return "";
  const segments = jsonPointer.split("/").filter(Boolean);
  const parts = [];
  for (let i = 0; i < segments.length; i++) {
    const seg = segments[i];
    if (seg === "keys") {
      // skip — next segment is the key name
    } else if (seg === "items") {
      if (parts.length) parts[parts.length - 1] += "[]";
    } else {
      parts.push(seg);
    }
  }
  const keyPath = parts.join(".");
  const link = keyPath
    ? `#/${target}/${encodeURI(keyPath)}?release=${release}`
    : `#/${target}?release=${release}`;
  return `<tr><td class="px-3 fw-semibold small text-muted">Cross-schema</td><td><a href="${link}" class="link-brand"><code>${escapeHtml(target)}</code> → <code>${escapeHtml(keyPath || "(root)")}</code></a></td></tr>`;
}

// ── utils ────────────────────────────────────────────────────────────────────

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;" }[c]));
}
function escapeAttr(s) { return escapeHtml(s).replace(/"/g, "&quot;"); }

function highlight(text, q) {
  if (!q || q.length < 2 || !text) return escapeHtml(text || "-");
  const lower = text.toLowerCase();
  const ql = q.toLowerCase();
  let out = "";
  let i = 0;
  while (i < text.length) {
    const idx = lower.indexOf(ql, i);
    if (idx < 0) { out += escapeHtml(text.slice(i)); break; }
    out += escapeHtml(text.slice(i, idx));
    out += `<mark class="schema-search-match">${escapeHtml(text.slice(idx, idx + q.length))}</mark>`;
    i = idx + q.length;
  }
  return out;
}

function debounce(fn, ms) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}

// ── embed mounting ──────────────────────────────────────────────────────────
//
// Renders a scoped tree view inside any <schema-explorer> element on the page.
// The element is treated like a sealed component: docs author drops the tag,
// the SPA fills it in.
//
// Supported data attributes:
//   release  — schema release tag (default: "devel")
//   module   — "eos_designs" | "eos_cli_config_gen" | "all" (default: "eos_designs")
//   root     — key_path prefix; only show that subtree (e.g. "router_bgp"). Optional.
//   view     — "tree" | "flat" (default: "tree")
//   height   — CSS max-height for the scroll container (default: "600px")
//   chrome   — "compact" | "none" (default: "compact"). "none" hides the
//              "N variables in M groups" / expand-all bar.

function _embedAttr(el, name, fallback) {
  return el.getAttribute(`data-${name}`) || el.getAttribute(name) || fallback;
}

function failEmbed(el, msg) {
  el.innerHTML = `<div class="alert alert-danger m-2 small"><i class="bi bi-exclamation-triangle me-1"></i>${escapeHtml(msg)}</div>`;
}

async function mountEmbed(el) {
  const release = _embedAttr(el, "release", DEFAULT_RELEASE);
  const module  = _embedAttr(el, "module", "eos_designs");
  const root    = _embedAttr(el, "root", "");
  const view    = _embedAttr(el, "view", "tree");
  const height  = _embedAttr(el, "height", "600px");
  const chrome  = _embedAttr(el, "chrome", "compact");

  // <schema-explorer> is an unknown HTML element → defaults to inline. Force
  // block + scroll container so the embed actually takes up space.
  Object.assign(el.style, {
    display: "block",
    maxHeight: height,
    overflow: "auto",
    border: "1px solid var(--md-default-fg-color--lightest, #e1e4e8)",
    borderRadius: "4px",
    margin: "0.75rem 0",
  });
  el.classList.add("schema-embed");
  el.innerHTML = `<div class="text-muted small p-3">
    <span class="spinner-border spinner-border-sm" role="status"></span>
    <span class="ms-2">Loading <code>${escapeHtml(module)}</code> schema…</span>
  </div>`;

  const db = await getDb(release);

  // Build the row set: scope to (module, root subtree). renderTreeResults
  // expects a list of matched vars; with no filter, that's just every row in
  // scope. With a `root` set, include the root itself plus its descendants so
  // the tree has a single rooted group.
  const conds = ["release = ?"];
  const ps = [release];
  if (module !== "all") { conds.push("module = ?"); ps.push(module); }
  if (root) {
    conds.push("(key_path = ? OR key_path LIKE ? OR key_path LIKE ?)");
    ps.push(root, `${root}.%`, `${root}[]%`);
  }
  const sql = `SELECT * FROM schema_vars WHERE ${conds.join(" AND ")} ORDER BY key_path LIMIT 20000`;
  const results = rows(db, sql, ps);
  if (!results.length) {
    failEmbed(el, `No variables match: module=${module}${root ? `, root=${root}` : ""}`);
    return;
  }

  const state = {
    q: "", requiredOnly: false, showDeprecated: false, showRemoved: false,
    category: "", docTable: "", view,
  };
  if (view === "tree") {
    renderTreeResults(el, db, release, module, state, results);
  } else {
    // Flat view — reuse renderResults by injecting a sub-container.
    const inner = document.createElement("div");
    el.innerHTML = "";
    el.appendChild(inner);
    // renderResults reads `#results` via getElementById, so wrap in a stub
    // that satisfies that contract just for this embed.
    inner.id = `embed-results-${++_treeRenderSeq}`;
    const origGet = document.getElementById.bind(document);
    document.getElementById = (id) => id === "results" ? inner : origGet(id);
    try { renderResults(el, db, release, module, state); }
    finally { document.getElementById = origGet; }
  }

  if (chrome === "none") {
    const header = el.querySelector(".border-bottom.d-flex, .border-bottom .text-muted")?.closest(".border-bottom");
    if (header) header.style.display = "none";
  }

  // Auto-expand the first (and usually only) group so the embed shows data
  // immediately instead of requiring a click.
  const firstCollapse = el.querySelector(".collapse");
  if (firstCollapse && typeof bootstrap !== "undefined") {
    bootstrap.Collapse.getOrCreateInstance(firstCollapse, { toggle: false }).show();
    el.querySelector(".schema-group-header")?.setAttribute("aria-expanded", "true");
  }
}
