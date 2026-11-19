import { defineConfig } from "@playwright/test";
import { fileURLToPath } from "node:url";

export default defineConfig({
  testDir: "./tests/browser",
  timeout: 30000,
  use: { baseURL: "http://127.0.0.1:8765", browserName: "chromium" },
  webServer: {
    command: "uv run --group doc python tools/schema-explorer/tests/serve_browser_site.py",
    cwd: fileURLToPath(new URL("../..", import.meta.url)),
    url: "http://127.0.0.1:8765/",
    timeout: 180000,
  },
});
