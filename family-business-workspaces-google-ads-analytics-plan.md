# Family Business Workspaces, Google Ads And Analytics Setup

Last updated: 2026-06-13

## Goal

Add two new advertising workspaces to the Piecode admin and campaign automation system:

1. `Kajax` - carpentry, joinery and B2B wooden components.
2. `Stolemowe Wzgorze` - modern cottages on Kashubia with SPA/garden/event potential.

The immediate phase is planning and measurement architecture. Do not spend ad budget until each site has a conversion-ready landing path and basic tracking.

## Workspace Model

### Kajax

```yaml
workspace_slug: kajax
display_name: Kajax
domain: kajax.eu
business_category: carpentry_joinery_b2b_components
default_locale: pl
currency: PLN
primary_conversion: quote_request
secondary_conversions:
  - phone_click
  - email_click
  - file_upload_complete
  - spec_download
core_segments:
  - b2b_wooden_components
  - construction_joinery
  - premium_custom_woodwork
```

### Stolemowe Wzgorze

```yaml
workspace_slug: stolemowe-wzgorze
display_name: Stolemowe Wzgorze
domain: stolemowewzgorze.pl
business_category: hospitality_vacation_rental_spa_events
default_locale: pl
currency: PLN
primary_conversion: booking_request
secondary_conversions:
  - availability_check
  - phone_click
  - email_click
  - ota_outbound_click
core_segments:
  - spa_cottages
  - group_weekends
  - small_events
  - wellness_yoga
```

## Setup Sequence

### Phase 0: Technical Readiness

#### Kajax

Blocker:

- `kajax.eu` currently returns Cloudflare 502.

Required before tracking/ads:

- restore origin,
- verify HTTPS,
- verify canonical host,
- remove 502,
- create at least one conversion landing page.

#### Stolemowe Wzgorze

Current state:

- site is live on Wix,
- SEO/title exists,
- contact details visible,
- mobile layout needs work,
- structured data phone must be fixed,
- booking CTA/funnel should be strengthened.

Required before ads:

- fix mobile overflow,
- correct schema phone,
- add/confirm booking form or clear availability request,
- define thank-you/confirmation path.

## Google Analytics 4

Create a separate GA4 property per business unless there is a strong reason to centralize. Separate properties keep reporting, permissions and conversions cleaner.

Recommended:

```text
GA4 Account: Piecode / Family Businesses
Property: Kajax
Property: Stolemowe Wzgorze
```

Use official GA4 recommended event names where they fit. Google recommends `generate_lead` for lead acquisition such as form submissions, newsletter sign-ups or demo/contact requests:

https://developers.google.com/analytics/devguides/collection/ga4/reference/events

### Kajax GA4 Events

| Event | Type | Notes |
| --- | --- | --- |
| `page_view` | standard | All pages. |
| `quote_form_view` | custom | Form enters viewport. |
| `quote_form_start` | custom | First form interaction. |
| `generate_lead` | recommended | Quote request sent. |
| `phone_click` | custom | Mobile call click. |
| `email_click` | custom | Email click. |
| `file_upload_complete` | custom | Project/spec file added. |
| `portfolio_view` | custom | Realization/gallery viewed. |
| `spec_download` | custom | B2B brief/spec template download. |

### Stolemowe GA4 Events

| Event | Type | Notes |
| --- | --- | --- |
| `page_view` | standard | All pages. |
| `availability_check` | custom | Calendar/availability click. |
| `booking_form_view` | custom | Form visible. |
| `booking_form_start` | custom | First form interaction. |
| `generate_lead` | recommended | Booking inquiry sent. |
| `phone_click` | custom | Mobile call click. |
| `email_click` | custom | Email click. |
| `package_click` | custom | SPA/event package selected. |
| `ota_outbound_click` | custom | User leaves to OTA/listing. |

## Google Tag Manager

Recommended:

- one GTM container per domain if the sites are not sharing code,
- clear naming:
  - `Kajax - Website`,
  - `Stolemowe Wzgorze - Website`.

Tags:

- GA4 base tag on all pages,
- Google Ads conversion linker on all pages if native Google Ads conversions are used,
- Google Ads conversion tag for primary conversion,
- optional remarketing tag after consent,
- custom event forwarding to GA4.

If using Wix, GTM may need to be added through Wix Marketing Integrations or custom code injection depending on plan.

## Google Ads

Use separate campaign portfolios under the same Google Ads manager if possible. Separate workspaces in Piecode must map to:

- `google_ads_customer_id`,
- `ga4_property_id`,
- `gtm_container_id`,
- `primary_domain`,
- `conversion_action_ids`.

### URL Tracking

Use direct final URLs for Search ads. Do not use short links as final URLs for Google Search.

Use Final URL Suffix for UTM parameters. Google Ads supports appending parameters through final URL suffix at account, campaign, ad group, ad or keyword levels:

https://support.google.com/google-ads/answer/9054021

Recommended suffix:

```text
utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={keyword}&gclid={gclid}
```

For human-readable reporting, campaign names should still be descriptive in Piecode and Google Ads.

