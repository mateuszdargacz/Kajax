# Kajax Photo Content Brief

Last updated: 2026-06-13

## Purpose

New photos should make Kajax feel like a capable production and made-to-measure joinery workshop, not a generic local carpenter.

The site needs visual proof for three commercial directions:

1. B2B wooden components, short series and semi-products.
2. Construction joinery: stairs, doors, trims, built-ins.
3. Unusual/project-based/premium details for architects, firms and demanding investors.

Use real Kajax workshop, tools, materials, people, details and finished work. Avoid stock photos, exaggerated luxury styling and rustic hobby aesthetics.

## General Photo Rules

- Shoot in natural or soft workshop light when possible.
- Clean visible clutter, but do not make the workshop sterile.
- Prefer real work surfaces, tools, dust extraction, clamps, machines, wood stacks and finished details.
- Capture both wide context and close detail for the same subject.
- Leave empty space on one side of selected hero photos for text overlay.
- Shoot horizontal, vertical and square variants where possible.
- Avoid strong blur on the actual product/detail; the user must be able to inspect the work.
- Avoid heavy filters. Keep wood color natural.
- Include hands/tools only when they communicate craft or scale.
- Do not show unsafe work practices.

## Required Ratios

- Hero desktop master: `16:9`, minimum `3200x1800`, export at least `2400x1350`.
- Hero mobile crop: `4:5`, minimum `1600x2000`; keep subject readable after vertical crop.
- Standard section image: `4:3`, minimum `2400x1800`, export at least `1600x1200`.
- Portfolio card image: `3:2` or `4:3`, minimum `2400px` on the long edge.
- Detail closeup: square `1:1`, minimum `2000x2000`; optional `4:3` crop at `2400x1800`.
- Open Graph/social: `1200x630`, generated from hero or strongest workshop/B2B image.

## Generation Style Guide

Use this as the global instruction for any AI image generation agent.

Positive style:

- photorealistic documentary product photography,
- real European joinery workshop in Poland,
- modern but not sterile,
- natural oak/ash/pine/walnut wood tones,
- visible workbench, clamps, templates, calipers, sanding tools, safe machinery, dust extraction,
- clean composition with believable dust, grain and small workshop traces,
- soft daylight or large softbox light,
- neutral warm color grade,
- premium craft and B2B reliability, not rustic hobby craft.

Negative style:

- no stock-photo smiles,
- no luxury mansion showroom,
- no fake glossy CGI look,
- no impossible geometry,
- no unsafe machine operation,
- no unreadable warped text on labels, drawings or signs,
- no visible brand names from other companies,
- no random decorative props,
- no chaotic clutter,
- no dark underexposed workshop corner,
- no exaggerated orange/brown filter,
- no cartoon/illustration/vector style.

Human presence:

- Hands are useful when they show scale, measuring, checking or finishing.
- Faces are optional and should not dominate.
- Avoid posed portraits for core conversion images.

Text and documents:

- Drawings/specifications may be visible, but they should not contain real client data.
- If generated, any written text should be abstract linework, dimensions and symbols rather than readable fake words.

Export rules:

- Use `.jpg` for all final files unless we later add an optimized responsive image pipeline.
- Keep the exact target filenames from the table below.
- Also keep high-resolution source files separately if generated; do not overwrite the final export names with low-quality previews.
- Final web exports should be sharp, sRGB, quality around 82-88, no watermark.
- Avoid upscaling small generations unless the result stays crisp on edges and grain.

## Implementation Placeholder Map

Until real files are delivered, the website renders named visual placeholders with only the target filename visible in the UI. Shot purpose, framing and replacement notes live in this document, not under images on the public pages.

Replace each placeholder by adding the final image with the mapped filename and then changing the placeholder renderer to a real image renderer.

