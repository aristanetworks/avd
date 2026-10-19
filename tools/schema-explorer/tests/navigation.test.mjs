import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appSource = await readFile(new URL("../static/js/app.js", import.meta.url), "utf8");

function loadApp() {
  const document = {
    addEventListener() {},
    getElementById() {
      return null;
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
  vm.runInContext(appSource, context, { filename: "app.js" });
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
