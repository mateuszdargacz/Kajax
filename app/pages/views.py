import json
from xml.sax.saxutils import escape as xml_escape

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.generic import TemplateView

from pages.content import (
    PATHS,
    get_localized_path,
    get_audience_cards,
    get_home_realization_cases,
    get_page_content,
    get_process_steps,
    get_realization_cases,
    iter_sitemap_pages,
    normalize_language,
)


OG_LOCALES = {
    "pl": "pl_PL",
    "en": "en_US",
    "de": "de_DE",
    "sv": "sv_SE",
    "da": "da_DK",
    "no": "nb_NO",
}

SITEMAP_PRIORITIES = {
    "home": "1.0",
    "production": "0.9",
    "quote": "0.9",
    "construction": "0.8",
    "local_goscicino": "0.7",
    "local_wejherowo": "0.7",
    "local_gdynia": "0.7",
    "local_gdansk": "0.7",
    "local_trojmiasto": "0.7",
    "local_pomorskie": "0.7",
    "architects": "0.8",
    "realizations": "0.7",
    "guide": "0.8",
    "short_series": "0.8",
    "advertising_events": "0.8",
    "contact": "0.7",
    "stairs_pricing": "0.8",
}

SITEMAP_LASTMOD = "2026-06-15"

SERVICE_AREAS = {
    "production": ["Polska", "Europa", "Europa B2B"],
    "construction": ["Pomorskie", "Gościcino", "Wejherowo", "Trójmiasto"],
    "local_goscicino": ["Gościcino", "Wejherowo", "Pomorskie"],
    "local_wejherowo": ["Wejherowo", "Reda", "Rumia", "Pomorskie"],
    "local_gdynia": ["Gdynia", "Trójmiasto", "Pomorskie"],
    "local_gdansk": ["Gdańsk", "Trójmiasto", "Pomorskie"],
    "local_trojmiasto": ["Gdańsk", "Gdynia", "Sopot", "Trójmiasto"],
    "local_pomorskie": ["Pomorskie", "Gościcino", "Wejherowo", "Trójmiasto"],
    "architects": ["Pomorskie", "Polska", "Europa"],
}

PAGE_ANALYTICS = {
    "home": {"page_type": "landing", "business_line": "mixed", "service_area": "pomorskie_b2b_europe"},
    "production": {"page_type": "service", "business_line": "b2b_wooden_components", "service_area": "poland_europe_b2b"},
    "short_series": {"page_type": "guide", "business_line": "b2b_wooden_components", "service_area": "poland_europe_b2b"},
    "advertising_events": {"page_type": "guide", "business_line": "b2b_wooden_components", "service_area": "poland_europe_b2b"},
    "construction": {"page_type": "service", "business_line": "construction_joinery", "service_area": "pomerania"},
    "local_goscicino": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "goscicino"},
    "local_wejherowo": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "wejherowo"},
    "local_gdynia": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "gdynia"},
    "local_gdansk": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "gdansk"},
    "local_trojmiasto": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "trojmiasto"},
    "local_pomorskie": {"page_type": "local_service", "business_line": "construction_joinery", "service_area": "pomerania"},
    "stairs_pricing": {"page_type": "guide", "business_line": "construction_joinery", "service_area": "pomerania"},
    "architects": {"page_type": "service", "business_line": "custom_architectural_details", "service_area": "poland_europe"},
    "realizations": {"page_type": "portfolio", "business_line": "mixed", "service_area": "pomorskie_b2b_europe"},
    "guide": {"page_type": "guide", "business_line": "mixed", "service_area": "pomorskie_b2b_europe"},
    "quote": {"page_type": "conversion", "business_line": "mixed", "service_area": "pomorskie_b2b_europe"},
    "contact": {"page_type": "contact", "business_line": "mixed", "service_area": "pomorskie_b2b_europe"},
}


