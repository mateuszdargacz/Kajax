from django.urls import path

from leads.views import QuoteRequestView
from pages.views import MarketingPageView, robots_txt, sitemap_xml


urlpatterns = [
    path("", MarketingPageView.as_view(page_key="home"), name="home"),
    path("produkcja-elementow-drewnianych/", MarketingPageView.as_view(page_key="production"), name="production"),
    path(
        "elementy-drewniane-dla-firm-reklamowych-i-eventowych/",
        MarketingPageView.as_view(page_key="advertising_events"),
        name="advertising_events",
    ),
    path("stolarka-budowlana/", MarketingPageView.as_view(page_key="construction"), name="construction"),
    path("stolarka-budowlana-goscicino/", MarketingPageView.as_view(page_key="local_goscicino"), name="local_goscicino"),
    path("stolarka-budowlana-wejherowo/", MarketingPageView.as_view(page_key="local_wejherowo"), name="local_wejherowo"),
    path("stolarka-budowlana-gdynia/", MarketingPageView.as_view(page_key="local_gdynia"), name="local_gdynia"),
    path("stolarka-budowlana-gdansk/", MarketingPageView.as_view(page_key="local_gdansk"), name="local_gdansk"),
    path("stolarka-budowlana-trojmiasto/", MarketingPageView.as_view(page_key="local_trojmiasto"), name="local_trojmiasto"),
    path("stolarka-budowlana-pomorskie/", MarketingPageView.as_view(page_key="local_pomorskie"), name="local_pomorskie"),
    path(
        "schody-drewniane-co-wplywa-na-cene-i-termin/",
        MarketingPageView.as_view(page_key="stairs_pricing"),
        name="stairs_pricing",
    ),
    path("dla-architektow-i-firm/", MarketingPageView.as_view(page_key="architects"), name="architects"),
    path("realizacje/", MarketingPageView.as_view(page_key="realizations"), name="realizations"),
    path("jak-przygotowac-zapytanie/", MarketingPageView.as_view(page_key="guide"), name="guide"),
    path(
        "kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/",
        MarketingPageView.as_view(page_key="short_series"),
        name="short_series",
    ),
    path("wycena/", QuoteRequestView.as_view(), name="quote"),
    path("kontakt/", MarketingPageView.as_view(page_key="contact"), name="contact"),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap_xml, name="sitemap_xml"),
]