| Code key | Target filename | Main use | Required crop | Minimum source |
| --- | --- | --- | --- | --- |
| `hero_workshop` | `hero-workshop-production.jpg` | Homepage hero | `16:9`, text-safe | `3200x1800` |
| `b2b_components_series` | `b2b-short-series-wood-components.jpg` | B2B landing, homepage B2B section | `4:3` | `2400x1800` |
| `b2b_components_detail` | `b2b-repeated-wooden-elements-detail.jpg` | B2B proof/detail sections | `1:1` and `4:3` | `2400x2400` |
| `b2b_packing` | `wood-components-packed-for-shipping.jpg` | Logistics/Europe B2B note | `4:3` | `2400x1800` |
| `drawing_spec` | `woodwork-from-drawing-specification.jpg` | Quote/process sections | `4:3` | `2400x1800` |
| `precision_detail` | `wood-joinery-detail-closeup.jpg` | Architects/details and trust sections | `1:1` | `2400x2400` |
| `finished_edge_detail` | `finished-wood-edge-detail.jpg` | Detail/quality section | `1:1` | `2400x2400` |
| `stairs_project` | `wooden-stairs-pomorskie.jpg` | Construction joinery and portfolio | `4:3` | `2400x1800` |
| `stairs_detail` | `wooden-stairs-detail-wejherowo.jpg` | Local SEO/detail section | `4:3` | `2400x1800` |
| `doors_detail` | `wooden-doors-joinery-detail.jpg` | Construction joinery page | `4:3` | `2400x1800` |
| `wooden_trims` | `wooden-trims-made-to-measure.jpg` | Trims/listwy content | `4:3` | `2400x1800` |
| `built_in_project` | `built-in-woodwork-project.jpg` | Built-in/project-based portfolio | `4:3` | `2400x1800` |
| `artistic_detail` | `architectural-woodwork-detail.jpg` | Architects/details page | `4:3` | `2400x1800` |
| `materials` | `wood-material-samples-workshop.jpg` | Materials/process section | `4:3` | `2400x1800` |
| `boards` | `solid-wood-boards-for-joinery.jpg` | Workshop/material background | `4:3` | `2400x1800` |
| `craft_checking` | `craftsman-checking-wood-detail.jpg` | Trust/process/human craft | `4:3` | `2400x1800` |
| `cutting_process` | `wood-cutting-workshop-process.jpg` | Workshop process | `4:3` | `2400x1800` |
| `sanding_process` | `wood-sanding-finishing-process.jpg` | Workshop process | `4:3` | `2400x1800` |
| `clamped_elements` | `wood-elements-clamped-for-assembly.jpg` | Production/process | `4:3` | `2400x1800` |

## Live Generated Image Reviews

Use this section while reviewing generated files from `Downloads`. Keep the current file name, intended target filename, decision and change notes so the next generated version can improve instead of starting from scratch.

### 2026-06-13 - `ChatGPT Image Jun 13, 2026, 09_29_24 AM.png`

Intended target: `hero-workshop-production.jpg`

Decision: used as the first live homepage hero asset, with optimized WebP and JPG exports.

What works:

- Strong workshop context: machinery, benches, wood stock and a worker are visible immediately.
- Good wide composition for the homepage hero; the dark overlay keeps the headline readable.
- Feels closer to a production-capable joinery workshop than to a small hobby carpenter.

Change in the next version:

- Generate a larger master file, ideally `3200x1800`; the current source is `1672x941`.
- Remove readable English branding from the wall and clothing. Use no text, or only subtle Kajax branding added intentionally later.
- Keep the human presence secondary; the workshop and production capability should remain the main subject.
- Leave a calmer left-side text area with fewer high-contrast details behind the headline.

### 2026-06-13 - `b2b_components_series.png`

Intended target: `b2b-short-series-wood-components.jpg`

Decision: used as a temporary live B2B section and B2B production-page image under `b2b-short-series-wood-components.jpg`, with optimized WebP and JPG exports. Keep it marked as temporary because the source is below the target master size.

Current web exports:

- `app/static/site/img/b2b-short-series-wood-components.webp`, `1448x1086`, about `105 KB`
- `app/static/site/img/b2b-short-series-wood-components.jpg`, `1448x1086`, about `264 KB`

What works:

- Repeatability is instantly clear: many similar wooden parts are arranged in rows.
- The old workbench and caliper make the scene feel practical and workshop-based, not showroom-like.
- The 4:3 crop fits the current section image slots well.

Change in the next version:

- Generate at least `2400x1800`; the current file is `1448x1086`.
- Make the components a little more technical and less like plain rounded blocks: add one repeated routed profile, small holes, grooves or a template-driven shape.
- Reduce the cut-off board in the bottom-right corner or remove it; it distracts from the repeated batch.
- Keep at least 20 pieces visible, but make the front row sharper and the background slightly calmer.
- Avoid making every edge look too perfect or CGI-like; add believable small workshop variation while keeping the series consistent.

### 2026-06-13 - `b2b_components_detail.png`

