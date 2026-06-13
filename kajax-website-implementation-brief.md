# Kajax Website Implementation Brief

Last updated: 2026-06-13

## Main Decision

Kajax nie ma być pozycjonowany jako "lokalny stolarz od wszystkiego".

Nowa strona ma pozycjonować firmę jako:

> Doświadczona stolarnia produkcyjno-budowlana z Pomorza dla firm, architektów i inwestorów, którzy potrzebują elementów drewnianych, stolarki budowlanej albo trudniejszych realizacji na wymiar.

Najważniejszy kierunek biznesowy:

> mniej przypadkowych małych zleceń, więcej powtarzalnej pracy B2B, półproduktów, serii elementów i współpracy z większymi firmami.

## Critical Before Any Design Work

`kajax.eu` obecnie pokazuje Cloudflare 502. To trzeba naprawić przed SEO, Ads i wdrożeniem trackingów.

Etap 0:

1. Naprawić hosting/origin.
2. Ustalić canonical host: najlepiej `https://kajax.eu`.
3. Wymusić HTTPS.
4. Dodać prostą stronę tymczasową, jeśli pełny rebuild potrwa dłużej niż kilka dni.

## Website Goal

Strona ma filtrować lepsze zapytania.

Nie chcemy komunikacji typu:

> Zadzwoń, zrobimy wszystko z drewna.

Chcemy komunikacji typu:

> Wyślij zdjęcie, rysunek albo specyfikację. Ocenimy, czy możemy wykonać element, krótką serię albo stolarkę na wymiar.

## Primary Audiences

### 1. Firmy B2B

Najważniejszy segment.

Przykłady:

- producenci mebli,
- firmy reklamowe/POS,
- firmy eventowe,
- wykonawcy wnętrz,
- małe manufaktury potrzebujące drewnianych półproduktów,
- firmy potrzebujące krótkich serii elementów.

Potrzeba:

- czy zrobicie powtarzalne elementy?
- czy przyjmiecie rysunek/specyfikację?
- czy można zacząć od próbki?
- czy ogarniecie pakowanie/wysyłkę?

### 2. Architekci I Projektanci

Segment prestiżowy i dobre portfolio.

Potrzeba:

- czy da się wykonać trudny detal?
- czy stolarz rozumie projekt?
- czy można pracować na rysunkach?
- czy realizacja będzie wyglądać dobrze u klienta premium?

### 3. Inwestorzy Prywatni Premium

Nie odrzucać, ale filtrować.

Potrzeba:

- schody,
- drzwi,
- listwy,
- zabudowy,
- elementy wykończeniowe.

## Required Site Map

Minimalna wersja:

```text
/
/produkcja-elementow-drewnianych
/stolarka-budowlana
/dla-architektow-i-firm
/realizacje
/wycena
/kontakt
```

Wersja docelowa:

```text
/
/produkcja-elementow-drewnianych
/elementy-drewniane-dla-firm
/stolarka-budowlana
/schody-drewniane
/drzwi-i-listwy-drewniane
/stolarstwo-artystyczne
/dla-architektow-i-projektantow
/realizacje
/jak-przygotowac-zapytanie
/wycena
/kontakt
```

## Homepage Structure

### Hero

Hero powinien używać realnego zdjęcia warsztatu, detalu drewnianego, produkcji albo gotowej realizacji. Nie używać stockowego zdjęcia.

Headline:

```text
Stolarnia dla firm, architektów i wymagających realizacji z drewna
```

Subheadline:

```text
Wykonujemy elementy drewniane, stolarkę budowlaną i projekty na wymiar. Pracujemy na zdjęciach, rysunkach i specyfikacjach - od pojedynczego detalu po krótką serię.
```

Primary CTA:

```text
Wyślij projekt do wyceny
```

Secondary CTA:

```text
Zobacz zakres prac
```

Trust row:

```text
Stolarnia z Pomorza | krótkie serie | stolarka budowlana | realizacje custom | wycena ze zdjęcia lub rysunku
```

### Section 1: Three Paths

Trzy kafle, każdy prowadzi do osobnej podstrony:

1. `Elementy drewniane dla firm`
   - krótkie serie,
   - półprodukty,
   - elementy według wzoru,
   - pakowanie/wysyłka, jeśli realne.

2. `Stolarka budowlana`
   - schody,
   - drzwi,
   - listwy,
   - zabudowy.

3. `Custom i trudniejsze realizacje`
   - dla architektów,
   - detale,
   - nietypowe projekty,
   - stolarstwo artystyczne.

### Section 2: B2B Production

Ta sekcja ma być bardzo konkretna.

Nagłówek:

```text
Potrzebujesz powtarzalnych elementów drewnianych?
```

Tekst:

```text
Możemy przygotować pojedynczy prototyp, krótką serię albo powtarzalne elementy według wzoru. To dobry kierunek dla firm, które nie chcą budować własnej małej stolarni, ale potrzebują sprawdzonego wykonawcy.
```