## Google Ads Conversion Strategy

### Kajax

Primary:

- submitted quote form: `generate_lead`.

Secondary:

- phone click,
- email click,
- file upload,
- spec/template download.

Do not optimize against page views or gallery views.

### Stolemowe Wzgorze

Primary:

- booking inquiry sent: `generate_lead`.

Secondary:

- availability check,
- phone click,
- email click,
- OTA outbound click.

If a booking engine exists later, direct booking completion becomes the primary conversion.

## Search Console

Add/verify:

- `kajax.eu`
- `stolemowewzgorze.pl`

Submit:

- `/sitemap.xml`
- any Wix-generated sitemap for Stolemowe,
- future landing page sitemaps if using custom rebuild.

Use URL inspection after publishing priority pages.

## Google Business Profile

### Kajax

Must have:

- real category: stolarnia / stolarz / producent,
- service areas,
- photos of work and workshop,
- products/services listed,
- quote CTA,
- reviews.

### Stolemowe Wzgorze

Must have:

- lodging/vacation rental category,
- correct phone and booking URL,
- amenities,
- photos,
- review generation process,
- posts with seasonal availability.

## First Campaign Portfolio

### Kajax

Do not launch until website is live.

Planned tests:

1. `B2B wooden components`
   - goal: quote request from companies,
   - landing: `/produkcja-elementow-drewnianych`,
   - daily budget: low until query quality is proven.

2. `Local joinery`
   - goal: profitable local projects,
   - landing: `/stolarka-budowlana`.

3. `Architect/custom`
   - goal: premium custom projects,
   - landing: `/dla-architektow-i-producentow`.

### Stolemowe Wzgorze

Can launch after quick landing/CTA fixes.

Planned tests:

1. `SPA cottages`
   - landing: `/domki-kaszuby-spa`,
   - target: people searching for cottages with sauna/jacuzzi/Kaszuby.

2. `Groups and events`
   - landing: `/imprezy-kameralne-kaszuby`,
   - target: birthdays, hen parties, group weekends.

3. `Wellness/yoga`
   - landing: `/weekend-spa-joga-kaszuby`,
   - target: off-season weekend demand.

## Admin UX Requirements

Each workspace should show:

- current domain health,
- GA4/GTM/Search Console status,
- Google Ads status,
- primary conversions configured or missing,
- active campaigns,
- spend today/month,
- leads/bookings/quote requests,
- search terms,
- next recommended action,
- human todo list.

Workspace health badges:

- `tracking missing`,
- `site unavailable`,
- `ads paused`,
- `conversion unverified`,
- `ready for small test`,
- `active`.

## Human Required Checklist

### Kajax

- Hosting/Cloudflare/origin access.
- Real photo set.
- Exact services and limits.
- Google Business Profile access.
- GA4/GTM/Search Console access.
- Google Ads customer mapping.
- Phone/email confirmation.

### Stolemowe Wzgorze

- Wix access.
- Google Business Profile access.
- Best photos/videos.
- Booking/calendar source.
- Confirmation of event capacity and rules.
- Current pricing and seasonal calendar.
- GA4/GTM/Search Console access.
- Google Ads customer mapping.

## Sources Checked

- Kajax public registry/listing footprint:
  - https://monitorfirm.pb.pl/firma/kajax-s-c-jacek-dargacz-wieslawa-dargacz/
  - https://www.gowork.pl/kajax-s.c.-jacek-dargacz-wieslawa-dargacz%2C26938838/dane-kontaktowe-firmy
  - https://mapa.targeo.pl/5881179176/nip/firma
- Stolemowe website and listings:
  - https://www.stolemowewzgorze.pl/
  - https://www.stolemowewzgorze.pl/kontakt
  - https://www.nocowanie.pl/rezerwuj/1571336-domki-caloroczne-stolemowe-wzgorze-perlino/
  - https://revngo.com/domki-caloroczne-stolemowe-wzgorze-perlino
- Tourism trends:
  - https://stat.gov.pl/wyszukiwarka/?query=tag%3Atury%C5%9Bci
  - https://www.booking.com/articles/travelpredictions2025.html
  - https://news.airbnb.com/2025-spring-trends-travelers-embrace-soft-slow-travel/
- Furniture/wood market context:
  - https://www.trade.gov.pl/aktualnosci/meble-z-polski-solidna-marka-w-zmieniajacym-sie-swiecie/
  - https://www.paih.gov.pl/news/polskie-meble-coraz-lepiej-znane-w-usa/
  - https://pfr.pl/document/2761
- Google tracking:
  - https://developers.google.com/analytics/devguides/collection/ga4/reference/events
  - https://support.google.com/google-ads/answer/9054021

## Next Implementation Step

After human approval:

1. Create `kajax` and `stolemowe-wzgorze` workspaces in Mongo/admin.
2. Add brand profiles and conversion definitions.
3. Add missing workspace health checks.
4. Build Kajax temporary landing if origin cannot be restored quickly.
5. Patch Stolemowe tracking/landing once Wix access is available.
6. Create paused campaign drafts only after conversion events are verified.
