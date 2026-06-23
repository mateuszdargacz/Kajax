from functools import lru_cache

from django.conf import settings
from django.utils.translation import get_language

from pages.content import get_nav_items
from pages.ui import get_ui_copy


@lru_cache(maxsize=1)
def static_asset_version():
    configured = getattr(settings, "STATIC_VERSION", "")
    if configured:
        return configured
    asset_paths = []
    static_dirs = [settings.BASE_DIR / "static"]
    static_root = getattr(settings, "STATIC_ROOT", None)
    if static_root:
        static_dirs.append(static_root)

    for static_dir in static_dirs:
        asset_paths.extend(
            [
                static_dir / "site" / "css" / "styles.css",
                static_dir / "site" / "js" / "site.js",
            ],
        )
        image_dir = static_dir / "site" / "img"
        if image_dir.exists():
            asset_paths.extend(path for path in image_dir.iterdir() if path.is_file())
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
            "piecode_workspace_id": settings.PIECODE_WORKSPACE_ID,
            "piecode_events_sdk_enabled": settings.PIECODE_EVENTS_SDK_ENABLED,
            "piecode_events_sdk_url": settings.PIECODE_EVENTS_SDK_URL,
            "piecode_events_auto_consent": settings.PIECODE_EVENTS_AUTO_CONSENT,
            "piecode_events_auto_page_view": settings.PIECODE_EVENTS_AUTO_PAGE_VIEW,
        },
        "nav_items": get_nav_items(language),
    }