class MarketingPageView(TemplateView):
    page_key = "home"

    def get_template_names(self):
        language = get_language()
        return [get_page_content(self.page_key, language)["template"]]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language()
        page = get_page_content(self.page_key, language)
        context.update(
            {
                "page": page,
                "audience_cards": get_audience_cards(language),
                "process_steps": get_process_steps(language),
                "home_realization_cases": get_home_realization_cases(language),
                "realization_cases": get_realization_cases(language),
                **build_seo_context(page, language),
            }
        )
        return context


def robots_txt(request):
    body = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {settings.SITE_URL}/sitemap.xml",
            "",
        ]
    )
    return HttpResponse(body, content_type="text/plain")


def sitemap_xml(request):
    language = get_language() or settings.LANGUAGE_CODE
    items = []
    for code, _label in settings.LANGUAGES:
        for page in iter_sitemap_pages(code):
            url = absolute_url(page["path"], code)
            alternates = "\n".join(
                f'<xhtml:link rel="alternate" hreflang="{item["code"]}" href="{xml_escape(item["url"])}" />'
                for item in alternate_urls(page["path"])
            )
            priority = SITEMAP_PRIORITIES.get(page["key"], "0.6")
            items.append(
                "\n".join(
                    [
                        "<url>",
                        f"<loc>{xml_escape(url)}</loc>",
                        alternates,
                        f"<lastmod>{SITEMAP_LASTMOD}</lastmod>",
                        "<changefreq>weekly</changefreq>",
                        f"<priority>{priority}</priority>",
                        "</url>",
                    ]
                )
            )

    body = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        f'{"".join(items)}</urlset>'
    )
    response = HttpResponse(body, content_type="application/xml")
    response["Content-Language"] = language
    return response


def absolute_url(path, language_code):
    return f"{settings.SITE_URL}{get_localized_path(path, language_code)}"


def alternate_urls(path):
    urls = [{"code": code, "url": absolute_url(path, code)} for code, _label in settings.LANGUAGES]
    urls.append({"code": "x-default", "url": absolute_url(path, settings.LANGUAGE_CODE)})
    return urls


def build_seo_context(page, language_code):
    code = normalize_language(language_code)
    canonical_url = absolute_url(page["path"], code)
    og_image_url = build_og_image_url(page)
    return {
        "canonical_url": canonical_url,
        "alternate_urls": alternate_urls(page["path"]),
        "og_locale": OG_LOCALES.get(code, code),
        "og_image_url": og_image_url,
        "page_analytics": build_page_analytics(page, code),
        "structured_data": json.dumps(build_structured_data(page, canonical_url, code, og_image_url), ensure_ascii=False),
    }


def build_og_image_url(page):
    image = page.get("og_image")
    if not image:
        return ""
    return f"{settings.SITE_URL}{settings.STATIC_URL}site/img/{image}"


def build_page_analytics(page, language_code):
    analytics = PAGE_ANALYTICS.get(page["key"], PAGE_ANALYTICS["home"]).copy()
    analytics["page_key"] = page["key"]
    analytics["language"] = normalize_language(language_code)
    return analytics