Intended target: `b2b-repeated-wooden-elements-detail.jpg`, and possibly a stronger B2B production-page hero direction than the simpler block series.

Decision: used as a temporary live portfolio/realizations B2B proof image under `b2b-repeated-wooden-elements-detail.jpg`, with optimized WebP and JPG exports. This is the strongest B2B marketing direction so far, especially for buyers who need repeatable profiles, semi-products and short production runs.

Current web exports:

- `app/static/site/img/b2b-repeated-wooden-elements-detail.webp`, `1448x1086`, about `129 KB`
- `app/static/site/img/b2b-repeated-wooden-elements-detail.jpg`, `1448x1086`, about `316 KB`

What works:

- Immediately communicates larger B2B capability: stacked profiles, repeated machining, active workshop and machinery in the background.
- The foreground elements have useful detail: holes, grooves and profile shapes make the work look more technical.
- Human presence supports scale and process without turning the image into a posed portrait.
- The scene better supports the business direction toward semi-products and repeatable orders for companies.

Change in the next version:

- Generate a larger master: ideally `2400x2400` for the detail asset, plus a `2400x1800` crop for standard page sections. The current file is `1448x1086`.
- Create a closer square variant focused on the front stacks so it can work as `b2b-repeated-wooden-elements-detail.jpg`.
- Keep the worker and machine in the background, but make sure the machined profiles remain the sharpest and most important visual subject.
- Reduce the bright window area slightly so the wood profiles and workshop depth carry the composition.
- Avoid fake screens, fake labels or readable UI on machinery; any visible text should be absent or non-readable.

### 2026-06-13 - `b2b_packing_1.png` and `b2b_packing_2.png`

Intended target: `wood-components-packed-for-shipping.jpg`

Decision: used `b2b_packing_2.png` as a temporary live packing/logistics image under `wood-components-packed-for-shipping.jpg`, with optimized WebP and JPG exports. It is shown in the short-series guide aside. `b2b_packing_1.png` was not used because the fake label and readable English branding pull attention away from the practical logistics message.

Current web exports:

- `app/static/site/img/wood-components-packed-for-shipping.webp`, `1448x1086`, about `139 KB`
- `app/static/site/img/wood-components-packed-for-shipping.jpg`, `1448x1086`, about `340 KB`

What works:

- Version 2 communicates practical B2B logistics better: protected wooden profiles inside a crate, with foam and straps visible.
- The image supports the short-series argument that repeatable elements can be packed, protected and handed over or shipped when logistics make sense.
- It avoids courier labels and fake brand text.

Change in the next version:

- Generate at least `2400x1800`; the current file is `1448x1086`.
- Keep the crate and protection visible, but darken or calm the busy workshop background slightly.
- Add a little more separation between finished components and packing material so the viewer reads "protected parts" immediately.
- Avoid readable labels, brand marks, fake handling icons or fake shipping documents.

### 2026-06-13 - `ChatGPT Image Jun 13, 2026, 11_31_57 AM.png`

Intended target: `woodwork-from-drawing-specification.jpg`

Decision: renamed and used as a temporary live drawing/specification image under `woodwork-from-drawing-specification.jpg`, with optimized WebP and JPG exports. It is shown in the quote-preparation guide aside.

Current web exports:

- `app/static/site/img/woodwork-from-drawing-specification.webp`, `1448x1086`, about `88 KB`
- `app/static/site/img/woodwork-from-drawing-specification.jpg`, `1448x1086`, about `228 KB`

What works:

- Strongly supports the "send a drawing, photo or specification" conversion path.
- The caliper, wooden sample and marked-up drawing make the quoting process feel concrete and technical.
- Human presence feels natural and does not dominate the frame.

Change in the next version:

- Generate at least `2400x1800`; the current file is `1448x1086`.
- Keep technical drawings abstract enough to avoid fake readable project data.
- Move the person's face further out of frame or keep it cropped; the hand, drawing and sample should remain the subject.
- Keep the sample piece and caliper visible, because they make the workflow easy to understand.

## AI Generation Asset Briefs

Each asset below is written so an image-generation agent can produce a usable website image without guessing the business context.

### `hero-workshop-production.jpg`

Purpose: first impression on the homepage. It must immediately say: serious workshop, production capability, wood craft, not a generic carpenter.

Required output:

