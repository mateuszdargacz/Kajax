# Kajax Django 6 Rebuild Plan

Last updated: 2026-06-13

## Goal

Rebuild Kajax from the current Django 1.9/AngularJS/Bootstrap 3 site into a modern, fast, conversion-oriented Django 6.0 site running on Python 3.13.

The new site should reposition Kajax away from "local carpenter for everything" and toward:

- B2B wooden components, short series and semi-products,
- construction joinery: stairs, doors, trims, built-ins,
- custom/artistic/premium woodwork for architects, designers and demanding investors.

The site must generate better-qualified leads, support SEO and Ads measurement from the start, and keep the existing server convention: Docker Compose app service + per-project nginx config included by the central nginx container.

## Current State Confirmed

- Repository is migrated to GitHub: `https://github.com/mateuszdargacz/Kajax`.
- Server checkout is `/projects/kajax`.
- `kajax.eu` currently returns Cloudflare `502 Bad Gateway`.
- Production database has been copied locally to `data/kajax.db`.
- Production `data/public` has been copied locally to `data/public`.
- Runtime data is ignored by git via `data/`.
- Existing DB content is small:
  - `CompanyData`: 1
  - `Service`: 5
  - `Client`: 8
  - `Project`: 1
  - `ProjectImage`: 1
  - `Slider`: 1
  - `SliderImage`: 3
  - `Message`: 10
- Existing dynamic content is not enough to justify a CMS-heavy rebuild.
- Existing production static directory contains old theme assets that are missing from git. These should be used only as reference/assets, not as the basis for the new frontend.

## Key Architecture Decisions

### Confirmed Human Decisions

- Database: SQLite for v1, because the database will mainly store leads and uploaded quote files.
- Languages: prepare translation infrastructure for Polish, English, Norwegian, Swedish, Danish and German.
- Initial content language: Polish first. Other locales may initially fall back, but templates, forms, URLs and metadata must be translation-ready from the beginning.
- Packing/shipping: communicate cautiously as "do ustalenia". Kajax can evaluate logistics and has practical ways to handle it, but it should not be sold as a fixed guaranteed service before each project is qualified.
- Geography:
  - private/custom/construction joinery leads: Pomorskie and local region first,
  - B2B wooden components: Europe-wide if the project, logistics and series size make sense.
- Photos: current production media can be used as temporary reference/placeholder assets, but the new site should be designed around a fresh photo set.
- Public data confirmed:
  - display name: `Kajax Stolarstwo`,
  - address: `84-241 Gościcino, ul. Zielona 17`,
  - phone: `604 238 246`,
  - current email: `kajax-stolarstwo@o2.pl`,
  - future email: new company-domain mailbox to be configured.
- Email: assume SMTP will be available. Quote submission should notify Kajax and send confirmation to the requester.
- DNS/Cloudflare: DNS is considered correct. Current `502` is caused by the broken/outdated app build on the server.
- Performance: the site must be extremely fast from the start. No SPA, no external fonts, no heavy JS framework, no large unoptimized images, no nonessential third-party scripts before tracking is explicitly configured.

### Backend

- Python: `3.13`
- Django: `6.0.x`
- App style: server-rendered Django templates, not SPA
- Database for first release: SQLite in `data/`
- Admin: keep Django admin for leads and optional portfolio management
- API: remove old DRF/Angular API unless a specific need appears
- Static/media:
  - static collected to `data/public/static`
  - uploads/media stored in `data/public/media`
- Secrets:
  - no hardcoded `SECRET_KEY`
  - config from environment variables
  - production values outside git

### Frontend

- No AngularJS.
- No React/Next for this project.
- No external web fonts in v1.
- No production images embedded until they are selected, compressed and mapped through the photo placeholder list.
- Build a custom server-rendered frontend with:
  - semantic HTML,
  - custom CSS or a very small CSS layer,
  - minimal vanilla JS for tracking/form UX,
  - progressive enhancement only.
- Use real workshop/project photos. No generic stock.
- The first viewport must immediately communicate: production-capable workshop, B2B/custom joinery, quote CTA.

### Performance Budget

- HTML must be server-rendered and useful without JavaScript.
- Critical CSS should stay small and local.
- JavaScript should only handle tracking and small UX enhancements.
- No render-blocking third-party assets except explicitly configured GTM/GA tags.
- Images must be compressed, dimensioned and lazy-loaded outside the hero.
- Use named placeholders during implementation so no accidental heavy legacy images ship in v1.
- Target Lighthouse performance: 90+ on mobile before launch.

### Content

Use a hybrid model:

- Hardcoded/page-managed in code:
  - positioning,
  - service pages,
  - SEO copy,
  - FAQs,
  - process sections,
  - CTA text,
  - structured data copy.
