from django.test import TestCase, override_settings
from django.urls import reverse


class PublicPagesTests(TestCase):
    def test_public_pages_render(self):
        names = [
            "home",
            "production",
            "advertising_events",
            "construction",
            "local_goscicino",
            "local_wejherowo",
            "local_gdynia",
            "local_gdansk",
            "local_trojmiasto",
            "local_pomorskie",
            "stairs_pricing",
            "architects",
            "realizations",
            "guide",
            "short_series",
            "quote",
            "contact",
        ]
        for name in names:
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    @override_settings(
        PIECODE_EVENTS_SDK_ENABLED=True,
        PIECODE_WORKSPACE_ID="kajax",
        PIECODE_EVENTS_SDK_URL="https://piecode.pl/sdk/piecode-events.js",
        PIECODE_EVENTS_AUTO_CONSENT=True,
        PIECODE_EVENTS_AUTO_PAGE_VIEW=True,
    )
    def test_piecode_sdk_is_loaded_with_kajax_workspace(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'src="https://piecode.pl/sdk/piecode-events.js"')
        self.assertContains(response, 'data-workspace-id="kajax"')
        self.assertContains(response, 'data-consent="manual"')
        self.assertContains(response, 'data-auto-page-view="true"')
        self.assertContains(response, 'data-piecode-auto-consent="true"')

    def test_robots_and_sitemap_render(self):
        robots = self.client.get(reverse("robots_txt"))
        sitemap = self.client.get(reverse("sitemap_xml"))

        self.assertEqual(robots.status_code, 200)
        self.assertEqual(robots["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(robots["Cache-Control"], "public, max-age=300")
        self.assertContains(robots, "Sitemap:")
        self.assertEqual(sitemap.status_code, 200)
        self.assertEqual(sitemap["Content-Type"], "application/xml; charset=utf-8")
        self.assertEqual(sitemap["Cache-Control"], "public, max-age=300")
        self.assertContains(sitemap, "<urlset")
        self.assertContains(sitemap, 'xmlns:xhtml="http://www.w3.org/1999/xhtml"')
        self.assertContains(sitemap, 'hreflang="de"')
        self.assertContains(sitemap, "https://kajax.eu/de/produkcja-elementow-drewnianych/")
        self.assertContains(sitemap, "https://kajax.eu/jak-przygotowac-zapytanie/")
        self.assertContains(sitemap, "https://kajax.eu/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/")
        self.assertContains(sitemap, "https://kajax.eu/elementy-drewniane-dla-firm-reklamowych-i-eventowych/")
        self.assertContains(sitemap, "https://kajax.eu/schody-drewniane-co-wplywa-na-cene-i-termin/")
        self.assertContains(sitemap, "https://kajax.eu/stolarka-budowlana-wejherowo/")
        self.assertContains(sitemap, "https://kajax.eu/stolarka-budowlana-trojmiasto/")
        self.assertContains(sitemap, "<lastmod>2026-06-15</lastmod>")

    def test_localized_page_keeps_language_in_links_and_meta(self):
        response = self.client.get("/de/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<html lang="de">')
        self.assertContains(response, "B2B-Fertigung von Holzelementen aus Polen")
        self.assertContains(response, 'href="https://kajax.eu/de/"')
        self.assertContains(response, 'hreflang="en" href="https://kajax.eu/en/"')
        self.assertContains(response, 'href="/de/produkcja-elementow-drewnianych/"')
        self.assertNotContains(response, "Production and construction joinery from Pomerania")

    def test_norwegian_public_prefix_renders(self):
        response = self.client.get("/no/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<html lang="no">')
        self.assertContains(response, "B2B-produksjon av trekomponenter fra Polen")
        self.assertContains(response, 'href="https://kajax.eu/no/"')
        self.assertContains(response, 'href="/no/wycena/"')

    def test_international_home_pages_keep_b2b_positioning(self):
        expectations = [
            ("/en/", "Wood components, samples and short production runs from Poland", "Outsource a wooden component without building a joinery line", "Poland"),
            ("/de/", "Holzelemente, Muster und Kleinserien aus Polen", "Holzelement auslagern, ohne eigene Tischlereilinie aufzubauen", "Polen"),
            ("/sv/", "Träkomponenter, prover och korta serier från Polen", "Lägg ut träkomponenten utan egen snickerikapacitet", "Polen"),
            ("/da/", "Trækomponenter, prøver og korte serier fra Polen", "Outsource trækomponenten uden egen snedkerkapacitet", "Polen"),
            ("/no/", "Trekomponenter, prøver og korte serier fra Polen", "Sett bort trekomponenten uten egen snekkerkapasitet", "Polen"),
        ]

        for path, h1, b2b_message, country in expectations:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, h1)
                self.assertContains(response, b2b_message)
                self.assertContains(response, country)

    def test_structured_data_uses_graph_and_page_service_entities(self):
        response = self.client.get(reverse("production"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"@graph"')
        self.assertContains(response, '"@type": "Service"')
        self.assertContains(response, '"@type": "FAQPage"')
        self.assertContains(response, '"@type": "OfferCatalog"')
        self.assertContains(response, '"@type": "BreadcrumbList"')
        self.assertContains(response, "elementy POS, displaye i ekspozytory")
        self.assertContains(response, '"@type": "CommunicateAction"')
        self.assertContains(response, 'data-page-key="production"')
        self.assertContains(response, 'data-business-line="b2b_wooden_components"')
        self.assertContains(response, 'property="og:image"')
        self.assertContains(response, "og-b2b-components.jpg")

    def test_home_uses_shorter_meta_and_b2b_proof_strip(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kajax Stolarstwo | Elementy drewniane B2B i stolarka na wymiar")
        self.assertContains(response, "Stolarnia z Gościcina: elementy drewniane dla firm")
        self.assertContains(response, "Produkcja dla firm")
        self.assertContains(response, "Elementy POS")
        self.assertContains(response, "og-home-workshop.jpg")

    def test_local_landing_page_has_service_schema_and_local_copy(self):
        response = self.client.get(reverse("local_wejherowo"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Stolarka budowlana Wejherowo")
        self.assertContains(response, "Schody, drzwi i listwy")
        self.assertContains(response, '"@type": "Service"')
        self.assertContains(response, 'data-page-type="local_service"')
        self.assertContains(response, "og-construction-joinery.jpg")

    def test_realizations_include_case_study_facts(self):
        response = self.client.get(reverse("realizations"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Krótka seria drewnianych elementów dla firmy")
        self.assertContains(response, "<dt>Problem</dt>")
        self.assertContains(response, "<dt>Zakres</dt>")
        self.assertContains(response, "<dt>Efekt</dt>")

    def test_guide_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("guide"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jak opisać zlecenie")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Element drewniany albo krótka seria dla firmy")

    def test_short_series_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("short_series"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Krótka seria elementów drewnianych")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Element, który ma być powtarzalny")

    def test_advertising_events_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("advertising_events"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Drewniane displaye")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Gdy materiał ma budować wrażenie marki")

    def test_stairs_pricing_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("stairs_pricing"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Schody drewniane: od czego zależy cena")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Układ i wymiary schodów")