- Main file: `hero-workshop-production.jpg`
- Ratio: `16:9`
- Minimum source: `3200x1800`
- Web export: `2400x1350`
- Optional mobile crop: `hero-workshop-production-mobile.jpg`, `4:5`, `1600x2000`
- Optional OG crop: `hero-workshop-production-og.jpg`, `1200x630`

Composition:

- Wide workshop interior with real workbench, machines, clamps, stacks of wood and partly finished components.
- Leave 40-45% calm negative space on the left side for hero text.
- Main visual weight should sit middle-right.
- One person may work in the background, but the workshop and capability should dominate.
- Camera height around chest level, natural perspective, no extreme wide-angle distortion.

Prompt:

```text
Photorealistic documentary photo of a serious European joinery workshop in Poland, prepared for small batch wooden component production, workbench, clamps, dust extraction, saw or planer in background, stacks of oak and pine boards, several finished wooden parts on the bench, warm natural daylight from side windows, clean but real workshop, premium craft, B2B reliability, calm empty space on the left for website headline, subject weight on the right, 35mm lens, realistic color, sharp wood grain, no logos
```

Negative prompt:

```text
stock photo, smiling posed carpenter, luxury mansion, rustic hobby shed, messy chaos, dark underexposed corner, fake CGI render, cartoon, watermark, readable brand logos, unsafe machine use, distorted machines, warped wood geometry, excessive orange filter
```

Quality checks:

- Text overlay must be readable over the darkened left side.
- The workshop should look capable enough for B2B, not only one-off furniture repair.
- No fake readable signage.

Alt text:

- `Warsztat stolarski Kajax w Gościcinie przygotowany do produkcji elementów drewnianych`

### `b2b-short-series-wood-components.jpg`

Purpose: strongest proof for B2B wooden components and small repeatable batches.

Required output:

- Main file: `b2b-short-series-wood-components.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`
- Optional crop: `b2b-short-series-wood-components-square.jpg`, `2000x2000`

Composition:

- 20-40 repeated wooden components arranged in rows or grouped batches.
- Show repeatability: same shape, same material, same finish.
- Include a template, caliper or ruler only if it looks natural.
- Use a workshop table, not a showroom table.
- Keep background quiet and slightly darker than the parts.

Prompt:

```text
Photorealistic product-documentary photo of a short production run of identical wooden components arranged in clean rows on a joinery workshop bench, oak or beech pieces with precise edges and repeated shape, small-batch B2B production, caliper and simple template nearby, warm side light, realistic workshop background softly out of focus, sharp repeatability, premium but practical, no logos
```

Negative prompt:

```text
single unique artwork, random scattered pieces, plastic objects, glossy CGI, showroom luxury, dirty unusable bench, labels with text, hands covering the components, unsafe tools, cartoon, watermark
```

Quality checks:

- Viewer must understand "we can repeat this element".
- At least 12 components should be clearly visible.
- Edges must look straight and believable.

Alt text:

- `Krótka seria powtarzalnych elementów drewnianych wykonanych na zamówienie dla firmy`

### `b2b-repeated-wooden-elements-detail.jpg`

Purpose: close proof of repeatability and finish for B2B buyers.

Required output:

- Main file: `b2b-repeated-wooden-elements-detail.jpg`
- Ratio: `1:1`
- Minimum source: `2400x2400`
- Optional `4:3` crop: `2400x1800`

Composition:

- Close view of several identical milled wooden parts stacked or aligned.
- Focus on edges, holes, profiles, repeated milling or finish.
- Depth of field may be shallow, but at least the front 3-5 pieces must be sharp.

Prompt:

```text
Photorealistic closeup of repeated milled wooden parts for B2B production, identical oak components stacked and aligned, precise edges, visible grain, small holes or routing details, workshop bench surface, soft directional light, shallow depth of field with front pieces sharp, premium technical craftsmanship, no logos, no readable text
```

Negative prompt:

```text
random scraps, rough broken edges, toy-like pieces, fake plastic wood, excessive blur, unreadable fake labels, CGI, watermark, impossible geometry
```

Alt text:

- `Powtarzalne drewniane elementy pokazujące precyzję wykonania i wykończenia`

### `wood-components-packed-for-shipping.jpg`

Purpose: support the message that B2B work can be packed and shipped when logistics make sense.

Required output:

- Main file: `wood-components-packed-for-shipping.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Finished wooden components grouped and protected in cardboard, paper, foam or dividers.
- Show practical packing, not huge industrial logistics.
- Include 1-2 open boxes and a small stack of packed elements.
- Avoid courier brand logos and fake shipping labels.

Prompt:

```text
Photorealistic photo of small-batch wooden components prepared for pickup or shipping in a joinery workshop, identical wooden parts protected with cardboard dividers and kraft paper, open box on workbench, several finished parts visible, practical B2B packaging, warm workshop light, clean composition, no courier logos, no readable labels
```

Negative prompt:

```text
Amazon warehouse, industrial conveyor, branded shipping labels, messy packaging waste, damaged wood, luxury gift packaging, fake text, CGI, watermark
```

Alt text:

- `Elementy drewniane przygotowane do odbioru lub wysyłki po uzgodnieniu logistyki`

### `woodwork-from-drawing-specification.jpg`

Purpose: make the "send a drawing, photo or specification" CTA feel concrete and trustworthy.

Required output:

- Main file: `woodwork-from-drawing-specification.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Printed technical drawing or sketch on a workbench, next to a wooden part or sample.
- Include pencil, caliper or ruler.
- Hands may point at a detail.
- Any text on paper should be abstract or blurred enough not to look fake.

Prompt:

```text
Photorealistic workshop photo of a wooden component being planned from a drawing, printed technical sketch with simple dimension lines on a workbench, caliper, pencil, oak sample and partially finished wooden part next to it, craftsman's hand pointing at one detail, warm natural light, practical joinery workshop, no readable client data, no logos
```

Negative prompt:

```text
fake readable text, blueprint full of gibberish words, computer screen UI, office desk, stock business meeting, plastic ruler only, messy papers, CGI, watermark
```

Alt text:

- `Przygotowanie elementu drewnianego na podstawie rysunku lub specyfikacji`

### `wood-joinery-detail-closeup.jpg`

Purpose: premium trust image for architects, demanding buyers and details sections.

Required output:

- Main file: `wood-joinery-detail-closeup.jpg`
- Ratio: `1:1`
- Minimum source: `2400x2400`
- Optional `4:3` crop: `2400x1800`

Composition:

- Macro or close product shot of a clean joint, edge, profile, corner or fitted wooden detail.
- Grain and finish must be sharp.
- Keep detail readable: do not blur the entire subject.

Prompt:

```text
Photorealistic macro closeup of premium wood joinery detail, clean fitted joint and finished edge, visible natural grain, smooth oil or matte lacquer finish, precise corner, warm side light, dark neutral workshop background, shallow depth of field but main joint fully sharp, architectural woodwork quality, no logos
```

Negative prompt:

```text
rough unfinished scrap, glue stains, plastic-looking wood, excessive blur, impossible joint, CGI, cartoon, watermark, over-saturated orange wood
```

Alt text:

- `Detal stolarski pokazujący dokładne spasowanie i wykończenie drewna`

### `finished-wood-edge-detail.jpg`

Purpose: show finish quality, edge work and material sensitivity.

Required output:

- Main file: `finished-wood-edge-detail.jpg`
- Ratio: `1:1`
- Minimum source: `2400x2400`

Composition:

- Close view of a finished edge, rounded profile, chamfer, stair tread edge, door edge or trim edge.
- Include light grazing the surface so finish quality is visible.
- One hand may hold the piece only if it adds scale.

Prompt:

```text
Photorealistic square closeup of a finished wooden edge profile, precise chamfer or rounded edge, smooth tactile surface, natural oak grain, warm grazing light showing finish quality, workshop background softly blurred, premium joinery detail, realistic texture, no logos
```

Negative prompt:

```text
splinters, chipped edge, fake plastic material, overprocessed shine, heavy blur, CGI, watermark, unreadable text
```

Alt text:

- `Wykończona krawędź drewnianego elementu pokazująca jakość obróbki`

### `wooden-stairs-pomorskie.jpg`

Purpose: local construction joinery proof for stairs.

Required output:

- Main file: `wooden-stairs-pomorskie.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`
- Optional vertical crop: `1600x2000`

Composition:

- Finished wooden stairs in a real modern interior.
- Show whole stair form, treads, railing or side detail.
- Keep vertical lines straight.
- Interior should feel lived-in or architectural, not a luxury catalog render.

Prompt:

```text
Photorealistic interior photo of made-to-measure wooden stairs in a modern Polish home, natural oak treads, clean railing detail, precise fitting to walls and floor, warm daylight, realistic interior, vertical lines straight, premium but practical construction joinery, no people posing, no logos
```