Lista:

- elementy według zdjęcia,
- elementy według rysunku,
- serie próbne,
- krótkie partie,
- możliwość stałej współpracy,
- jasne wymagania przed wyceną.

CTA:

```text
Zapytaj o produkcję elementów
```

### Section 3: How Quoting Works

Pokazać proces:

1. Wysyłasz zdjęcie, rysunek albo opis.
2. Dopytujemy o materiał, ilość, termin i wykończenie.
3. Oceniamy wykonalność i orientacyjny koszt.
4. Przy serii można zacząć od próbki/prototypu.
5. Ustalamy produkcję, odbiór lub wysyłkę.

### Section 4: Realizations

Nie robić samej galerii. Każda realizacja powinna mieć kontekst:

- co to było,
- dla kogo,
- materiał,
- zakres,
- co było trudne,
- efekt.

### Section 5: Contact / Quote Form

Formularz musi być prosty, ale kwalifikujący.

Fields:

- imię,
- email,
- telefon,
- firma,
- typ zapytania:
  - elementy drewniane B2B,
  - stolarka budowlana,
  - custom/artystyczne,
  - inne,
- ilość / skala:
  - 1 sztuka,
  - mała seria,
  - stała współpraca,
  - nie wiem jeszcze,
- opis,
- możliwość dodania pliku/zdjęcia,
- zgoda kontaktowa.

## Landing Page: Produkcja Elementów Drewnianych

To będzie najważniejszy landing pod reklamy B2B.

Headline:

```text
Elementy drewniane na zamówienie dla firm
```

Subheadline:

```text
Krótkie serie, półprodukty i detale drewniane według wzoru, zdjęcia albo rysunku. Dla producentów, wykonawców, firm reklamowych i projektantów.
```

Sections:

1. Dla kogo pracujemy.
2. Jakie elementy możemy wykonywać.
3. Jak przygotować zapytanie.
4. Prototyp / próbka / seria.
5. Realizacje.
6. Formularz wyceny.

CTA copy:

```text
Wyślij specyfikację do wyceny
```

## Landing Page: Stolarka Budowlana

Headline:

```text
Schody, drzwi, listwy i stolarka drewniana na wymiar
```

Subheadline:

```text
Wykonujemy stolarkę budowlaną dla domów, lokali i inwestycji, gdzie liczy się solidne wykonanie i dopasowanie do projektu.
```

Sections:

- zakres prac,
- materiały,
- kiedy najlepiej zgłosić się do wyceny,
- przykładowe realizacje,
- formularz.

## Landing Page: Dla Architektów I Firm

Headline:

```text
Stolarnia do trudniejszych projektów i detali drewnianych
```

Subheadline:

```text
Pomagamy wykonać niestandardowe elementy drewniane do wnętrz, ekspozycji i realizacji projektowych.
```

This page should feel more premium and portfolio-led.

## Visual Direction

No generic stock.

Needed photos:

- hands/tools/detail,
- workshop,
- raw wood,
- finished stairs/doors/listwy,
- packed components,
- repeated elements arranged in series,
- closeups of joints/finish,
- before/after if possible.

Style:

- clean,
- craft + production,
- not rustic hobby,
- not luxury-only,
- practical and competent.

## SEO Requirements

Every page needs:

- one clear H1,
- location terms where natural,
- service keywords,
- internal links to quote page,
- real image alt text,
- FAQ section,
- Organization/LocalBusiness schema,
- service schema if possible.

Important phrases:

- `elementy drewniane na zamówienie`,
- `produkcja elementów drewnianych`,
- `stolarnia produkcyjna pomorskie`,
- `stolarka budowlana pomorskie`,
- `schody drewniane Wejherowo`,
- `stolarz Gościcino`,
- `stolarnia Wejherowo`,
- `stolarz dla architekta`.

## Tracking Requirements

Implement:

- GA4,
- GTM,
- Search Console,
- Google Ads conversion linker,
- conversion on quote submit,
- phone click tracking,
- email click tracking,
- file upload tracking,
- form start tracking.

Primary conversion:

```text
generate_lead / quote_request_submit
```

Secondary:

```text
phone_click
email_click
file_upload_complete
```

## What Not To Do

- Nie zaczynać od bloga.
- Nie reklamować strony z błędem 502.
- Nie pisać "najlepsza stolarnia" bez dowodów.
- Nie robić samej wizytówki z telefonem.
- Nie robić galerii bez opisów.
- Nie celować reklamą tylko w "stolarz", bo to ściągnie przypadkowe małe zlecenia.

## First Implementation Sprint

1. Naprawić 502.
2. Zebrać 20-40 zdjęć.
3. Zrobić homepage + landing B2B + formularz.
4. Dodać tracking.
5. Dodać Google Business Profile / poprawić istniejący.
6. Dopiero potem uruchomić pierwszą kampanię Search B2B.
