const { test, expect } = require("@playwright/test");

const publicPages = [
  { path: "/", h1: "Stolarnia dla firm, architektów i wymagających realizacji z drewna" },
  { path: "/produkcja-elementow-drewnianych/", h1: "Elementy drewniane na zamówienie dla firm" },
  { path: "/stolarka-budowlana/", h1: "Schody, drzwi, listwy i stolarka drewniana na wymiar" },
  { path: "/dla-architektow-i-firm/", h1: "Stolarnia do trudniejszych projektów i detali drewnianych" },
  { path: "/realizacje/", h1: "Realizacje i kierunki prac, które dobrze pasują do naszej stolarni" },
  { path: "/jak-przygotowac-zapytanie/", h1: "Jak przygotować zapytanie do stolarni, żeby szybciej dostać konkretną odpowiedź" },
  { path: "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/", h1: "Kiedy opłaca się zamówić elementy drewniane w krótkiej serii?" },
  { path: "/kontakt/", h1: "Kontakt" },
];

async function expectNoHorizontalOverflow(page) {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  expect(overflow).toBeLessThanOrEqual(1);
}

async function expectVersionedStaticAssets(page) {
  const cssHref = await page.locator('link[rel="stylesheet"]').first().getAttribute("href");
  const jsSrc = await page.locator('script[src*="site/js/site.js"]').first().getAttribute("src");
  expect(cssHref).toMatch(/\/static\/site\/css\/styles\.css\?v=\d+/);
  expect(jsSrc).toMatch(/\/static\/site\/js\/site\.js\?v=\d+/);
}

