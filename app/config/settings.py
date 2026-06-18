import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent


def env_bool(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "t", "yes", "y", "on"}


def env_list(name, default=None):
    value = os.environ.get(name)
    if not value:
        return default or []
    return [item.strip() for item in value.split(",") if item.strip()]


DEBUG = env_bool("DJANGO_DEBUG", default=True)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-local-dev-only-change-me")

if not DEBUG and SECRET_KEY == "django-insecure-local-dev-only-change-me":
    raise ImproperlyConfigured("DJANGO_SECRET_KEY must be set when DJANGO_DEBUG=false.")

ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
    ["kajax.eu", "www.kajax.eu", "localhost", "127.0.0.1"],
)
CSRF_TRUSTED_ORIGINS = env_list(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    ["https://kajax.eu", "https://www.kajax.eu"],
)

SITE_URL = os.environ.get("DJANGO_SITE_URL", "https://kajax.eu").rstrip("/")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "leads",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "leads.middleware.AttributionCaptureMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "pages.context_processors.site_context",
            ],
        },
    },
]

candidate_data_dir = BASE_DIR / "data"
DATA_DIR = Path(os.environ.get("DATA_DIR", candidate_data_dir if candidate_data_dir.exists() else PROJECT_ROOT / "data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("SQLITE_PATH", str(DATA_DIR / "site.sqlite3")),
    }
}

LANGUAGE_CODE = "pl"
LANGUAGES = [
    ("pl", _("Polski")),
    ("en", _("English")),
    ("no", _("Norsk")),
    ("sv", _("Svenska")),
    ("da", _("Dansk")),
    ("de", _("Deutsch")),
]
LOCALE_PATHS = [BASE_DIR / "locale"]
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = DATA_DIR / "public" / "static"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = DATA_DIR / "public" / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CONTACT_EMAIL = os.environ.get("KAJAX_CONTACT_EMAIL", "mail@kajax.eu")
CONTACT_PHONE = os.environ.get("KAJAX_CONTACT_PHONE", "604 238 246")
CONTACT_PHONE_URI = "".join(char for char in CONTACT_PHONE if char.isdigit() or char == "+")
CONTACT_ADDRESS = os.environ.get("KAJAX_CONTACT_ADDRESS", "84-241 Gościcino, ul. Zielona 17")
COMPANY_NAME = os.environ.get("KAJAX_COMPANY_NAME", "Kajax Stolarstwo")
LEAD_RECIPIENTS = env_list("KAJAX_LEAD_RECIPIENTS", [CONTACT_EMAIL])

if os.environ.get("EMAIL_HOST"):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env_bool("EMAIL_USE_TLS", default=True)
EMAIL_USE_SSL = env_bool("EMAIL_USE_SSL", default=False)
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "Kajax Stolarstwo <mail@kajax.eu>")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
LEAD_EMAIL_FAIL_SILENTLY = env_bool("LEAD_EMAIL_FAIL_SILENTLY", default=True)

GTM_ID = os.environ.get("GTM_ID", "")
GA4_MEASUREMENT_ID = os.environ.get("GA4_MEASUREMENT_ID", "")
GOOGLE_SITE_VERIFICATION = os.environ.get("GOOGLE_SITE_VERIFICATION", "")

PIECODE_LEAD_SYNC_ENABLED = env_bool("PIECODE_LEAD_SYNC_ENABLED", default=False)
PIECODE_LEAD_SYNC_SEND_LEAD = env_bool("PIECODE_LEAD_SYNC_SEND_LEAD", default=False)
PIECODE_LEAD_SYNC_LEAD_URL = os.environ.get("PIECODE_LEAD_SYNC_LEAD_URL", "").strip()
PIECODE_LEAD_SYNC_EVENT_URL = os.environ.get("PIECODE_LEAD_SYNC_EVENT_URL", "").strip()
PIECODE_LEAD_SYNC_TIMEOUT_SECONDS = float(os.environ.get("PIECODE_LEAD_SYNC_TIMEOUT_SECONDS", "4"))

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = env_bool("DJANGO_SECURE_SSL_REDIRECT", default=False)
X_FRAME_OPTIONS = "DENY"
