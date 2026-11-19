import { test, expect } from "@playwright/test";

const payload = '<img src=x onerror="window.schemaExplorerXss=true">';

for (const mode of ["standalone", "embedded"]) {
  test(`${mode}: locked runtime assets load and support search, details and YAML`, async ({ page }) => {
    const errors = [];
    const requests = [];
    page.on("pageerror", error => errors.push(error.message));
    page.on("console", message => { if (message.type() === "error") errors.push(message.text()); });
    page.on("requestfailed", request => errors.push(`${request.url()}: ${request.failure()?.errorText}`));
    page.on("response", response => { if (response.status() >= 400) errors.push(`${response.status()} ${response.url()}`); });
    page.on("request", request => requests.push(request.url()));
    await page.goto(mode === "standalone" ? "/_assets/schema-explorer/index.html" : "/");
    if (mode === "standalone") await page.locator('a[href="#/eos_designs"]').click();
    const host = page.locator(mode === "standalone" ? "#app" : "schema-explorer");
    await host.getByRole("searchbox", { name: "Search", exact: true }).fill("fabric_name");
    await host.locator('[data-reference-select="eos_designs:fabric_name"]').last().click();
    await expect(host.locator(".schema-reference-detail")).toContainText(payload);
    await expect(host.locator(".schema-reference-detail img")).toHaveCount(0);
    expect(await page.evaluate(() => window.schemaExplorerXss)).toBeUndefined();
    if (mode === "standalone") await host.locator("#btn-view-yaml").click();
    else await page.goto("/yaml/");
    const group = host.locator('[data-schema-group-id="fabric_name"]');
    await expect(group.locator(".schema-yaml-block")).toBeVisible();
    // Exercise Bootstrap's actual collapse plugin rather than checking its global.
    const collapse = group.locator('[data-bs-toggle="collapse"]');
    await expect(collapse).toBeVisible();
    const target = host.locator(await collapse.getAttribute("data-bs-target"));
    const expanded = await collapse.getAttribute("aria-expanded");
    await collapse.click();
    await expect(collapse).toHaveAttribute("aria-expanded", expanded === "true" ? "false" : "true");
    await expect(target).toHaveClass(expanded === "true" ? /collapse(?!.*show)/ : /show/);
    await page.evaluate(() => document.fonts.ready);
    expect(requests.some(url => url.endsWith("sql-wasm.wasm"))).toBe(true);
    expect(requests.some(url => /bootstrap-icons\.woff2?/.test(url))).toBe(true);
    expect(requests.every(url => new URL(url).origin === "http://127.0.0.1:8765")).toBe(true);
    expect(errors).toEqual([]);
  });
}

test("plain docs do not load runtime dependencies or Bootstrap CSS", async ({ page }) => {
  const requests = [];
  page.on("request", request => requests.push(request.url()));
  await page.goto("/plain/");
  await expect(page.locator("h1")).toHaveText("Plain documentation page");
  expect(requests.filter(url => url.includes("/vendor/") || url.endsWith("schema.sqlite"))).toEqual([]);
});
