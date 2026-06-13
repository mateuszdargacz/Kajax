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
    "architects": "0.8",
    "realizations": "0.7",
    "guide": "0.8",
    "contact": "0.7",
}

SERVICE_AREAS = {
    "production": ["Polska", "Europa", "Europa B2B"],
    "construction": ["Pomorskie", "Gościcino", "Wejherowo", "Trójmiasto"],
    "architects": ["Pomorskie", "Polska", "Europa"],
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
    return {
        "canonical_url": canonical_url,
        "alternate_urls": alternate_urls(page["path"]),
        "og_locale": OG_LOCALES.get(code, code),
        "structured_data": json.dumps(build_structured_data(page, canonical_url, code), ensure_ascii=False),
    }


def build_structured_data(page, canonical_url=None, language_code=None):
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
    graph = [organization, website, webpage]
    if page["key"] in {"production", "construction", "architects"}:
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
    if page["key"] == "guide":
        graph.extend(build_guide_structured_data(page, canonical_url, language_code, organization_id))
    return {"@context": "https://schema.org", "@graph": graph}


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


def build_guide_structured_data(page, canonical_url, language_code, organization_id):
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
