const { test, expect } = require("@playwright/test");

const publicPages = [
  { path: "/", h1: "Komponenty drewniane dla firm oraz schody i drzwi na wymiar" },
  { path: "/produkcja-elementow-drewnianych/", h1: "Elementy drewniane B2B dla firm w całej Polsce" },
  { path: "/elementy-drewniane-dla-firm-reklamowych-i-eventowych/", h1: "Drewniane displaye, elementy POS i detale eventowe" },
  { path: "/stolarka-budowlana/", h1: "Schody drewniane, drzwi i stolarka na wymiar w Pomorskiem" },
  { path: "/stolarka-budowlana-wejherowo/", h1: "Stolarka budowlana Wejherowo" },
  { path: "/stolarka-budowlana-trojmiasto/", h1: "Stolarka budowlana Trójmiasto" },
  { path: "/stolarka-budowlana-pomorskie/", h1: "Schody, drzwi, listwy i custom joinery w Pomorskiem" },
  { path: "/schody-drewniane-co-wplywa-na-cene-i-termin/", h1: "Schody drewniane: od czego zależy cena i termin?" },
  { path: "/dla-architektow-i-firm/", h1: "Zabudowy i detale drewniane, których nie bierze się z katalogu" },
  { path: "/realizacje/", h1: "Przykłady zleceń: komponenty, schody, drzwi i detale" },
  { path: "/jak-przygotowac-zapytanie/", h1: "Jak opisać zlecenie, żeby szybciej dostać rzeczową odpowiedź?" },
  { path: "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/", h1: "Krótka seria elementów drewnianych: kiedy ma sens?" },
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

async function installDataLayerRecorder(page, storageKey) {
  await page.addInitScript((key) => {
    window.dataLayer = window.dataLayer || [];
    const originalPush = window.dataLayer.push.bind(window.dataLayer);
    window.dataLayer.push = (...items) => {
      const events = JSON.parse(window.localStorage.getItem(key) || "[]");
      events.push(
        ...items.filter((item) => {
          if (!item || !item.event) {
            return false;
          }
          return !String(item.event).startsWith("gtm.");
        }),
      );
      window.localStorage.setItem(key, JSON.stringify(events));
      return originalPush(...items);
    };
  }, storageKey);
}

async function installPiecodeRecorder(page, storageKey) {
  await page.addInitScript((key) => {
    const state = {
      context: {},
      consentGranted: false,
      devMode: false,
    };
    const saveEvent = (event) => {
      const events = JSON.parse(window.localStorage.getItem(key) || "[]");
      events.push(event);
      window.localStorage.setItem(key, JSON.stringify(events));
    };
    window.PiecodeEvents = {
      setContext(context) {
        state.context = { ...state.context, ...(context || {}) };
      },
      setConsent(granted) {
        state.consentGranted = granted === true;
      },
      setDevMode(enabled) {
        state.devMode = enabled === true;
      },
      track(eventName, params, options) {
        saveEvent({
          event_name: eventName,
          params: { ...state.context, ...(params || {}) },
          options: options || {},
          consent_granted: state.consentGranted,
          dev_mode: state.devMode,
        });
      },
      page(params) {
        this.track("page_view", { page_type: "page", ...(params || {}) }, { immediate: true });
      },
      flush() {
        return Promise.resolve(true);
      },
      getState() {
        return { consent_granted: state.consentGranted, dev_mode: state.devMode };
      },
    };
  }, storageKey);
}

test.describe("public marketing pages", () => {
  for (const publicPage of publicPages) {
    test(`${publicPage.path} renders cleanly`, async ({ page }, testInfo) => {
      const response = await page.goto(publicPage.path);
      expect(response.status()).toBe(200);

      await expect(page.locator("h1")).toHaveCount(1);
      await expect(page.locator("h1")).toContainText(publicPage.h1);
      await expect(page.getByRole("banner").getByRole("link", { name: "604 238 246" })).toBeVisible();
      if (testInfo.project.name === "mobile") {
        await expect(page.getByRole("banner").getByText("Menu")).toBeVisible();
      } else {
        await expect(page.getByRole("navigation", { name: "Główna nawigacja" })).toBeVisible();
        await expect(page.getByRole("navigation", { name: "Wybór języka" }).getByRole("link", { name: "PL" })).toBeVisible();
      }
      await expect(page.locator('meta[property="og:image"]')).toHaveAttribute("content", /\/static\/site\/img\/og-.+\.jpg$/);
      await expect(page.locator('meta[name="twitter:image"]')).toHaveAttribute("content", /\/static\/site\/img\/og-.+\.jpg$/);
      await expect(page.locator("body")).not.toContainText("hero_workshop");
      await expect(page.locator("body")).not.toContainText("Homepage hero");
      await expect(page.locator("body")).not.toContainText("Wide workshop");
      await expectNoHorizontalOverflow(page);
      await expectVersionedStaticAssets(page);
    });
  }

  test("home has visible conversion CTAs and mapped images", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByRole("link", { name: "Wyślij zdjęcie lub rysunek" })).toBeVisible();
    await expect(page.getByRole("link", { name: "Co przygotować do wyceny" })).toHaveAttribute("href", "/jak-przygotowac-zapytanie/");
    await expect(page.getByRole("link", { name: "Sprawdź checklistę" })).toBeVisible();
    await expect(page.locator(".hero-proof-grid")).toContainText("Produkcja dla firm");
    await expect(page.locator(".hero-proof-grid")).toContainText("Elementy POS");
    await expect(page.locator("body")).toContainText("Dla firm wykonujemy elementy z drewna na podstawie rysunku, próbki albo wzoru");
    await expect(page.locator("body")).not.toContainText("Czego nie obiecujemy bez danych");
    await expect(page.locator('a[hreflang="en"]').first()).toHaveAttribute("href", "https://kajax.eu/en/");
    await expect(page.locator('a[hreflang="de"]').first()).toHaveAttribute("href", "https://kajax.eu/de/");
    await expect(page.locator(".hero-media source")).toHaveAttribute("srcset", /hero-workshop-production-\d+\.webp/);
    await expect(page.locator(".hero-media img")).toHaveAttribute("src", /hero-workshop-production\.jpg/);
    await expect(page.locator(".hero-media img")).toHaveAttribute(
      "alt",
      "Warsztat Kajax z maszynami stolarskimi i drewnem przygotowanym do obróbki",
    );
    await expect(page.locator(".feature-image source")).toHaveAttribute("srcset", /b2b-short-series-wood-components-\d+\.webp/);
    await expect(page.locator(".feature-image img")).toHaveAttribute("src", /b2b-short-series-wood-components\.jpg/);
    await expect(page.locator(".case-card").first().locator("source")).toHaveAttribute("srcset", /b2b-repeated-wooden-elements-detail-\d+\.webp/);
    await expect(page.locator(".case-card").first().locator("img")).toHaveAttribute("src", /b2b-repeated-wooden-elements-detail\.jpg/);
    await expect(page.locator(".case-card").nth(1).locator("source")).toHaveAttribute("srcset", /wooden-stairs-pomorskie-\d+\.webp/);
    await expect(page.locator(".case-card").nth(2)).toContainText("Zabudowa albo element wnętrza pod projekt");
    await expect(page.locator(".case-card").nth(2).locator("source")).toHaveAttribute("srcset", /built-in-woodwork-project-\d+\.webp/);
    await expect(page.locator(".photo-placeholder-name")).toHaveCount(0);
    await expect(page.locator(".photo-placeholder small")).toHaveCount(0);
    await expectNoHorizontalOverflow(page);
  });

  test("quote guide explains input requirements and exposes schema", async ({ page }) => {
    await page.goto("/jak-przygotowac-zapytanie/");

    await expect(page.locator("h1")).toContainText("Jak opisać zlecenie");
    await expect(page.locator("body")).toContainText("Element drewniany albo krótka seria dla firmy");
    await expect(page.locator("body")).toContainText("Co zwykle wydłuża odpowiedź");
    await expect(page.getByRole("link", { name: "Wyślij zapytanie" }).first()).toBeVisible();
    await expect(page.locator(".guide-aside source")).toHaveAttribute("srcset", /woodwork-from-drawing-specification-\d+\.webp/);
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("short series guide qualifies B2B component leads and links back to production", async ({ page }) => {
    await page.goto("/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/");

    await expect(page.locator("h1")).toContainText("Krótka seria elementów drewnianych");
    await expect(page.locator("body")).toContainText("Gdy własny warsztat się nie opłaca");
    await expect(page.locator("body")).toContainText("Kiedy nie zaczynać od większej partii");
    await expect(page.locator(".guide-aside source")).toHaveAttribute("srcset", /wood-components-packed-for-shipping-\d+\.webp/);
    await expect(page.getByRole("link", { name: /Elementy drewniane dla firm/ })).toHaveAttribute(
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

    await expect(page.getByRole("link", { name: "Wyślij rysunek lub próbkę" }).first()).toBeVisible();
    await expect(page.locator("body")).toContainText("nie musisz budować własnego zaplecza stolarskiego");
    await expect(page.locator(".service-proof-list")).toContainText("Dla firm w Polsce");
    await expect(page.locator(".compact-case").first()).toContainText("Profile i półprodukty");
    await expect(page.locator("body")).toContainText("Proces B2B: próbka, akceptacja, seria");
    await expect(page.locator("body")).toContainText("Co ustalamy przed powtarzalną serią");
    await expect(page.getByRole("link", { name: /Kiedy krótka seria ma sens/ })).toHaveAttribute(
      "href",
      "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/",
    );
    await expect(page.getByRole("link", { name: /Drewniane displaye i elementy POS/ })).toHaveAttribute(
      "href",
      "/elementy-drewniane-dla-firm-reklamowych-i-eventowych/",
    );
    await expect(page.locator(".related-card", { hasText: "Jak opisać zlecenie" })).toHaveAttribute(
      "href",
      "/jak-przygotowac-zapytanie/",
    );
    await expectNoHorizontalOverflow(page);
  });

  test("advertising event guide qualifies POS and event leads", async ({ page }) => {
    await page.goto("/elementy-drewniane-dla-firm-reklamowych-i-eventowych/");

    await expect(page.locator("h1")).toContainText("Drewniane displaye");
    await expect(page.locator("body")).toContainText("Gdy materiał ma budować wrażenie marki");
    await expect(page.locator("body")).toContainText("Co może zablokować szybkie wdrożenie");
    await expect(page.locator(".related-card", { hasText: "Elementy drewniane dla firm" })).toHaveAttribute(
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
    await expect(page.locator(".related-card", { hasText: "Schody i stolarka na wymiar" })).toHaveAttribute("href", "/stolarka-budowlana/");
    const schema = await page.locator('script[type="application/ld+json"]').textContent();
    expect(schema).toContain('"@type": "HowTo"');
    expect(schema).toContain('"@type": "Article"');
    await expectNoHorizontalOverflow(page);
  });

  test("construction page links to stairs quote guide", async ({ page }) => {
    await page.goto("/stolarka-budowlana/");

    await expect(page.getByRole("link", { name: "Poproś o wycenę" }).first()).toBeVisible();
    await expect(page.locator(".service-proof-list")).toContainText("Schody i drzwi");
    await expect(page.getByRole("link", { name: /Od czego zależy cena schodów drewnianych/ })).toHaveAttribute(
      "href",
      "/schody-drewniane-co-wplywa-na-cene-i-termin/",
    );
    await expect(page.getByRole("link", { name: /Stolarka budowlana Wejherowo/ })).toHaveAttribute("href", "/stolarka-budowlana-wejherowo/");
    await expect(page.getByRole("link", { name: /Stolarka budowlana Trójmiasto/ })).toHaveAttribute("href", "/stolarka-budowlana-trojmiasto/");
    await expectNoHorizontalOverflow(page);
  });

  test("pomorskie paid landing keeps quote CTA and portfolio proof above fold", async ({ page }) => {
    await installDataLayerRecorder(page, "e2ePomorskieEvents");
    await page.goto("/stolarka-budowlana-pomorskie/");

    await expect(page.locator("h1")).toContainText("Schody, drzwi, listwy i custom joinery w Pomorskiem");
    await expect(page.getByRole("link", { name: "Poproś o wycenę" }).first()).toBeVisible();
    await expect(page.locator(".service-proof-list")).toContainText("Pomorskie");
    await expect(page.locator(".compact-case").first()).toContainText("Schody drewniane");
    await expect(page.locator("body")).toContainText("Gościcino, Wejherowo, Trójmiasto");
    await page.locator(".compact-case").first().scrollIntoViewIfNeeded();
    await page.waitForFunction(() => {
      const events = JSON.parse(window.localStorage.getItem("e2ePomorskieEvents") || "[]");
      return events.some((event) => event.event === "portfolio_view");
    });
    const events = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2ePomorskieEvents") || "[]"));
    expect(events).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          event: "portfolio_view",
          business_line: "construction_joinery",
          service_area: "pomerania",
        }),
      ]),
    );
    await expectNoHorizontalOverflow(page);
  });

  test("realizations page reads like case studies", async ({ page }) => {
    await page.goto("/realizacje/");

    await expect(page.locator(".realization")).toHaveCount(9);
    await expect(page.locator("body")).toContainText("przykłady tematów, które warto wysłać do oceny");
    await expect(page.locator("body")).not.toContainText("To nie jest katalog gotowych produktów");
    await expect(page.locator("body")).toContainText("Serie drzwi i elementów do hoteli lub lokali");
    await expect(page.locator("body")).toContainText("drzwi do hoteli i lokali");
    await expect(
      page.locator(".realization", { hasText: "Serie drzwi i elementów do hoteli lub lokali" }).locator("source").first()
    ).toHaveAttribute("srcset", /hotel-door-series-workshop-\d+\.webp/);
    await expect(
      page.locator(".realization", { hasText: "Listwy, profile i małe elementy montowane" }).locator("source").first()
    ).toHaveAttribute("srcset", /contractor-trim-profile-batch-\d+\.webp/);
    await expect(page.locator(".case-study-facts").first()).toContainText("Problem");
    await expect(page.locator(".case-study-facts").first()).toContainText("Zakres");
    await expect(page.locator(".case-study-facts").first()).toContainText("Efekt");
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
      const thirdPartyHosts = thirdPartyResources.map((entry) => new URL(entry.name).hostname);
      const unexpectedHosts = thirdPartyHosts.filter(
        (host) => (
          host !== "www.googletagmanager.com"
          && host !== "piecode.pl"
          && !/\.google-analytics\.com$/.test(host)
        ),
      );
      expect(unexpectedHosts).toEqual([]);
      expect(thirdPartyHosts.length).toBeLessThanOrEqual(7);
    } else {
      expect(thirdPartyResources).toEqual([]);
    }
    expect(staticResources.length).toBeLessThanOrEqual(7);
    expect(decodedBytes).toBeLessThan(430000);
  });

  test("conversion CTAs are trackable and mobile actions stay device-specific", async ({ page }, testInfo) => {
    await installDataLayerRecorder(page, "e2eCtaEvents");
    await page.goto("/", { waitUntil: "domcontentloaded" });

    await page.getByRole("link", { name: "Co przygotować do wyceny" }).click();
    const ctaEvents = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2eCtaEvents") || "[]"));
    expect(ctaEvents).toContainEqual(
      expect.objectContaining({
        event: "cta_click",
        cta_id: "home_hero_guide",
        cta_location: "home_hero",
        business_line: "mixed",
        intent: "guide",
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

  test("contact clicks and guide interactions push non-PII analytics events", async ({ page }) => {
    await installDataLayerRecorder(page, "e2eContactEvents");
    await page.goto("/jak-przygotowac-zapytanie/");

    await page.locator(".faq-list details").first().locator("summary").click();
    await page.getByRole("banner").getByRole("link", { name: "604 238 246" }).dispatchEvent("click");
    await page.getByRole("contentinfo").getByRole("link", { name: "mail@kajax.eu" }).dispatchEvent("click");

    const events = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2eContactEvents") || "[]"));
    expect(events).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ event: "kajax_page_view", page_key: "guide", page_type: "guide" }),
        expect.objectContaining({ event: "faq_open", faq_id: "guide_faq_1" }),
        expect.objectContaining({ event: "phone_click", cta_location: "header" }),
        expect.objectContaining({ event: "email_click", cta_location: "footer" }),
      ]),
    );
  });
});

