# Legacy Database Audit

Last updated: 2026-06-13

Source database: `data/kajax.db`

## Summary

The legacy database is small and mostly useful as historical context. It should not drive the new public website content.

Keep the database file as the production SQLite database so that old admin users and old contact messages remain archived. The Django 6 app can add its new `leads_*` tables next to the legacy `home_*` tables.

## Table Counts

| Table | Rows | Usefulness |
| --- | ---: | --- |
| `home_companydata` | 1 | Keep as reference for NAP data. |
| `home_service` | 5 | Useful only as a reminder of old service categories. |
| `home_client` | 8 | Useful as possible portfolio/client proof after legal/content review. |
| `home_project` | 1 | Looks like test/demo content, not suitable for public migration. |
| `home_projectimage` | 1 | Demo project image only. |
| `home_slider` | 1 | Legacy slider container. |
| `home_sliderimage` | 3 | Old homepage messaging and image references. |
| `home_message` | 10 | Historical inquiries from 2016-2025; keep archived, do not publish. |

## Company Data

- Name: `Kajax Stolarstwo`
- Address: `84-241 Gościcino ul. Zielona 17`
- Phone: `604 238 246`
- Email: `kajax-stolarstwo@o2.pl`

This matches the contact data currently used in the rebuild.

## Legacy Services

| Service | Legacy Description | Image |
| --- | --- | --- |
| Drzwi | Wykonywanie drzwi w dowolnym wzorze, wewnętrznych i zewnętrznych. | `services/images/modern-internal-doors.jpg` |
| Schody | Schody na własnej konstrukcji oraz na beton. | `services/images/stairs_small.jpg` |
| Listwy przypodłogowe | Listwy przypodłogowe w wybranym kolorze i wzorze. | `services/images/skirting-big55.jpg` |
| Tarasy | Tarasy, również z drewna egzotycznego. | `services/images/modern_wood_terrace_2-2.jpg` |
| Meble | Meble szyte na miarę. | `services/images/6a00d834515c5b69e2010536feb38b970c-2.jpg` |

Content decision: these categories support the construction/custom side, but the new site should keep stronger B2B positioning. Do not restore the old "everything from wood" structure.

## Legacy Clients

The database contains client/logo records for:

- Hotel Meridian
- Darbud
- Lime brains
- Raiko
- Abacosun
- BusPrestige
- Palac ciekocinko
- Dwor lisewski

Content decision: these can inspire a future "clients/selected cooperation" proof section, but should not be shown publicly until the relationship, logo rights and actual work scope are confirmed.

## Legacy Project

Only one project exists:

- Name: `Shoddy w pensjonacie`
- Location: `Gdynia`
- Client: `Hotel Meridian`
- Date range: 2016-06-12 to 2016-06-23
- Image: `projects/images/1.jpg`

The title and description look like placeholder/test content. Do not migrate it as a public realization.

## Legacy Slider

The slider has three entries:

- `Schody`: "Zadbamy aby Twoje schody były elementem wystroju wnętrz!"
- `Drzwi`: "Twoje wymarzone"
- `Wnętrze`: "Oferujemy również kompleksowe wykończenie wnętrz"

Content decision: the tone is too generic for the new B2B/lead-generation direction. The only reusable idea is that stairs, doors and interiors were historically important.

## Legacy Messages

There are 10 old contact messages from 2016-11-06 to 2025-09-08.

Recent subjects include:

- `Drzwi i zabudowa ( szafy)`
- `Zapytanie o schody`
- `Zapyranue`
- `szafka sprzed 300 lat`
- `Schody na beton`
- `Renowacja drzwi zewn. dębowych`
- `drzwi bezprzylgowe`
- `schody na betonie`

Content decision: the historical inquiries confirm demand for stairs, doors, built-ins and renovation/custom work. They do not provide enough structured material for public case studies.

## Deployment Decision

Use the legacy SQLite file as the active production database:

```text
SQLITE_PATH=/app/data/kajax.db
```

Then run Django migrations. The migration was tested locally on a copy of the legacy DB and created the new `leads_quoterequest` and `leads_quoteattachment` tables without removing legacy tables.
