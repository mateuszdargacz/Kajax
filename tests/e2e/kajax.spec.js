const { test, expect } = require("@playwright/test");

const publicPages = [
  { path: "/", h1: "Elementy drewniane, serie i stolarka wykonywane pod projekt" },
  { path: "/produkcja-elementow-drewnianych/", h1: "Produkcja elementów drewnianych dla firm" },
  { path: "/elementy-drewniane-dla-firm-reklamowych-i-eventowych/", h1: "Elementy drewniane dla firm reklamowych i eventowych" },
  { path: "/stolarka-budowlana/", h1: "Schody, drzwi i drewniane wykończenia na wymiar" },
  { path: "/schody-drewniane-co-wplywa-na-cene-i-termin/", h1: "Schody drewniane: co wpływa na cenę i termin realizacji?" },
  { path: "/dla-architektow-i-firm/", h1: "Drewniane detale dla architektów, projektantów i firm" },
  { path: "/realizacje/", h1: "Zakresy prac, które dobrze pasują do naszej stolarni" },
  { path: "/jak-przygotowac-zapytanie/", h1: "Jak przygotować zapytanie, żeby szybciej dostać konkretną wycenę" },
  { path: "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/", h1: "Kiedy krótka seria elementów drewnianych ma sens?" },
  { path: "/kontakt/", h1: "Kontakt z Kajax Stolarstwo" },
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
      await expect(page.getByRole("navigation", { name: "Wybór języka" }).getByRole("link", { name: "PL" })).toBeVisible();
      await expect(page.locator("body")).not.toContainText("hero_workshop");
      await expect(page.locator("body")).not.toContainText("Homepage hero");
      await expect(page.locator("body")).not.toContainText("Wide workshop");
      await expectNoHorizontalOverflow(page);
      await expectVersionedStaticAssets(page);
    });
  }

  test("home has visible conversion CTAs and mapped images", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByRole("link", { name: "Wyślij projekt do oceny" })).toBeVisible();
    await expect(page.getByRole("link", { name: "Sprawdź zakres" })).toBeVisible();
    await expect(page.getByRole("link", { name: "Zobacz checklistę do wyceny" })).toBeVisible();
    await expect(page.getByRole("navigation", { name: "Wybór języka" }).getByRole("link", { name: "EN" })).toHaveAttribute("href", "https://kajax.eu/en/");
    await expect(page.getByRole("navigation", { name: "Wybór języka" }).getByRole("link", { name: "DE" })).toHaveAttribute("href", "https://kajax.eu/de/");
    await expect(page.locator(".hero-media source")).toHaveAttribute("srcset", /hero-workshop-production-\d+\.webp/);
    await expect(page.locator(".hero-media img")).toHaveAttribute("src", /hero-workshop-production\.jpg/);
    await expect(page.locator(".hero-media img")).toHaveAttribute(
      "alt",
      "Warsztat stolarski przygotowany do produkcji elementów drewnianych i realizacji na wymiar",
    );
    await expect(page.locator(".feature-image source")).toHaveAttribute("srcset", /b2b-short-series-wood-components-\d+\.webp/);
    await expect(page.locator(".feature-image img")).toHaveAttribute("src", /b2b-short-series-wood-components\.jpg/);
    await expect(page.locator(".case-card").first().locator("source")).toHaveAttribute("srcset", /b2b-repeated-wooden-elements-detail-\d+\.webp/);
    await expect(page.locator(".case-card").first().locator("img")).toHaveAttribute("src", /b2b-repeated-wooden-elements-detail\.jpg/);
    await expect(page.locator(".case-card").nth(1).locator("source")).toHaveAttribute("srcset", /wooden-stairs-pomorskie-\d+\.webp/);
    await expect(page.locator(".case-card").nth(2).locator("source")).toHaveAttribute("srcset", /wood-joinery-detail-closeup-\d+\.webp/);
    await expect(page.locator(".photo-placeholder-name")).toHaveCount(0);
    await expect(page.locator(".photo-placeholder small")).toHaveCount(0);
    await expectNoHorizontalOverflow(page);
  });

  test("quote guide explains input requirements and exposes schema", async ({ page }) => {
    await page.goto("/jak-przygotowac-zapytanie/");

    await expect(page.locator("h1")).toContainText("Jak przygotować zapytanie");
    await expect(page.locator("body")).toContainText("Gdy element ma być powtarzalny");
    await expect(page.locator("body")).toContainText("Co zwykle blokuje szybką odpowiedź");
    await expect(page.getByRole("link", { name: "Wyślij projekt do wyceny" }).first()).toBeVisible();
    await expect(page.locator(".guide-aside source")).toHaveAttribute("srcset", /woodwork-from-drawing-specification-\d+\.webp/);
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("short series guide qualifies B2B component leads and links back to production", async ({ page }) => {
    await page.goto("/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/");

    await expect(page.locator("h1")).toContainText("Kiedy krótka seria elementów drewnianych ma sens");
    await expect(page.locator("body")).toContainText("Gdy własna produkcja byłaby za droga albo zbyt wolna");
    await expect(page.locator("body")).toContainText("Kiedy seria nie powinna być pierwszym krokiem");
    await expect(page.locator(".guide-aside source")).toHaveAttribute("srcset", /wood-components-packed-for-shipping-\d+\.webp/);
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

    await expect(page.getByRole("link", { name: /Kiedy krótka seria elementów drewnianych ma sens/ })).toHaveAttribute(
      "href",
      "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/",
    );
    await expect(page.getByRole("link", { name: /Elementy drewniane dla firm reklamowych/ })).toHaveAttribute(
      "href",
      "/elementy-drewniane-dla-firm-reklamowych-i-eventowych/",
    );
    await expect(page.getByRole("link", { name: /Jak przygotować zapytanie do stolarni/ })).toHaveAttribute(
      "href",
      "/jak-przygotowac-zapytanie/",
    );
    await expectNoHorizontalOverflow(page);
  });

  test("advertising event guide qualifies POS and event leads", async ({ page }) => {
    await page.goto("/elementy-drewniane-dla-firm-reklamowych-i-eventowych/");

    await expect(page.locator("h1")).toContainText("firm reklamowych");
    await expect(page.locator("body")).toContainText("Kiedy drewno wnosi wartość do ekspozycji");
    await expect(page.locator("body")).toContainText("Co może zablokować szybkie wdrożenie");
    await expect(page.locator(".related-card", { hasText: "Produkcja elementów drewnianych" })).toHaveAttribute(
      "href",
      "/produkcja-elementow-drewnianych/",
    );
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("stairs pricing guide qualifies construction joinery leads", async ({ page }) => {
    await page.goto("/schody-drewniane-co-wplywa-na-cene-i-termin/");

    await expect(page.locator("h1")).toContainText("Schody drewniane");
    await expect(page.locator("body")).toContainText("Układ i wymiary schodów");
    await expect(page.locator("body")).toContainText("Co najczęściej opóźnia wycenę schodów");
    await expect(page.locator(".related-card", { hasText: "Stolarka budowlana" })).toHaveAttribute("href", "/stolarka-budowlana/");
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("construction page links to stairs quote guide", async ({ page }) => {
    await page.goto("/stolarka-budowlana/");

    await expect(page.getByRole("link", { name: /Co wpływa na cenę i termin schodów drewnianych/ })).toHaveAttribute(
      "href",
      "/schody-drewniane-co-wplywa-na-cene-i-termin/",
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

    if (process.env.E2E_ALLOW_GTM === "1") {
      expect(thirdPartyResources.map((entry) => new URL(entry.name).hostname)).toEqual(["www.googletagmanager.com"]);
    } else {
      expect(thirdPartyResources).toEqual([]);
    }
    expect(staticResources.length).toBeLessThanOrEqual(7);
    expect(decodedBytes).toBeLessThan(430000);
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

    await page.getByRole("link", { name: "Sprawdź zakres" }).click();
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
  test("German and Norwegian pages render translated content", async ({ page }) => {
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

    await page.goto("/de/elementy-drewniane-dla-firm-reklamowych-i-eventowych/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Werbe- und Eventfirmen");
    await expect(page.locator(".related-card", { hasText: "Holzelemente" })).toHaveAttribute("href", "/de/produkcja-elementow-drewnianych/");
    await expectNoHorizontalOverflow(page);

    await page.goto("/de/schody-drewniane-co-wplywa-na-cene-i-termin/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Holztreppen");
    await expect(page.locator(".related-card", { hasText: "Bauschreinerei" })).toHaveAttribute("href", "/de/stolarka-budowlana/");
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
    await page.getByLabel("Jaki to rodzaj projektu?").selectOption("custom_artistic");
    await page.getByLabel("Opisz krótko, co ma powstać").fill(
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