- Database-managed:
  - quote requests/leads,
  - uploaded files,
  - optional portfolio cases if we want the owner/admin to add them later,
  - company/contact details only if we still want admin editing.

This keeps the marketing site fast, stable and reviewable in git while preserving admin usefulness for leads.

## Target URL Structure

Initial release:

```text
/
/produkcja-elementow-drewnianych
/stolarka-budowlana
/dla-architektow-i-firm
/realizacje
/wycena
/kontakt
/robots.txt
/sitemap.xml
```

Planned expansion:

```text
/elementy-drewniane-dla-firm
/schody-drewniane
/drzwi-i-listwy-drewniane
/stolarstwo-artystyczne
/dla-architektow-i-projektantow
/jak-przygotowac-zapytanie
```

## Page Requirements

### Home

- H1: `Stolarnia dla firm, architektów i wymagających realizacji z drewna`
- Primary CTA: `Wyślij projekt do wyceny`
- Secondary CTA: `Zobacz zakres prac`
- Three paths:
  - elementy drewniane dla firm,
  - stolarka budowlana,
  - custom i trudniejsze realizacje.
- B2B production section.
- Quoting process section.
- Selected realizations with context.
- Contact/quote CTA.

### B2B Landing

Route: `/produkcja-elementow-drewnianych`

Purpose: main Ads and SEO landing.

Must explain:

- who this is for,
- what types of elements can be produced,
- prototype/sample/short series workflow,
- what input is needed for quote,
- whether shipping/packing is available,
- CTA to upload/send specification.

### Construction Joinery Landing

Route: `/stolarka-budowlana`

Must cover:

- stairs,
- doors,
- trims,
- built-ins,
- premium local projects,
- when to contact for quote,
- local SEO terms: Gościcino, Wejherowo, Pomorskie.

### Architects/Firms Landing

Route: `/dla-architektow-i-firm`

Must feel more premium and portfolio-led:

- difficult details,
- design/specification cooperation,
- custom interior and commercial elements,
- work from drawings/photos.

### Quote Form

Route: `/wycena`

Required fields:

- name,
- email,
- phone,
- company,
- inquiry type:
  - B2B wooden components,
  - construction joinery,
  - custom/artistic,
  - other,
- scale:
  - one piece,
  - small series,
  - recurring cooperation,
  - not sure yet,
- location,
- expected timing,
- description,
- file/photo upload,
- consent checkbox.

Store leads in DB and expose them in admin. Send an email notification to Kajax and a confirmation email to the requester when SMTP settings are configured.

## Internationalization

Implement i18n from the start.

Initial setup:

- `LANGUAGE_CODE = "pl"`
- `LANGUAGES`:
  - `pl`: Polski
  - `en`: English
  - `no`: Norsk
  - `sv`: Svenska
  - `da`: Dansk
  - `de`: Deutsch
- wrap visible strings with `{% translate %}` or `gettext_lazy`
- keep templates ready for `makemessages`
- use locale files under `locale/`
- avoid baking untranslatable text into JS

Polish is the source content for v1. Other languages may be translated iteratively, but the implementation must avoid hard-to-translate strings.

Implementation rules:

- Templates render keyed copy such as `ui.*`, `page.*` and content dictionaries, not hardcoded Polish strings.
- Translate copy as it is added, with context-specific wording instead of literal phrase replacement.
- Do not include non-Polish URLs in `sitemap.xml` until page-level content, forms, emails and metadata are fully translated for that locale.

## SEO Requirements

Every public page:

- one H1,
- unique title,
- unique meta description,
- canonical URL,
- Open Graph title/description/image,
- image alt text,
- internal links to `/wycena`,
- FAQ section where appropriate,
- LocalBusiness/Organization JSON-LD,
- Service schema for service pages where useful.

Required generated files:

- `sitemap.xml`
- `robots.txt`

Primary SEO clusters:

- `produkcja elementów drewnianych na zamówienie`
- `elementy drewniane dla firm`
- `drewniane półprodukty na zamówienie`
- `krótkie serie drewniane`
- `stolarnia produkcyjna pomorskie`
- `stolarka budowlana pomorskie`
- `schody drewniane Wejherowo`
- `stolarz Gościcino`
- `stolarz dla architekta`

## Tracking Requirements

Implement dataLayer events without hardcoding tracking IDs.

Environment/config values:

- `GTM_ID`
- `GA4_MEASUREMENT_ID` if used directly
- `GOOGLE_SITE_VERIFICATION`

Events:

- `quote_form_view`
- `quote_form_start`
- `generate_lead`
- `phone_click`
- `email_click`
- `file_upload_complete`
- `portfolio_view`
- `project_type_select`
- `spec_download` if a downloadable B2B brief is added

Primary conversion:

- `generate_lead`

Secondary conversions:

- `phone_click`
- `email_click`
- `file_upload_complete`

## Data Migration Plan

1. Keep copied production SQLite DB in `data/kajax.db`.
2. Create new Django 6 models:
   - `QuoteRequest`,
   - `QuoteAttachment`,
   - optional `PortfolioCase`,
   - optional `PortfolioImage`.
3. Decide whether old content tables should be migrated or replaced:
   - services: likely replace with hardcoded content,
   - clients: likely use as logo/reference list only if still useful,
   - projects: one weak old project, likely replace with new portfolio cases,
   - messages: preserve in backup, optionally import as legacy leads.
4. Preserve all media files in `data/public/media`.
5. Write a one-off management command if old records need to be imported into new models.

## Docker And Nginx Plan

Keep the existing convention:

- repo path: `/projects/kajax`
- central nginx includes `/projects/*/nginx/*.conf`
- project nginx config lives in `nginx/kajax.conf`
- Docker Compose service is `web`
- app binds Gunicorn to `/nginx/kajax.sock`
- `./data` is mounted into the container
- `./nginx` is mounted into the container

New Docker target:

- base image: `python:3.13-slim`
- install only required system libs for Pillow/builds
- install Python dependencies from a locked requirements file or `pyproject.toml`
- run as non-root if practical
- command in compose:
  - `gunicorn config.wsgi:application --workers 2 --bind unix:///nginx/kajax.sock`

Nginx requirements:

- `kajax.eu` canonical
- `www.kajax.eu` redirect to canonical
- static alias: `/projects/kajax/data/public/static`
- media alias: `/projects/kajax/data/public/media`
- file upload size high enough for quote attachments
- add HTTPS/canonical handling according to existing Cloudflare/origin setup

## Implementation Phases

### Phase 0: Safety And Baseline

- Work on a new branch, e.g. `rebuild/django6`.
- Keep production checkout untouched until local Docker run works.
- Keep DB/media backup in ignored `data/`.
- Confirm domain/origin problem before deployment.

### Phase 1: Django 6 Skeleton

- Add Python 3.13/Django 6 dependency setup.
- Replace old Django 1.9 project structure.
- Add settings, URL routing, WSGI/ASGI.
- Add static/media settings.
- Add env-based config.
- Add basic health endpoint.
- Add admin.
- Add i18n scaffolding.

### Phase 2: Data And Forms

- Add quote request models.
- Add file upload handling.
- Add admin for leads.
- Add form validation and consent.
- Add tests for form submission.

### Phase 3: Marketing Frontend

- Build layout system and design tokens.
- Build responsive header, footer, CTA surfaces.
- Build Home.
- Build B2B landing.
- Build construction joinery landing.
- Build architects/firms landing.
- Build realizations page.
- Build quote/contact pages.
- Use real media from `data/public/media` as placeholders until better photos arrive.

### Phase 4: SEO And Tracking

- Add page metadata model/config in code.
- Add canonical tags.
- Add JSON-LD.
- Add sitemap.
- Add robots.
- Add dataLayer events.
- Add GTM/GA config hooks.

### Phase 5: Docker, Nginx, Deployment

- Build Docker image locally.
- Run app via Docker Compose locally.
- Run migrations.
- Run collectstatic.
- Verify Unix socket config.
- Deploy to server branch.
- Rebuild container.
- Reload central nginx if needed.
- Verify `https://kajax.eu` no longer returns 502.

### Phase 6: QA

- `python manage.py check`
- migrations apply cleanly
- form creates lead
- file upload works
- admin opens
- sitemap/robots respond
- static/media respond through nginx
- responsive screenshots for desktop/mobile
- Lighthouse/core SEO checks
- verify no secrets in git

## Open Questions Before Implementation

These need human confirmation before replacing the application:

1. Should the first release stay SQLite for minimal deployment risk, or do we move to PostgreSQL immediately?
2. Should v1 be Polish-only with i18n infrastructure, or do we ship English pages too?
3. Is shipping/packing B2B orders outside Pomorskie real today, planned soon, or only aspirational?
4. What are the real production limits: materials, machines, minimum series, max dimensions, finishing options?
5. Can existing old photos be used as temporary public assets, or should the new site wait for a fresh photo set?
6. Confirm public contact data: company display name, legal name, address, phone, email.
7. Who receives quote notifications, and is SMTP/email sending available?
8. Do we have Cloudflare/DNS access to fix the 502 and canonical HTTPS, or should deployment assume the existing Cloudflare setup remains external?
