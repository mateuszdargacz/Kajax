from django.test import TestCase
from django.urls import reverse


class PublicPagesTests(TestCase):
    def test_public_pages_render(self):
        names = [
            "home",
            "production",
            "advertising_events",
            "construction",
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

    def test_robots_and_sitemap_render(self):
        robots = self.client.get(reverse("robots_txt"))
        sitemap = self.client.get(reverse("sitemap_xml"))

        self.assertEqual(robots.status_code, 200)
        self.assertContains(robots, "Sitemap:")
        self.assertEqual(sitemap.status_code, 200)
        self.assertContains(sitemap, "<urlset")
        self.assertContains(sitemap, 'xmlns:xhtml="http://www.w3.org/1999/xhtml"')
        self.assertContains(sitemap, 'hreflang="de"')
        self.assertContains(sitemap, "https://kajax.eu/de/produkcja-elementow-drewnianych/")
        self.assertContains(sitemap, "https://kajax.eu/jak-przygotowac-zapytanie/")
        self.assertContains(sitemap, "https://kajax.eu/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/")
        self.assertContains(sitemap, "https://kajax.eu/elementy-drewniane-dla-firm-reklamowych-i-eventowych/")
        self.assertContains(sitemap, "https://kajax.eu/schody-drewniane-co-wplywa-na-cene-i-termin/")

    def test_localized_page_keeps_language_in_links_and_meta(self):
        response = self.client.get("/de/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<html lang="de">')
        self.assertContains(response, "Produktions- und Bauschreinerei aus Pommern")
        self.assertContains(response, 'href="https://kajax.eu/de/"')
        self.assertContains(response, 'hreflang="en" href="https://kajax.eu/en/"')
        self.assertContains(response, 'href="/de/produkcja-elementow-drewnianych/"')
        self.assertNotContains(response, "Production and construction joinery from Pomerania")

    def test_norwegian_public_prefix_renders(self):
        response = self.client.get("/no/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<html lang="no">')
        self.assertContains(response, "Produksjons- og byggsnekkerverksted fra Pommern")
        self.assertContains(response, 'href="https://kajax.eu/no/"')
        self.assertContains(response, 'href="/no/wycena/"')

    def test_structured_data_uses_graph_and_page_service_entities(self):
        response = self.client.get(reverse("production"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"@graph"')
        self.assertContains(response, '"@type": "Service"')
        self.assertContains(response, '"@type": "FAQPage"')
        self.assertContains(response, '"@type": "OfferCatalog"')
        self.assertContains(response, "elementy POS i displayów")
        self.assertContains(response, '"@type": "CommunicateAction"')

    def test_guide_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("guide"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jak przygotować zapytanie")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Gdy element ma być powtarzalny")

    def test_short_series_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("short_series"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kiedy krótka seria elementów drewnianych ma sens")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Gdy element będzie wracał w zamówieniach")

    def test_advertising_events_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("advertising_events"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Elementy drewniane dla firm reklamowych")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Kiedy drewno wnosi wartość do ekspozycji")

    def test_stairs_pricing_page_uses_article_and_howto_schema(self):
        response = self.client.get(reverse("stairs_pricing"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Schody drewniane: co wpływa na cenę")
        self.assertContains(response, '"@type": "Article"')
        self.assertContains(response, '"@type": "HowTo"')
        self.assertContains(response, "Układ i wymiary schodów")