Negative prompt:

```text
luxury mansion showroom, impossible floating stairs, warped perspective, glossy CGI render, unsafe railing, cluttered room, fake brand signage, cartoon, watermark
```

Alt text:

- `Schody drewniane wykonane na wymiar przez Kajax Stolarstwo`

### `wooden-stairs-detail-wejherowo.jpg`

Purpose: close proof for stairs quality and local SEO support.

Required output:

- Main file: `wooden-stairs-detail-wejherowo.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Detail of tread, nosing, railing connection, stringer or wall fit.
- Show precise fit and finish.
- Keep enough context to recognize it is a stair detail.

Prompt:

```text
Photorealistic close detail of wooden stairs, oak tread edge and railing or wall connection, precise fitting, smooth matte finish, natural light, modern interior context softly visible, high-quality construction joinery, sharp grain and clean lines, no logos
```

Negative prompt:

```text
damaged stairs, loose railing, impossible geometry, heavy blur, CGI, luxury showroom render, cartoon, watermark
```

Alt text:

- `Detal schodów drewnianych pokazujący dopasowanie stopni i wykończenie`

### `wooden-doors-joinery-detail.jpg`

Purpose: support doors and construction joinery service.

Required output:

- Main file: `wooden-doors-joinery-detail.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Wooden door, frame, casing or threshold detail in context.
- Show clean fit between door/frame/wall/floor.
- Avoid old damaged doors unless the goal is restoration.

Prompt:

```text
Photorealistic photo of made-to-measure wooden door and frame detail in a real interior, clean casing, threshold and trim fitting, natural wood grain, matte finish, warm daylight, precise construction joinery, modern but realistic Polish interior, no logos, no people posing
```

Negative prompt:

```text
damaged old door, fake luxury palace door, warped perspective, plastic veneer look, CGI, messy hallway, readable brand labels, watermark
```

Alt text:

- `Drzwi drewniane i opaski wykonane na wymiar jako element stolarki budowlanej`

### `wooden-trims-made-to-measure.jpg`

Purpose: show listwy, profiles, thresholds and small construction elements.

Required output:

- Main file: `wooden-trims-made-to-measure.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Several wooden trims/profiles arranged on a bench or installed along a wall/floor.
- Show profile shapes and finish.
- Good if it includes repeated profiles for both B2B and construction contexts.

Prompt:

```text
Photorealistic photo of made-to-measure wooden trims and profiles, several oak or pine mouldings arranged cleanly on a workshop bench, visible profile shapes, precise milling, natural grain, warm side light, practical joinery workshop, no logos, no labels
```

Negative prompt:

```text
plastic strips, random scrap wood, messy pile, fake text labels, CGI, over-saturated orange color, watermark
```

Alt text:

- `Listwy i profile drewniane wykonane na wymiar`

### `built-in-woodwork-project.jpg`

Purpose: show project-based built-ins and fitted elements without making the site feel like only furniture.

Required output:

- Main file: `built-in-woodwork-project.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Fitted wooden element in an interior: built-in panel, bench, niche, display, wall detail or functional built-in.
- Show fit to architecture and careful detail.
- Avoid generic kitchen cabinet imagery.

Prompt:

```text
Photorealistic interior photo of a project-based wooden built-in detail, fitted oak panel or display element integrated with architecture, clean lines, precise joints, warm natural light, premium but practical interior woodwork, realistic Polish commercial or residential interior, no logos, no people posing
```

Negative prompt:

```text
generic kitchen catalog, luxury palace, IKEA-style flatpack, fake CGI, warped lines, clutter, brand logos, watermark
```

Alt text:

- `Zabudowa i drewniany element wnętrza wykonany według projektu`

### `architectural-woodwork-detail.jpg`

Purpose: make architects and demanding clients believe Kajax can handle unusual details.

Required output:

- Main file: `architectural-woodwork-detail.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`
- Optional square crop: `2000x2000`

Composition:

- Unusual but believable wooden detail: curved element, routed profile, decorative screen, restored detail, display detail or complex joinery part.
- Should feel special without becoming fantasy craft.
- Include enough context to understand scale.

Prompt:

```text
Photorealistic photo of an unusual architectural woodwork detail made in a joinery workshop, curved or precisely routed oak element, complex profile, clean finish, part of an interior or display project, hands or template may show scale, warm natural light, premium craftsmanship, realistic and buildable, no logos
```

