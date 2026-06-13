const { defineConfig, devices } = require("@playwright/test");

const port = Number(process.env.E2E_PORT || 8061);
const python = process.env.E2E_PYTHON || "../.venv/bin/python";
const sqlitePath = process.env.E2E_SQLITE_PATH || "/tmp/kajax-e2e.sqlite3";
const dataDir = process.env.E2E_DATA_DIR || "/tmp/kajax-e2e-data";
const baseURL = process.env.E2E_BASE_URL || `http://127.0.0.1:${port}`;

const djangoEnv = [
  `SQLITE_PATH=${sqlitePath}`,
  `DATA_DIR=${dataDir}`,
  "EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend",
  "DJANGO_DEBUG=true",
].join(" ");

module.exports = defineConfig({
  testDir: "./tests/e2e",
  timeout: 30000,
  expect: {
    timeout: 5000,
  },
  fullyParallel: false,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL,
    actionTimeout: 10000,
    navigationTimeout: 15000,
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  webServer: process.env.E2E_BASE_URL
    ? undefined
    : {
        command: [
          "bash -lc",
          `'rm -f ${sqlitePath}; mkdir -p ${dataDir}; cd app && ${djangoEnv} ${python} manage.py migrate --noinput && ${djangoEnv} ${python} manage.py runserver 127.0.0.1:${port}'`,
        ].join(" "),
        url: baseURL,
        timeout: 120000,
        reuseExistingServer: !process.env.CI,
      },
  projects: [
    {
      name: "desktop",
      use: {
        ...devices["Desktop Chrome"],
        viewport: { width: 1440, height: 1200 },
      },
    },
    {
      name: "tablet",
      use: {
        ...devices["Desktop Chrome"],
        viewport: { width: 768, height: 1100 },
        hasTouch: true,
        isMobile: true,
      },
    },
    {
      name: "mobile",
      use: {
        ...devices["Pixel 5"],
        viewport: { width: 390, height: 1200 },
      },
    },
  ],
});
