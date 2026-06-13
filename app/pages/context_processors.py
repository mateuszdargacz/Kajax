from django.conf import settings
from django.utils.translation import get_language

from pages.content import get_nav_items
from pages.ui import get_ui_copy


def static_asset_version():
    configured = getattr(settings, "STATIC_VERSION", "")
    if configured:
        return configured
    asset_paths = [
        settings.BASE_DIR / "static" / "site" / "css" / "styles.css",
        settings.BASE_DIR / "static" / "site" / "js" / "site.js",
    ]
    mtimes = []
    for path in asset_paths:
        try:
            mtimes.append(path.stat().st_mtime)
        except OSError:
            continue
    return str(int(max(mtimes))) if mtimes else "1"


def site_context(request):
    language = get_language() or settings.LANGUAGE_CODE
    return {
        "ui": get_ui_copy(language),
        "static_version": static_asset_version(),
        "site": {
            "name": settings.COMPANY_NAME,
            "url": settings.SITE_URL,
            "email": settings.CONTACT_EMAIL,
            "phone": settings.CONTACT_PHONE,
            "phone_uri": settings.CONTACT_PHONE_URI,
            "address": settings.CONTACT_ADDRESS,
            "gtm_id": settings.GTM_ID,
            "ga4_measurement_id": settings.GA4_MEASUREMENT_ID,
            "google_site_verification": settings.GOOGLE_SITE_VERIFICATION,
        },
        "nav_items": get_nav_items(language),
    }
