from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.utils import translation

from leads.views import QuoteRequestView
from pages.views import MarketingPageView


def health(request):
    return JsonResponse({"ok": True, "service": "kajax"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
    path("i18n/", include("django.conf.urls.i18n")),
]


def force_language(view, language_code):
    def wrapped(request, *args, **kwargs):
        previous_language = translation.get_language()
        translation.activate(language_code)
        request.LANGUAGE_CODE = language_code
        try:
            response = view(request, *args, **kwargs)
            if hasattr(response, "render") and not response.is_rendered:
                response.render()
            return response
        finally:
            if previous_language:
                translation.activate(previous_language)
            else:
                translation.deactivate()

    return wrapped


norwegian_urlpatterns = [
    path("no/", force_language(MarketingPageView.as_view(page_key="home"), "no")),
    path(
        "no/produkcja-elementow-drewnianych/",
        force_language(MarketingPageView.as_view(page_key="production"), "no"),
    ),
    path(
        "no/stolarka-budowlana/",
        force_language(MarketingPageView.as_view(page_key="construction"), "no"),
    ),
    path(
        "no/dla-architektow-i-firm/",
        force_language(MarketingPageView.as_view(page_key="architects"), "no"),
    ),
    path(
        "no/realizacje/",
        force_language(MarketingPageView.as_view(page_key="realizations"), "no"),
    ),
    path(
        "no/jak-przygotowac-zapytanie/",
        force_language(MarketingPageView.as_view(page_key="guide"), "no"),
    ),
    path("no/wycena/", force_language(QuoteRequestView.as_view(), "no")),
    path(
        "no/kontakt/",
        force_language(MarketingPageView.as_view(page_key="contact"), "no"),
    ),
]

urlpatterns += norwegian_urlpatterns

urlpatterns += i18n_patterns(
    path("", include("pages.urls")),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