test.describe("localized pages", () => {
  test("international home pages expose B2B export positioning", async ({ page }) => {
    const localizedHomes = [
      {
        path: "/en/",
        h1: "Wood components, samples and short production runs from Poland",
        message: "Outsource a wooden component without building a joinery line",
        cta: "Send a component to review",
      },
      {
        path: "/de/",
        h1: "Holzelemente, Muster und Kleinserien aus Polen",
        message: "Holzelement auslagern, ohne eigene Tischlereilinie aufzubauen",
        cta: "Element prüfen lassen",
      },
      {
        path: "/sv/",
        h1: "Träkomponenter, prover och korta serier från Polen",
        message: "Lägg ut träkomponenten utan egen snickerikapacitet",
        cta: "Skicka komponent för granskning",
      },
      {
        path: "/da/",
        h1: "Trækomponenter, prøver og korte serier fra Polen",
        message: "Outsource trækomponenten uden egen snedkerkapacitet",
        cta: "Send komponent til vurdering",
      },
      {
        path: "/no/",
        h1: "Trekomponenter, prøver og korte serier fra Polen",
        message: "Sett bort trekomponenten uten egen snekkerkapasitet",
        cta: "Send komponent for vurdering",
      },
    ];

    for (const localizedHome of localizedHomes) {
      await page.goto(localizedHome.path);
      await expect(page.locator("h1")).toContainText(localizedHome.h1);
      await expect(page.locator("body")).toContainText(localizedHome.message);
      await expect(page.getByRole("link", { name: localizedHome.cta })).toBeVisible();
      await expectNoHorizontalOverflow(page);
    }
  });

  test("German and Norwegian pages render translated content", async ({ page }) => {
    await page.goto("/de/");
    await expect(page.locator("html")).toHaveAttribute("lang", "de");
    await expect(page.locator("h1")).toContainText("Holzelemente, Muster und Kleinserien");
    await expect(page.locator('a[href="/de/produkcja-elementow-drewnianych/"]').first()).toHaveText("B2B-Elemente");
    await expect(page.locator('a[href="/de/produkcja-elementow-drewnianych/"]').first()).toHaveAttribute(
      "href",
      "/de/produkcja-elementow-drewnianych/",
    );
    await expectNoHorizontalOverflow(page);

    await page.goto("/no/");
    await expect(page.locator("html")).toHaveAttribute("lang", "no");
    await expect(page.locator("h1")).toContainText("Trekomponenter, prøver og korte serier");
    await expect(page.locator('a[href="/no/wycena/"]').first()).toHaveText("Forespørsel");
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
    await installDataLayerRecorder(page, "e2eDataLayerEvents");
    const piecodeRequests = [];
    if (process.env.E2E_ALLOW_GTM === "1") {
      page.on("request", (request) => {
        if (request.method() === "POST" && request.url() === "https://piecode.pl/api/events") {
          piecodeRequests.push(request.postData() || "");
        }
      });
    } else {
      await installPiecodeRecorder(page, "e2ePiecodeEvents");
    }
    const quoteUrl = process.env.E2E_PROD_SMOKE === "1" ? "/wycena/?piecode_dev=1&kajax_smoke=1" : "/wycena/?piecode_dev=1";
    await page.goto(quoteUrl);

    await page.getByLabel("Imię").fill("Lead E2E");
    await page.getByLabel("Telefon").fill("604000000");
    await page.getByLabel("Co mamy wykonać?").selectOption("custom_artistic");
    await page.getByLabel("Opisz element lub zakres prac").fill(
      "Potrzebujemy krótkiej serii precyzyjnych elementów drewnianych według rysunku.",
    );
    await page.getByLabel("Wyrażam zgodę na kontakt w sprawie przesłanego zapytania.").check();

    await page.locator("summary", { hasText: "Mam więcej danych" }).click();
    await page.getByLabel("Firma").fill("E2E Manufacturing");
    await page.getByLabel("Liczba sztuk").selectOption("small_series");
    await page.getByLabel("Lokalizacja").fill("Gdańsk / Europa");
    await page.getByLabel("Termin").fill("Próbka w czerwcu");
    await page.getByLabel("Zdjęcie, rysunek albo wzór").setInputFiles({
      name: "rysunek-testowy.txt",
      mimeType: "text/plain",
      buffer: Buffer.from("testowy opis rysunku"),
    });

    await page.getByRole("button", { name: "Wyślij zapytanie" }).click();
    await expect(page.locator(".message")).toContainText("Dziękujemy. Zapytanie dotarło");

    const events = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2eDataLayerEvents") || "[]"));
    expect(events).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ event: "quote_form_start", field_name: "name" }),
        expect.objectContaining({ event: "project_type_select", project_type: "custom_artistic", business_line: "custom_architectural_details", service_area: "poland_pomerania" }),
        expect.objectContaining({ event: "file_upload_complete", file_count: 1, project_type: "custom_artistic" }),
        expect.objectContaining({ event: "quote_form_submit_attempt", project_type: "custom_artistic" }),
        expect.objectContaining({ event: "quote_thank_you_view", project_type: "custom_artistic" }),
        expect.objectContaining({ event: "quote_sent", lead_type: "quote_request", project_type: "custom_artistic", service_area: "poland_pomerania" }),
        expect.objectContaining({ event: "generate_lead", lead_type: "quote_request", project_type: "custom_artistic", service_area: "poland_pomerania" }),
      ]),
    );
    const eventPayload = JSON.stringify(events);
    expect(eventPayload).not.toContain("Lead E2E");
    expect(eventPayload).not.toContain("604000000");
    expect(eventPayload).not.toContain("rysunek-testowy.txt");
    expect(eventPayload).not.toContain("Potrzebujemy krótkiej serii");
    let centralPayload = "";
    if (process.env.E2E_ALLOW_GTM === "1") {
      await expect.poll(() => piecodeRequests.length).toBeGreaterThan(0);
      centralPayload = piecodeRequests.join("\n");
      expect(centralPayload).toContain("generate_lead");
    } else {
      const piecodeEvents = await page.evaluate(() => JSON.parse(window.localStorage.getItem("e2ePiecodeEvents") || "[]"));
      expect(piecodeEvents).toEqual(
        expect.arrayContaining([
          expect.objectContaining({
            event_name: "lead_form_start",
            consent_granted: true,
            params: expect.objectContaining({
              page_type: "conversion",
            }),
          }),
          expect.objectContaining({
            event_name: "quote_attachment_added",
            params: expect.objectContaining({
              attachment_count: 1,
              project_type: "custom_artistic",
              service_area: "poland_pomerania",
            }),
          }),
          expect.objectContaining({
            event_name: "quote_sent",
            params: expect.objectContaining({
              lead_type: "quote_request",
              project_type: "custom_artistic",
              service_area: "poland_pomerania",
            }),
          }),
          expect.objectContaining({
            event_name: "generate_lead",
            options: expect.objectContaining({
              immediate: true,
              eventId: expect.stringMatching(/^kajax-quote-\d+-generate-lead$/),
            }),
            params: expect.objectContaining({
              lead_type: "quote_request",
              project_type: "custom_artistic",
              business_line: "custom_architectural_details",
              service_area: "poland_pomerania",
            }),
          }),
        ]),
      );
      centralPayload = JSON.stringify(piecodeEvents);
    }
    expect(centralPayload).not.toContain("Lead E2E");
    expect(centralPayload).not.toContain("604000000");
    expect(centralPayload).not.toContain("rysunek-testowy.txt");
    expect(centralPayload).not.toContain("Potrzebujemy krótkiej serii");
    await expectNoHorizontalOverflow(page);
  });

  test("keeps the quick form compact but exposes optional fields on demand", async ({ page }) => {
    await page.goto("/wycena/");

    await expect(page.locator("h1")).toContainText("Wyślij rysunek, zdjęcia miejsca albo opis elementu");
    await expect(page.locator(".quote-paths")).toContainText("B2B: element z rysunku");
    await expect(page.locator(".quote-paths")).toContainText("Pomorskie: schody, drzwi");
    await expect(page.locator(".file-prompt")).toContainText("Masz zdjęcie, rysunek albo wzór?");
    await expect(page.getByLabel("Zdjęcie, rysunek albo wzór")).toBeVisible();
    await expect(page.locator(".optional-fields")).not.toHaveAttribute("open", "");
    await page.locator("summary", { hasText: "Mam więcej danych" }).click();
    await expect(page.locator(".optional-fields")).toHaveAttribute("open", "");
    await expect(page.getByLabel("Firma")).toBeVisible();
    await expect(page.locator(".quote-aside").getByRole("link", { name: "Jak opisać zlecenie" })).toBeVisible();
    await expectNoHorizontalOverflow(page);
  });
});