test.describe("public marketing pages", () => {
  for (const publicPage of publicPages) {
    test(`${publicPage.path} renders cleanly`, async ({ page }) => {
      const response = await page.goto(publicPage.path);
      expect(response.status()).toBe(200);

      await expect(page.locator("h1")).toHaveCount(1);
      await expect(page.locator("h1")).toContainText(publicPage.h1);
      await expect(page.getByRole("banner").getByRole("link", { name: "604 238 246" })).toBeVisible();
      await expect(page.getByRole("navigation", { name: "Główna nawigacja" })).toBeVisible();
      await expect(page.locator("body")).not.toContainText("hero_workshop");
      await expect(page.locator("body")).not.toContainText("Homepage hero");
      await expect(page.locator("body")).not.toContainText("Wide workshop");
      await expectNoHorizontalOverflow(page);
      await expectVersionedStaticAssets(page);
    });
  }

  test("home has visible conversion CTAs and photo filename-only placeholders", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByRole("link", { name: "Wyślij projekt do wyceny" })).toBeVisible();
    await expect(page.getByRole("link", { name: "Zobacz zakres prac" })).toBeVisible();
    await expect(page.getByRole("link", { name: "Zobacz checklistę do wyceny" })).toBeVisible();
    await expect(page.locator(".photo-placeholder-name").first()).toContainText("hero-workshop-production.jpg");
    await expect(page.locator(".photo-placeholder small")).toHaveCount(0);
    await expectNoHorizontalOverflow(page);
  });

  test("quote guide explains input requirements and exposes schema", async ({ page }) => {
    await page.goto("/jak-przygotowac-zapytanie/");

    await expect(page.locator("h1")).toContainText("Jak przygotować zapytanie do stolarni");
    await expect(page.locator("body")).toContainText("Dla elementów B2B i krótkich serii");
    await expect(page.locator("body")).toContainText("Co najczęściej spowalnia wycenę");
    await expect(page.getByRole("link", { name: "Wyślij projekt do wyceny" }).first()).toBeVisible();
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("short series guide qualifies B2B component leads and links back to production", async ({ page }) => {
    await page.goto("/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/");

    await expect(page.locator("h1")).toContainText("Kiedy opłaca się zamówić elementy drewniane");
    await expect(page.locator("body")).toContainText("Gdy własna produkcja byłaby za droga albo zbyt wolna");
    await expect(page.locator("body")).toContainText("Kiedy seria może nie być dobrym pierwszym krokiem");
    await expect(page.getByRole("link", { name: /Produkcja elementów drewnianych/ })).toHaveAttribute(
      "href",
      "/produkcja-elementow-drewnianych/",
    );
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("production page links to B2B guides", async ({ page }) => {
    await page.goto("/produkcja-elementow-drewnianych/");

    await expect(page.getByRole("link", { name: /Kiedy opłaca się zamówić elementy drewniane/ })).toHaveAttribute(
      "href",
      "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/",
    );
    await expect(page.getByRole("link", { name: /Jak przygotować zapytanie do stolarni/ })).toHaveAttribute(
      "href",
      "/jak-przygotowac-zapytanie/",
    );
    await expectNoHorizontalOverflow(page);
  });

  test("home keeps the frontend payload lean", async ({ page }) => {
    await page.goto("/");
    const resources = await page.evaluate(() =>
      performance.getEntriesByType("resource").map((entry) => ({
        name: entry.name,
        decodedBodySize: entry.decodedBodySize || 0,
      })),
    );
    const thirdPartyResources = resources.filter((entry) => new URL(entry.name).origin !== new URL(page.url()).origin);
    const staticResources = resources.filter((entry) => entry.name.includes("/static/site/"));
    const decodedBytes = resources.reduce((sum, entry) => sum + entry.decodedBodySize, 0);

    expect(thirdPartyResources).toEqual([]);
    expect(staticResources.length).toBeLessThanOrEqual(2);
    expect(decodedBytes).toBeLessThan(90000);
  });

  test("conversion CTAs are trackable and mobile actions stay device-specific", async ({ page }, testInfo) => {
    await page.goto("/");
    await page.evaluate(() => {
      const originalPush = window.dataLayer.push.bind(window.dataLayer);
      window.localStorage.setItem("e2eCtaEvents", "[]");
      window.dataLayer.push = (...items) => {
        const events = JSON.parse(window.localStorage.getItem("e2eCtaEvents") || "[]");
        events.push(...items.filter((item) => item.event === "cta_click"));
        window.localStorage.setItem("e2eCtaEvents", JSON.stringify(events));
        return originalPush(...items);
      };
    });

    await page.getByRole("link", { name: "Zobacz zakres prac" }).click();
    const ctaEvents = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2eCtaEvents") || "[]"));
    expect(ctaEvents).toContainEqual(
      expect.objectContaining({
        cta_id: "home_hero_scope",
        cta_location: "home_hero",
      }),
    );

    const mobileBar = page.locator(".mobile-action-bar");
    if (testInfo.project.name === "mobile") {
      await expect(mobileBar).toBeVisible();
      await expect(mobileBar.getByRole("link", { name: "Zadzwoń" })).toHaveAttribute("href", "tel:604238246");
      await expect(mobileBar.getByRole("link", { name: "Wycena" })).toHaveAttribute("href", "/wycena/");
    } else {
      await expect(mobileBar).toBeHidden();
    }
    await expectNoHorizontalOverflow(page);
  });
});

test.describe("localized pages", () => {
  test("German and Norwegian prefixes render translated content", async ({ page }) => {
    await page.goto("/de/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Tischlerei für Unternehmen");
    await expect(page.getByRole("navigation", { name: "Hauptnavigation" }).getByRole("link", { name: "Elementfertigung" })).toHaveAttribute(
      "href",
      "/de/produkcja-elementow-drewnianych/",
    );
    await expectNoHorizontalOverflow(page);

    await page.goto("/no/");
    await expect(page.locator("html")).toHaveAttribute("lang", "no");
    await expect(page.locator("h1")).toContainText("Snekkerverksted for bedrifter");
    await expect(page.getByRole("navigation", { name: "Hovednavigasjon" }).getByRole("link", { name: "Forespørsel", exact: true })).toHaveAttribute("href", "/no/wycena/");
    await expect(page.locator(".mobile-action-bar [data-track-cta='mobile_quote']")).toHaveAttribute("href", "/no/wycena/");
    await expectNoHorizontalOverflow(page);

    await page.goto("/de/jak-przygotowac-zapytanie/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Tischlerei-Anfrage");
    await expectNoHorizontalOverflow(page);

    await page.goto("/de/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Kleinserie");
    await expect(page.getByRole("link", { name: /Fertigung von Holzelementen/ })).toHaveAttribute("href", "/de/produkcja-elementow-drewnianych/");
    await expectNoHorizontalOverflow(page);
  });
});

test.describe("quote form", () => {
  test("submits a qualified lead with optional fields and tracking events", async ({ page }) => {
    await page.goto("/wycena/");
    await page.evaluate(() => {
      const originalPush = window.dataLayer.push.bind(window.dataLayer);
      window.localStorage.setItem("e2eDataLayerEvents", "[]");
      window.dataLayer.push = (...items) => {
        const events = JSON.parse(window.localStorage.getItem("e2eDataLayerEvents") || "[]");
        events.push(...items.map((item) => item.event).filter(Boolean));
        window.localStorage.setItem("e2eDataLayerEvents", JSON.stringify(events));
        return originalPush(...items);
      };
    });

    await page.getByLabel("Imię").fill("Lead E2E");
    await page.getByLabel("Telefon").fill("604000000");
    await page.getByLabel("Czego dotyczy temat?").selectOption("custom_artistic");
    await page.getByLabel("Krótko opisz, co mamy wykonać").fill(
      "Potrzebujemy krótkiej serii precyzyjnych elementów drewnianych według rysunku.",
    );
    await page.getByLabel("Wyrażam zgodę na kontakt w sprawie przesłanego zapytania.").check();

    await page.locator("summary", { hasText: "Więcej informacji" }).click();
    await page.getByLabel("Firma").fill("E2E Manufacturing");
    await page.getByLabel("Ilość / skala").selectOption("small_series");
    await page.getByLabel("Lokalizacja").fill("Gdańsk / Europa");
    await page.getByLabel("Termin").fill("Próbka w czerwcu");
    await page.getByLabel("Zdjęcia, rysunki lub specyfikacja").setInputFiles({
      name: "rysunek-testowy.txt",
      mimeType: "text/plain",
      buffer: Buffer.from("testowy opis rysunku"),
    });

    await page.getByRole("button", { name: "Wyślij zapytanie" }).click();
    await expect(page.locator(".message")).toContainText("Dziękujemy. Zapytanie zostało zapisane");

    const events = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2eDataLayerEvents") || "[]"));
    expect(events).toEqual(expect.arrayContaining(["quote_form_start", "project_type_select", "file_upload_complete", "generate_lead"]));
    await expectNoHorizontalOverflow(page);
  });

  test("keeps the quick form compact but exposes optional fields on demand", async ({ page }) => {
    await page.goto("/wycena/");

    await expect(page.locator(".optional-fields")).not.toHaveAttribute("open", "");
    await page.locator("summary", { hasText: "Więcej informacji" }).click();
    await expect(page.locator(".optional-fields")).toHaveAttribute("open", "");
    await expect(page.getByLabel("Firma")).toBeVisible();
    await expect(page.getByLabel("Zdjęcia, rysunki lub specyfikacja")).toBeVisible();
    await expect(page.getByRole("link", { name: "Nie wiesz, co przygotować? Zobacz checklistę" })).toBeVisible();
    await expectNoHorizontalOverflow(page);
  });
});