def build_structured_data(page, canonical_url=None, language_code=None, image_url=""):
    canonical_url = canonical_url or absolute_url(page["path"], language_code or settings.LANGUAGE_CODE)
    language_code = normalize_language(language_code)
    organization_id = f"{settings.SITE_URL}/#organization"
    website_id = f"{settings.SITE_URL}/#website"
    webpage_id = f"{canonical_url}#webpage"
    organization = {
        "@id": organization_id,
        "@type": "LocalBusiness",
        "name": settings.COMPANY_NAME,
        "url": settings.SITE_URL,
        "telephone": settings.CONTACT_PHONE,
        "email": settings.CONTACT_EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "ul. Zielona 17",
            "postalCode": "84-241",
            "addressLocality": "Gościcino",
            "addressRegion": "Pomorskie",
            "addressCountry": "PL",
        },
        "areaServed": ["Pomorskie", "Polska", "Europa B2B"],
        "description": str(page.get("description", "")),
    }
    website = {
        "@id": website_id,
        "@type": "WebSite",
        "url": settings.SITE_URL,
        "name": settings.COMPANY_NAME,
        "publisher": {"@id": organization_id},
        "inLanguage": settings.LANGUAGE_CODE,
    }
    webpage = {
        "@id": webpage_id,
        "@type": "WebPage",
        "url": canonical_url,
        "name": str(page.get("title", "")),
        "description": str(page.get("description", "")),
        "isPartOf": {"@id": website_id},
        "about": {"@id": organization_id},
        "inLanguage": language_code,
    }
    if image_url:
        webpage["image"] = image_url
    graph = [organization, website, webpage, build_breadcrumb_structured_data(page, canonical_url, language_code)]
    if page["key"] in {"production", "construction", "architects"} or page["key"].startswith("local_"):
        service = {
            "@id": f"{canonical_url}#service",
            "@type": "Service",
            "name": str(page.get("h1", page.get("title", ""))),
            "description": str(page.get("lead", page.get("description", ""))),
            "serviceType": str(page.get("eyebrow", page["key"])),
            "provider": {"@id": organization_id},
            "areaServed": SERVICE_AREAS.get(page["key"], ["Pomorskie", "Polska", "Europa"]),
            "url": canonical_url,
            "potentialAction": {
                "@type": "CommunicateAction",
                "name": "Request a quote",
                "target": absolute_url(PATHS["quote"], language_code),
            },
        }
        offer_catalog = build_offer_catalog(page)
        if offer_catalog:
            service["hasOfferCatalog"] = offer_catalog
        graph.append(service)
    if page.get("faq"):
        graph.append(
            {
                "@id": f"{canonical_url}#faq",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": question,
                        "acceptedAnswer": {"@type": "Answer", "text": answer},
                    }
                    for question, answer in page["faq"]
                ],
            }
        )
    if page["key"] in {"guide", "short_series", "stairs_pricing", "advertising_events"}:
        graph.extend(build_guide_structured_data(page, canonical_url, language_code, organization_id, image_url))
    return {"@context": "https://schema.org", "@graph": graph}


def build_breadcrumb_structured_data(page, canonical_url, language_code):
    home_url = absolute_url(PATHS["home"], language_code)
    items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": settings.COMPANY_NAME,
            "item": home_url,
        }
    ]
    if page["key"] != "home":
        items.append(
            {
                "@type": "ListItem",
                "position": 2,
                "name": str(page.get("h1", page.get("title", ""))),
                "item": canonical_url,
            }
        )
    return {
        "@id": f"{canonical_url}#breadcrumb",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def build_offer_catalog(page):
    offers = []
    for section in page.get("sections", []):
        for item in section.get("items", []):
            offers.append(
                {
                    "@type": "Offer",
                    "category": str(section.get("title", "")),
                    "itemOffered": {
                        "@type": "Service",
                        "name": str(item),
                        "description": str(section.get("body", "")),
                    },
                }
            )
    if not offers:
        return None
    return {
        "@type": "OfferCatalog",
        "name": str(page.get("h1", page.get("title", ""))),
        "itemListElement": offers,
    }


def build_guide_structured_data(page, canonical_url, language_code, organization_id, image_url=""):
    article_id = f"{canonical_url}#article"
    howto_id = f"{canonical_url}#howto"
    article = {
        "@id": article_id,
        "@type": "Article",
        "headline": str(page.get("h1", page.get("title", ""))),
        "description": str(page.get("description", "")),
        "author": {"@id": organization_id},
        "publisher": {"@id": organization_id},
        "mainEntityOfPage": canonical_url,
        "inLanguage": normalize_language(language_code),
    }
    if image_url:
        article["image"] = image_url
    howto = {
        "@id": howto_id,
        "@type": "HowTo",
        "name": str(page.get("h1", page.get("title", ""))),
        "description": str(page.get("lead", page.get("description", ""))),
        "inLanguage": normalize_language(language_code),
        "step": [
            {
                "@type": "HowToStep",
                "name": str(section.get("title", "")),
                "text": " ".join([str(section.get("body", "")), " ".join(str(item) for item in section.get("items", []))]).strip(),
            }
            for section in page.get("sections", [])
        ],
    }
    return [article, howto]
