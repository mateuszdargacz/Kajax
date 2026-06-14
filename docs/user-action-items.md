# Kajax Action Items

Last updated: 2026-06-14

This file tracks what is already closed after the production deploy and what still needs user/business input. Items marked as user-owned should not block normal site maintenance, but they matter before paid traffic is scaled.

## Closed In Current Deploy

- [x] Production site runs from GitHub branch `rebuild/django6`.
- [x] Django 6 / Python 3.13 stack is deployed with Docker Compose and nginx.
- [x] Public contact email is `mail@kajax.eu`.
- [x] SMTP is configured for production lead notifications and visitor confirmations.
- [x] Lead notifications go to `mail@kajax.eu`, `mateuszdargacz@gmail.com` and `kajax-stolarstwo@o2.pl`.
- [x] GTM and GA4 are configured and production E2E allows the expected Google hosts only.
- [x] Technical SEO is present: canonical URLs, sitemap, robots, hreflang, structured data, social preview metadata.
- [x] `og:image` and `twitter:image` are present on public pages using current preview assets.
- [x] Mobile header is simplified: phone, menu, language links inside the menu, sticky bottom `Zadzwoń` / `Wycena`.
- [x] Quote form stays compact and exposes optional fields plus file upload on demand.
- [x] Public pages have real mapped image assets instead of filename placeholders.
- [x] `docs/photo-content-brief.md` maps target filenames, crops and replacement rules.
- [x] Photo review notes for all 19 current assets are saved in `/Users/mateuszdargacz/Downloads/kajax-photo-review-notes-2026-06-14.md`.
- [x] Local landing pages exist for Gościcino, Wejherowo, Gdynia, Gdańsk, Trójmiasto and Pomorskie.
- [x] Portfolio/realizations page is structured as case-study style entries with problem, scope, result and CTA.
- [x] Production E2E passed: 78/78 scenarios.

## User-Owned Before Strong Ads Push

- [ ] Replace generated preview images with real Kajax workshop and project photos, keeping the exact mapped filenames.
- [ ] Prioritize real replacements for `hero-workshop-production.jpg`, `b2b-short-series-wood-components.jpg`, `b2b-repeated-wooden-elements-detail.jpg`, `woodwork-from-drawing-specification.jpg`, `wooden-stairs-pomorskie.jpg`, `wooden-doors-joinery-detail.jpg` and `architectural-woodwork-detail.jpg`.
- [ ] Provide 3-5 strong B2B batch photos showing repeatable elements, profiles, semi-products or POS/display parts.
- [ ] Provide at least one real packing/logistics photo if B2B shipping outside Pomorskie should be promoted.
- [ ] Provide 3 portfolio case sets with: finished photo, detail photo, optional process photo, material, client type, challenge and result.
- [ ] Confirm real production capabilities: machinery, max/min dimensions, repeatable processes, materials and finishes.
- [ ] Confirm practical minimum order ranges for B2B short series.
- [ ] Confirm whether B2B shipping outside Pomorskie and Poland is realistic now.
- [ ] Confirm which product categories should be pushed first: POS/display parts, profiles/listwy, frames, semi-products, stairs, doors or unusual architectural details.
- [ ] Confirm what should be filtered out early: unrealistic deadlines, tiny one-off jobs, unclear unusual work or low-budget local tasks.
- [ ] Confirm exact public business name, address, phone and preferred contact hours.
- [ ] Provide or create Google Business Profile access.
- [ ] Provide Google Search Console access for `kajax.eu`.
- [ ] Collect 5-10 real reviews from previous clients after the new site is live.
- [ ] Review Polish copy with the father for business accuracy before paid campaigns scale.

## Developer-Owned Next Polish/Marketing Passes

- [ ] Replace preview OG images with real-photo OG crops after final photos arrive.
- [ ] Add more real case-study detail once the user provides project facts.
- [ ] Add Search Console verification meta tag when the verification token is available.
- [ ] Re-run production E2E after every content/photo replacement.
- [ ] Keep ads paused or low-budget until real photos, Search Console, Google Business Profile and offer boundaries are confirmed.
