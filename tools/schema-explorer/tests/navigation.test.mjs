import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appSource = await readFile(new URL("../static/js/app.js", import.meta.url), "utf8");

function loadApp(detailHost = null) {
  const document = {
    addEventListener() {},
    getElementById(id) {
      return id === "app" ? detailHost : null;
    },
    getElementsByTagName() {
      return [];
    },
    querySelectorAll() {
      return [];
    },
  };
  const context = { console, document, window: {} };
  context.globalThis = context;
  vm.createContext(context);
  // Exercise rendering without starting the runtime asset and database loader.
  const bootStart = appSource.indexOf("(async function boot() {");
  const bootEnd = appSource.indexOf('document.addEventListener("change"', bootStart);
  assert.ok(bootStart >= 0 && bootEnd > bootStart, "app startup boundaries must be present");
  vm.runInContext(appSource.slice(0, bootStart) + appSource.slice(bootEnd), context, { filename: "app.js" });
  return context;
}

const app = loadApp();

test("breadcrumb prefixes link list-item fields to their stored parent", () => {
  assert.deepEqual(JSON.parse(JSON.stringify(app.buildKeyPathPrefixes("ethernet_interfaces[].name"))), [
    { keyPath: "ethernet_interfaces", label: "ethernet_interfaces[]" },
    { keyPath: "ethernet_interfaces[].name", label: "name" },
  ]);
});

test("search selects the original match instead of an injected ancestor", () => {
  const parent = {
    module: "eos_cli_config_gen",
    key_path: "ethernet_interfaces",
    parent_path: "",
    depth: 1,
    var_type: "list",
  };
  const match = {
    module: "eos_cli_config_gen",
    key_path: "ethernet_interfaces[].name",
    parent_path: "ethernet_interfaces[]",
    depth: 2,
    var_type: "str",
  };
  const target = {
    innerHTML: "",
    querySelector(selector) {
      if (selector === ".schema-reference-nav") return { querySelectorAll: () => [] };
      if (selector === ".schema-reference-view") return { addEventListener() {} };
      return null;
    },
    querySelectorAll() {
      return [];
    },
  };
  const state = { q: "name", searchScope: "path" };

  // expandRowsWithAncestors() returns the matching row first, followed by the
  // context row it loaded for the hierarchy. The selected detail should stay
  // on that original search match.
  app.renderReferenceResults(target, null, "eos_cli_config_gen", state, [match, parent]);

  assert.equal(state.currentRowId, "eos_cli_config_gen:ethernet_interfaces[].name");
});

test("variable detail renders a reference to another allowed schema module", () => {
  const host = { innerHTML: "" };
  const detailApp = loadApp(host);
  const variable = {
    module: "eos_designs",
    key_path: "structured_config",
    var_type: "dict",
    cross_ref: "eos_cli_config_gen#/keys/router_bgp/keys/neighbors",
  };
  const db = {
    prepare() {
      let pending = true;
      return {
        bind(params) {
          assert.deepEqual(Array.from(params), ["eos_designs", "structured_config"]);
        },
        step() {
          const hasRow = pending;
          pending = false;
          return hasRow;
        },
        getAsObject() { return variable; },
        free() {},
      };
    },
  };

  detailApp.renderVarDetail(db, "eos_designs", "structured_config");

  assert.match(host.innerHTML, /Cross-schema<\/td>/);
  assert.ok(host.innerHTML.includes('href="#/eos_cli_config_gen/router_bgp.neighbors"'));
  assert.ok(host.innerHTML.includes("<code>eos_cli_config_gen</code>"));
});