Negative prompt:

```text
fantasy sculpture, ornamental palace carving, impossible shape, toy-like object, glossy CGI, messy clutter, unreadable fake text, watermark
```

Alt text:

- `Nietypowy detal drewniany wykonany na zamówienie według projektu`

### `wood-material-samples-workshop.jpg`

Purpose: support material knowledge and add visual warmth.

Required output:

- Main file: `wood-material-samples-workshop.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Samples of wood species, finishes, profiles or offcuts arranged cleanly.
- Include labels only if abstract/unreadable.
- Use as a calm supporting image, not hero.

Prompt:

```text
Photorealistic photo of wood material samples in a joinery workshop, oak, ash, pine and walnut boards or small samples arranged on a bench, visible grain and finish variations, simple profiles and offcuts, warm daylight, clean practical composition, no readable labels, no logos
```

Negative prompt:

```text
flooring showroom, plastic samples, messy scraps, fake readable labels, oversaturated colors, CGI, watermark
```

Alt text:

- `Próbki drewna i materiały wykorzystywane w stolarni Kajax`

### `solid-wood-boards-for-joinery.jpg`

Purpose: background/material proof for workshop and process sections.

Required output:

- Main file: `solid-wood-boards-for-joinery.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Stack of solid boards in a workshop, clean enough to look professional.
- Boards should show real grain, thickness and usable material.
- Works as a quiet background image.

Prompt:

```text
Photorealistic photo of solid wood boards stacked in a professional joinery workshop, oak and pine boards with visible grain and thickness, clean organized material storage, warm side light, tools softly visible in background, practical and credible, no labels, no logos
```

Negative prompt:

```text
random firewood pile, outdoor lumber yard, dirty chaotic storage, fake plastic wood, CGI, watermark, readable brand marks
```

Alt text:

- `Deski z litego drewna przygotowane do prac stolarskich`

### `craftsman-checking-wood-detail.jpg`

Purpose: add human craft and trust without turning the site into a personal portrait page.

Required output:

- Main file: `craftsman-checking-wood-detail.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Hands checking a wooden part with caliper, square, template or by fitting it to another element.
- Face should be absent or secondary.
- The action must communicate care, precision and judgement.

Prompt:

```text
Photorealistic documentary photo of a craftsman checking a wooden detail in a joinery workshop, hands using caliper or square on a finished oak component, focused technical inspection, workbench with tools, warm natural light, face not prominent, premium craft and precision, no logos, no readable text
```

Negative prompt:

```text
posed portrait looking at camera, thumbs up, unsafe machine use, fake text, messy clutter, plastic wood, CGI, watermark
```

Alt text:

- `Stolarz sprawdza detal drewniany podczas pracy w warsztacie`

### `wood-cutting-workshop-process.jpg`

Purpose: show process capability and machinery for production work.

Required output:

- Main file: `wood-cutting-workshop-process.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Safe cutting/preparation scene in workshop.
- Machine can be visible, but avoid dangerous close contact with blade.
- Prefer prepared part, guide, jig or machine table over action danger.

Prompt:

```text
Photorealistic workshop process photo of wooden components being prepared for cutting, saw table or planer setup with safety guards, wooden boards aligned with a guide or jig, craftsman's hands positioned safely away from blade, dust extraction visible, serious joinery production, warm workshop light, no logos
```

Negative prompt:

```text
unsafe hands near blade, flying debris, sparks, metal factory, dramatic danger scene, CGI, watermark, unreadable labels, messy chaos
```

Alt text:

- `Przygotowanie drewna do cięcia w stolarni produkcyjnej`

### `wood-sanding-finishing-process.jpg`

Purpose: show finishing quality and manual care.

Required output:

- Main file: `wood-sanding-finishing-process.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Sanding or finishing of a wooden element on a bench.
- Show dust extraction or clean working method if possible.
- Hands can be visible.

Prompt:

```text
Photorealistic workshop photo of sanding and finishing a wooden component, craftsman's hands using sanding block or orbital sander on oak part, smooth matte finish, dust extraction hose visible, warm natural light, clean workbench, precise manual finishing, no logos, no readable text
```

Negative prompt:

```text
excessive dust cloud, unsafe maskless industrial mess, glossy fake finish, CGI, cartoon, watermark, random tools covering the subject
```

Alt text:

- `Szlifowanie i wykańczanie elementu drewnianego w warsztacie`

### `wood-elements-clamped-for-assembly.jpg`

Purpose: show assembly, glue-up and repeatable workshop process.

Required output:

- Main file: `wood-elements-clamped-for-assembly.jpg`
- Ratio: `4:3`
- Minimum source: `2400x1800`

Composition:

- Wooden elements clamped on a workbench during assembly.
- Clamps should look functional and properly placed.
- Show repeatable parts or one precise assembly.

Prompt:

```text
Photorealistic photo of wooden elements clamped for assembly in a joinery workshop, several clamps holding oak parts on a workbench, precise alignment, glue-up or dry fit, repeated components nearby, warm side light, practical production process, no logos, no readable labels
```

Negative prompt:

```text
random clamp chaos, glue mess everywhere, impossible floating parts, plastic wood, CGI, watermark, unsafe setup
```

Alt text:

- `Elementy drewniane zaciśnięte do montażu w warsztacie stolarskim`

### 12. Portfolio Case Sets

Purpose:

- Each realization page/card needs context, not just a gallery.

For each important project, collect:

- one wide finished shot,
- two detail shots,
- one process shot if available,
- one before/during shot if it helps explain difficulty,
- short notes: client type, material, scope, challenge, result.

Suggested per-case filenames:

- `case-[short-name]-finished.jpg`
- `case-[short-name]-detail-1.jpg`
- `case-[short-name]-detail-2.jpg`
- `case-[short-name]-process.jpg`

Required output:

- Finished shot: `4:3`, minimum `2400x1800`.
- Detail shots: square `1:1`, minimum `2000x2000`, or `4:3` at `2400x1800`.
- Process shot: `4:3`, minimum `2400x1800`.
- Optional before/during shot: `4:3`, minimum `1600x1200`.

Case prompt template:

```text
Photorealistic case-study photo set for a Polish joinery workshop, [PROJECT TYPE], made-to-measure wooden element, [WOOD SPECIES] wood, precise fit and finish, real interior or workshop context, warm natural light, practical premium craftsmanship, show finished result plus close detail and process, no logos, no readable private data
```

Case negative prompt:

```text
generic furniture catalog, luxury showroom render, fake CGI, warped perspective, cluttered room, unreadable fake labels, watermark, impossible construction
```

Alt text template:

- `[Project type] wykonany na wymiar: [material/detail] dla [client type or place]`

## Minimum Photo Set For Launch

The site can launch well with:

- 1 strong workshop hero,
- 3 B2B repeated-elements photos,
- 1 packing/logistics photo,
- 2 drawing/specification photos,
- 4 precision detail photos,
- 3 construction joinery photos,
- 2 architectural/unusual detail photos,
- 2 material/process photos,
- 3 portfolio case sets with at least 3 photos each.

Minimum total: about 25-30 usable photos.

## Nice-To-Have Photo Set

For stronger SEO, Ads and future content:

- 5-8 B2B component batches,
- 5 process photos,
- 8-12 detail closeups,
- 5 construction joinery projects,
- 3-5 architectural/unusual detail projects,
- 2 photos of packaging/dispatch,
- 1 simple owner/workshop portrait for trust sections.

Target total: 50-70 photos.

## What To Shoot On A Phone If Time Is Short

Use a recent phone camera and shoot in good daylight.

Priority order:

1. Repeated elements arranged cleanly.
2. Workshop wide shot.
3. Detail closeups of best work.
4. Drawing/spec next to a part.
5. Finished stairs/doors/listwy.
6. Packing/ready-for-transport shot.

Phone tips:

- clean lens,
- no zoom if possible,
- tap focus on the wood/detail,
- shoot several exposures,
- keep vertical lines straight,
- take both horizontal and vertical versions.

## Page Mapping

Home:

- hero workshop,
- B2B repeated elements,
- construction joinery,
- architectural detail,
- process/detail closeups.

`/produkcja-elementow-drewnianych`:

- repeated components,
- drawing/specification,
- packaging/logistics,
- machine/process,
- detail precision.

`/stolarka-budowlana`:

- stairs,
- doors,
- trims,
- installed interior details.

`/dla-architektow-i-firm`:

- unusual details,
- drawings/specs,
- premium closeups,
- selected portfolio cases.

`/realizacje`:

- case sets with captions and context.

`/wycena`:

- calm background/detail photo,
- optional drawing/spec photo near upload instructions.
