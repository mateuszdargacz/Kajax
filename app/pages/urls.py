from django.urls import path

from leads.views import QuoteRequestView
from pages.views import MarketingPageView, robots_txt, sitemap_xml


urlpatterns = [
    path("", MarketingPageView.as_view(page_key="home"), name="home"),
    path("produkcja-elementow-drewnianych/", MarketingPageView.as_view(page_key="production"), name="production"),
    path("stolarka-budowlana/", MarketingPageView.as_view(page_key="construction"), name="construction"),
    path("dla-architektow-i-firm/", MarketingPageView.as_view(page_key="architects"), name="architects"),
    path("realizacje/", MarketingPageView.as_view(page_key="realizations"), name="realizations"),
    path("jak-przygotowac-zapytanie/", MarketingPageView.as_view(page_key="guide"), name="guide"),
    path("wycena/", QuoteRequestView.as_view(), name="quote"),
    path("kontakt/", MarketingPageView.as_view(page_key="contact"), name="contact"),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap_xml, name="sitemap_xml"),
]
