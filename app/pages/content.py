PHOTO_PLACEHOLDERS = {
    "hero_workshop": {
        "key": "hero_workshop",
        "filename": "hero-workshop-production.jpg",
        "label": "Homepage hero",
        "description": "Wide workshop/production-capable photo with space for headline text.",
    },
    "b2b_components_series": {
        "key": "b2b_components_series",
        "filename": "b2b-short-series-wood-components.jpg",
        "label": "B2B repeated wooden elements",
        "description": "Repeated components arranged in a row, stack or batch.",
    },
    "drawing_spec": {
        "key": "drawing_spec",
        "filename": "woodwork-from-drawing-specification.jpg",
        "label": "Work from drawing/specification",
        "description": "Drawing, template or dimensions next to a wood sample or part.",
    },
    "precision_detail": {
        "key": "precision_detail",
        "filename": "wood-joinery-detail-closeup.jpg",
        "label": "Precision joinery detail",
        "description": "Sharp closeup of joint, edge, grain or finish.",
    },
    "stairs_project": {
        "key": "stairs_project",
        "filename": "wooden-stairs-pomorskie.jpg",
        "label": "Wooden stairs project",
        "description": "Finished stairs in a real interior, with clean geometry.",
    },
    "doors_detail": {
        "key": "doors_detail",
        "filename": "wooden-doors-joinery-detail.jpg",
        "label": "Wooden doors detail",
        "description": "Doors, trims or construction joinery detail in context.",
    },
    "artistic_detail": {
        "key": "artistic_detail",
        "filename": "architectural-woodwork-detail.jpg",
        "label": "Architectural woodwork detail",
        "description": "Unusual detail, premium element or architectural woodwork.",
    },
}

PATHS = {
    "home": "/",
    "production": "/produkcja-elementow-drewnianych/",
    "advertising_events": "/elementy-drewniane-dla-firm-reklamowych-i-eventowych/",
    "construction": "/stolarka-budowlana/",
    "stairs_pricing": "/schody-drewniane-co-wplywa-na-cene-i-termin/",
    "architects": "/dla-architektow-i-firm/",
    "realizations": "/realizacje/",
    "guide": "/jak-przygotowac-zapytanie/",
    "short_series": "/kiedy-oplaca-sie-zamowic-elementy-drewniane-w-krotkiej-serii/",
    "quote": "/wycena/",
    "contact": "/kontakt/",
}

DEFAULT_LANGUAGE = "pl"

TEMPLATES = {
    "home": "pages/home.html",
    "production": "pages/service_page.html",
    "advertising_events": "pages/guide.html",
    "construction": "pages/service_page.html",
    "stairs_pricing": "pages/guide.html",
    "architects": "pages/service_page.html",
    "realizations": "pages/realizations.html",
    "guide": "pages/guide.html",
    "short_series": "pages/guide.html",
    "quote": "pages/quote.html",
    "contact": "pages/contact.html",
}

PAGE_ORDER = ["home", "production", "short_series", "advertising_events", "construction", "stairs_pricing", "architects", "realizations", "guide", "quote", "contact"]

CONTENT = {
    "pl": {
        "nav": {
            "production": "Produkcja elementów",
            "construction": "Stolarka budowlana",
            "architects": "Dla architektów i firm",
            "realizations": "Realizacje",
            "quote": "Wycena",
            "contact": "Kontakt",
        },
        "pages": {
            "home": {
                "title": "Kajax Stolarstwo | Elementy drewniane dla firm i stolarka na wymiar",
                "description": "Stolarnia z Gościcina dla firm, architektów i inwestorów. Drewniane elementy dla produkcji, reklamy i wnętrz, schody, drzwi, listwy oraz detale wykonywane według zdjęcia, rysunku albo wzoru.",
                "hero_photo": "hero_workshop",
                "b2b_photo": "b2b_components_series",
                "hero_alt": "Warsztat stolarski przygotowany do produkcji elementów drewnianych i realizacji na wymiar",
                "eyebrow": "Stolarnia z Gościcina. Drewno dla firm, inwestycji i wnętrz",
                "h1": "Drewno wykonane pod konkretny projekt",
                "lead": "Jeśli potrzebujesz elementu z drewna, którego nie kupisz z półki, wyślij zdjęcie, rysunek albo wzór. Robimy partie dla firm, schody, drzwi, listwy i detale do wnętrz. Najpierw sprawdzamy, czy temat pasuje do warsztatu, potem mówimy, czego potrzeba do wyceny.",
                "primary_cta": "Wyślij zdjęcie lub rysunek",
                "secondary_cta": "Sprawdź zakres",
            },
            "production": {
                "title": "Elementy drewniane dla firm: próbki i małe partie | Kajax",
                "description": "Drewniane elementy, próbki, półprodukty i małe partie według wzoru, zdjęcia albo rysunku. Dla producentów, wykonawców, agencji reklamowych, firm eventowych i projektantów.",
                "hero_photo": "b2b_components_series",
                "hero_alt": "Powtarzalne elementy drewniane wykonane w krótkiej serii dla firmy",
                "eyebrow": "Dla producentów, reklamy, eventów i wykonawców",
                "h1": "Elementy drewniane dla firm bez własnej stolarni",
                "lead": "Potrzebujesz drewnianej części do produktu, ekspozycji, opakowania albo montażu? Możemy wykonać próbkę, małą partię i powtarzalne zamówienia według wzoru. Zaczynamy od konkretu: zdjęcia, rysunku, próbki albo opisu zastosowania.",
                "primary_cta": "Wyślij element do oceny",
                "sections": [
                    {
                        "title": "Gdy firma potrzebuje drewnianych części",
                        "body": "Wykonujemy elementy dla producentów, agencji reklamowych, firm eventowych, wykonawców wnętrz, manufaktur i projektantów. Dobrze pasują tematy, które można powtórzyć po zaakceptowaniu próbki.",
                        "items": ["próbki i prototypy", "małe partie", "elementy według wzoru", "powtarzalne zamówienia po akceptacji"],
                    },
                    {
                        "title": "Co warto zlecić na zewnątrz",
                        "body": "Najlepiej sprawdzają się elementy, które da się opisać wymiarem, materiałem, wykończeniem i sposobem użycia. Jeśli element ma wracać w kolejnych zamówieniach, możemy od razu myśleć o pakowaniu, odbiorze i wysyłce.",
                        "items": ["listwy, profile i ramy", "drewniane półprodukty", "elementy ekspozycji i displayów", "detale do dalszego montażu lub wykończenia"],
                    },
                    {
                        "title": "Jak zaczynamy współpracę",
                        "body": "Wyślij zdjęcie, rysunek, próbkę albo krótki opis. Dopytamy o materiał, ilość, tolerancję, wykończenie i termin. Przy większej liczbie sztuk najbezpieczniej zacząć od próbki.",
                        "items": ["zdjęcie, rysunek albo wzór", "orientacyjna liczba sztuk", "materiał i wykończenie", "termin oraz sposób odbioru"],
                    },
                ],
                "faq": [
                    ("Czy realizujecie zamówienia B2B poza Pomorzem?", "Tak, jeśli element da się bezpiecznie zapakować i wysłać. Przy B2B możemy rozmawiać o Polsce i Europie, ale logistykę ustalamy dopiero po poznaniu wymiaru, materiału i liczby sztuk."),
                    ("Czy można zacząć od jednej próbki?", "Tak. Przy powtarzalnych elementach próbka często jest najlepszym sposobem ustalenia wymiaru, wykończenia i kosztu serii."),
                ],
            },
            "construction": {
                "title": "Stolarka budowlana Pomorskie | Schody, drzwi i listwy | Kajax",
                "description": "Schody drewniane, drzwi, listwy, zabudowy i elementy wykończeniowe na wymiar. Stolarnia z Gościcina obsługująca Pomorskie i okolice Wejherowa.",
                "hero_photo": "stairs_project",
                "hero_alt": "Schody drewniane wykonane na wymiar jako przykład stolarki budowlanej",
                "eyebrow": "Schody / drzwi / listwy / zabudowy",
                "h1": "Schody, drzwi i stolarka na wymiar w Pomorskiem",
                "lead": "Robimy schody, drzwi, listwy, zabudowy i elementy wykończeniowe tam, gdzie gotowy produkt nie pasuje do wnętrza. Najlepiej zacząć od zdjęć miejsca, wymiarów i informacji, na jakim etapie jest inwestycja.",
                "primary_cta": "Zapytaj o stolarkę budowlaną",
                "sections": [
                    {
                        "title": "Co wykonujemy",
                        "body": "Wchodzimy w tematy, w których liczy się pomiar, dopasowanie do wnętrza i porządne wykończenie widocznych detali.",
                        "items": ["schody drewniane", "drzwi wewnętrzne i zewnętrzne", "listwy, progi, opaski i parapety", "zabudowy i nietypowe elementy wykończeniowe"],
                    },
                    {
                        "title": "Kiedy zgłosić projekt",
                        "body": "Im wcześniej znamy wymiary, miejsce montażu i termin, tym łatwiej ocenić wykonalność i uniknąć zmian na budowie. Zdjęcia z telefonu wystarczą do pierwszej rozmowy.",
                        "items": ["rzuty lub pomiary", "zdjęcia miejsca montażu", "informacja o materiale", "termin inwestycji"],
                    },
                ],
                "faq": [
                    ("Czy pracujecie lokalnie?", "Dla stolarki budowlanej priorytetem jest Pomorskie, okolice Gościcina, Wejherowa i Trójmiasta."),
                    ("Czy można wysłać zdjęcia zamiast rysunku?", "Tak. Zdjęcia wystarczą do pierwszej rozmowy, ale przy wycenie potrzebne będą wymiary i ustalenia techniczne."),
                ],
            },
            "architects": {
                "title": "Stolarnia dla architektów, projektantów i firm | Kajax",
                "description": "Nietypowe detale drewniane, stolarka według projektu i trudniejsze realizacje dla architektów, projektantów, wykonawców i firm.",
                "hero_photo": "artistic_detail",
                "hero_alt": "Nietypowy detal drewniany wykonany według projektu dla architekta lub firmy",
                "eyebrow": "Detale / projekty specjalne",
                "h1": "Stolarnia do detali, których nie ma w katalogu",
                "lead": "Dla architektów, projektantów, wykonawców i firm, które mają pomysł albo rysunek, ale potrzebują sprawdzić, jak zrobić to z drewna. Pomagamy dobrać materiał, uprościć technologię, zrobić próbkę lub od razu wycenić zakres.",
                "primary_cta": "Wyślij detal do rozmowy",
                "sections": [
                    {
                        "title": "Kiedy warto napisać",
                        "body": "Gdy projekt wymaga rozmowy o detalu, materiale, montażu albo technologii, a gotowe rozwiązanie psuje efekt albo nie mieści się w wymiarach.",
                        "items": ["detale do wnętrz premium", "elementy ekspozycji i lokali", "zabudowy według projektu", "odtworzenia lub nietypowe profile"],
                    },
                    {
                        "title": "Jak współpracujemy",
                        "body": "Najpierw rozumiemy efekt, który ma powstać. Potem doprecyzowujemy materiał, wymiary, wykończenie, montaż i termin, żeby projekt dało się realnie wykonać.",
                        "items": ["analiza rysunku lub zdjęć", "doprecyzowanie technologii", "próbka, jeśli ma sens", "realizacja i odbiór"],
                    },
                ],
                "faq": [
                    ("Czy wykonujecie pojedyncze nietypowe elementy?", "Tak, jeśli projekt ma jasny zakres i da się go sensownie wykonać technologicznie."),
                    ("Czy pracujecie z architektami?", "Tak. Najlepiej, gdy zapytanie zawiera rysunek, inspirację, materiał i oczekiwany efekt końcowy."),
                ],
            },
            "realizations": {
                "title": "Realizacje i typy projektów stolarskich | Kajax",
                "description": "Schody, drzwi, listwy, detale drewniane, elementy B2B i projekty na wymiar. Zobacz, jakie prace warto wysłać do wyceny w Kajax.",
                "h1": "Jakie projekty warto wysłać do naszej stolarni",
                "lead": "Najlepiej pracujemy tam, gdzie drewno wymaga dokładności, dopasowania i rozmowy o detalu. Poniżej są typy zleceń, które dobrze pasują do warsztatu i warto wysłać do oceny.",
            },
            "quote": {
                "title": "Wyślij projekt do wyceny | Kajax",
                "description": "Wyślij zdjęcie, rysunek, specyfikację albo opis projektu. Ocenimy, czy możemy wykonać element, krótką serię lub stolarkę na wymiar.",
                "h1": "Wyślij projekt. Ocenimy, czy możemy go wykonać",
                "lead": "Na start wystarczy krótki opis, zdjęcie, rysunek albo specyfikacja oraz telefon lub email. Jeśli temat pasuje do warsztatu, dopytamy o wymiary, materiał, ilość, termin i odbiór albo wysyłkę.",
            },
            "contact": {
                "title": "Kontakt | Kajax Stolarstwo Gościcino",
                "description": "Kontakt z Kajax Stolarstwo: Gościcino, Pomorskie. Zapytania B2B, stolarka budowlana, nietypowe detale i projekty na wymiar.",
                "h1": "Kontakt",
                "lead": "Najwygodniej zacząć od formularza z krótkim opisem projektu. Przy pilnych sprawach można zadzwonić, ale zdjęcie lub rysunek i tak przyspieszą konkretną odpowiedź.",
            },
        },
        "process_steps": [
            ("Wysyłasz punkt startu", "Zdjęcie, rysunek, specyfikację, wzór albo krótki opis elementu i jego zastosowania."),
            ("Dopytujemy o decyzje", "Ustalamy materiał, ilość, wymiary, termin, wykończenie oraz odbiór, pakowanie lub wysyłkę."),
            ("Mówimy, czy temat pasuje", "Sprawdzamy, czy projekt da się sensownie wykonać w warsztacie, w realnym terminie i bez przepalania budżetu."),
            ("Próbka albo wycena", "Przy powtarzalnych elementach warto zacząć od próbki. Przy prostszych pracach przechodzimy do wyceny po ustaleniu zakresu."),
        ],
        "audience_cards": [
            {"title": "Elementy drewniane dla firm", "body": "Próbki, małe partie i części według wzoru. Dobre, gdy firma chce sprawdzić element i wracać po kolejne zamówienia.", "url": PATHS["production"], "cta": "Zobacz elementy dla firm"},
            {"title": "Schody, drzwi i listwy", "body": "Stolarka do domów, lokali i inwestycji w Pomorskiem, gdy gotowy element nie pasuje wymiarem albo standardem.", "url": PATHS["construction"], "cta": "Zobacz stolarkę budowlaną"},
            {"title": "Detale poza katalogiem", "body": "Elementy według rysunku, inspiracji albo pomysłu architekta. Dobre tam, gdzie trzeba porozmawiać o technologii.", "url": PATHS["architects"], "cta": "Zobacz współpracę projektową"},
        ],
        "realization_cases": [
            {"title": "Schody drewniane z dopracowanym detalem", "category": "Stolarka budowlana", "photo": "stairs_project", "alt": "Schody drewniane z balustradą jako przykład realizacji stolarskiej", "meta": ["materiał: drewno", "zakres: wykonanie i dopasowanie", "typ: inwestor prywatny"], "body": "Dobry kierunek dla inwestycji, w których liczy się pomiar, stabilna konstrukcja, dopasowanie do wnętrza i staranne wykończenie widocznych detali."},
            {"title": "Drewniany detal do wnętrza lub ekspozycji", "category": "Detale / wnętrza", "photo": "precision_detail", "alt": "Precyzyjny detal drewniany do wnętrza premium", "meta": ["zakres: detal i wykończenie", "typ: projekt indywidualny", "obszar: Pomorskie"], "body": "Dobre zapytanie zaczyna się od zdjęcia, rysunku albo inspiracji. Po ocenie materiału, skali i montażu można dobrać sensowny sposób wykonania."},
            {"title": "Drzwi, listwy i elementy stolarki", "category": "Drzwi / listwy / elementy", "photo": "doors_detail", "alt": "Drzwi drewniane jako przykład stolarki budowlanej na wymiar", "meta": ["zakres: stolarka budowlana", "typ: drzwi i wykończenie", "wycena: po zdjęciach i wymiarach"], "body": "To kierunek dla domów, lokali i inwestycji lokalnych, gdzie gotowy element nie pasuje wymiarem, materiałem albo oczekiwanym standardem wykonania."},
        ],
    },
}

CONTENT["en"] = {
    "nav": {
        "production": "Component production",
        "construction": "Construction joinery",
        "architects": "For architects and companies",
        "realizations": "Work",
        "quote": "Quote",
        "contact": "Contact",
    },
    "pages": {
        "home": {
            "title": "Kajax Joinery | Wooden components for companies and made-to-measure joinery",
            "description": "A Gościcino workshop for companies, architects and investors. Short runs of wooden components, stairs, doors, trims and demanding made-to-measure projects.",
            "hero_photo": "hero_workshop",
            "b2b_photo": "b2b_components_series",
            "hero_alt": "Joinery workshop prepared for wooden component production and made-to-measure projects",
            "eyebrow": "Production and construction joinery from Pomerania",
            "h1": "A joinery workshop for companies, architects and demanding wood projects",
            "lead": "We make wooden components for companies, short runs, construction joinery and unusual details. We work from photos, drawings and specifications, then clarify scope, material, timing and logistics before pricing.",
            "primary_cta": "Send project for a quote",
            "secondary_cta": "See what we do",
        },
        "production": {
            "title": "Wooden components and short runs for companies | Kajax",
            "description": "Short runs, semi-finished wooden parts and details made from a sample, photo or drawing. For manufacturers, contractors, advertising and event companies, and designers.",
            "hero_photo": "b2b_components_series",
            "hero_alt": "Repeatable wooden components made in a short run for a company",
            "eyebrow": "B2B / short runs / semi-finished parts",
            "h1": "Wooden components and short runs for companies",
            "lead": "We help companies order wooden details, semi-finished parts and short runs without building their own joinery setup. We can start from a photo, drawing, sample or specification, then move toward repeatable orders once the process is aligned.",
            "primary_cta": "Send a specification for pricing",
            "sections": [
                {"title": "For companies that need a predictable workshop", "body": "For manufacturers, POS and advertising agencies, event companies, interior contractors, small manufacturers and designers who need wooden parts in small or repeatable batches.", "items": ["prototypes and samples", "short production runs", "parts made from a sample", "recurring cooperation after the process is aligned"]},
                {"title": "Which components fit best", "body": "The strongest projects can be described by dimensions, material, finish and repeatability. If the project makes logistical sense, we can also discuss packing, shipping and recurring batches.", "items": ["trims, profiles and frames", "wooden semi-finished parts", "display and POS components", "parts for further assembly or finishing"]},
                {"title": "The simplest way to start", "body": "Send a photo, drawing, sample or short description. We will ask about material, quantity, tolerance, finish and timing. For larger runs, a sample or prototype is usually the safest first step.", "items": ["photo or drawing", "approximate quantity", "material and finish", "deadline and pickup or logistics"]},
            ],
            "faq": [
                ("Do you handle B2B orders outside Pomerania?", "Yes, if the project and logistics make sense. For B2B components we can discuss cooperation in Poland and across Europe, with shipping, packing and protection agreed individually."),
                ("Can we start with one sample?", "Yes. For repeatable components, a sample is often the best way to confirm dimensions, finish and the cost of a production run."),
            ],
        },
        "construction": {
            "title": "Construction joinery in Pomerania | Stairs, doors and trims | Kajax",
            "description": "Made-to-measure wooden stairs, doors, trims, built-ins and finishing elements. A Gościcino workshop serving Pomerania and the Wejherowo area.",
            "hero_photo": "stairs_project",
            "hero_alt": "Made-to-measure wooden stairs as an example of construction joinery",
            "eyebrow": "Stairs / doors / trims / built-ins",
            "h1": "Made-to-measure wooden stairs, doors and construction joinery in Pomerania",
            "lead": "We make stairs, doors, trims, built-ins and finishing elements for homes, venues and local investments in Pomerania. This offer fits projects where an off-the-shelf element does not match the dimensions, material or expected standard.",
            "primary_cta": "Ask about construction joinery",
            "sections": [
                {"title": "Scope of work", "body": "We help with wooden finishing and structural details, especially where measurement, fit to the interior and careful finishing of visible details matter.", "items": ["wooden stairs", "internal and external doors", "trims, thresholds, casings and window boards", "built-ins and unusual finishing elements"]},
                {"title": "When to get in touch", "body": "The earlier we know the dimensions, installation place and expected timing, the easier it is to assess feasibility and avoid costly changes on site.", "items": ["plans or measurements", "photos of the installation area", "material information", "project timeline"]},
            ],
            "faq": [
                ("Do you work locally?", "For construction joinery, the priority is Pomerania, Gościcino, Wejherowo and the Tricity area."),
                ("Can I send photos instead of a drawing?", "Yes. Photos are enough for the first conversation, but pricing will require dimensions and technical details."),
            ],
        },
        "architects": {
            "title": "Joinery for architects, designers and companies | Kajax",
            "description": "Unusual wooden details, project-based woodwork and made-to-measure joinery for architects, designers, contractors and companies.",
            "hero_photo": "artistic_detail",
            "hero_alt": "Unusual wooden detail made to a project for an architect or company",
            "eyebrow": "Details / special projects",
            "h1": "A workshop for unusual details and architect-led wood projects",
            "lead": "We help turn a concept into a feasible wooden detail for interiors, displays, venues and special projects. We work from drawings, references, photos and technical agreements with an architect or contractor.",
            "primary_cta": "Discuss a project",
            "sections": [
                {"title": "When it is worth writing", "body": "When a project needs a conversation about detail, material, installation method or production technology, and a ready-made solution does not deliver the intended effect.", "items": ["premium interior details", "display and commercial elements", "project-based built-ins", "recreated or unusual profiles"]},
                {"title": "How we cooperate", "body": "First we clarify the design intent and technical constraints. Then we specify material, dimensions, finish, installation and timing.", "items": ["drawing or photo review", "technical refinement", "sample if it makes sense", "production and handover"]},
            ],
            "faq": [
                ("Do you make single unusual elements?", "Yes, if the project has a clear scope and can be made sensibly with the workshop's technology."),
                ("Do you work with architects?", "Yes. The best inquiry includes a drawing, reference, material and the intended final effect."),
            ],
        },
        "realizations": {
            "title": "Woodwork projects and project types | Kajax",
            "description": "Stairs, doors, trims, wooden details, B2B components and made-to-measure projects. See which work is worth sending to Kajax for assessment.",
            "h1": "Which projects are worth sending to our workshop",
            "lead": "We are at our best where wood requires precision, fitting and a technical conversation about detail. Below are the kinds of inquiries that fit the workshop and are worth sending for assessment.",
        },
        "quote": {
            "title": "Send a project for a quote | Kajax",
            "description": "Send a photo, drawing, specification or short project description. We will assess whether we can make the component, short run or made-to-measure joinery.",
            "h1": "Send a project. We will assess whether we can make it",
            "lead": "A short description, photo, drawing or specification plus a phone number or email is enough to start. If the topic fits the workshop, we will ask about dimensions, material, quantity, timing and logistics.",
        },
        "contact": {
            "title": "Contact | Kajax Joinery Gościcino",
            "description": "Contact Kajax Joinery in Gościcino, Pomerania. B2B inquiries, construction joinery, unusual projects and made-to-measure woodwork.",
            "h1": "Contact",
            "lead": "The easiest way to start is the quote form with a short project description. For urgent matters, call us, but a photo or drawing will still help us give a concrete answer faster.",
        },
    },
    "process_steps": [
        ("You send materials", "A photo, drawing, specification or short description of the component, use case and expected result."),
        ("We ask technical questions", "We clarify material, quantity, dimensions, tolerances, timing, finish and pickup, packing or logistics."),
        ("We assess fit", "We check whether the project fits the workshop, makes sense economically and can be repeated or installed properly."),
        ("Sample or concrete quote", "For a production run, a sample can be the first step. Simpler projects can move to pricing after the scope is clear."),
    ],
    "audience_cards": [
        {"title": "Wooden components for companies", "body": "Short runs, semi-finished parts, sample-based components and B2B projects where repeatability and a safe sample start matter.", "url": PATHS["production"], "cta": "See B2B production"},
        {"title": "Construction joinery", "body": "Stairs, doors, trims, built-ins and wooden finishing elements for local projects in Pomerania.", "url": PATHS["construction"], "cta": "See construction joinery"},
        {"title": "Unusual and demanding projects", "body": "Unusual details, project-based work and cooperation with architects, designers and contractors.", "url": PATHS["architects"], "cta": "See project cooperation"},
    ],
    "realization_cases": [
        {"title": "Wooden stairs with refined details", "category": "Construction joinery", "photo": "stairs_project", "alt": "Wooden stairs with railing as an example of made-to-measure joinery", "meta": ["material: wood", "scope: production and fitting", "type: private investor"], "body": "A good fit for projects where measurement, a stable structure, interior alignment and careful finishing of visible details all matter."},
        {"title": "Wooden detail for an interior or display", "category": "Details / interiors", "photo": "precision_detail", "alt": "Precise wooden detail for a premium interior", "meta": ["scope: detail and finish", "type: individual project", "region: Pomerania"], "body": "A useful inquiry starts with a photo, drawing or reference. After reviewing material, scale and installation method, we can choose a sensible production approach."},
        {"title": "Doors, trims and joinery elements", "category": "Doors / trims / elements", "photo": "doors_detail", "alt": "Wooden doors as an example of made-to-measure construction joinery", "meta": ["scope: construction joinery", "type: doors and finishing", "quote: based on photos and dimensions"], "body": "This direction fits homes, venues and local projects where an off-the-shelf element does not match the dimensions, material or expected execution standard."},
    ],
}


_SERVICE_TRANSLATIONS = {
    "de": {
        "nav": {"production": "Elementfertigung", "construction": "Bauschreinerei", "architects": "Für Architekten und Firmen", "realizations": "Referenzen", "quote": "Anfrage", "contact": "Kontakt"},
        "home": ("Kajax Tischlerei | Holzelemente für Unternehmen und Schreinerei nach Maß", "Tischlerei aus Gościcino für Unternehmen, Architekten und Investoren. Kleinserien von Holzelementen, Treppen, Türen, Leisten und anspruchsvolle Sonderanfertigungen.", "Tischlerei für Unternehmen, Architekten und anspruchsvolle Holzprojekte", "Wir fertigen Holzelemente für Firmen, Kleinserien, Bauschreinerei und ungewöhnliche Details. Wir arbeiten nach Fotos, Zeichnungen und Spezifikationen und klären vor der Anfrage Umfang, Material, Termin und Logistik.", "Projekt zur Anfrage senden", "Leistungsumfang ansehen"),
        "production_h1": "Holzelemente und Kleinserien für Unternehmen",
        "production_lead": "Wir helfen Unternehmen, Holzdetails, Halbzeuge und Kleinserien zu bestellen, ohne eigene Tischlereikapazitäten aufzubauen. Der Start kann mit Foto, Zeichnung, Muster oder Spezifikation erfolgen; nach Abstimmung des Prozesses sind wiederkehrende Bestellungen möglich.",
        "construction_h1": "Holztreppen, Türen und Bauschreinerei nach Maß in Pommern",
        "construction_lead": "Wir fertigen Treppen, Türen, Leisten, Einbauten und Ausbauelemente für Häuser, Objekte und lokale Investitionen in Pommern. Das passt zu Projekten, bei denen Standardteile bei Maß, Material oder Ausführungsniveau nicht reichen.",
        "architects_h1": "Tischlerei für ungewöhnliche Details und Architekturprojekte",
        "architects_lead": "Wir helfen, ein Konzept in ein umsetzbares Holzdetail für Innenräume, Displays, Objekte und Sonderprojekte zu übersetzen. Wir arbeiten mit Zeichnungen, Referenzen, Fotos und technischen Abstimmungen mit Architekten oder Ausführenden.",
        "quote_h1": "Projekt zur Anfrage senden",
        "quote_lead": "Eine kurze Beschreibung, ein Foto, eine Zeichnung oder Spezifikation sowie Telefon oder E-Mail reichen für den Start. Wenn das Thema zur Werkstatt passt, fragen wir nach Maßen, Material, Menge, Termin und Logistik.",
        "contact_h1": "Kontakt",
        "contact_lead": "Der einfachste Start ist das kurze Anfrageformular. In dringenden Fällen können Sie anrufen.",
    },
    "sv": {
        "nav": {"production": "Komponentproduktion", "construction": "Byggsnickeri", "architects": "För arkitekter och företag", "realizations": "Referenser", "quote": "Offert", "contact": "Kontakt"},
        "home": ("Kajax Snickeri | Träkomponenter för företag och måttanpassat snickeri", "Snickeri från Gościcino för företag, arkitekter och investerare. Korta serier av träkomponenter, trappor, dörrar, lister och krävande specialprojekt.", "Snickeri för företag, arkitekter och krävande träprojekt", "Vi tillverkar träkomponenter för företag, korta serier, byggsnickeri och ovanliga detaljer. Vi arbetar från foton, ritningar och specifikationer och klargör omfattning, material, tidplan och logistik före offert.", "Skicka projekt för offert", "Se vad vi gör"),
        "production_h1": "Träkomponenter och korta serier för företag",
        "production_lead": "Vi hjälper företag att beställa trädetaljer, halvfabrikat och korta serier utan att bygga egen snickerikapacitet. Starten kan vara ett foto, en ritning, ett prov eller en specifikation, och efter processanpassning kan arbetet bli återkommande.",
        "construction_h1": "Trappor, dörrar och byggsnickeri i trä i Pommern",
        "construction_lead": "Vi utför trappor, dörrar, lister, inbyggnader och avslutningsdetaljer för hem, lokaler och lokala projekt i Pommern. Det passar när standardlösningar inte räcker i mått, material eller utförandenivå.",
        "architects_h1": "Snickeri för ovanliga detaljer och arkitektprojekt",
        "architects_lead": "Vi hjälper till att översätta en idé till en genomförbar trädetalj för interiörer, displayer, lokaler och specialprojekt. Vi arbetar från ritningar, referenser, foton och tekniska avstämningar.",
        "quote_h1": "Skicka projekt för offert",
        "quote_lead": "En kort beskrivning, foto, ritning eller specifikation samt telefon eller e-post räcker för start. Om uppdraget passar verkstaden frågar vi om mått, material, antal, tidplan och logistik.",
        "contact_h1": "Kontakt",
        "contact_lead": "Det enklaste sättet att börja är det korta offertformuläret. Vid brådskande ärenden kan du ringa.",
    },
    "da": {
        "nav": {"production": "Komponentproduktion", "construction": "Byggesnedkeri", "architects": "For arkitekter og virksomheder", "realizations": "Referencer", "quote": "Tilbud", "contact": "Kontakt"},
        "home": ("Kajax Snedkeri | Trækomponenter til virksomheder og snedkeri på mål", "Snedkeri fra Gościcino for virksomheder, arkitekter og investorer. Korte serier af trækomponenter, trapper, døre, lister og krævende specialprojekter.", "Snedkeri for virksomheder, arkitekter og krævende træprojekter", "Vi fremstiller trækomponenter til virksomheder, korte serier, byggesnedkeri og usædvanlige detaljer. Vi arbejder ud fra fotos, tegninger og specifikationer og afklarer omfang, materiale, tidsplan og logistik før tilbud.", "Send projekt til tilbud", "Se hvad vi laver"),
        "production_h1": "Trækomponenter og korte serier til virksomheder",
        "production_lead": "Vi hjælper virksomheder med at bestille trædetaljer, halvfabrikata og korte serier uden at opbygge egen snedkerkapacitet. Starten kan være foto, tegning, prøve eller specifikation, og efter procesafstemning kan arbejdet blive løbende.",
        "construction_h1": "Trapper, døre og byggesnedkeri i træ i Pommern",
        "construction_lead": "Vi udfører trapper, døre, lister, indbygninger og afslutningsdetaljer til boliger, lokaler og lokale projekter i Pommern. Det passer, når standardløsninger ikke rækker i mål, materiale eller udførelsesniveau.",
        "architects_h1": "Snedkeri til usædvanlige detaljer og arkitektprojekter",
        "architects_lead": "Vi hjælper med at omsætte en idé til en mulig trædetalje til interiører, displays, lokaler og specialprojekter. Vi arbejder ud fra tegninger, referencer, fotos og tekniske afklaringer.",
        "quote_h1": "Send projekt til tilbud",
        "quote_lead": "En kort beskrivelse, foto, tegning eller specifikation samt telefon eller e-mail er nok til start. Hvis opgaven passer til værkstedet, spørger vi om mål, materiale, antal, tidsplan og logistik.",
        "contact_h1": "Kontakt",
        "contact_lead": "Den nemmeste start er den korte tilbudsformular. Ved hastesager kan du ringe.",
    },
    "no": {
        "nav": {"production": "Komponentproduksjon", "construction": "Byggsnekkerarbeid", "architects": "For arkitekter og bedrifter", "realizations": "Referanser", "quote": "Forespørsel", "contact": "Kontakt"},
        "home": ("Kajax Snekkerverksted | Trekomponenter for bedrifter og snekkerarbeid på mål", "Snekkerverksted fra Gościcino for bedrifter, arkitekter og investorer. Korte serier av trekomponenter, trapper, dører, lister og krevende spesialprosjekter.", "Snekkerverksted for bedrifter, arkitekter og krevende treprosjekter", "Vi lager trekomponenter for bedrifter, korte serier, byggsnekkerarbeid og uvanlige detaljer. Vi arbeider ut fra bilder, tegninger og spesifikasjoner og avklarer omfang, materiale, tidsplan og logistikk før vurdering.", "Send prosjekt til vurdering", "Se hva vi gjør"),
        "production_h1": "Trekomponenter og korte serier for bedrifter",
        "production_lead": "Vi hjelper bedrifter med å bestille tredetaljer, halvfabrikata og korte serier uten å bygge egen snekkerkapasitet. Starten kan være bilde, tegning, prøve eller spesifikasjon, og etter prosessavklaring kan arbeidet bli fast.",
        "construction_h1": "Trapper, dører og byggsnekkerarbeid i tre i Pommern",
        "construction_lead": "Vi utfører trapper, dører, lister, innbygginger og avslutningsdetaljer for boliger, lokaler og lokale prosjekter i Pommern. Det passer når standardløsninger ikke strekker til på mål, materiale eller utførelsesnivå.",
        "architects_h1": "Snekkerverksted for uvanlige detaljer og arkitektprosjekter",
        "architects_lead": "Vi hjelper med å oversette en idé til en gjennomførbar tredetalj for interiør, displays, lokaler og spesialprosjekter. Vi jobber fra tegninger, referanser, bilder og tekniske avklaringer.",
        "quote_h1": "Send prosjekt til vurdering",
        "quote_lead": "En kort beskrivelse, bilde, tegning eller spesifikasjon samt telefon eller e-post er nok til start. Hvis oppdraget passer verkstedet, spør vi om mål, materiale, antall, tidsplan og logistikk.",
        "contact_h1": "Kontakt",
        "contact_lead": "Den enkleste starten er det korte forespørselsskjemaet. Ved hastesaker kan du ringe.",
    },
}

_LOCALIZED_DETAILS = {
    "de": {
        "production_sections": [
            {"title": "Für Unternehmen, die eine verlässliche Werkstatt brauchen", "body": "Für Hersteller, POS- und Werbeagenturen, Eventfirmen, Innenausbauer, kleine Manufakturen und Designer, die Holzteile in kleinen oder wiederholbaren Serien benötigen.", "items": ["Prototypen und Muster", "Kleinserien", "Elemente nach Muster", "regelmäßige Zusammenarbeit nach Prozessabstimmung"]},
            {"title": "Welche Elemente am besten passen", "body": "Am stärksten sind Projekte, die sich klar über Maße, Material, Oberfläche und Wiederholbarkeit beschreiben lassen. Wenn die Logistik sinnvoll ist, sprechen wir auch über Verpackung, Versand und wiederkehrende Partien.", "items": ["Leisten, Profile und Rahmen", "Holz-Halbzeuge", "Display- und POS-Elemente", "Teile zur weiteren Montage oder Veredelung"]},
            {"title": "Der einfachste Start", "body": "Senden Sie ein Foto, eine Zeichnung, ein Muster oder eine kurze Beschreibung. Wir fragen nach Material, Menge, Toleranzen, Oberfläche und Termin. Bei größeren Serien ist ein Muster oder Prototyp meist der sicherste erste Schritt.", "items": ["Foto oder Zeichnung", "ungefähre Menge", "Material und Oberfläche", "Termin sowie Abholung oder Logistik"]},
        ],
        "production_faq": [
            ("Bearbeiten Sie B2B-Aufträge außerhalb Pommerns?", "Ja, wenn Projekt und Logistik sinnvoll sind. Für B2B-Holzelemente können wir über Zusammenarbeit in Polen und Europa sprechen; Versand, Verpackung und Schutz werden individuell abgestimmt."),
            ("Können wir mit einem Muster beginnen?", "Ja. Bei wiederholbaren Elementen ist ein Muster oft der beste Weg, um Maße, Oberfläche und Kosten einer Serie zu bestätigen."),
        ],
        "construction_sections": [
            {"title": "Leistungsumfang", "body": "Wir unterstützen bei Holzdetails für Ausbau und Konstruktion, besonders dort, wo Aufmaß, Anpassung an den Innenraum und saubere Ausführung sichtbarer Details wichtig sind.", "items": ["Holztreppen", "Innen- und Außentüren", "Leisten, Schwellen, Verkleidungen und Fensterbänke", "Einbauten und ungewöhnliche Ausbauelemente"]},
            {"title": "Wann Sie sich melden sollten", "body": "Je früher wir Maße, Einbauort und gewünschten Termin kennen, desto leichter können wir Machbarkeit bewerten und teure Änderungen auf der Baustelle vermeiden.", "items": ["Pläne oder Maße", "Fotos des Einbauorts", "Information zum Material", "Zeitplan des Projekts"]},
        ],
        "construction_faq": [
            ("Arbeiten Sie lokal?", "Bei Bauschreinerei liegt der Schwerpunkt auf Pommern, Gościcino, Wejherowo und der Dreistadt."),
            ("Kann ich Fotos statt einer Zeichnung senden?", "Ja. Fotos reichen für das erste Gespräch, für eine belastbare Anfrage brauchen wir später Maße und technische Details."),
        ],
        "architects_sections": [
            {"title": "Wann sich eine Anfrage lohnt", "body": "Wenn ein Projekt eine Abstimmung zu Detail, Material, Montage oder Fertigungstechnologie braucht und Standardlösungen den gewünschten Effekt nicht erreichen.", "items": ["Details für hochwertige Innenräume", "Display- und Gewerbeelemente", "maßgefertigte Einbauten", "Nachbildungen oder ungewöhnliche Profile"]},
            {"title": "Wie wir zusammenarbeiten", "body": "Zuerst klären wir Entwurfsabsicht und technische Grenzen. Danach präzisieren wir Material, Maße, Oberfläche, Montage und Termin.", "items": ["Prüfung von Zeichnungen oder Fotos", "technische Präzisierung", "Muster, wenn sinnvoll", "Fertigung und Übergabe"]},
        ],
        "architects_faq": [
            ("Fertigen Sie einzelne ungewöhnliche Elemente?", "Ja, wenn der Umfang klar ist und das Element mit der Werkstatttechnologie sinnvoll gefertigt werden kann."),
            ("Arbeiten Sie mit Architekten?", "Ja. Am hilfreichsten sind Zeichnung, Referenzbild, Materialangabe und die Beschreibung des gewünschten Endeffekts."),
        ],
        "process_steps": [
            ("Sie senden Unterlagen", "Ein Foto, eine Zeichnung, eine Spezifikation oder eine kurze Beschreibung des Elements, der Nutzung und des gewünschten Ergebnisses."),
            ("Wir stellen technische Fragen", "Wir klären Material, Menge, Maße, Toleranzen, Termin, Oberfläche sowie Abholung, Verpackung oder Logistik."),
            ("Wir prüfen die Passung", "Wir bewerten, ob das Projekt zur Werkstatt passt, wirtschaftlich sinnvoll ist und gut wiederholt oder montiert werden kann."),
            ("Muster oder konkretes Angebot", "Bei Serien kann ein Muster der erste Schritt sein. Einfachere Projekte gehen nach Klärung des Umfangs in die Preisfindung."),
        ],
        "audience_cards": [
            {"title": "Holzelemente für Unternehmen", "body": "Kleinserien, Halbzeuge, Elemente nach Muster und B2B-Projekte, bei denen Wiederholbarkeit und ein sicherer Musterstart zählen.", "url": PATHS["production"], "cta": "B2B-Fertigung ansehen"},
            {"title": "Bauschreinerei", "body": "Treppen, Türen, Leisten, Einbauten und Holzdetails für lokale Bau- und Ausbauprojekte.", "url": PATHS["construction"], "cta": "Bauschreinerei ansehen"},
            {"title": "Sonderanfertigungen und anspruchsvolle Projekte", "body": "Ungewöhnliche Details, projektbezogene Arbeiten und Zusammenarbeit mit Architekten, Designern und Ausführenden.", "url": PATHS["architects"], "cta": "Projektzusammenarbeit ansehen"},
        ],
        "realization_cases": [
            {"title": "Holztreppe mit ausgearbeitetem Detail", "category": "Bauschreinerei", "photo": "stairs_project", "alt": "Holztreppe mit Geländer als Beispiel für maßgefertigte Schreinerarbeit", "meta": ["Material: Holz", "Umfang: Fertigung und Anpassung", "Typ: privater Investor"], "body": "Passend für Projekte, bei denen Aufmaß, stabile Konstruktion, Anpassung an den Innenraum und saubere Ausführung sichtbarer Details zählen."},
            {"title": "Holzdetail für Innenraum oder Display", "category": "Sonderanfertigung / Innenraum", "photo": "precision_detail", "alt": "Präzises Holzdetail für einen hochwertigen Innenraum", "meta": ["Umfang: Detail und Oberfläche", "Typ: individuelles Projekt", "Region: Pommern"], "body": "Eine gute Anfrage beginnt mit Foto, Zeichnung oder Referenz. Nach Prüfung von Material, Umfang und Montageart wählen wir eine sinnvolle Fertigungslösung."},
            {"title": "Türen, Leisten und Schreinerteile", "category": "Türen / Leisten / Elemente", "photo": "doors_detail", "alt": "Holztüren als Beispiel für maßgefertigte Bauschreinerei", "meta": ["Umfang: Bauschreinerei", "Typ: Türen und Ausbau", "Anfrage: nach Fotos und Maßen"], "body": "Geeignet für Häuser, Lokale und lokale Projekte, bei denen Standardteile in Maß, Material oder gewünschtem Ausführungsniveau nicht passen."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Werkstatt für Holzelemente, Bauschreinerei und Sonderprojekte", "eyebrow": "Produktions- und Bauschreinerei aus Pommern"},
            "production": {"title": "Holzelemente und Kleinserien für Unternehmen | Kajax", "description": "Kleinserien, Halbzeuge und Holzdetails nach Muster, Foto oder Zeichnung. Für Hersteller, Handwerker, Werbeagenturen, Eventfirmen und Designer.", "hero_alt": "Wiederholbare Holzelemente in Kleinserie für ein Unternehmen", "eyebrow": "B2B / Kleinserien / Halbzeuge", "primary_cta": "Spezifikation zur Anfrage senden"},
            "construction": {"title": "Bauschreinerei in Pommern | Treppen, Türen und Leisten | Kajax", "description": "Holztreppen, Türen, Leisten, Einbauten und Ausbauelemente nach Maß. Tischlerei aus Gościcino für Pommern und Umgebung Wejherowo.", "hero_alt": "Holztreppe nach Maß als Beispiel für Bauschreinerei", "eyebrow": "Treppen / Türen / Leisten / Einbauten", "primary_cta": "Bauschreinerei anfragen"},
            "architects": {"title": "Tischlerei für Architekten, Designer und Firmen | Kajax", "description": "Sonderdetails aus Holz, projektbezogene Schreinerarbeit und maßgefertigte Elemente für Architekten, Designer, Ausführende und Unternehmen.", "hero_alt": "Ungewöhnliches Holzdetail nach Projekt für Architekt oder Unternehmen", "eyebrow": "Sonderanfertigung / Details / Spezialprojekte", "primary_cta": "Projekt besprechen"},
            "realizations": {"title": "Schreinerprojekte und passende Anfragen | Kajax", "description": "Treppen, Türen, Leisten, Holzdetails, B2B-Elemente und Sonderanfertigungen. Sehen Sie, welche Arbeiten sich für eine Anfrage bei Kajax eignen.", "h1": "Welche Projekte sich für unsere Tischlerei lohnen", "lead": "Wir arbeiten am stärksten dort, wo Holz Präzision, Anpassung und technische Abstimmung über Details braucht. Unten sehen Sie Projektarten, die gut zur Werkstatt passen."},
            "quote": {"title": "Projekt zur Anfrage senden | Kajax", "description": "Senden Sie Foto, Zeichnung, Spezifikation oder kurze Projektbeschreibung. Wir prüfen, ob wir Element, Kleinserie oder Sonderanfertigung umsetzen können."},
            "contact": {"title": "Kontakt | Kajax Tischlerei Gościcino", "description": "Kontakt zu Kajax Tischlerei in Gościcino, Pommern. B2B-Anfragen, Bauschreinerei, Sonderprojekte und maßgefertigte Holzelemente."},
        },
    },
    "sv": {
        "production_sections": [
            {"title": "För företag som behöver en förutsägbar verkstad", "body": "För tillverkare, POS- och reklambyråer, eventföretag, inredningsentreprenörer, små tillverkare och designers som behöver trädelar i små eller återkommande serier.", "items": ["prototyper och prover", "korta serier", "delar efter prov", "återkommande samarbete efter processanpassning"]},
            {"title": "Vilka komponenter passar bäst", "body": "De starkaste projekten kan beskrivas tydligt med mått, material, finish och repeterbarhet. Om logistiken är rimlig kan vi också prata om packning, frakt och återkommande batcher.", "items": ["lister, profiler och ramar", "halvfabrikat i trä", "display- och POS-komponenter", "delar för vidare montering eller ytbehandling"]},
            {"title": "Enklaste vägen att börja", "body": "Skicka ett foto, en ritning, ett prov eller en kort beskrivning. Vi frågar om material, antal, toleranser, finish och tidplan. Vid större serier är ett prov eller en prototyp oftast tryggaste första steget.", "items": ["foto eller ritning", "ungefärligt antal", "material och finish", "deadline samt upphämtning eller logistik"]},
        ],
        "production_faq": [
            ("Tar ni B2B-uppdrag utanför Pommern?", "Ja, om projektet och logistiken är rimliga. För B2B-komponenter kan vi diskutera samarbete i Polen och Europa, men frakt, packning och skydd avtalas individuellt."),
            ("Kan vi börja med ett prov?", "Ja. För återkommande komponenter är ett prov ofta det bästa sättet att bekräfta mått, ytbehandling och kostnad för en serie."),
        ],
        "construction_sections": [
            {"title": "Omfattning", "body": "Vi hjälper till med trädetaljer för bygg och inredning, särskilt där mätning, passform mot interiören och noggrann finish av synliga detaljer är viktigt.", "items": ["trätrappor", "inner- och ytterdörrar", "lister, trösklar, foder och fönsterbänkar", "inbyggnader och ovanliga avslutningsdetaljer"]},
            {"title": "När du bör kontakta oss", "body": "Ju tidigare vi känner till mått, plats för montage och önskad tidplan, desto lättare är det att bedöma genomförbarhet och undvika dyra ändringar på plats.", "items": ["ritningar eller mått", "foton av montageplatsen", "information om material", "projektets tidplan"]},
        ],
        "construction_faq": [
            ("Arbetar ni lokalt?", "För byggsnickeri prioriterar vi Pommern, Gościcino, Wejherowo och Tricity-området."),
            ("Kan jag skicka foton istället för ritning?", "Ja. Foton räcker för första samtalet, men för offert behövs mått och tekniska detaljer."),
        ],
        "architects_sections": [
            {"title": "När det är värt att skriva", "body": "När projektet kräver samtal om detalj, material, montage eller tillverkningsteknik och färdiga lösningar inte ger rätt effekt.", "items": ["detaljer till premiuminteriörer", "display- och kommersiella element", "specialanpassade inbyggnader", "återskapade eller ovanliga profiler"]},
            {"title": "Så samarbetar vi", "body": "Först klargör vi designintention och tekniska begränsningar. Därefter specificerar vi material, mått, ytbehandling, montage och tidplan.", "items": ["granskning av ritning eller foto", "teknisk precisering", "prov om det är relevant", "tillverkning och överlämning"]},
        ],
        "architects_faq": [
            ("Gör ni enstaka ovanliga element?", "Ja, om projektet har tydlig omfattning och kan tillverkas på ett tekniskt rimligt sätt."),
            ("Arbetar ni med arkitekter?", "Ja. Den bästa förfrågan innehåller ritning, referens, material och önskat slutresultat."),
        ],
        "process_steps": [
            ("Du skickar underlag", "Foto, ritning, specifikation eller en kort beskrivning av komponenten, användningen och önskat resultat."),
            ("Vi ställer tekniska frågor", "Vi klargör material, antal, mått, toleranser, tidplan, finish samt upphämtning, packning eller logistik."),
            ("Vi bedömer passform", "Vi kontrollerar om projektet passar verkstaden, är ekonomiskt rimligt och kan upprepas eller monteras på rätt sätt."),
            ("Prov eller konkret offert", "Vid serier kan ett prov vara första steget. Enklare projekt går vidare till offert när omfattningen är tydlig."),
        ],
        "audience_cards": [
            {"title": "Träkomponenter för företag", "body": "Korta serier, halvfabrikat, komponenter efter prov och B2B-projekt där repeterbarhet och en trygg provstart är viktig.", "url": PATHS["production"], "cta": "Se B2B-produktion"},
            {"title": "Byggsnickeri", "body": "Trappor, dörrar, lister, inbyggnader och trädetaljer för lokala projekt.", "url": PATHS["construction"], "cta": "Se byggsnickeri"},
            {"title": "Special och krävande projekt", "body": "Ovanliga detaljer, projektbaserat arbete och samarbete med arkitekter, designers och entreprenörer.", "url": PATHS["architects"], "cta": "Se projektsamarbete"},
        ],
        "realization_cases": [
            {"title": "Trätrappa med genomarbetad detalj", "category": "Byggsnickeri", "photo": "stairs_project", "alt": "Trätrappa med räcke som exempel på specialsnickeri", "meta": ["material: trä", "omfattning: tillverkning och anpassning", "typ: privat investerare"], "body": "Passar projekt där mätning, stabil konstruktion, anpassning till interiören och noggrann finish av synliga detaljer är viktigt."},
            {"title": "Trädetalj för interiör eller display", "category": "Special / interiör", "photo": "precision_detail", "alt": "Precis trädetalj för en premiuminteriör", "meta": ["omfattning: detalj och finish", "typ: individuellt projekt", "region: Pommern"], "body": "En bra förfrågan börjar med foto, ritning eller referens. Efter granskning av material, skala och montage kan vi välja rätt tillverkningssätt."},
            {"title": "Dörrar, lister och snickeridelar", "category": "Dörrar / lister / delar", "photo": "doors_detail", "alt": "Trädörrar som exempel på måttanpassat byggsnickeri", "meta": ["omfattning: byggsnickeri", "typ: dörrar och finish", "offert: efter foton och mått"], "body": "Passar hem, lokaler och lokala projekt där standarddelar inte stämmer med mått, material eller önskad utförandenivå."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snickeriverkstad för träkomponenter, byggsnickeri och specialprojekt", "eyebrow": "Produktions- och byggsnickeri från Pommern"},
            "production": {"title": "Träkomponenter och korta serier för företag | Kajax", "description": "Korta serier, halvfabrikat och trädetaljer efter prov, foto eller ritning. För tillverkare, entreprenörer, reklambyråer, eventföretag och designers.", "hero_alt": "Återkommande träkomponenter tillverkade i kort serie för ett företag", "eyebrow": "B2B / korta serier / halvfabrikat", "primary_cta": "Skicka specifikation för offert"},
            "construction": {"title": "Byggsnickeri i Pommern | Trappor, dörrar och lister | Kajax", "description": "Trätrappor, dörrar, lister, inbyggnader och avslutningsdetaljer på mått. Snickeri från Gościcino för Pommern och området kring Wejherowo.", "hero_alt": "Måttanpassad trätrappa som exempel på byggsnickeri", "eyebrow": "Trappor / dörrar / lister / inbyggnader", "primary_cta": "Fråga om byggsnickeri"},
            "architects": {"title": "Snickeri för arkitekter, designers och företag | Kajax", "description": "Specialdetaljer i trä, projektbaserat snickeri och måttanpassade element för arkitekter, designers, entreprenörer och företag.", "hero_alt": "Ovanlig trädetalj tillverkad enligt projekt för arkitekt eller företag", "eyebrow": "Special / detaljer / särskilda projekt", "primary_cta": "Diskutera projekt"},
            "realizations": {"title": "Snickeriprojekt och lämpliga förfrågningar | Kajax", "description": "Trappor, dörrar, lister, trädetaljer, B2B-komponenter och måttanpassade projekt. Se vilka uppdrag som passar att skicka till Kajax för bedömning.", "h1": "Vilka projekt är värda att skicka till vår verkstad", "lead": "Vi är som starkast där trä kräver precision, anpassning och teknisk dialog om detaljer. Nedan visas projekt som passar verkstaden väl."},
            "quote": {"title": "Skicka projekt för offert | Kajax", "description": "Skicka foto, ritning, specifikation eller kort projektbeskrivning. Vi bedömer om vi kan tillverka komponenten, serien eller specialsnickeriet."},
            "contact": {"title": "Kontakt | Kajax Snickeri Gościcino", "description": "Kontakt med Kajax Snickeri i Gościcino, Pommern. B2B-förfrågningar, byggsnickeri, specialprojekt och måttanpassat träarbete."},
        },
    },
    "da": {
        "production_sections": [
            {"title": "For virksomheder der har brug for et forudsigeligt værksted", "body": "For producenter, POS- og reklamebureauer, eventfirmaer, indretningsentreprenører, små producenter og designere, der har brug for trædele i små eller gentagelige serier.", "items": ["prototyper og prøver", "korte serier", "dele efter prøve", "løbende samarbejde efter procesafstemning"]},
            {"title": "Hvilke komponenter passer bedst", "body": "De stærkeste projekter kan beskrives klart med mål, materiale, finish og gentagelighed. Hvis logistikken giver mening, kan vi også tale om pakning, forsendelse og gentagelige partier.", "items": ["lister, profiler og rammer", "halvfabrikata i træ", "display- og POS-komponenter", "dele til videre montage eller finish"]},
            {"title": "Den enkleste start", "body": "Send et foto, en tegning, en prøve eller en kort beskrivelse. Vi spørger ind til materiale, antal, tolerancer, finish og tidsplan. Ved større serier er en prøve eller prototype ofte det tryggeste første skridt.", "items": ["foto eller tegning", "omtrentligt antal", "materiale og finish", "deadline samt afhentning eller logistik"]},
        ],
        "production_faq": [
            ("Tager I B2B-opgaver uden for Pommern?", "Ja, hvis projekt og logistik giver mening. For B2B-komponenter kan vi drøfte samarbejde i Polen og Europa; forsendelse, pakning og beskyttelse aftales individuelt."),
            ("Kan vi starte med én prøve?", "Ja. For gentagelige komponenter er en prøve ofte den bedste måde at bekræfte mål, finish og pris for en serie."),
        ],
        "construction_sections": [
            {"title": "Omfang", "body": "Vi hjælper med trædetaljer til byggeri og indretning, især hvor opmåling, tilpasning til interiøret og omhyggelig finish af synlige detaljer er vigtig.", "items": ["trætrapper", "indvendige og udvendige døre", "lister, tærskler, gerigter og vinduesplader", "indbygninger og usædvanlige afslutningsdetaljer"]},
            {"title": "Hvornår du bør kontakte os", "body": "Jo tidligere vi kender mål, montagested og ønsket tidsplan, desto lettere er det at vurdere gennemførlighed og undgå dyre ændringer på stedet.", "items": ["tegninger eller mål", "fotos af montagestedet", "information om materiale", "projektets tidsplan"]},
        ],
        "construction_faq": [
            ("Arbejder I lokalt?", "For byggesnedkeri prioriterer vi Pommern, Gościcino, Wejherowo og Tricity-området."),
            ("Kan jeg sende fotos i stedet for tegning?", "Ja. Fotos er nok til den første samtale, men et tilbud kræver mål og tekniske detaljer."),
        ],
        "architects_sections": [
            {"title": "Hvornår det er værd at skrive", "body": "Når projektet kræver dialog om detalje, materiale, montage eller produktionsteknik, og færdige løsninger ikke giver den ønskede effekt.", "items": ["detaljer til premiuminteriør", "display- og erhvervselementer", "specialtilpassede indbygninger", "genskabte eller usædvanlige profiler"]},
            {"title": "Sådan samarbejder vi", "body": "Først afklarer vi designintention og tekniske begrænsninger. Derefter præciserer vi materiale, mål, finish, montage og tidsplan.", "items": ["gennemgang af tegning eller foto", "teknisk præcisering", "prøve hvis det giver mening", "produktion og aflevering"]},
        ],
        "architects_faq": [
            ("Laver I enkelte usædvanlige elementer?", "Ja, hvis projektet har et klart omfang og kan fremstilles teknisk fornuftigt."),
            ("Arbejder I med arkitekter?", "Ja. Den bedste forespørgsel indeholder tegning, reference, materiale og ønsket slutresultat."),
        ],
        "process_steps": [
            ("Du sender materiale", "Foto, tegning, specifikation eller en kort beskrivelse af komponenten, brugen og det ønskede resultat."),
            ("Vi stiller tekniske spørgsmål", "Vi afklarer materiale, antal, mål, tolerancer, tidsplan, finish samt afhentning, pakning eller logistik."),
            ("Vi vurderer pasform", "Vi kontrollerer, om projektet passer til værkstedet, giver økonomisk mening og kan gentages eller monteres korrekt."),
            ("Prøve eller konkret tilbud", "Ved serier kan en prøve være første skridt. Enklere projekter går videre til pris, når omfanget er klart."),
        ],
        "audience_cards": [
            {"title": "Trækomponenter til virksomheder", "body": "Korte serier, halvfabrikata, komponenter efter prøve og B2B-projekter, hvor gentagelighed og en tryg prøvestart er vigtig.", "url": PATHS["production"], "cta": "Se B2B-produktion"},
            {"title": "Byggesnedkeri", "body": "Trapper, døre, lister, indbygninger og trædetaljer til lokale projekter.", "url": PATHS["construction"], "cta": "Se byggesnedkeri"},
            {"title": "Special og krævende projekter", "body": "Usædvanlige detaljer, projektbaseret arbejde og samarbejde med arkitekter, designere og entreprenører.", "url": PATHS["architects"], "cta": "Se projektsamarbejde"},
        ],
        "realization_cases": [
            {"title": "Trætrappe med gennemarbejdet detalje", "category": "Byggesnedkeri", "photo": "stairs_project", "alt": "Trætrappe med rækværk som eksempel på specialsnedkeri", "meta": ["materiale: træ", "omfang: produktion og tilpasning", "type: privat investor"], "body": "Passer til projekter, hvor opmåling, stabil konstruktion, tilpasning til interiøret og omhyggelig finish af synlige detaljer er vigtig."},
            {"title": "Trædetalje til interiør eller display", "category": "Special / interiør", "photo": "precision_detail", "alt": "Præcis trædetalje til et premiuminteriør", "meta": ["omfang: detalje og finish", "type: individuelt projekt", "region: Pommern"], "body": "En god forespørgsel starter med foto, tegning eller reference. Efter vurdering af materiale, skala og montage kan vi vælge en fornuftig produktionsmetode."},
            {"title": "Døre, lister og snedkerdele", "category": "Døre / lister / dele", "photo": "doors_detail", "alt": "Trædøre som eksempel på måltilpasset byggesnedkeri", "meta": ["omfang: byggesnedkeri", "type: døre og finish", "tilbud: efter fotos og mål"], "body": "Passer til boliger, lokaler og lokale projekter, hvor standarddele ikke passer til mål, materiale eller ønsket udførelsesniveau."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snedkerværksted til trækomponenter, byggesnedkeri og specialprojekter", "eyebrow": "Produktions- og byggesnedkeri fra Pommern"},
            "production": {"title": "Trækomponenter og korte serier til virksomheder | Kajax", "description": "Korte serier, halvfabrikata og trædetaljer efter prøve, foto eller tegning. For producenter, entreprenører, reklamebureauer, eventfirmaer og designere.", "hero_alt": "Gentagelige trækomponenter fremstillet i kort serie til en virksomhed", "eyebrow": "B2B / korte serier / halvfabrikata", "primary_cta": "Send specifikation til tilbud"},
            "construction": {"title": "Byggesnedkeri i Pommern | Trapper, døre og lister | Kajax", "description": "Trætrapper, døre, lister, indbygninger og afslutningsdetaljer på mål. Snedkeri fra Gościcino for Pommern og området omkring Wejherowo.", "hero_alt": "Måltilpasset trætrappe som eksempel på byggesnedkeri", "eyebrow": "Trapper / døre / lister / indbygninger", "primary_cta": "Spørg om byggesnedkeri"},
            "architects": {"title": "Snedkeri for arkitekter, designere og virksomheder | Kajax", "description": "Specialdetaljer i træ, projektbaseret snedkeri og måltilpassede elementer til arkitekter, designere, entreprenører og virksomheder.", "hero_alt": "Usædvanlig trædetalje fremstillet efter projekt til arkitekt eller virksomhed", "eyebrow": "Special / detaljer / særlige projekter", "primary_cta": "Drøft projekt"},
            "realizations": {"title": "Snedkeriprojekter og passende forespørgsler | Kajax", "description": "Trapper, døre, lister, trædetaljer, B2B-komponenter og måltilpassede projekter. Se hvilke opgaver der er værd at sende til Kajax for vurdering.", "h1": "Hvilke projekter er værd at sende til vores værksted", "lead": "Vi er stærkest der, hvor træ kræver præcision, tilpasning og teknisk dialog om detaljer. Nedenfor er projekter, der passer godt til værkstedet."},
            "quote": {"title": "Send projekt til tilbud | Kajax", "description": "Send foto, tegning, specifikation eller kort projektbeskrivelse. Vi vurderer, om vi kan fremstille komponenten, serien eller specialsnedkeriet."},
            "contact": {"title": "Kontakt | Kajax Snedkeri Gościcino", "description": "Kontakt Kajax Snedkeri i Gościcino, Pommern. B2B-forespørgsler, byggesnedkeri, specialprojekter og måltilpasset træarbejde."},
        },
    },
    "no": {
        "production_sections": [
            {"title": "For bedrifter som trenger et forutsigbart verksted", "body": "For produsenter, POS- og reklamebyråer, eventbedrifter, interiørentreprenører, små produsenter og designere som trenger tredeler i små eller repeterbare serier.", "items": ["prototyper og prøver", "korte serier", "deler etter prøve", "fast samarbeid etter prosessavklaring"]},
            {"title": "Hvilke komponenter passer best", "body": "De sterkeste prosjektene kan beskrives tydelig med mål, materiale, overflate og repeterbarhet. Hvis logistikken gir mening, kan vi også snakke om pakking, frakt og repeterbare partier.", "items": ["lister, profiler og rammer", "halvfabrikata i tre", "display- og POS-komponenter", "deler for videre montering eller finish"]},
            {"title": "Den enkleste starten", "body": "Send et bilde, en tegning, en prøve eller en kort beskrivelse. Vi spør om materiale, antall, toleranser, overflate og tidsplan. Ved større serier er en prøve eller prototype ofte tryggeste første steg.", "items": ["bilde eller tegning", "omtrentlig antall", "materiale og overflate", "frist samt henting eller logistikk"]},
        ],
        "production_faq": [
            ("Tar dere B2B-oppdrag utenfor Pommern?", "Ja, hvis prosjekt og logistikk gir mening. For B2B-komponenter kan vi diskutere samarbeid i Polen og Europa; frakt, pakking og beskyttelse avtales individuelt."),
            ("Kan vi starte med én prøve?", "Ja. For repeterbare komponenter er en prøve ofte den beste måten å bekrefte mål, overflate og kostnad for en serie."),
        ],
        "construction_sections": [
            {"title": "Omfang", "body": "Vi hjelper med tredetaljer til bygg og interiør, særlig der oppmåling, tilpasning til interiøret og nøyaktig finish på synlige detaljer er viktig.", "items": ["tretrapper", "innvendige og utvendige dører", "lister, terskler, gerikter og vindusbrett", "innbygginger og uvanlige avslutningsdetaljer"]},
            {"title": "Når du bør ta kontakt", "body": "Jo tidligere vi kjenner mål, monteringssted og ønsket tidsplan, desto lettere er det å vurdere gjennomførbarhet og unngå dyre endringer på stedet.", "items": ["tegninger eller mål", "bilder av monteringsstedet", "informasjon om materiale", "prosjektets tidsplan"]},
        ],
        "construction_faq": [
            ("Jobber dere lokalt?", "For byggsnekkerarbeid prioriterer vi Pommern, Gościcino, Wejherowo og Tricity-området."),
            ("Kan jeg sende bilder i stedet for tegning?", "Ja. Bilder holder for første samtale, men et tilbud krever mål og tekniske detaljer."),
        ],
        "architects_sections": [
            {"title": "Når det er verdt å skrive", "body": "Når prosjektet krever dialog om detalj, materiale, montering eller produksjonsteknikk, og ferdige løsninger ikke gir ønsket effekt.", "items": ["detaljer til premiuminteriør", "display- og næringselementer", "spesialtilpassede innbygginger", "gjenskapte eller uvanlige profiler"]},
            {"title": "Slik samarbeider vi", "body": "Først avklarer vi designintensjon og tekniske begrensninger. Deretter presiserer vi materiale, mål, overflate, montering og tidsplan.", "items": ["gjennomgang av tegning eller bilde", "teknisk presisering", "prøve hvis det gir mening", "produksjon og overlevering"]},
        ],
        "architects_faq": [
            ("Lager dere enkelte uvanlige elementer?", "Ja, hvis prosjektet har tydelig omfang og kan lages på en teknisk fornuftig måte."),
            ("Jobber dere med arkitekter?", "Ja. Den beste forespørselen inneholder tegning, referanse, materiale og ønsket sluttresultat."),
        ],
        "process_steps": [
            ("Du sender materiale", "Bilde, tegning, spesifikasjon eller en kort beskrivelse av komponenten, bruken og ønsket resultat."),
            ("Vi stiller tekniske spørsmål", "Vi avklarer materiale, antall, mål, toleranser, tidsplan, overflate samt henting, pakking eller logistikk."),
            ("Vi vurderer passform", "Vi sjekker om prosjektet passer verkstedet, gir økonomisk mening og kan repeteres eller monteres riktig."),
            ("Prøve eller konkret tilbud", "Ved serier kan en prøve være første steg. Enklere prosjekter går videre til pris når omfanget er klart."),
        ],
        "audience_cards": [
            {"title": "Trekomponenter for bedrifter", "body": "Korte serier, halvfabrikata, komponenter etter prøve og B2B-prosjekter der repeterbarhet og en trygg prøvestart er viktig.", "url": PATHS["production"], "cta": "Se B2B-produksjon"},
            {"title": "Byggsnekkerarbeid", "body": "Trapper, dører, lister, innbygginger og tredetaljer for lokale prosjekter.", "url": PATHS["construction"], "cta": "Se byggsnekkerarbeid"},
            {"title": "Spesial og krevende prosjekter", "body": "Uvanlige detaljer, prosjektbasert arbeid og samarbeid med arkitekter, designere og entreprenører.", "url": PATHS["architects"], "cta": "Se prosjektsamarbeid"},
        ],
        "realization_cases": [
            {"title": "Tretrapp med gjennomarbeidet detalj", "category": "Byggsnekkerarbeid", "photo": "stairs_project", "alt": "Tretrapp med rekkverk som eksempel på spesialtilpasset snekkerarbeid", "meta": ["materiale: tre", "omfang: produksjon og tilpasning", "type: privat investor"], "body": "Passer prosjekter der oppmåling, stabil konstruksjon, tilpasning til interiøret og nøyaktig finish på synlige detaljer er viktig."},
            {"title": "Tredetalj til interiør eller display", "category": "Spesial / interiør", "photo": "precision_detail", "alt": "Presis tredetalj til et premiuminteriør", "meta": ["omfang: detalj og finish", "type: individuelt prosjekt", "region: Pommern"], "body": "En god forespørsel starter med bilde, tegning eller referanse. Etter vurdering av materiale, skala og montering kan vi velge en fornuftig produksjonsmåte."},
            {"title": "Dører, lister og snekkerdeler", "category": "Dører / lister / deler", "photo": "doors_detail", "alt": "Tredører som eksempel på måltilpasset byggsnekkerarbeid", "meta": ["omfang: byggsnekkerarbeid", "type: dører og finish", "tilbud: etter bilder og mål"], "body": "Passer boliger, lokaler og lokale prosjekter der standarddeler ikke stemmer med mål, materiale eller ønsket utførelsesnivå."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snekkerverksted for trekomponenter, byggsnekkerarbeid og spesialprosjekter", "eyebrow": "Produksjons- og byggsnekkerverksted fra Pommern"},
            "production": {"title": "Trekomponenter og korte serier for bedrifter | Kajax", "description": "Korte serier, halvfabrikata og tredetaljer etter prøve, bilde eller tegning. For produsenter, entreprenører, reklamebyråer, eventbedrifter og designere.", "hero_alt": "Repeterbare trekomponenter produsert i kort serie for en bedrift", "eyebrow": "B2B / korte serier / halvfabrikata", "primary_cta": "Send spesifikasjon for vurdering"},
            "construction": {"title": "Byggsnekkerarbeid i Pommern | Trapper, dører og lister | Kajax", "description": "Tretrapper, dører, lister, innbygginger og avslutningsdetaljer på mål. Snekkerverksted fra Gościcino for Pommern og området rundt Wejherowo.", "hero_alt": "Måltilpasset tretrapp som eksempel på byggsnekkerarbeid", "eyebrow": "Trapper / dører / lister / innbygginger", "primary_cta": "Spør om byggsnekkerarbeid"},
            "architects": {"title": "Snekkerverksted for arkitekter, designere og bedrifter | Kajax", "description": "Spesialdetaljer i tre, prosjektbasert snekkerarbeid og måltilpassede elementer for arkitekter, designere, entreprenører og bedrifter.", "hero_alt": "Uvanlig tredetalj laget etter prosjekt for arkitekt eller bedrift", "eyebrow": "Spesial / detaljer / særlige prosjekter", "primary_cta": "Diskuter prosjekt"},
            "realizations": {"title": "Snekkerprosjekter og passende forespørsler | Kajax", "description": "Trapper, dører, lister, tredetaljer, B2B-komponenter og måltilpassede prosjekter. Se hvilke oppdrag som passer å sende til Kajax for vurdering.", "h1": "Hvilke prosjekter er verdt å sende til verkstedet vårt", "lead": "Vi er best der tre krever presisjon, tilpasning og teknisk dialog om detaljer. Nedenfor er prosjekter som passer verkstedet godt."},
            "quote": {"title": "Send prosjekt til vurdering | Kajax", "description": "Send bilde, tegning, spesifikasjon eller kort prosjektbeskrivelse. Vi vurderer om vi kan lage komponenten, serien eller spesialarbeidet."},
            "contact": {"title": "Kontakt | Kajax Snekkerverksted Gościcino", "description": "Kontakt Kajax Snekkerverksted i Gościcino, Pommern. B2B-forespørsler, byggsnekkerarbeid, spesialprosjekter og måltilpasset trearbeid."},
        },
    },
}


def _localized_variant(code):
    base = CONTENT["en"].copy()
    variant = _SERVICE_TRANSLATIONS[code]
    pages = {key: value.copy() for key, value in CONTENT["en"]["pages"].items()}
    title, desc, h1, lead, primary, secondary = variant["home"]
    pages["home"].update({"title": title, "description": desc, "h1": h1, "lead": lead, "primary_cta": primary, "secondary_cta": secondary})
    pages["production"].update({"h1": variant["production_h1"], "lead": variant["production_lead"]})
    pages["construction"].update({"h1": variant["construction_h1"], "lead": variant["construction_lead"]})
    pages["architects"].update({"h1": variant["architects_h1"], "lead": variant["architects_lead"]})
    pages["quote"].update({"h1": variant["quote_h1"], "lead": variant["quote_lead"]})
    pages["contact"].update({"h1": variant["contact_h1"], "lead": variant["contact_lead"]})
    details = _LOCALIZED_DETAILS[code]
    for page_key, updates in details["page_updates"].items():
        pages[page_key].update(updates)
    pages["production"].update({"sections": details["production_sections"], "faq": details["production_faq"]})
    pages["construction"].update({"sections": details["construction_sections"], "faq": details["construction_faq"]})
    pages["architects"].update({"sections": details["architects_sections"], "faq": details["architects_faq"]})
    base["nav"] = variant["nav"]
    base["pages"] = pages
    base["process_steps"] = details["process_steps"]
    base["audience_cards"] = details["audience_cards"]
    base["realization_cases"] = details["realization_cases"]
    return base


for _code in ("de", "sv", "da", "no"):
    CONTENT[_code] = _localized_variant(_code)


GUIDE_PAGES = {
    "pl": {
        "title": "Jak przygotować zapytanie do stolarni produkcyjnej? | Kajax",
        "description": "Checklista do wyceny elementów drewnianych, krótkich serii, schodów, drzwi i nietypowych projektów według rysunku. Co wysłać, żeby szybciej dostać odpowiedź.",
        "eyebrow": "Poradnik do wyceny",
        "h1": "Jak przygotować zapytanie do stolarni, żeby szybciej dostać konkretną odpowiedź",
        "lead": "Nie musisz mieć pełnej dokumentacji. Wystarczy pokazać, co ma powstać, w jakiej ilości, z jakiego materiału i na kiedy. Im konkretniejszy punkt startu, tym szybciej powiemy, czy temat pasuje do warsztatu i czego brakuje do wyceny.",
        "primary_cta": "Wyślij projekt do wyceny",
        "aside_title": "Minimum, które wystarczy na start",
        "aside_body": "Jeśli nie masz rysunku technicznego, wyślij zdjęcie, szkic albo przykład podobnego elementu. To wystarczy, żeby rozpocząć rozmowę i ustalić kolejne dane.",
        "aside_items": ["zdjęcie, szkic lub rysunek", "orientacyjne wymiary", "liczba sztuk lub skala", "materiał i wykończenie, jeśli są znane", "termin oraz lokalizacja"],
        "sections": [
            {"title": "Dla elementów B2B i krótkich serii", "body": "Przy powtarzalnych elementach liczy się jasny punkt odniesienia: wzór, zdjęcie, rysunek albo prototyp. Dzięki temu szybciej ustalimy, czy projekt nadaje się na próbkę, małą partię albo stałe zamówienia.", "items": ["docelowa liczba sztuk i pierwsza partia", "czy element ma być gotowy, czy do dalszego montażu", "tolerancje, frezy, otwory i widoczne krawędzie", "czy potrzebne będzie pakowanie lub wysyłka", "czy w grę wchodzi stała współpraca"]},
            {"title": "Dla schodów, drzwi i stolarki budowlanej", "body": "Przy pracach montowanych lokalnie liczy się miejsce inwestycji, etap budowy i możliwość pomiaru. Zdjęcia z telefonu często wystarczą, żeby ocenić, czy temat jest do dalszej rozmowy.", "items": ["miejscowość inwestycji", "zdjęcia miejsca montażu", "rzuty, pomiary lub orientacyjne wymiary", "oczekiwany termin", "informacja, czy projekt jest w trakcie budowy czy remontu"]},
            {"title": "Dla architektów i nietypowych detali", "body": "Przy trudniejszych elementach opisz efekt końcowy, ograniczenia montażowe i priorytet: wygląd, trwałość, powtarzalność albo budżet. To pomaga dobrać technologię bez tracenia charakteru projektu.", "items": ["rysunek, inspiracja lub wizualizacja", "materiał i kolorystyka", "miejsce montażu lub sposób użycia", "widoczne detale i oczekiwany standard", "elementy, które mogą być uproszczone technologicznie"]},
        ],
        "avoid_title": "Co najczęściej spowalnia wycenę",
        "avoid_body": "Najwięcej czasu zabiera odgadywanie skali, wymiarów i oczekiwanego efektu. Lepiej wysłać prosty opis z niedoskonałym zdjęciem niż ogólne pytanie bez konkretów.",
        "avoid_items": ["brak wymiarów lub choćby skali", "brak informacji o ilości", "same inspiracje bez wskazania, co ma być wykonane", "niejasny termin", "brak telefonu albo emaila do doprecyzowania"],
        "faq": [
            ("Czy muszę mieć rysunek techniczny?", "Nie. Rysunek pomaga, ale na start wystarczy zdjęcie, szkic albo opis. Przy wycenie technicznej i tak doprecyzujemy wymiary oraz materiał."),
            ("Czy mogę wysłać tylko zdjęcie podobnego elementu?", "Tak. Zdjęcie jest dobrym początkiem, jeśli dodasz orientacyjne wymiary, ilość i informację, do czego element ma służyć."),
            ("Czy zapytanie B2B może dotyczyć Europy?", "Tak, jeśli element, skala i logistyka mają sens. Pakowanie i wysyłka są zawsze ustalane indywidualnie."),
        ],
    },
    "en": {
        "title": "How to prepare a joinery inquiry? | Kajax",
        "description": "A practical checklist for pricing wooden components, short runs, stairs, doors and made-to-measure woodwork. What to send so the workshop can reply faster.",
        "eyebrow": "Quote guide",
        "h1": "How to prepare a joinery inquiry so you get a concrete answer faster",
        "lead": "You do not need complete documentation. It is enough to show what should be made, in what quantity, from which material and by when. The clearer the starting point, the faster we can say whether the project fits the workshop and what is still missing for pricing.",
        "primary_cta": "Send project for a quote",
        "aside_title": "Minimum that is enough to start",
        "aside_body": "If you do not have a technical drawing, send a photo, sketch or a similar reference. That is enough to start the conversation and define the next details.",
        "aside_items": ["photo, sketch or drawing", "approximate dimensions", "quantity or scale", "material and finish if known", "timing and location"],
        "sections": [
            {"title": "For B2B components and short runs", "body": "For repeatable components, a clear reference matters most: sample, photo, drawing or prototype. It helps us decide faster whether the project should start with a sample, small batch or recurring order.", "items": ["target quantity and first batch", "finished part or part for further assembly", "tolerances, milling, holes and visible edges", "whether packing or shipping may be needed", "whether recurring cooperation is possible"]},
            {"title": "For stairs, doors and construction joinery", "body": "For locally installed joinery, project location, building stage and measurement access matter. Phone photos are often enough to say whether the topic is worth a deeper conversation.", "items": ["project location", "photos of the installation area", "plans, measurements or approximate dimensions", "expected timing", "whether it is a new build or renovation"]},
            {"title": "For architects and unusual details", "body": "For unusual details, describe the intended final effect, installation limits and the priority: appearance, durability, repeatability or budget. It helps choose a workable method without losing the design intent.", "items": ["drawing, reference or visualization", "material and colour direction", "installation place or use case", "visible details and expected standard", "elements that may be simplified technically"]},
        ],
        "avoid_title": "What usually slows down pricing",
        "avoid_body": "Most time is lost guessing scale, dimensions and the expected effect. A simple description with an imperfect photo is more useful than a general question without specifics.",
        "avoid_items": ["no dimensions or scale", "no quantity", "references without saying what should be made", "unclear timing", "no phone or email for clarification"],
        "faq": [
            ("Do I need a technical drawing?", "No. A drawing helps, but a photo, sketch or description is enough to start. Technical details can be clarified before pricing."),
            ("Can I send only a photo of a similar element?", "Yes. A photo is a good start if you add approximate dimensions, quantity and what the part will be used for."),
            ("Can a B2B inquiry be Europe-wide?", "Yes, if the component, scale and logistics make sense. Packing and shipping are always agreed individually."),
        ],
    },
    "de": {
        "title": "Wie bereitet man eine Tischlerei-Anfrage vor? | Kajax",
        "description": "Praktische Checkliste für Holzelemente, Kleinserien, Treppen, Türen und Sonderanfertigungen. Welche Informationen eine schnellere Einschätzung ermöglichen.",
        "eyebrow": "Anfrage-Leitfaden",
        "h1": "Wie Sie eine Tischlerei-Anfrage vorbereiten, damit schneller eine konkrete Antwort möglich ist",
        "lead": "Sie brauchen keine vollständige Dokumentation. Es reicht, zu zeigen, was entstehen soll, in welcher Menge, aus welchem Material und bis wann. Je klarer der Startpunkt ist, desto schneller können wir sagen, ob das Projekt zur Werkstatt passt und was für die Anfrage noch fehlt.",
        "primary_cta": "Projekt zur Anfrage senden",
        "aside_title": "Das Minimum für den Start",
        "aside_body": "Wenn keine technische Zeichnung vorhanden ist, senden Sie ein Foto, eine Skizze oder ein ähnliches Beispiel. Die restlichen Details klären wir im Gespräch.",
        "aside_items": ["Foto, Skizze oder Zeichnung", "ungefähre Maße", "Menge oder Umfang", "Material und Oberfläche, falls bekannt", "Termin und Standort"],
        "sections": [
            {"title": "Für B2B-Elemente und Kleinserien", "body": "Bei wiederholbaren Elementen zählen Wiederholbarkeit und ein klarer Bezugspunkt. Am besten funktionieren Muster, Foto, Zeichnung oder Prototyp.", "items": ["Zielmenge und erste Serie", "fertiges Element oder Teil zur weiteren Montage", "Toleranzen, Fräsungen, Bohrungen und sichtbare Kanten", "ob Verpackung oder Versand nötig sein kann", "ob regelmäßige Zusammenarbeit denkbar ist"]},
            {"title": "Für Treppen, Türen und Bauschreinerei", "body": "Bei lokal montierten Arbeiten zählen Projektort, Bauphase und Aufmaß. Fotos helfen, den Umfang vor einem Termin besser einzuschätzen.", "items": ["Projektort", "Fotos des Montagebereichs", "Pläne, Maße oder ungefähre Abmessungen", "gewünschter Termin", "Neubau oder Renovierung"]},
            {"title": "Für Architekten und Sonderprojekte", "body": "Bei ungewöhnlichen Details beschreiben Sie den gewünschten Endeffekt, Montagegrenzen und was am wichtigsten ist: Optik, Haltbarkeit, Wiederholbarkeit oder Budget.", "items": ["Zeichnung, Referenz oder Visualisierung", "Material und Farbrichtung", "Montageort oder Nutzung", "sichtbare Details und erwarteter Standard", "Elemente, die technisch vereinfacht werden können"]},
        ],
        "avoid_title": "Was eine Anfrage meist verlangsamt",
        "avoid_body": "Am meisten Zeit kostet das Erraten von Umfang und Erwartungen. Eine einfache Beschreibung mit einem unperfekten Foto ist hilfreicher als eine allgemeine Frage ohne Details.",
        "avoid_items": ["keine Maße oder Größenordnung", "keine Mengenangabe", "nur Inspiration ohne Angabe, was gefertigt werden soll", "unklarer Termin", "keine Telefon- oder E-Mail-Angabe"],
        "faq": [
            ("Brauche ich eine technische Zeichnung?", "Nein. Eine Zeichnung hilft, aber Foto, Skizze oder Beschreibung reichen für den Start. Technische Details klären wir vor der Preisfindung."),
            ("Kann ich nur ein Foto eines ähnlichen Elements senden?", "Ja. Ein Foto ist ein guter Anfang, wenn Sie ungefähre Maße, Menge und Verwendung ergänzen."),
            ("Kann eine B2B-Anfrage europaweit sein?", "Ja, wenn Element, Umfang und Logistik sinnvoll sind. Verpackung und Versand werden individuell abgestimmt."),
        ],
    },
    "sv": {
        "title": "Hur förbereder man en förfrågan till ett snickeri? | Kajax",
        "description": "Praktisk checklista för träkomponenter, korta serier, trappor, dörrar och specialsnickeri. Vad du bör skicka för snabbare bedömning.",
        "eyebrow": "Offertguide",
        "h1": "Så förbereder du en snickeriförfrågan och får ett konkret svar snabbare",
        "lead": "Du behöver inte komplett dokumentation. Det räcker att visa vad som ska tillverkas, i vilken mängd, av vilket material och till när. Ju tydligare startpunkt, desto snabbare kan vi säga om projektet passar verkstaden och vad som saknas för offert.",
        "primary_cta": "Skicka projekt för offert",
        "aside_title": "Minsta underlag för start",
        "aside_body": "Om du inte har en teknisk ritning kan du skicka ett foto, en skiss eller en liknande referens. Resten kan vi reda ut i dialog.",
        "aside_items": ["foto, skiss eller ritning", "ungefärliga mått", "antal eller omfattning", "material och finish om känt", "tidplan och plats"],
        "sections": [
            {"title": "För B2B-komponenter och korta serier", "body": "För återkommande komponenter är upprepbarhet och tydlig referens viktigast. Prov, foto, ritning eller prototyp fungerar bäst.", "items": ["målvolym och första serie", "färdig detalj eller del för vidare montage", "toleranser, fräsningar, hål och synliga kanter", "om packning eller frakt kan behövas", "om återkommande samarbete är möjligt"]},
            {"title": "För trappor, dörrar och byggsnickeri", "body": "För lokalt monterat snickeri är projektplats, byggskede och mätning viktiga. Foton hjälper oss bedöma omfattningen före ett platsbesök.", "items": ["projektplats", "foton av monteringsplatsen", "planer, mått eller ungefärliga dimensioner", "önskad tidplan", "nybyggnation eller renovering"]},
            {"title": "För arkitekter och specialprojekt", "body": "Vid ovanliga detaljer bör du beskriva slutresultat, monteringsbegränsningar och vad som är viktigast: utseende, hållbarhet, upprepbarhet eller budget.", "items": ["ritning, referens eller visualisering", "material och färgriktning", "monteringsplats eller användning", "synliga detaljer och förväntad standard", "delar som kan förenklas tekniskt"]},
        ],
        "avoid_title": "Vad som oftast bromsar offerten",
        "avoid_body": "Mest tid går åt till att gissa omfattning och förväntningar. En enkel beskrivning med ett ofullkomligt foto är bättre än en allmän fråga utan detaljer.",
        "avoid_items": ["inga mått eller skala", "inget antal", "referenser utan att säga vad som ska tillverkas", "oklar tidplan", "ingen telefon eller e-post för följdfrågor"],
        "faq": [
            ("Behöver jag en teknisk ritning?", "Nej. Ritning hjälper, men foto, skiss eller beskrivning räcker för start. Tekniska detaljer klargörs före prissättning."),
            ("Kan jag bara skicka ett foto av en liknande detalj?", "Ja. Foto är en bra start om du lägger till ungefärliga mått, antal och användning."),
            ("Kan en B2B-förfrågan gälla Europa?", "Ja, om komponent, omfattning och logistik är rimliga. Packning och frakt avtalas individuellt."),
        ],
    },
    "da": {
        "title": "Hvordan forbereder man en forespørgsel til et snedkeri? | Kajax",
        "description": "Praktisk checkliste til trækomponenter, korte serier, trapper, døre og specialsnedkeri. Hvad du bør sende for hurtigere vurdering.",
        "eyebrow": "Tilbudsguide",
        "h1": "Sådan forbereder du en snedkerforespørgsel og får et konkret svar hurtigere",
        "lead": "Du behøver ikke komplet dokumentation. Det er nok at vise, hvad der skal fremstilles, i hvilket antal, af hvilket materiale og hvornår. Jo tydeligere startpunkt, desto hurtigere kan vi vurdere, om projektet passer til værkstedet, og hvad der mangler til et tilbud.",
        "primary_cta": "Send projekt til tilbud",
        "aside_title": "Minimum til at starte",
        "aside_body": "Hvis du ikke har en teknisk tegning, kan du sende foto, skitse eller lignende reference. Resten kan vi afklare i dialog.",
        "aside_items": ["foto, skitse eller tegning", "omtrentlige mål", "antal eller omfang", "materiale og finish hvis kendt", "tidsplan og placering"],
        "sections": [
            {"title": "Til B2B-komponenter og korte serier", "body": "For gentagelige komponenter er gentagelighed og en klar reference vigtigst. Prøve, foto, tegning eller prototype fungerer bedst.", "items": ["målantal og første serie", "færdig del eller del til videre montage", "tolerancer, fræsninger, huller og synlige kanter", "om pakning eller forsendelse kan være nødvendig", "om løbende samarbejde er relevant"]},
            {"title": "Til trapper, døre og byggesnedkeri", "body": "For lokalt monteret snedkeri er projektsted, byggefase og opmåling vigtige. Fotos hjælper med at vurdere omfanget før et besøg.", "items": ["projektets placering", "fotos af montagestedet", "planer, mål eller omtrentlige dimensioner", "ønsket tidsplan", "nybyggeri eller renovering"]},
            {"title": "Til arkitekter og specialprojekter", "body": "Ved usædvanlige detaljer bør du beskrive slutresultat, montagebegrænsninger og hvad der er vigtigst: udtryk, holdbarhed, gentagelighed eller budget.", "items": ["tegning, reference eller visualisering", "materiale og farveretning", "montagested eller brug", "synlige detaljer og forventet standard", "dele der kan forenkles teknisk"]},
        ],
        "avoid_title": "Hvad der oftest forsinker tilbuddet",
        "avoid_body": "Mest tid går med at gætte omfang og forventninger. En enkel beskrivelse med et uperfekt foto er bedre end et generelt spørgsmål uden detaljer.",
        "avoid_items": ["ingen mål eller skala", "intet antal", "referencer uden at sige hvad der skal fremstilles", "uklar tidsplan", "ingen telefon eller e-mail til afklaring"],
        "faq": [
            ("Behøver jeg en teknisk tegning?", "Nej. Tegning hjælper, men foto, skitse eller beskrivelse er nok til start. Tekniske detaljer afklares før prissætning."),
            ("Kan jeg kun sende et foto af en lignende del?", "Ja. Foto er en god start, hvis du tilføjer omtrentlige mål, antal og brug."),
            ("Kan en B2B-forespørgsel dække Europa?", "Ja, hvis komponent, omfang og logistik giver mening. Pakning og forsendelse aftales individuelt."),
        ],
    },
    "no": {
        "title": "Hvordan forberede en forespørsel til et snekkerverksted? | Kajax",
        "description": "Praktisk sjekkliste for trekomponenter, korte serier, trapper, dører og spesialarbeid. Hva du bør sende for raskere vurdering.",
        "eyebrow": "Forespørselsguide",
        "h1": "Slik forbereder du en snekkerforespørsel og får et konkret svar raskere",
        "lead": "Du trenger ikke komplett dokumentasjon. Det holder å vise hva som skal lages, i hvilket antall, av hvilket materiale og til når. Jo tydeligere startpunkt, desto raskere kan vi vurdere om prosjektet passer verkstedet og hva som mangler for pris.",
        "primary_cta": "Send prosjekt til vurdering",
        "aside_title": "Minimum for å starte",
        "aside_body": "Hvis du ikke har teknisk tegning, kan du sende bilde, skisse eller lignende referanse. Resten kan vi avklare i dialog.",
        "aside_items": ["bilde, skisse eller tegning", "omtrentlige mål", "antall eller omfang", "materiale og overflate hvis kjent", "tidsplan og sted"],
        "sections": [
            {"title": "For B2B-komponenter og korte serier", "body": "For repeterbare komponenter er repeterbarhet og tydelig referanse viktigst. Prøve, bilde, tegning eller prototype fungerer best.", "items": ["målantall og første serie", "ferdig del eller del for videre montering", "toleranser, fresing, hull og synlige kanter", "om pakking eller frakt kan være nødvendig", "om fast samarbeid er aktuelt"]},
            {"title": "For trapper, dører og byggsnekkerarbeid", "body": "For lokalt montert arbeid er prosjektsted, byggefase og oppmåling viktig. Bilder hjelper oss å vurdere omfanget før et besøk.", "items": ["prosjektsted", "bilder av monteringsstedet", "planer, mål eller omtrentlige dimensjoner", "ønsket tidsplan", "nybygg eller renovering"]},
            {"title": "For arkitekter og spesialprosjekter", "body": "Ved uvanlige detaljer bør du beskrive sluttresultat, monteringsbegrensninger og hva som er viktigst: uttrykk, holdbarhet, repeterbarhet eller budsjett.", "items": ["tegning, referanse eller visualisering", "materiale og fargeretning", "monteringssted eller bruk", "synlige detaljer og forventet standard", "deler som kan forenkles teknisk"]},
        ],
        "avoid_title": "Hva som oftest forsinker vurderingen",
        "avoid_body": "Mest tid går med til å gjette omfang og forventninger. En enkel beskrivelse med et uperfekt bilde er bedre enn et generelt spørsmål uten detaljer.",
        "avoid_items": ["ingen mål eller skala", "intet antall", "referanser uten å si hva som skal lages", "uklar tidsplan", "ingen telefon eller e-post for avklaring"],
        "faq": [
            ("Trenger jeg teknisk tegning?", "Nei. Tegning hjelper, men bilde, skisse eller beskrivelse er nok for start. Tekniske detaljer avklares før pris."),
            ("Kan jeg bare sende bilde av en lignende del?", "Ja. Bilde er en god start hvis du legger til omtrentlige mål, antall og bruksområde."),
            ("Kan en B2B-forespørsel gjelde Europa?", "Ja, hvis komponent, omfang og logistikk gir mening. Pakking og frakt avtales individuelt."),
        ],
    },
}

SHORT_SERIES_GUIDE_PAGES = {
    "pl": {
        "title": "Kiedy opłaca się zamówić elementy drewniane w krótkiej serii? | Kajax",
        "description": "Poradnik B2B: kiedy krótka seria drewnianych elementów ma sens, kiedy zacząć od prototypu i jakie dane wysłać do wyceny.",
        "eyebrow": "B2B / krótkie serie",
        "h1": "Kiedy opłaca się zamówić elementy drewniane w krótkiej serii?",
        "lead": "Krótka seria ma sens wtedy, gdy firma potrzebuje powtarzalnych elementów, ale nie chce inwestować we własne zaplecze stolarskie. Najbezpieczniej zacząć od próbki, wzoru albo małej partii, a po ustaleniu wykonania przejść do regularnych zamówień.",
        "primary_cta": "Zapytaj o krótką serię",
        "aside_title": "Krótka seria ma sens, gdy",
        "aside_body": "Najlepsze zapytania B2B dotyczą elementów, które można jasno opisać, powtórzyć i sensownie zapakować albo przekazać dalej do montażu, lakierowania lub kompletacji.",
        "aside_items": ["element będzie zamawiany ponownie", "liczy się powtarzalność wymiaru", "masz wzór, zdjęcie lub rysunek", "potrzebujesz próbki przed większą partią", "własna produkcja byłaby nieopłacalna"],
        "sections": [
            {"title": "Gdy element ma wracać w kolejnych zamówieniach", "body": "Krótka seria działa najlepiej, gdy po pierwszej partii można powtórzyć ten sam element bez zaczynania od zera. Wtedy warto dopracować wzór, tolerancje, wykończenie, pakowanie i sposób odbioru.", "items": ["listwy, profile i ramy", "drewniane półprodukty do dalszego montażu", "elementy POS, ekspozycji i displayów", "detale do mebli lub wnętrz", "części wykonywane według stałego wzoru"]},
            {"title": "Gdy własna produkcja byłaby za droga albo zbyt wolna", "body": "Dla wielu firm problemem nie jest sama obróbka drewna, tylko czas, miejsce, sprzęt i ludzie potrzebni do małej, niestandardowej partii. Zewnętrzna stolarnia pozwala sprawdzić produkt bez rozbudowywania własnego warsztatu.", "items": ["brak własnej stolarni", "zbyt mała skala na produkcję przemysłową", "potrzeba elastycznej partii próbnej", "krótki termin wdrożenia", "projekt wymaga rozmowy o detalu"]},
            {"title": "Gdy warto zacząć od próbki lub prototypu", "body": "Próbka zmniejsza ryzyko, jeśli element ma być później powtarzany. Pozwala ocenić materiał, krawędzie, frezy, otwory, kolor i tolerancje zanim zamówienie wejdzie w większą partię albo stałą współpracę.", "items": ["nowy element bez historii produkcji", "ważny detal widoczny dla klienta końcowego", "niepewny materiał lub wykończenie", "planowana większa seria po testach", "potrzeba sprawdzenia pakowania i wysyłki"]},
        ],
        "avoid_title": "Kiedy seria może nie być dobrym pierwszym krokiem",
        "avoid_body": "Nie każde zlecenie trzeba od razu planować jako serię. Jeśli projekt jest jednorazowy, bardzo zmienny albo nie ma jeszcze wymiarów, lepiej zacząć od doprecyzowania zakresu.",
        "avoid_items": ["brak wymiaru, wzoru i skali", "projekt zmienia się po każdej rozmowie", "jednorazowy detal wymaga długiego przygotowania", "nie wiadomo, do czego element ma służyć", "termin jest krótszy niż realne przygotowanie próbki"],
        "faq": [
            ("Jaka ilość to krótka seria?", "Nie ma jednej granicy. Czasem jest to kilka sztuk testowych, czasem kilkadziesiąt lub więcej. Ważniejsze od liczby jest to, czy element da się powtarzać według stałych założeń."),
            ("Czy można zacząć od jednej próbki?", "Tak. Przy elementach B2B próbka często jest najlepszym początkiem, bo pozwala ustalić koszt, technologię i standard wykonania przed większą partią."),
            ("Czy możliwe jest pakowanie i wysyłka?", "Tak, jeśli element i skala mają sens logistycznie. Pakowanie, zabezpieczenie i wysyłkę ustalamy po poznaniu wymiarów, materiału i liczby sztuk."),
        ],
    },
    "en": {
        "title": "When does it pay to order wooden components in a short run? | Kajax",
        "description": "B2B guide: when a short run of wooden components makes sense, when to start with a prototype and what to send for pricing.",
        "eyebrow": "B2B / short runs",
        "h1": "When does it pay to order wooden components in a short run?",
        "lead": "A short run makes sense when a company needs repeatable wooden parts but does not want to invest in its own joinery setup. The safest route is usually a sample, reference part or first small batch, followed by recurring orders once the process is aligned.",
        "primary_cta": "Ask about a short run",
        "aside_title": "A short run makes sense when",
        "aside_body": "The strongest B2B inquiries concern components that can be described clearly, repeated and sensibly packed or passed on for assembly, finishing or completion.",
        "aside_items": ["the component will be ordered again", "dimension repeatability matters", "you have a sample, photo or drawing", "you need a sample before a larger batch", "in-house production would not pay off"],
        "sections": [
            {"title": "When the component will come back in future orders", "body": "A short run is most valuable when the first batch can lead to repeat production without starting from zero every time. Then it is worth refining the reference, tolerances, finish, packing and pickup method.", "items": ["trims, profiles and frames", "wooden semi-finished parts for further assembly", "POS, display and exhibition components", "details for furniture or interiors", "parts made to a stable reference"]},
            {"title": "When in-house production would be too costly or too slow", "body": "For many companies, the problem is not only woodworking itself but also the space, tools, time and people needed for a small non-standard batch. An external workshop lets you test a product without expanding your own production setup.", "items": ["no in-house joinery", "too small for industrial production", "need for a flexible trial batch", "short implementation timeline", "the project needs detail discussion"]},
            {"title": "When it is better to start with a sample or prototype", "body": "A sample lowers risk when the component is meant to be repeated later. It helps confirm material, edges, milling, holes, colour and tolerances before moving into a larger batch or recurring cooperation.", "items": ["new component with no production history", "visible detail important to the end customer", "uncertain material or finish", "larger run planned after testing", "packing and shipping need to be checked"]},
        ],
        "avoid_title": "When a series may not be the right first step",
        "avoid_body": "Not every job should be planned as a run immediately. If the project is one-off, changing heavily or still lacks dimensions, it is better to clarify the scope first.",
        "avoid_items": ["no dimensions, reference or scale", "the design changes after every conversation", "a one-off detail needs long preparation", "the use of the component is unclear", "the deadline is shorter than realistic sample preparation"],
        "faq": [
            ("What quantity counts as a short run?", "There is no fixed threshold. Sometimes it is a few test pieces, sometimes dozens or more. More important than the number is whether the component can be repeated to stable assumptions."),
            ("Can we start with one sample?", "Yes. For B2B components, a sample is often the best start because it helps confirm cost, process and execution standard before a larger batch."),
            ("Can packing and shipping be handled?", "Yes, if the component and scale make logistical sense. Packing, protection and shipping are agreed after we know the dimensions, material and quantity."),
        ],
    },
    "de": {
        "title": "Wann lohnt sich eine Kleinserie von Holzelementen? | Kajax",
        "description": "B2B-Leitfaden: wann eine Kleinserie von Holzelementen sinnvoll ist, wann ein Prototyp hilft und welche Daten für eine Anfrage wichtig sind.",
        "eyebrow": "B2B / Kleinserien",
        "h1": "Wann lohnt sich eine Kleinserie von Holzelementen?",
        "lead": "Eine Kleinserie ist sinnvoll, wenn ein Unternehmen wiederholbare Holzelemente braucht, aber nicht in eigene Tischlereikapazitäten investieren möchte. Der sicherste Weg beginnt oft mit Muster, Referenzteil oder kleiner erster Serie und führt nach Prozessabstimmung zu wiederkehrenden Bestellungen.",
        "primary_cta": "Kleinserie anfragen",
        "aside_title": "Eine Kleinserie passt, wenn",
        "aside_body": "Die besten B2B-Anfragen betreffen Elemente, die sich klar beschreiben, wiederholen und sinnvoll verpacken oder weiterverarbeiten lassen.",
        "aside_items": ["das Element wieder bestellt wird", "Maßwiederholbarkeit wichtig ist", "Muster, Foto oder Zeichnung vorhanden sind", "vor der größeren Serie ein Muster nötig ist", "eigene Fertigung sich nicht lohnt"],
        "sections": [
            {"title": "Wenn das Element in weiteren Bestellungen wiederkommt", "body": "Der größte Wert einer Kleinserie entsteht, wenn die erste Partie später wiederholt werden kann, ohne jedes Mal neu zu beginnen. Dann lohnt es sich, Referenz, Toleranzen, Oberfläche und Verpackung sauber festzulegen.", "items": ["Leisten, Profile und Rahmen", "Holz-Halbzeuge zur Weiterverarbeitung", "POS-, Display- und Ausstellungselemente", "Details für Möbel oder Innenräume", "Teile nach stabilem Muster"]},
            {"title": "Wenn eigene Fertigung zu teuer oder zu langsam wäre", "body": "Für viele Firmen liegt das Problem nicht nur in der Holzbearbeitung, sondern in Platz, Werkzeug, Zeit und Personal für eine kleine Sonderpartie. Eine externe Werkstatt ermöglicht Produkttests ohne Ausbau eigener Fertigung.", "items": ["keine eigene Tischlerei", "zu kleine Menge für Industrieproduktion", "flexible Testserie nötig", "kurze Einführungszeit", "Projekt braucht Detailabstimmung"]},
            {"title": "Wenn ein Muster oder Prototyp sinnvoller ist", "body": "Ein Muster senkt das Risiko, wenn das Element später wiederholt werden soll. Es hilft, Material, Kanten, Fräsungen, Bohrungen, Farbe und Toleranzen vor einer größeren Partie zu bestätigen.", "items": ["neues Element ohne Fertigungshistorie", "sichtbares Detail für Endkunden", "unklares Material oder Oberfläche", "größere Serie nach Test geplant", "Verpackung und Versand müssen geprüft werden"]},
        ],
        "avoid_title": "Wann eine Serie nicht der beste erste Schritt ist",
        "avoid_body": "Nicht jedes Projekt sollte sofort als Serie geplant werden. Wenn es ein Einzelstück ist, stark wechselt oder noch keine Maße hat, sollte zuerst der Umfang geklärt werden.",
        "avoid_items": ["keine Maße, kein Muster und keine Größenordnung", "das Design ändert sich nach jedem Gespräch", "ein Einzelteil braucht lange Vorbereitung", "die Nutzung des Elements ist unklar", "der Termin ist kürzer als realistische Mustervorbereitung"],
        "faq": [
            ("Welche Menge gilt als Kleinserie?", "Es gibt keine feste Grenze. Manchmal sind es wenige Testteile, manchmal einige Dutzend oder mehr. Wichtiger ist, ob das Element nach festen Annahmen wiederholt werden kann."),
            ("Können wir mit einem Muster beginnen?", "Ja. Bei B2B-Elementen ist ein Muster oft der beste Start, um Kosten, Technologie und Ausführungsstandard vor einer größeren Serie zu bestätigen."),
            ("Sind Verpackung und Versand möglich?", "Ja, wenn Element und Umfang logistisch sinnvoll sind. Verpackung, Schutz und Versand werden nach Klärung von Maßen, Material und Menge abgestimmt."),
        ],
    },
    "sv": {
        "title": "När lönar det sig att beställa träkomponenter i kort serie? | Kajax",
        "description": "B2B-guide: när en kort serie träkomponenter är rimlig, när en prototyp är bäst och vilket underlag som behövs för offert.",
        "eyebrow": "B2B / korta serier",
        "h1": "När lönar det sig att beställa träkomponenter i kort serie?",
        "lead": "En kort serie är vettig när ett företag behöver återkommande träkomponenter men inte vill investera i egen snickerikapacitet. Tryggast är ofta att börja med ett prov, en referensdel eller en liten första serie och gå vidare till återkommande beställningar när processen fungerar.",
        "primary_cta": "Fråga om kort serie",
        "aside_title": "En kort serie passar när",
        "aside_body": "De bästa B2B-förfrågningarna gäller komponenter som kan beskrivas tydligt, upprepas och packas eller lämnas vidare för montage på ett rimligt sätt.",
        "aside_items": ["komponenten ska beställas igen", "måttupprepning är viktig", "du har prov, foto eller ritning", "du behöver prov före större serie", "egen produktion inte lönar sig"],
        "sections": [
            {"title": "När komponenten återkommer i nya beställningar", "body": "En kort serie ger störst värde när den första omgången kan upprepas utan att starta om varje gång. Då är det värt att justera referens, toleranser, finish och packning.", "items": ["lister, profiler och ramar", "halvfabrikat i trä för vidare montage", "POS-, display- och utställningskomponenter", "detaljer för möbler eller interiörer", "delar efter stabil referens"]},
            {"title": "När egen produktion vore för dyr eller långsam", "body": "För många företag handlar utmaningen inte bara om träbearbetning utan om plats, verktyg, tid och personal för en liten specialserie. En extern verkstad låter er testa en produkt utan att bygga egen produktion.", "items": ["ingen egen snickeriverkstad", "för liten skala för industriell produktion", "behov av flexibel testserie", "kort införandetid", "projektet kräver detaljdialog"]},
            {"title": "När ett prov eller en prototyp är bättre först", "body": "Ett prov minskar risken när komponenten ska upprepas senare. Det hjälper till att bekräfta material, kanter, fräsningar, hål, färg och toleranser före en större serie.", "items": ["ny komponent utan produktionshistorik", "synlig detalj viktig för slutkund", "osäkert material eller finish", "större serie planerad efter test", "packning och frakt behöver kontrolleras"]},
        ],
        "avoid_title": "När en serie kanske inte är rätt första steg",
        "avoid_body": "Alla uppdrag ska inte planeras som serie direkt. Om projektet är en engångsdetalj, ändras mycket eller saknar mått är det bättre att först tydliggöra omfattningen.",
        "avoid_items": ["inga mått, ingen referens och ingen skala", "designen ändras efter varje samtal", "en engångsdetalj kräver lång förberedelse", "komponentens användning är oklar", "tidsfristen är kortare än realistisk provframtagning"],
        "faq": [
            ("Vilken mängd räknas som kort serie?", "Det finns ingen fast gräns. Ibland är det några testdelar, ibland tiotals eller fler. Viktigare än antalet är om komponenten kan upprepas enligt stabila antaganden."),
            ("Kan vi börja med ett prov?", "Ja. För B2B-komponenter är ett prov ofta bästa starten eftersom det bekräftar kostnad, process och utförandenivå före en större serie."),
            ("Kan ni hantera packning och frakt?", "Ja, om komponent och omfattning är logistiskt rimliga. Packning, skydd och frakt avtalas efter att vi känner mått, material och antal."),
        ],
    },
    "da": {
        "title": "Hvornår kan det betale sig at bestille trækomponenter i kort serie? | Kajax",
        "description": "B2B-guide: hvornår en kort serie trækomponenter giver mening, hvornår en prototype er bedst, og hvilket materiale der skal bruges til tilbud.",
        "eyebrow": "B2B / korte serier",
        "h1": "Hvornår kan det betale sig at bestille trækomponenter i kort serie?",
        "lead": "En kort serie giver mening, når en virksomhed har brug for gentagelige trækomponenter, men ikke vil investere i egen snedkerkapacitet. Det tryggeste er ofte at starte med en prøve, referencedel eller lille første serie og gå videre til løbende bestillinger, når processen er afstemt.",
        "primary_cta": "Spørg om kort serie",
        "aside_title": "En kort serie passer når",
        "aside_body": "De stærkeste B2B-forespørgsler handler om komponenter, der kan beskrives tydeligt, gentages og pakkes eller sendes videre til montage på en fornuftig måde.",
        "aside_items": ["komponenten skal bestilles igen", "gentagelige mål er vigtige", "du har prøve, foto eller tegning", "du skal bruge en prøve før større serie", "egen produktion ikke kan betale sig"],
        "sections": [
            {"title": "Når komponenten vender tilbage i nye bestillinger", "body": "En kort serie giver størst værdi, når den første batch kan gentages uden at starte forfra hver gang. Så kan det betale sig at afstemme reference, tolerancer, finish og pakning.", "items": ["lister, profiler og rammer", "halvfabrikata i træ til videre montage", "POS-, display- og udstillingselementer", "detaljer til møbler eller interiører", "dele efter fast reference"]},
            {"title": "Når egen produktion er for dyr eller langsom", "body": "For mange virksomheder handler udfordringen ikke kun om træbearbejdning, men om plads, værktøj, tid og medarbejdere til en lille specialserie. Et eksternt værksted gør det muligt at teste et produkt uden at opbygge egen produktion.", "items": ["ingen egen snedkerproduktion", "for lille skala til industriproduktion", "behov for fleksibel testserie", "kort implementeringstid", "projektet kræver dialog om detaljer"]},
            {"title": "Når en prøve eller prototype er bedst først", "body": "En prøve mindsker risikoen, hvis komponenten senere skal gentages. Den hjælper med at bekræfte materiale, kanter, fræsninger, huller, farve og tolerancer før en større serie.", "items": ["ny komponent uden produktionshistorik", "synlig detalje vigtig for slutkunden", "usikkert materiale eller finish", "større serie planlagt efter test", "pakning og forsendelse skal kontrolleres"]},
        ],
        "avoid_title": "Når en serie måske ikke er det rigtige første skridt",
        "avoid_body": "Ikke alle opgaver skal planlægges som serie med det samme. Hvis projektet er en engangsdetalje, ændrer sig meget eller mangler mål, bør omfanget først præciseres.",
        "avoid_items": ["ingen mål, reference eller skala", "designet ændrer sig efter hver samtale", "en engangsdetalje kræver lang forberedelse", "komponentens brug er uklar", "tidsfristen er kortere end realistisk prøveforberedelse"],
        "faq": [
            ("Hvilket antal regnes som en kort serie?", "Der findes ingen fast grænse. Nogle gange er det få testdele, andre gange flere dusin eller mere. Vigtigere end antallet er, om komponenten kan gentages efter faste forudsætninger."),
            ("Kan vi starte med én prøve?", "Ja. For B2B-komponenter er en prøve ofte den bedste start, fordi den bekræfter pris, proces og udførelsesniveau før en større serie."),
            ("Kan pakning og forsendelse håndteres?", "Ja, hvis komponent og omfang giver logistisk mening. Pakning, beskyttelse og forsendelse aftales, når vi kender mål, materiale og antal."),
        ],
    },
    "no": {
        "title": "Når lønner det seg å bestille trekomponenter i kort serie? | Kajax",
        "description": "B2B-guide: når en kort serie trekomponenter gir mening, når en prototype er best og hva som bør sendes for vurdering.",
        "eyebrow": "B2B / korte serier",
        "h1": "Når lønner det seg å bestille trekomponenter i kort serie?",
        "lead": "En kort serie gir mening når en bedrift trenger repeterbare trekomponenter, men ikke vil investere i egen snekkerkapasitet. Det tryggeste er ofte å starte med en prøve, referansedel eller liten første serie og gå videre til faste bestillinger når prosessen fungerer.",
        "primary_cta": "Spør om kort serie",
        "aside_title": "En kort serie passer når",
        "aside_body": "De beste B2B-forespørslene gjelder komponenter som kan beskrives tydelig, repeteres og pakkes eller sendes videre til montering på en fornuftig måte.",
        "aside_items": ["komponenten skal bestilles igjen", "repeterbare mål er viktige", "du har prøve, bilde eller tegning", "du trenger prøve før større serie", "egen produksjon ikke lønner seg"],
        "sections": [
            {"title": "Når komponenten kommer tilbake i nye bestillinger", "body": "En kort serie gir størst verdi når første parti kan repeteres uten å starte på nytt hver gang. Da lønner det seg å avklare referanse, toleranser, overflate og pakking.", "items": ["lister, profiler og rammer", "halvfabrikata i tre for videre montering", "POS-, display- og utstillingselementer", "detaljer til møbler eller interiør", "deler etter stabil referanse"]},
            {"title": "Når egen produksjon ville vært for dyr eller treg", "body": "For mange bedrifter handler utfordringen ikke bare om trebearbeiding, men om plass, verktøy, tid og folk til en liten spesialserie. Et eksternt verksted gjør det mulig å teste et produkt uten å bygge egen produksjon.", "items": ["ingen egen snekkerproduksjon", "for liten skala for industriproduksjon", "behov for fleksibel testserie", "kort innføringstid", "prosjektet krever dialog om detaljer"]},
            {"title": "Når en prøve eller prototype er best først", "body": "En prøve reduserer risiko når komponenten senere skal repeteres. Den hjelper med å bekrefte materiale, kanter, fresing, hull, farge og toleranser før en større serie.", "items": ["ny komponent uten produksjonshistorikk", "synlig detalj viktig for sluttkunden", "usikkert materiale eller overflate", "større serie planlagt etter test", "pakking og frakt må kontrolleres"]},
        ],
        "avoid_title": "Når en serie kanskje ikke er riktig første steg",
        "avoid_body": "Ikke alle oppdrag bør planlegges som serie med en gang. Hvis prosjektet er en engangsdetalj, endrer seg mye eller mangler mål, bør omfanget først avklares.",
        "avoid_items": ["ingen mål, referanse eller skala", "designet endres etter hver samtale", "en engangsdetalj krever lang forberedelse", "bruken av komponenten er uklar", "fristen er kortere enn realistisk prøveforberedelse"],
        "faq": [
            ("Hvilket antall regnes som kort serie?", "Det finnes ingen fast grense. Noen ganger er det få testdeler, andre ganger flere titalls eller mer. Viktigere enn antallet er om komponenten kan repeteres etter stabile forutsetninger."),
            ("Kan vi starte med én prøve?", "Ja. For B2B-komponenter er en prøve ofte beste start fordi den bekrefter pris, prosess og utførelsesnivå før en større serie."),
            ("Kan pakking og frakt håndteres?", "Ja, hvis komponent og omfang gir logistisk mening. Pakking, beskyttelse og frakt avtales når vi kjenner mål, materiale og antall."),
        ],
    },
}

STAIRS_PRICING_GUIDE_PAGES = {
    "pl": {
        "title": "Schody drewniane: co wpływa na cenę i termin? | Kajax",
        "description": "Poradnik dla inwestorów z Pomorskiego: co wpływa na cenę i termin schodów drewnianych, jakie zdjęcia i wymiary przygotować do wyceny.",
        "eyebrow": "Stolarka budowlana / schody",
        "h1": "Schody drewniane: co wpływa na cenę i termin realizacji?",
        "lead": "Na cenę schodów wpływa nie tylko liczba stopni. Ważny jest układ, miejsce montażu, materiał, wykończenie, etap inwestycji i możliwość dokładnego pomiaru. Im szybciej znamy te dane, tym szybciej ocenimy realny zakres prac i termin.",
        "primary_cta": "Zapytaj o schody",
        "aside_title": "Do pierwszej rozmowy przygotuj",
        "aside_body": "Nie musisz mieć pełnego projektu. Na start wystarczą zdjęcia miejsca, orientacyjne wymiary i informacja, czy inwestycja jest w budowie, remoncie czy wymianie istniejących schodów.",
        "aside_items": ["miejscowość inwestycji", "zdjęcia otworu lub istniejących schodów", "wysokość kondygnacji i szerokość miejsca", "preferowany materiał lub kolor", "oczekiwany termin montażu"],
        "sections": [
            {"title": "Układ i wymiary schodów", "body": "Proste schody zwykle wycenia się łatwiej niż zabiegowe, z podestem albo z nietypowym biegiem. Znaczenie ma liczba stopni, szerokość, wysokość kondygnacji i to, ile miejsca jest na konstrukcję.", "items": ["schody proste, zabiegowe lub z podestem", "liczba stopni i wysokość kondygnacji", "szerokość biegu", "miejsce na policzki, konstrukcję i balustradę", "zdjęcia obecnego stanu"]},
            {"title": "Materiał, konstrukcja i wykończenie", "body": "Cena zmienia się wraz z gatunkiem drewna, grubością elementów, sposobem konstrukcji oraz wykończeniem. Inaczej planuje się same stopnie na konstrukcji metalowej, a inaczej pełne schody drewniane z balustradą.", "items": ["gatunek drewna i klasa materiału", "stopnie, podstopnice, policzki lub okładziny", "balustrada i detale widoczne", "olej, lakier, bejca lub kolor", "odporność na intensywne użytkowanie"]},
            {"title": "Etap inwestycji i montaż", "body": "Termin zależy od gotowości miejsca, możliwości pomiaru, dostępności materiału i kolejności prac na budowie. Najlepiej zgłosić temat zanim wykończenia zamkną dostęp do miejsc pomiarowych.", "items": ["czy są gotowe posadzki i ściany", "czy można wykonać pomiar", "czy schody mają pasować do innych elementów wnętrza", "termin wejścia innych ekip", "lokalizacja w Pomorskiem i dojazd"]},
        ],
        "avoid_title": "Co najczęściej opóźnia wycenę schodów",
        "avoid_body": "Najwięcej czasu tracimy, gdy trzeba zgadywać wymiary, etap budowy albo oczekiwany standard. Nawet proste zdjęcia z telefonu pomagają szybciej powiedzieć, czy temat jest do dalszej rozmowy.",
        "avoid_items": ["brak zdjęć miejsca montażu", "brak wysokości kondygnacji lub szerokości biegu", "niejasny zakres: same stopnie czy całe schody", "brak informacji o terminie i miejscowości", "oczekiwanie ceny bez ustalenia materiału"],
        "faq": [
            ("Czy do pierwszej wyceny wystarczą zdjęcia?", "Tak, zdjęcia wystarczą do wstępnej rozmowy, jeśli dodasz miejscowość, orientacyjne wymiary i informację, czy chodzi o nowe schody, okładzinę czy wymianę istniejących."),
            ("Kiedy najlepiej zgłosić schody do wyceny?", "Najlepiej zanim inwestycja wejdzie w końcowe wykończenia. Wtedy łatwiej zaplanować pomiar, konstrukcję i kolejność montażu."),
            ("Czy realizujecie schody poza okolicą Gościcina?", "Dla schodów i stolarki budowlanej priorytetem jest Pomorskie, okolice Wejherowa i Trójmiasta. Dalsze lokalizacje wymagają indywidualnej oceny."),
        ],
    },
    "en": {
        "title": "Wooden stairs: what affects price and lead time? | Kajax",
        "description": "Guide for investors: what affects the price and lead time of wooden stairs, and which photos and measurements help with the first quote.",
        "eyebrow": "Construction joinery / stairs",
        "h1": "Wooden stairs: what affects price and lead time?",
        "lead": "The price of wooden stairs is not determined only by the number of steps. Layout, installation site, material, finish, construction stage and measurement access all matter. The earlier these details are clear, the faster we can assess the real scope and timing.",
        "primary_cta": "Ask about stairs",
        "aside_title": "Prepare for the first conversation",
        "aside_body": "You do not need a complete design. Photos of the place, approximate dimensions and whether this is a build, renovation or replacement of existing stairs are enough to start.",
        "aside_items": ["project location", "photos of the opening or existing stairs", "floor-to-floor height and available width", "preferred material or colour", "expected installation timing"],
        "sections": [
            {"title": "Stair layout and dimensions", "body": "Straight stairs are usually easier to assess than winding stairs, stairs with a landing or unusual runs. The number of steps, width, floor-to-floor height and available structural space all matter.", "items": ["straight, winding or landing stairs", "number of steps and floor-to-floor height", "run width", "space for stringers, structure and railing", "photos of the current state"]},
            {"title": "Material, structure and finish", "body": "Price changes with wood species, element thickness, structure and finish. Treads on a metal structure are planned differently from full wooden stairs with railing.", "items": ["wood species and material grade", "treads, risers, stringers or cladding", "railing and visible details", "oil, varnish, stain or colour", "resistance to intensive use"]},
            {"title": "Project stage and installation", "body": "Timing depends on site readiness, measurement access, material availability and the sequence of works on site. It is best to raise the topic before final finishes block measurement points.", "items": ["whether floors and walls are ready", "whether precise measurement is possible", "whether stairs must match other interior elements", "timing of other trades", "location and access"]},
        ],
        "avoid_title": "What most often slows down stair pricing",
        "avoid_body": "Most delays come from missing dimensions, unclear building stage or unclear expected standard. Even simple phone photos help us say faster whether the topic is worth a detailed discussion.",
        "avoid_items": ["no photos of the installation area", "no floor-to-floor height or run width", "unclear scope: treads only or full stairs", "no timing or location", "expecting a price before material is defined"],
        "faq": [
            ("Are photos enough for the first quote?", "Yes, photos are enough for an initial conversation if you add location, approximate dimensions and whether you need new stairs, cladding or replacement of existing stairs."),
            ("When should I ask for stair pricing?", "Ideally before the project reaches final finishing. It is easier to plan measurement, structure and installation sequence then."),
            ("Do you install stairs outside the Gościcino area?", "For stairs and construction joinery, the priority is Pomerania, the Wejherowo area and the Tricity region. More distant locations are assessed individually."),
        ],
    },
    "de": {
        "title": "Holztreppen: was beeinflusst Preis und Termin? | Kajax",
        "description": "Leitfaden für Investoren: was Preis und Termin von Holztreppen beeinflusst und welche Fotos und Maße bei der ersten Anfrage helfen.",
        "eyebrow": "Bauschreinerei / Treppen",
        "h1": "Holztreppen: was beeinflusst Preis und Ausführungszeit?",
        "lead": "Der Preis einer Holztreppe hängt nicht nur von der Anzahl der Stufen ab. Entscheidend sind Grundriss, Einbauort, Material, Oberfläche, Bauphase und die Möglichkeit eines genauen Aufmaßes. Je früher diese Informationen klar sind, desto schneller lassen sich realer Umfang und Termin einschätzen.",
        "primary_cta": "Treppen anfragen",
        "aside_title": "Für das erste Gespräch vorbereiten",
        "aside_body": "Ein vollständiger Entwurf ist nicht nötig. Fotos des Ortes, ungefähre Maße und die aktuelle Bau- oder Renovierungsphase reichen für den Start.",
        "aside_items": ["Projektort", "Fotos der Öffnung oder vorhandenen Treppe", "Geschosshöhe und verfügbare Breite", "gewünschtes Material oder Farbe", "gewünschter Montagetermin"],
        "sections": [
            {"title": "Treppenform und Maße", "body": "Gerade Treppen lassen sich meist leichter einschätzen als gewendelte Treppen, Treppen mit Podest oder ungewöhnliche Läufe. Relevant sind Stufenzahl, Breite, Geschosshöhe und Platz für die Konstruktion.", "items": ["gerade, gewendelte Treppe oder Treppe mit Podest", "Stufenzahl und Geschosshöhe", "Laufbreite", "Platz für Wangen, Konstruktion und Geländer", "Fotos des aktuellen Zustands"]},
            {"title": "Material, Konstruktion und Oberfläche", "body": "Der Preis verändert sich je nach Holzart, Elementstärke, Konstruktion und Oberfläche. Einzelne Stufen auf Metallkonstruktion werden anders geplant als eine vollständige Holztreppe mit Geländer.", "items": ["Holzart und Materialklasse", "Stufen, Setzstufen, Wangen oder Verkleidungen", "Geländer und sichtbare Details", "Öl, Lack, Beize oder Farbton", "Beständigkeit bei intensiver Nutzung"]},
            {"title": "Bauphase und Montage", "body": "Der Termin hängt von der Bereitschaft des Ortes, Zugang zum Aufmaß, Materialverfügbarkeit und Reihenfolge der Arbeiten ab. Am besten wird das Thema gemeldet, bevor Endarbeiten Messpunkte verdecken.", "items": ["ob Böden und Wände fertig sind", "ob ein genaues Aufmaß möglich ist", "ob die Treppe zu anderen Innenelementen passen muss", "Termine anderer Gewerke", "Standort und Anfahrt"]},
        ],
        "avoid_title": "Was die Treppenanfrage meist verlangsamt",
        "avoid_body": "Die meiste Zeit geht verloren, wenn Maße, Bauphase oder erwarteter Standard fehlen. Selbst einfache Handyfotos helfen schneller einzuschätzen, ob das Thema weiter besprochen werden sollte.",
        "avoid_items": ["keine Fotos des Montageorts", "keine Geschosshöhe oder Laufbreite", "unklarer Umfang: nur Stufen oder ganze Treppe", "kein Termin und kein Standort", "Preisfrage ohne festgelegtes Material"],
        "faq": [
            ("Reichen Fotos für die erste Anfrage?", "Ja, Fotos reichen für das erste Gespräch, wenn Standort, ungefähre Maße und der Umfang ergänzt werden: neue Treppe, Verkleidung oder Austausch einer bestehenden Treppe."),
            ("Wann sollte eine Treppe angefragt werden?", "Am besten bevor das Projekt in die Endausführung geht. Dann lassen sich Aufmaß, Konstruktion und Montagereihenfolge leichter planen."),
            ("Montieren Sie Treppen außerhalb von Gościcino?", "Für Treppen und Bauschreinerei liegt der Schwerpunkt auf Pommern, Umgebung Wejherowo und Dreistadt. Weitere Orte werden individuell geprüft."),
        ],
    },
    "sv": {
        "title": "Trätrappor: vad påverkar pris och leveranstid? | Kajax",
        "description": "Guide för investerare: vad som påverkar pris och tidplan för trätrappor, och vilka foton och mått som hjälper inför offert.",
        "eyebrow": "Byggsnickeri / trappor",
        "h1": "Trätrappor: vad påverkar pris och leveranstid?",
        "lead": "Priset på en trätrappa beror inte bara på antalet steg. Planlösning, montageplats, material, finish, byggskede och möjlighet till noggrann mätning spelar stor roll. Ju tidigare detta är tydligt, desto snabbare kan verklig omfattning och tidplan bedömas.",
        "primary_cta": "Fråga om trappor",
        "aside_title": "Förbered inför första dialogen",
        "aside_body": "Du behöver inte ha komplett projektering. Foton av platsen, ungefärliga mått och information om bygg- eller renoveringsskede räcker för start.",
        "aside_items": ["projektplats", "foton av öppning eller befintlig trappa", "våningshöjd och tillgänglig bredd", "önskat material eller färg", "önskad tid för montage"],
        "sections": [
            {"title": "Trappans form och mått", "body": "Raka trappor är oftast enklare att bedöma än svängda trappor, trappor med vilplan eller ovanliga lösningar. Antal steg, bredd, våningshöjd och plats för konstruktion är viktigt.", "items": ["rak trappa, svängd trappa eller trappa med vilplan", "antal steg och våningshöjd", "trapploppets bredd", "plats för vangstycken, konstruktion och räcke", "foton av nuvarande skick"]},
            {"title": "Material, konstruktion och finish", "body": "Priset påverkas av träslag, dimensioner, konstruktion och ytbehandling. Steg på metallkonstruktion planeras annorlunda än en komplett trätrappa med räcke.", "items": ["träslag och materialklass", "steg, sättsteg, vangstycken eller beklädnad", "räcke och synliga detaljer", "olja, lack, bets eller färg", "tålighet vid intensiv användning"]},
            {"title": "Byggskede och montage", "body": "Tidplanen beror på platsens beredskap, möjlighet till mätning, materialtillgång och ordning mellan olika arbeten. Det är bäst att ta upp trappan innan slutfinish stänger mätpunkter.", "items": ["om golv och väggar är klara", "om exakt mätning är möjlig", "om trappan ska matcha andra inredningsdetaljer", "tidplan för andra yrkesgrupper", "plats och tillgänglighet"]},
        ],
        "avoid_title": "Vad som oftast bromsar offert på trappa",
        "avoid_body": "Mest tid går förlorad när mått, byggskede eller förväntad nivå saknas. Även enkla mobilbilder hjälper oss snabbare avgöra om projektet är värt en mer detaljerad dialog.",
        "avoid_items": ["inga foton av montageplatsen", "ingen våningshöjd eller bredd", "oklar omfattning: bara steg eller hel trappa", "ingen tidplan eller plats", "prisfråga utan valt material"],
        "faq": [
            ("Räcker foton för första offerten?", "Ja, foton räcker för första dialogen om du lägger till plats, ungefärliga mått och om det gäller ny trappa, beklädnad eller byte av befintlig trappa."),
            ("När bör man fråga om pris på trappa?", "Helst innan projektet går in i slutfinish. Då är det lättare att planera mätning, konstruktion och montageordning."),
            ("Monterar ni trappor utanför Gościcino?", "För trappor och byggsnickeri prioriteras Pommern, Wejherowo-området och Tricity. Andra platser bedöms individuellt."),
        ],
    },
    "da": {
        "title": "Trætrapper: hvad påvirker pris og leveringstid? | Kajax",
        "description": "Guide for investorer: hvad der påvirker pris og tidsplan for trætrapper, og hvilke fotos og mål der hjælper før tilbud.",
        "eyebrow": "Byggesnedkeri / trapper",
        "h1": "Trætrapper: hvad påvirker pris og leveringstid?",
        "lead": "Prisen på en trætrappe afhænger ikke kun af antallet af trin. Udformning, montagested, materiale, finish, byggefase og mulighed for præcis opmåling betyder meget. Jo tidligere oplysningerne er klare, desto hurtigere kan det reelle omfang og tidsplan vurderes.",
        "primary_cta": "Spørg om trapper",
        "aside_title": "Forbered til første dialog",
        "aside_body": "Du behøver ikke komplet projektering. Fotos af stedet, omtrentlige mål og information om bygge- eller renoveringsfase er nok til at starte.",
        "aside_items": ["projektets placering", "fotos af åbning eller eksisterende trappe", "etagehøjde og tilgængelig bredde", "ønsket materiale eller farve", "ønsket tidspunkt for montage"],
        "sections": [
            {"title": "Trappens form og mål", "body": "Lige trapper er normalt lettere at vurdere end drejede trapper, trapper med repos eller usædvanlige løsninger. Antal trin, bredde, etagehøjde og plads til konstruktion er vigtigt.", "items": ["lige trappe, drejet trappe eller trappe med repos", "antal trin og etagehøjde", "trappeløbets bredde", "plads til vanger, konstruktion og gelænder", "fotos af nuværende tilstand"]},
            {"title": "Materiale, konstruktion og finish", "body": "Prisen påvirkes af træsort, dimensioner, konstruktion og overfladebehandling. Trin på metalkonstruktion planlægges anderledes end en komplet trætrappe med gelænder.", "items": ["træsort og materialeklasse", "trin, stødtrin, vanger eller beklædning", "gelænder og synlige detaljer", "olie, lak, bejdse eller farve", "modstand ved intensiv brug"]},
            {"title": "Byggefase og montage", "body": "Tidsplanen afhænger af stedets klarhed, adgang til opmåling, materialetilgængelighed og rækkefølgen mellem fag. Det er bedst at tage trappen op, før slutfinish lukker for målepunkter.", "items": ["om gulve og vægge er klar", "om præcis opmåling er mulig", "om trappen skal passe til andre interiørdele", "tidsplan for andre fag", "placering og adgang"]},
        ],
        "avoid_title": "Hvad der oftest forsinker tilbud på trapper",
        "avoid_body": "Mest tid går tabt, når mål, byggefase eller forventet standard mangler. Selv enkle mobilfotos hjælper os hurtigere med at vurdere, om projektet bør drøftes mere detaljeret.",
        "avoid_items": ["ingen fotos af montagestedet", "ingen etagehøjde eller bredde", "uklart omfang: kun trin eller hel trappe", "ingen tidsplan eller placering", "prisforespørgsel uden valgt materiale"],
        "faq": [
            ("Er fotos nok til første tilbud?", "Ja, fotos er nok til første dialog, hvis du tilføjer placering, omtrentlige mål og om det gælder ny trappe, beklædning eller udskiftning af eksisterende trappe."),
            ("Hvornår bør man spørge om pris på trappe?", "Helst før projektet går ind i slutfinish. Så er det lettere at planlægge opmåling, konstruktion og montagerækkefølge."),
            ("Monterer I trapper uden for Gościcino?", "For trapper og byggesnedkeri prioriteres Pommern, Wejherowo-området og Tricity. Andre placeringer vurderes individuelt."),
        ],
    },
    "no": {
        "title": "Tretrapper: hva påvirker pris og leveringstid? | Kajax",
        "description": "Guide for investorer: hva som påvirker pris og tidsplan for tretrapper, og hvilke bilder og mål som hjelper før vurdering.",
        "eyebrow": "Byggsnekkerarbeid / trapper",
        "h1": "Tretrapper: hva påvirker pris og leveringstid?",
        "lead": "Prisen på en tretrapp bestemmes ikke bare av antall trinn. Utforming, monteringssted, materiale, overflate, byggefase og mulighet for nøyaktig oppmåling betyr mye. Jo tidligere dette er klart, desto raskere kan reelt omfang og tidsplan vurderes.",
        "primary_cta": "Spør om trapper",
        "aside_title": "Forbered til første dialog",
        "aside_body": "Du trenger ikke komplett prosjektering. Bilder av stedet, omtrentlige mål og informasjon om bygge- eller renoveringsfase er nok til å starte.",
        "aside_items": ["prosjektsted", "bilder av åpning eller eksisterende trapp", "etasjehøyde og tilgjengelig bredde", "ønsket materiale eller farge", "ønsket tidspunkt for montering"],
        "sections": [
            {"title": "Trappens form og mål", "body": "Rette trapper er vanligvis lettere å vurdere enn svingtrapper, trapper med repos eller uvanlige løsninger. Antall trinn, bredde, etasjehøyde og plass til konstruksjon er viktig.", "items": ["rett trapp, svingtrapp eller trapp med repos", "antall trinn og etasjehøyde", "trappeløpets bredde", "plass til vanger, konstruksjon og rekkverk", "bilder av nåværende tilstand"]},
            {"title": "Materiale, konstruksjon og overflate", "body": "Prisen påvirkes av treslag, dimensjoner, konstruksjon og overflatebehandling. Trinn på metallkonstruksjon planlegges annerledes enn en komplett tretrapp med rekkverk.", "items": ["treslag og materialklasse", "trinn, opptrinn, vanger eller kledning", "rekkverk og synlige detaljer", "olje, lakk, beis eller farge", "motstand ved intensiv bruk"]},
            {"title": "Byggefase og montering", "body": "Tidsplanen avhenger av hvor klart stedet er, tilgang til oppmåling, materialtilgang og rekkefølgen mellom fag. Det er best å ta opp trappen før sluttfinish stenger målepunkter.", "items": ["om gulv og vegger er klare", "om presis oppmåling er mulig", "om trappen skal passe til andre interiørdeler", "tidsplan for andre fag", "plassering og tilgang"]},
        ],
        "avoid_title": "Hva som oftest forsinker vurdering av trapper",
        "avoid_body": "Mest tid går tapt når mål, byggefase eller forventet standard mangler. Selv enkle mobilbilder hjelper oss raskere å vurdere om prosjektet bør diskuteres mer detaljert.",
        "avoid_items": ["ingen bilder av monteringsstedet", "ingen etasjehøyde eller bredde", "uklart omfang: bare trinn eller hel trapp", "ingen tidsplan eller plassering", "prisforespørsel uten valgt materiale"],
        "faq": [
            ("Er bilder nok for første vurdering?", "Ja, bilder er nok for første dialog hvis du legger til sted, omtrentlige mål og om det gjelder ny trapp, kledning eller utskifting av eksisterende trapp."),
            ("Når bør man spørre om pris på trapp?", "Helst før prosjektet går inn i sluttfinish. Da er det lettere å planlegge oppmåling, konstruksjon og monteringsrekkefølge."),
            ("Monterer dere trapper utenfor Gościcino?", "For trapper og byggsnekkerarbeid prioriteres Pommern, Wejherowo-området og Tricity. Andre steder vurderes individuelt."),
        ],
    },
}

ADVERTISING_EVENT_GUIDE_PAGES = {
    "pl": {
        "title": "Elementy drewniane dla firm reklamowych i eventowych | Kajax",
        "description": "Drewniane elementy POS, displaye, ekspozytory, prototypy i krótkie serie dla firm reklamowych, eventowych i wystawienniczych.",
        "eyebrow": "B2B / reklama / eventy",
        "h1": "Elementy drewniane dla firm reklamowych i eventowych",
        "lead": "Drewno dobrze działa tam, gdzie ekspozycja, stoisko albo element marki ma wyglądać solidniej, cieplej i bardziej premium niż typowy nośnik z tworzywa. Wykonujemy prototypy, krótkie serie i powtarzalne elementy na podstawie zdjęcia, rysunku, wzoru albo specyfikacji.",
        "primary_cta": "Zapytaj o elementy reklamowe",
        "aside_title": "Najlepsze zapytania mają",
        "aside_body": "Przy projektach reklamowych najważniejszy jest termin, skala i jasny opis efektu. Jeśli element ma jechać na event albo do punktów sprzedaży, od razu warto ocenić pakowanie, transport i odporność użytkową.",
        "aside_items": ["wizualizację, szkic lub zdjęcie referencyjne", "liczbę sztuk i termin eventu", "wymiary oraz sposób użycia", "informację, co będzie widoczne dla klienta", "wymagania pakowania lub transportu"],
        "sections": [
            {"title": "Kiedy drewno ma sens w reklamie i POS", "body": "Drewno warto rozważyć, gdy element ma budować lepsze wrażenie marki, wracać w kolejnych kampaniach albo działać jako detal w ekspozycji premium. Najlepiej sprawdzają się projekty opisane wymiarem, materiałem i sposobem montażu.", "items": ["ekspozytory i displaye", "podstawki, ramy i elementy ekspozycji", "detale do stoisk i scenografii", "drewniane nośniki oznaczeń", "elementy do krótkiej serii kampanijnej"]},
            {"title": "Prototyp, próbka i krótka seria", "body": "Przy kampaniach i eventach często najlepszym początkiem jest prototyp albo pierwsza mała partia. Pozwala to sprawdzić proporcje, stabilność, wykończenie, widoczne krawędzie oraz to, czy element da się rozsądnie pakować.", "items": ["pierwszy wzór do akceptacji", "dopasowanie materiału i koloru", "test stabilności lub montażu", "krótka seria po akceptacji próbki", "możliwość powtarzania w kolejnych kampaniach"]},
            {"title": "Co wpływa na termin i koszt", "body": "Największe znaczenie mają: ilość, wymiar, złożoność kształtu, wykończenie oraz data wydarzenia. Przy większych lub delikatnych elementach trzeba też ocenić, czy pakowanie i wysyłka są realne w założonym terminie.", "items": ["liczba sztuk i docelowy termin", "czy element jest płaski, przestrzenny czy składany", "widoczne strony i standard wykończenia", "otwory, frezy, logo lub dodatkowe detale", "pakowanie, odbiór albo wysyłka"]},
        ],
        "avoid_title": "Co może zablokować szybkie wdrożenie",
        "avoid_body": "Najtrudniejsze są projekty z bardzo krótkim terminem, bez wymiarów albo z założeniami, których nie da się sprawdzić przed produkcją. Lepiej wysłać niedoskonały szkic niż tylko ogólny opis kampanii.",
        "avoid_items": ["brak wymiarów i liczby sztuk", "termin eventu bez zapasu na próbkę", "niejasne obciążenie lub sposób montażu", "duży element bez planu transportu", "brak informacji, które powierzchnie są widoczne"],
        "faq": [
            ("Czy możecie pracować na wizualizacji od agencji?", "Tak. Wizualizacja, szkic lub zdjęcie referencyjne wystarczą do pierwszej rozmowy, jeśli dodasz wymiary, liczbę sztuk i termin."),
            ("Czy robicie pojedynczy prototyp przed serią?", "Tak. Przy elementach POS i eventowych prototyp często jest najlepszym sposobem sprawdzenia proporcji, stabilności i wykończenia."),
            ("Czy możliwa jest wysyłka elementów na event?", "Tak, jeśli element i termin mają sens logistycznie. Pakowanie, zabezpieczenie i wysyłkę ustalamy indywidualnie po poznaniu projektu."),
        ],
    },
    "en": {
        "title": "Wooden components for advertising and event companies | Kajax",
        "description": "Wooden POS elements, displays, prototypes and short runs for advertising, event and exhibition companies.",
        "eyebrow": "B2B / advertising / events",
        "h1": "Wooden components for advertising and event companies",
        "lead": "Wood works well when a display, stand or brand element should feel more solid, warmer and more premium than a typical plastic carrier. We make prototypes, short runs and repeatable components based on a photo, drawing, sample or specification.",
        "primary_cta": "Ask about advertising components",
        "aside_title": "The best inquiries include",
        "aside_body": "For advertising projects, timing, scale and a clear description of the intended effect matter most. If the component is going to an event or retail locations, packing, transport and usage durability should be considered from the start.",
        "aside_items": ["visual, sketch or reference photo", "quantity and event deadline", "dimensions and use case", "which surfaces will be visible", "packing or transport requirements"],
        "sections": [
            {"title": "When wood makes sense in advertising and POS", "body": "Wood is worth considering when the element should improve brand perception, return in future campaigns or work as a premium display detail. The best projects are described by dimensions, material and assembly method.", "items": ["displays and POS elements", "bases, frames and exhibition details", "stand and scenery components", "wooden sign carriers", "short campaign production runs"]},
            {"title": "Prototype, sample and short run", "body": "For campaigns and events, the best first step is often a prototype or a first small batch. It helps confirm proportions, stability, finish, visible edges and whether the component can be packed sensibly.", "items": ["first sample for approval", "material and colour alignment", "stability or assembly test", "short run after sample approval", "repeatability for future campaigns"]},
            {"title": "What affects timing and cost", "body": "Quantity, size, shape complexity, finish and event date matter most. Larger or delicate components also require checking whether packing and shipping are realistic within the timeline.", "items": ["quantity and target deadline", "flat, spatial or foldable element", "visible sides and finish standard", "holes, milling, logo or extra details", "packing, pickup or shipping"]},
        ],
        "avoid_title": "What can block a fast launch",
        "avoid_body": "The hardest projects are those with a very short deadline, no dimensions or assumptions that cannot be tested before production. An imperfect sketch is more useful than a general campaign description.",
        "avoid_items": ["no dimensions or quantity", "event deadline without time for a sample", "unclear load or assembly method", "large component without transport plan", "no information about visible surfaces"],
        "faq": [
            ("Can you work from an agency visual?", "Yes. A visual, sketch or reference photo is enough for the first conversation if you add dimensions, quantity and deadline."),
            ("Can you make one prototype before the run?", "Yes. For POS and event components, a prototype is often the best way to check proportions, stability and finish."),
            ("Can components be shipped to an event?", "Yes, if the component and timing make logistical sense. Packing, protection and shipping are agreed individually after we understand the project."),
        ],
    },
    "de": {
        "title": "Holzelemente für Werbe- und Eventfirmen | Kajax",
        "description": "Holzelemente für POS, Displays, Prototypen und Kleinserien für Werbe-, Event- und Messefirmen.",
        "eyebrow": "B2B / Werbung / Events",
        "h1": "Holzelemente für Werbe- und Eventfirmen",
        "lead": "Holz funktioniert dort gut, wo ein Display, Stand oder Markenelement solider, wärmer und hochwertiger wirken soll als ein typischer Kunststoffträger. Wir fertigen Prototypen, Kleinserien und wiederholbare Elemente nach Foto, Zeichnung, Muster oder Spezifikation.",
        "primary_cta": "Werbeelemente anfragen",
        "aside_title": "Gute Anfragen enthalten",
        "aside_body": "Bei Werbeprojekten zählen Termin, Umfang und eine klare Beschreibung des gewünschten Effekts. Wenn das Element zu einem Event muss, sollten Verpackung und Transport früh mitgedacht werden.",
        "aside_items": ["Visualisierung, Skizze oder Referenzfoto", "Menge und Eventtermin", "Maße und Nutzung", "sichtbare Flächen", "Anforderungen an Verpackung oder Transport"],
        "sections": [
            {"title": "Wann Holz in Werbung und POS sinnvoll ist", "body": "Holz lohnt sich, wenn ein Element die Markenwirkung verbessert, wiederholbar sein soll oder als hochwertiges Displaydetail dient. Am besten sind Projekte, die sich über Maße, Material und Montageart beschreiben lassen.", "items": ["Displays und POS-Elemente", "Sockel, Rahmen und Ausstellungsteile", "Stand- und Szenografieelemente", "Holzträger für Beschriftung", "Kleinserien für Kampagnen"]},
            {"title": "Prototyp, Muster und Kleinserie", "body": "Bei Kampagnen und Events ist ein Prototyp oder eine kleine erste Serie oft der beste Start. So lassen sich Proportionen, Stabilität, Oberfläche, sichtbare Kanten und Verpackbarkeit prüfen.", "items": ["erstes Muster zur Freigabe", "Abstimmung von Material und Farbe", "Test von Stabilität oder Montage", "Kleinserie nach Musterfreigabe", "Wiederholbarkeit für weitere Kampagnen"]},
            {"title": "Was Termin und Kosten beeinflusst", "body": "Menge, Größe, Formkomplexität, Oberfläche und Eventdatum sind entscheidend. Bei größeren oder empfindlichen Elementen muss zusätzlich geprüft werden, ob Verpackung und Versand im Termin realistisch sind.", "items": ["Menge und Zieltermin", "flaches, räumliches oder klappbares Element", "sichtbare Seiten und Oberflächenstandard", "Bohrungen, Fräsungen, Logo oder Zusatzdetails", "Verpackung, Abholung oder Versand"]},
        ],
        "avoid_title": "Was eine schnelle Umsetzung blockieren kann",
        "avoid_body": "Schwierig sind Projekte mit sehr kurzem Termin, ohne Maße oder mit Annahmen, die vor der Fertigung nicht geprüft werden können. Eine einfache Skizze ist hilfreicher als eine allgemeine Kampagnenbeschreibung.",
        "avoid_items": ["keine Maße und keine Menge", "Eventtermin ohne Zeit für ein Muster", "unklare Belastung oder Montageart", "großes Element ohne Transportplan", "keine Angabe zu sichtbaren Flächen"],
        "faq": [
            ("Können Sie nach einer Agenturvisualisierung arbeiten?", "Ja. Visualisierung, Skizze oder Referenzfoto reichen für die erste Abstimmung, wenn Maße, Menge und Termin ergänzt werden."),
            ("Fertigen Sie einen Prototyp vor der Serie?", "Ja. Bei POS- und Eventelementen ist ein Prototyp oft der beste Weg, um Proportionen, Stabilität und Oberfläche zu prüfen."),
            ("Ist Versand zu einem Event möglich?", "Ja, wenn Element und Termin logistisch sinnvoll sind. Verpackung, Schutz und Versand werden nach Prüfung des Projekts individuell abgestimmt."),
        ],
    },
    "sv": {
        "title": "Träkomponenter för reklam- och eventföretag | Kajax",
        "description": "Träkomponenter för POS, displayer, prototyper och korta serier för reklam-, event- och utställningsföretag.",
        "eyebrow": "B2B / reklam / event",
        "h1": "Träkomponenter för reklam- och eventföretag",
        "lead": "Trä fungerar bra när en display, monter eller varumärkesdetalj ska kännas mer gedigen, varm och premium än en vanlig plastbärare. Vi tillverkar prototyper, korta serier och återkommande komponenter efter foto, ritning, prov eller specifikation.",
        "primary_cta": "Fråga om reklamkomponenter",
        "aside_title": "Bra förfrågningar innehåller",
        "aside_body": "För reklamprojekt är tidplan, omfattning och tydlig effektbeskrivning viktigast. Om komponenten ska till ett event behöver packning och transport bedömas tidigt.",
        "aside_items": ["visualisering, skiss eller referensfoto", "antal och eventdeadline", "mått och användning", "vilka ytor som är synliga", "krav på packning eller transport"],
        "sections": [
            {"title": "När trä passar i reklam och POS", "body": "Trä är värt att välja när detaljen ska stärka varumärkesintrycket, kunna upprepas eller fungera som premiumdetalj i exponering. Bäst är projekt som kan beskrivas med mått, material och montage.", "items": ["displayer och POS-element", "baser, ramar och utställningsdetaljer", "monter- och scenografidetaljer", "träbärare för skyltning", "korta serier för kampanjer"]},
            {"title": "Prototyp, prov och kort serie", "body": "För kampanjer och event är en prototyp eller liten första serie ofta bästa starten. Den visar proportioner, stabilitet, finish, synliga kanter och om detaljen kan packas rimligt.", "items": ["första prov för godkännande", "material- och färgavstämning", "test av stabilitet eller montage", "kort serie efter godkänt prov", "upprepning i kommande kampanjer"]},
            {"title": "Vad påverkar tid och kostnad", "body": "Antal, storlek, formens komplexitet, finish och eventdatum påverkar mest. Större eller känsliga delar kräver också kontroll av packning och frakt inom tidplanen.", "items": ["antal och måltermin", "platt, rumslig eller hopfällbar komponent", "synliga sidor och finishnivå", "hål, fräsningar, logotyp eller extra detaljer", "packning, upphämtning eller frakt"]},
        ],
        "avoid_title": "Vad kan stoppa snabb produktion",
        "avoid_body": "Svårast är projekt med mycket kort tid, utan mått eller med antaganden som inte kan testas före produktion. En enkel skiss är bättre än en allmän kampanjbeskrivning.",
        "avoid_items": ["inga mått eller antal", "eventdeadline utan tid för prov", "oklar belastning eller montering", "stor komponent utan transportplan", "ingen information om synliga ytor"],
        "faq": [
            ("Kan ni arbeta från en visualisering från byrån?", "Ja. Visualisering, skiss eller referensfoto räcker för första dialogen om du lägger till mått, antal och deadline."),
            ("Kan ni göra en prototyp före serien?", "Ja. För POS- och eventkomponenter är prototyp ofta bästa sättet att testa proportioner, stabilitet och finish."),
            ("Kan komponenter skickas till ett event?", "Ja, om komponent och tidplan är logistiskt rimliga. Packning, skydd och frakt avtalas individuellt efter att vi känner projektet."),
        ],
    },
    "da": {
        "title": "Trækomponenter til reklame- og eventfirmaer | Kajax",
        "description": "Trækomponenter til POS, displays, prototyper og korte serier for reklame-, event- og udstillingsfirmaer.",
        "eyebrow": "B2B / reklame / events",
        "h1": "Trækomponenter til reklame- og eventfirmaer",
        "lead": "Træ fungerer godt, når en display, stand eller branddetalje skal føles mere solid, varm og premium end en typisk plastbærer. Vi fremstiller prototyper, korte serier og gentagelige komponenter efter foto, tegning, prøve eller specifikation.",
        "primary_cta": "Spørg om reklamekomponenter",
        "aside_title": "Gode forespørgsler indeholder",
        "aside_body": "For reklameprojekter er tidsplan, omfang og en tydelig beskrivelse af effekten vigtigst. Hvis komponenten skal til et event, bør pakning og transport vurderes fra starten.",
        "aside_items": ["visualisering, skitse eller referencefoto", "antal og eventdeadline", "mål og brug", "hvilke flader der er synlige", "krav til pakning eller transport"],
        "sections": [
            {"title": "Hvornår træ giver mening i reklame og POS", "body": "Træ er værd at vælge, når elementet skal styrke brandindtrykket, kunne gentages eller fungere som en premiumdetalje i en udstilling. De bedste projekter kan beskrives med mål, materiale og montage.", "items": ["displays og POS-elementer", "baser, rammer og udstillingsdetaljer", "stand- og scenografidele", "træbærere til skiltning", "korte serier til kampagner"]},
            {"title": "Prototype, prøve og kort serie", "body": "Ved kampagner og events er en prototype eller lille første serie ofte den bedste start. Den viser proportioner, stabilitet, finish, synlige kanter og om elementet kan pakkes fornuftigt.", "items": ["første prøve til godkendelse", "afstemning af materiale og farve", "test af stabilitet eller montage", "kort serie efter godkendt prøve", "gentagelse i kommende kampagner"]},
            {"title": "Hvad påvirker tid og pris", "body": "Antal, størrelse, formens kompleksitet, finish og eventdato betyder mest. Større eller sarte dele kræver også vurdering af pakning og forsendelse inden for tidsplanen.", "items": ["antal og måltermin", "flad, rumlig eller foldbar komponent", "synlige sider og finishniveau", "huller, fræsninger, logo eller ekstra detaljer", "pakning, afhentning eller forsendelse"]},
        ],
        "avoid_title": "Hvad kan blokere hurtig produktion",
        "avoid_body": "De sværeste projekter har meget kort tid, ingen mål eller antagelser, der ikke kan testes før produktion. En enkel skitse er bedre end en generel kampagnebeskrivelse.",
        "avoid_items": ["ingen mål eller antal", "eventdeadline uden tid til prøve", "uklar belastning eller montage", "stor komponent uden transportplan", "ingen information om synlige flader"],
        "faq": [
            ("Kan I arbejde ud fra en visualisering fra bureauet?", "Ja. Visualisering, skitse eller referencefoto er nok til første dialog, hvis du tilføjer mål, antal og deadline."),
            ("Kan I lave en prototype før serien?", "Ja. For POS- og eventkomponenter er en prototype ofte den bedste måde at teste proportioner, stabilitet og finish."),
            ("Kan komponenter sendes til et event?", "Ja, hvis komponent og tidsplan giver logistisk mening. Pakning, beskyttelse og forsendelse aftales individuelt efter projektgennemgang."),
        ],
    },
    "no": {
        "title": "Trekomponenter for reklame- og eventbedrifter | Kajax",
        "description": "Trekomponenter for POS, displayer, prototyper og korte serier for reklame-, event- og utstillingsbedrifter.",
        "eyebrow": "B2B / reklame / event",
        "h1": "Trekomponenter for reklame- og eventbedrifter",
        "lead": "Tre fungerer godt når en display, stand eller merkevaredetalj skal føles mer solid, varm og premium enn en vanlig plastbærer. Vi lager prototyper, korte serier og repeterbare komponenter etter bilde, tegning, prøve eller spesifikasjon.",
        "primary_cta": "Spør om reklamekomponenter",
        "aside_title": "Gode forespørsler inneholder",
        "aside_body": "For reklameprosjekter er tidsplan, omfang og en tydelig beskrivelse av ønsket effekt viktigst. Hvis komponenten skal til et event, bør pakking og transport vurderes fra start.",
        "aside_items": ["visualisering, skisse eller referansebilde", "antall og eventfrist", "mål og bruk", "hvilke flater som er synlige", "krav til pakking eller transport"],
        "sections": [
            {"title": "Når tre passer i reklame og POS", "body": "Tre er verdt å velge når elementet skal styrke merkevareinntrykket, kunne repeteres eller fungere som en premiumdetalj i en utstilling. De beste prosjektene kan beskrives med mål, materiale og montering.", "items": ["displayer og POS-elementer", "baser, rammer og utstillingsdetaljer", "stand- og scenografideler", "trebærere for skilt", "korte serier for kampanjer"]},
            {"title": "Prototype, prøve og kort serie", "body": "Ved kampanjer og eventer er en prototype eller liten første serie ofte beste start. Den viser proporsjoner, stabilitet, overflate, synlige kanter og om elementet kan pakkes fornuftig.", "items": ["første prøve for godkjenning", "avklaring av materiale og farge", "test av stabilitet eller montering", "kort serie etter godkjent prøve", "gjentakelse i kommende kampanjer"]},
            {"title": "Hva påvirker tid og pris", "body": "Antall, størrelse, formens kompleksitet, overflate og eventdato betyr mest. Større eller skjøre deler krever også vurdering av pakking og frakt innenfor tidsplanen.", "items": ["antall og målfrist", "flat, romlig eller sammenleggbar komponent", "synlige sider og finishnivå", "hull, fresing, logo eller ekstra detaljer", "pakking, henting eller frakt"]},
        ],
        "avoid_title": "Hva kan stoppe rask produksjon",
        "avoid_body": "De vanskeligste prosjektene har veldig kort tid, ingen mål eller antakelser som ikke kan testes før produksjon. En enkel skisse er bedre enn en generell kampanjebeskrivelse.",
        "avoid_items": ["ingen mål eller antall", "eventfrist uten tid til prøve", "uklar belastning eller montering", "stor komponent uten transportplan", "ingen informasjon om synlige flater"],
        "faq": [
            ("Kan dere jobbe ut fra en visualisering fra byrået?", "Ja. Visualisering, skisse eller referansebilde er nok for første dialog hvis du legger til mål, antall og frist."),
            ("Kan dere lage en prototype før serien?", "Ja. For POS- og eventkomponenter er en prototype ofte beste måte å teste proporsjoner, stabilitet og overflate."),
            ("Kan komponenter sendes til et event?", "Ja, hvis komponent og tidsplan gir logistisk mening. Pakking, beskyttelse og frakt avtales individuelt etter prosjektgjennomgang."),
        ],
    },
}

for _code, _page in GUIDE_PAGES.items():
    CONTENT[_code]["pages"]["guide"] = _page

for _code, _page in SHORT_SERIES_GUIDE_PAGES.items():
    CONTENT[_code]["pages"]["short_series"] = _page

for _code, _page in STAIRS_PRICING_GUIDE_PAGES.items():
    CONTENT[_code]["pages"]["stairs_pricing"] = _page

for _code, _page in ADVERTISING_EVENT_GUIDE_PAGES.items():
    CONTENT[_code]["pages"]["advertising_events"] = _page

RELATED_LINK_SECTIONS = {
    "pl": {
        "production": {
            "related_eyebrow": "Poradniki B2B",
            "related_title": "Jak szybciej przejść od pomysłu do wyceny",
            "related_links": [
                {"page": "short_series", "eyebrow": "Krótkie serie", "title": "Kiedy opłaca się zamówić elementy drewniane w krótkiej serii?", "body": "Sprawdź, kiedy warto zacząć od próbki, małej partii albo powtarzalnego procesu."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Minimum informacji, które pomaga szybciej ocenić projekt B2B albo nietypowy detal."},
            ],
        },
        "guide": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Jeśli temat dotyczy elementów dla firmy",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "Kiedy krótka seria ma sens?", "body": "Poradnik dla firm, które rozważają próbkę, pierwszą partię lub stałą współpracę."},
                {"page": "production", "eyebrow": "Oferta", "title": "Elementy drewniane dla firm", "body": "Zobacz zakres produkcji B2B, półproduktów i elementów według wzoru."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Przygotuj temat do rozmowy",
            "related_links": [
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Co wysłać, żeby szybciej dostać konkretną odpowiedź."},
                {"page": "production", "eyebrow": "Oferta", "title": "Produkcja elementów drewnianych", "body": "Zakres prac dla firm, krótkich serii i drewnianych półproduktów."},
            ],
        },
    },
    "en": {
        "production": {
            "related_eyebrow": "B2B guides",
            "related_title": "How to move from idea to pricing faster",
            "related_links": [
                {"page": "short_series", "eyebrow": "Short runs", "title": "When does a short run of wooden components pay off?", "body": "See when to start with a sample, first batch or repeatable process."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "The minimum input that helps assess a B2B or unusual project faster."},
            ],
        },
        "guide": {
            "related_eyebrow": "Next step",
            "related_title": "If the project concerns components for a company",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "When does a short run make sense?", "body": "A guide for companies considering a sample, first batch or recurring cooperation."},
                {"page": "production", "eyebrow": "Offer", "title": "Wooden components for companies", "body": "See the scope of B2B production, semi-finished parts and sample-based components."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Next step",
            "related_title": "Prepare the project for discussion",
            "related_links": [
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "What to send to get a concrete answer faster."},
                {"page": "production", "eyebrow": "Offer", "title": "Wooden component production", "body": "Scope for companies, short runs and wooden semi-finished parts."},
            ],
        },
    },
    "de": {
        "production": {
            "related_eyebrow": "B2B-Leitfäden",
            "related_title": "Schneller von der Idee zur Anfrage",
            "related_links": [
                {"page": "short_series", "eyebrow": "Kleinserien", "title": "Wann lohnt sich eine Kleinserie von Holzelementen?", "body": "Wann Muster, erste Partie oder wiederholbarer Prozess sinnvoll sind."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Das Minimum an Informationen für eine schnellere Einschätzung."},
            ],
        },
        "guide": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Wenn es um Elemente für Unternehmen geht",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "Wann ist eine Kleinserie sinnvoll?", "body": "Ein Leitfaden für Muster, erste Serien und wiederkehrende Zusammenarbeit."},
                {"page": "production", "eyebrow": "Angebot", "title": "Holzelemente für Unternehmen", "body": "Umfang für B2B-Fertigung, Halbzeuge und Elemente nach Muster."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Projekt für die Anfrage vorbereiten",
            "related_links": [
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Was Sie senden sollten, um schneller eine konkrete Antwort zu bekommen."},
                {"page": "production", "eyebrow": "Angebot", "title": "Fertigung von Holzelementen", "body": "Leistungsumfang für Firmen, Kleinserien und Holz-Halbzeuge."},
            ],
        },
    },
    "sv": {
        "production": {
            "related_eyebrow": "B2B-guider",
            "related_title": "Snabbare från idé till offert",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korta serier", "title": "När lönar sig en kort serie träkomponenter?", "body": "När prov, första serie eller återkommande process är rätt väg."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Minsta underlag som hjälper oss bedöma projektet snabbare."},
            ],
        },
        "guide": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Om projektet gäller komponenter för företag",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "När är en kort serie rimlig?", "body": "Guide för prov, första serie och återkommande samarbete."},
                {"page": "production", "eyebrow": "Erbjudande", "title": "Träkomponenter för företag", "body": "Omfattning för B2B-produktion, halvfabrikat och komponenter efter prov."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Förbered projektet för dialog",
            "related_links": [
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Vad du bör skicka för att få ett konkret svar snabbare."},
                {"page": "production", "eyebrow": "Erbjudande", "title": "Produktion av träkomponenter", "body": "Omfattning för företag, korta serier och halvfabrikat i trä."},
            ],
        },
    },
    "da": {
        "production": {
            "related_eyebrow": "B2B-guides",
            "related_title": "Hurtigere fra idé til tilbud",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Hvornår kan en kort serie trækomponenter betale sig?", "body": "Hvornår prøve, første serie eller gentagelig proces er den rigtige vej."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Minimumsgrundlaget der hjælper os med at vurdere projektet hurtigere."},
            ],
        },
        "guide": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Hvis projektet handler om komponenter til virksomheder",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "Hvornår giver en kort serie mening?", "body": "Guide til prøve, første serie og løbende samarbejde."},
                {"page": "production", "eyebrow": "Tilbud", "title": "Trækomponenter til virksomheder", "body": "Omfang for B2B-produktion, halvfabrikata og komponenter efter prøve."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Forbered projektet til dialog",
            "related_links": [
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Hvad du bør sende for at få et konkret svar hurtigere."},
                {"page": "production", "eyebrow": "Tilbud", "title": "Produktion af trækomponenter", "body": "Omfang for virksomheder, korte serier og halvfabrikata i træ."},
            ],
        },
    },
    "no": {
        "production": {
            "related_eyebrow": "B2B-guider",
            "related_title": "Raskere fra idé til vurdering",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Når lønner en kort serie trekomponenter seg?", "body": "Når prøve, første serie eller repeterbar prosess er riktig vei."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Minimumsgrunnlaget som hjelper oss å vurdere prosjektet raskere."},
            ],
        },
        "guide": {
            "related_eyebrow": "Neste steg",
            "related_title": "Hvis prosjektet gjelder komponenter for bedrifter",
            "related_links": [
                {"page": "short_series", "eyebrow": "B2B", "title": "Når gir en kort serie mening?", "body": "Guide for prøve, første serie og fast samarbeid."},
                {"page": "production", "eyebrow": "Tilbud", "title": "Trekomponenter for bedrifter", "body": "Omfang for B2B-produksjon, halvfabrikata og komponenter etter prøve."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Neste steg",
            "related_title": "Forbered prosjektet for dialog",
            "related_links": [
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Hva du bør sende for å få et konkret svar raskere."},
                {"page": "production", "eyebrow": "Tilbud", "title": "Produksjon av trekomponenter", "body": "Omfang for bedrifter, korte serier og halvfabrikata i tre."},
            ],
        },
    },
}

for _code, _pages in RELATED_LINK_SECTIONS.items():
    for _page_key, _data in _pages.items():
        CONTENT[_code]["pages"][_page_key].update(_data)

STAIRS_RELATED_LINK_SECTIONS = {
    "pl": {
        "construction": {
            "related_eyebrow": "Poradniki stolarki budowlanej",
            "related_title": "Jak przygotować temat schodów i elementów montowanych",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Schody", "title": "Co wpływa na cenę i termin schodów drewnianych?", "body": "Najważniejsze dane do pierwszej rozmowy o schodach, pomiarze i montażu."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Checklista informacji, które przyspieszają odpowiedź przed wyceną."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Przygotuj zapytanie do wyceny",
            "related_links": [
                {"page": "construction", "eyebrow": "Oferta", "title": "Stolarka budowlana", "body": "Schody, drzwi, listwy i elementy drewniane na wymiar dla inwestycji lokalnych."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Co wysłać, żeby szybciej dostać konkretną odpowiedź."},
            ],
        },
    },
    "en": {
        "construction": {
            "related_eyebrow": "Construction joinery guides",
            "related_title": "How to prepare stairs and installed joinery topics",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Stairs", "title": "What affects the price and lead time of wooden stairs?", "body": "Key details for the first conversation about stairs, measurement and installation."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "A checklist of information that speeds up the first response."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Next step",
            "related_title": "Prepare the quote inquiry",
            "related_links": [
                {"page": "construction", "eyebrow": "Offer", "title": "Construction joinery", "body": "Stairs, doors, trims and wooden elements made to measure for local projects."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "What to send to get a concrete answer faster."},
            ],
        },
    },
    "de": {
        "construction": {
            "related_eyebrow": "Leitfäden zur Bauschreinerei",
            "related_title": "Treppen und montierte Holzarbeiten vorbereiten",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Treppen", "title": "Was beeinflusst Preis und Termin von Holztreppen?", "body": "Wichtige Angaben für die erste Abstimmung zu Treppe, Aufmaß und Montage."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Checkliste mit Informationen, die eine erste Antwort beschleunigen."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Anfrage für die Preisfindung vorbereiten",
            "related_links": [
                {"page": "construction", "eyebrow": "Angebot", "title": "Bauschreinerei", "body": "Treppen, Türen, Leisten und Holzelemente nach Maß für lokale Projekte."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Was Sie senden sollten, um schneller eine konkrete Antwort zu bekommen."},
            ],
        },
    },
    "sv": {
        "construction": {
            "related_eyebrow": "Guider för byggsnickeri",
            "related_title": "Så förbereder du trappor och monterat snickeri",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Trappor", "title": "Vad påverkar pris och leveranstid för trätrappor?", "body": "Viktiga uppgifter inför första dialogen om trappa, mätning och montage."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Checklista med information som snabbar upp första svaret."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Förbered underlaget för offert",
            "related_links": [
                {"page": "construction", "eyebrow": "Erbjudande", "title": "Byggsnickeri", "body": "Trappor, dörrar, lister och måttanpassade träelement för lokala projekt."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Vad du bör skicka för att få ett konkret svar snabbare."},
            ],
        },
    },
    "da": {
        "construction": {
            "related_eyebrow": "Guides til byggesnedkeri",
            "related_title": "Sådan forbereder du trapper og monteret snedkeri",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Trapper", "title": "Hvad påvirker pris og leveringstid for trætrapper?", "body": "Vigtige oplysninger før første dialog om trappe, opmåling og montage."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Checkliste med information, der gør første svar hurtigere."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Forbered materialet til tilbud",
            "related_links": [
                {"page": "construction", "eyebrow": "Tilbud", "title": "Byggesnedkeri", "body": "Trapper, døre, lister og måltilpassede træelementer til lokale projekter."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Hvad du bør sende for at få et konkret svar hurtigere."},
            ],
        },
    },
    "no": {
        "construction": {
            "related_eyebrow": "Guider for byggsnekkerarbeid",
            "related_title": "Slik forbereder du trapper og montert snekkerarbeid",
            "related_links": [
                {"page": "stairs_pricing", "eyebrow": "Trapper", "title": "Hva påvirker pris og leveringstid for tretrapper?", "body": "Viktig informasjon før første dialog om trapp, oppmåling og montering."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Sjekkliste med informasjon som gjør første svar raskere."},
            ],
        },
        "stairs_pricing": {
            "related_eyebrow": "Neste steg",
            "related_title": "Forbered grunnlaget for vurdering",
            "related_links": [
                {"page": "construction", "eyebrow": "Tilbud", "title": "Byggsnekkerarbeid", "body": "Trapper, dører, lister og måltilpassede treelementer for lokale prosjekter."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Hva du bør sende for å få et konkret svar raskere."},
            ],
        },
    },
}

for _code, _pages in STAIRS_RELATED_LINK_SECTIONS.items():
    for _page_key, _data in _pages.items():
        CONTENT[_code]["pages"][_page_key].update(_data)

ADVERTISING_RELATED_LINK_SECTIONS = {
    "pl": {
        "production": {
            "related_eyebrow": "Poradniki B2B",
            "related_title": "Jak szybciej przejść od pomysłu do wyceny",
            "related_links": [
                {"page": "short_series", "eyebrow": "Krótkie serie", "title": "Kiedy opłaca się zamówić elementy drewniane w krótkiej serii?", "body": "Sprawdź, kiedy warto zacząć od próbki, małej partii albo powtarzalnego procesu."},
                {"page": "advertising_events", "eyebrow": "Reklama i eventy", "title": "Elementy drewniane dla firm reklamowych i eventowych", "body": "Jak przygotować zapytanie o displaye, elementy POS, prototypy i krótkie serie kampanijne."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Minimum informacji, które pomaga szybciej ocenić projekt B2B albo nietypowy detal."},
            ],
        },
        "guide": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Jeśli temat dotyczy elementów dla firmy",
            "related_links": [
                {"page": "production", "eyebrow": "Oferta", "title": "Elementy drewniane dla firm", "body": "Zobacz zakres produkcji B2B, półproduktów i elementów według wzoru."},
                {"page": "short_series", "eyebrow": "Krótkie serie", "title": "Kiedy krótka seria ma sens?", "body": "Poradnik dla firm, które rozważają próbkę, pierwszą partię lub stałą współpracę."},
                {"page": "advertising_events", "eyebrow": "Reklama i eventy", "title": "Elementy drewniane dla firm reklamowych i eventowych", "body": "Osobna ścieżka dla displayów, POS i krótkich serii kampanijnych."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Przygotuj temat do rozmowy",
            "related_links": [
                {"page": "production", "eyebrow": "Oferta", "title": "Produkcja elementów drewnianych", "body": "Zakres prac dla firm, krótkich serii i drewnianych półproduktów."},
                {"page": "advertising_events", "eyebrow": "Reklama i eventy", "title": "Elementy drewniane dla firm reklamowych i eventowych", "body": "Jak opisać display, prototyp lub serię na event."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Co wysłać, żeby szybciej dostać konkretną odpowiedź."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Dalszy krok",
            "related_title": "Doprecyzuj serię lub wyślij brief",
            "related_links": [
                {"page": "production", "eyebrow": "Oferta", "title": "Produkcja elementów drewnianych", "body": "Zakres prac dla firm, krótkich serii i drewnianych półproduktów."},
                {"page": "short_series", "eyebrow": "Krótkie serie", "title": "Kiedy krótka seria ma sens?", "body": "Poradnik o próbce, pierwszej partii i powtarzalnym procesie."},
                {"page": "guide", "eyebrow": "Wycena", "title": "Jak przygotować zapytanie do stolarni", "body": "Co wysłać, żeby szybciej dostać konkretną odpowiedź."},
            ],
        },
    },
    "en": {
        "production": {
            "related_eyebrow": "B2B guides",
            "related_title": "How to move from idea to pricing faster",
            "related_links": [
                {"page": "short_series", "eyebrow": "Short runs", "title": "When does a short run of wooden components pay off?", "body": "See when to start with a sample, first batch or repeatable process."},
                {"page": "advertising_events", "eyebrow": "Advertising and events", "title": "Wooden components for advertising and event companies", "body": "How to prepare a request for displays, POS elements, prototypes and campaign runs."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "The minimum input that helps assess a B2B or unusual project faster."},
            ],
        },
        "guide": {
            "related_eyebrow": "Next step",
            "related_title": "If the project concerns components for a company",
            "related_links": [
                {"page": "production", "eyebrow": "Offer", "title": "Wooden components for companies", "body": "See the scope of B2B production, semi-finished parts and sample-based components."},
                {"page": "short_series", "eyebrow": "Short runs", "title": "When does a short run make sense?", "body": "A guide for companies considering a sample, first batch or recurring cooperation."},
                {"page": "advertising_events", "eyebrow": "Advertising and events", "title": "Wooden components for advertising and event companies", "body": "A separate path for displays, POS and campaign short runs."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Next step",
            "related_title": "Prepare the project for discussion",
            "related_links": [
                {"page": "production", "eyebrow": "Offer", "title": "Wooden component production", "body": "Scope for companies, short runs and wooden semi-finished parts."},
                {"page": "advertising_events", "eyebrow": "Advertising and events", "title": "Wooden components for advertising and event companies", "body": "How to describe a display, prototype or event series."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "What to send to get a concrete answer faster."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Next step",
            "related_title": "Clarify the run or send a brief",
            "related_links": [
                {"page": "production", "eyebrow": "Offer", "title": "Wooden component production", "body": "Scope for companies, short runs and wooden semi-finished parts."},
                {"page": "short_series", "eyebrow": "Short runs", "title": "When does a short run make sense?", "body": "A guide to samples, first batches and a repeatable process."},
                {"page": "guide", "eyebrow": "Quote", "title": "How to prepare a joinery inquiry", "body": "What to send to get a concrete answer faster."},
            ],
        },
    },
    "de": {
        "production": {
            "related_eyebrow": "B2B-Leitfäden",
            "related_title": "Schneller von der Idee zur Anfrage",
            "related_links": [
                {"page": "short_series", "eyebrow": "Kleinserien", "title": "Wann lohnt sich eine Kleinserie von Holzelementen?", "body": "Wann Muster, erste Partie oder wiederholbarer Prozess sinnvoll sind."},
                {"page": "advertising_events", "eyebrow": "Werbung und Events", "title": "Holzelemente für Werbe- und Eventfirmen", "body": "So bereiten Sie Anfragen zu Displays, POS-Elementen, Prototypen und Kampagnenserien vor."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Das Minimum an Informationen für eine schnellere Einschätzung."},
            ],
        },
        "guide": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Wenn es um Elemente für Unternehmen geht",
            "related_links": [
                {"page": "production", "eyebrow": "Angebot", "title": "Holzelemente für Unternehmen", "body": "Umfang für B2B-Fertigung, Halbzeuge und Elemente nach Muster."},
                {"page": "short_series", "eyebrow": "Kleinserien", "title": "Wann ist eine Kleinserie sinnvoll?", "body": "Ein Leitfaden für Muster, erste Serien und wiederkehrende Zusammenarbeit."},
                {"page": "advertising_events", "eyebrow": "Werbung und Events", "title": "Holzelemente für Werbe- und Eventfirmen", "body": "Ein eigener Weg für Displays, POS und kurze Kampagnenserien."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Projekt für die Anfrage vorbereiten",
            "related_links": [
                {"page": "production", "eyebrow": "Angebot", "title": "Fertigung von Holzelementen", "body": "Leistungsumfang für Firmen, Kleinserien und Holz-Halbzeuge."},
                {"page": "advertising_events", "eyebrow": "Werbung und Events", "title": "Holzelemente für Werbe- und Eventfirmen", "body": "Wie Display, Prototyp oder Eventserie beschrieben werden sollte."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Was Sie senden sollten, um schneller eine konkrete Antwort zu bekommen."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Nächster Schritt",
            "related_title": "Serie klären oder Briefing senden",
            "related_links": [
                {"page": "production", "eyebrow": "Angebot", "title": "Fertigung von Holzelementen", "body": "Leistungsumfang für Firmen, Kleinserien und Holz-Halbzeuge."},
                {"page": "short_series", "eyebrow": "Kleinserien", "title": "Wann ist eine Kleinserie sinnvoll?", "body": "Ein Leitfaden zu Muster, erster Partie und wiederholbarem Prozess."},
                {"page": "guide", "eyebrow": "Anfrage", "title": "Tischlerei-Anfrage vorbereiten", "body": "Was Sie senden sollten, um schneller eine konkrete Antwort zu bekommen."},
            ],
        },
    },
    "sv": {
        "production": {
            "related_eyebrow": "B2B-guider",
            "related_title": "Snabbare från idé till offert",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korta serier", "title": "När lönar sig en kort serie träkomponenter?", "body": "När prov, första serie eller återkommande process är rätt väg."},
                {"page": "advertising_events", "eyebrow": "Reklam och event", "title": "Träkomponenter för reklam- och eventföretag", "body": "Så förbereder du en fråga om displayer, POS, prototyper och kampanjserier."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Minsta underlag som hjälper oss bedöma projektet snabbare."},
            ],
        },
        "guide": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Om projektet gäller komponenter för företag",
            "related_links": [
                {"page": "production", "eyebrow": "Erbjudande", "title": "Träkomponenter för företag", "body": "Omfattning för B2B-produktion, halvfabrikat och komponenter efter prov."},
                {"page": "short_series", "eyebrow": "Korta serier", "title": "När är en kort serie rimlig?", "body": "Guide för prov, första serie och återkommande samarbete."},
                {"page": "advertising_events", "eyebrow": "Reklam och event", "title": "Träkomponenter för reklam- och eventföretag", "body": "En separat väg för displayer, POS och korta kampanjserier."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Förbered projektet för dialog",
            "related_links": [
                {"page": "production", "eyebrow": "Erbjudande", "title": "Produktion av träkomponenter", "body": "Omfattning för företag, korta serier och halvfabrikat i trä."},
                {"page": "advertising_events", "eyebrow": "Reklam och event", "title": "Träkomponenter för reklam- och eventföretag", "body": "Så beskriver du en display, prototyp eller eventserie."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Vad du bör skicka för att få ett konkret svar snabbare."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Nästa steg",
            "related_title": "Tydliggör serien eller skicka brief",
            "related_links": [
                {"page": "production", "eyebrow": "Erbjudande", "title": "Produktion av träkomponenter", "body": "Omfattning för företag, korta serier och halvfabrikat i trä."},
                {"page": "short_series", "eyebrow": "Korta serier", "title": "När är en kort serie rimlig?", "body": "Guide om prov, första serie och repeterbar process."},
                {"page": "guide", "eyebrow": "Offert", "title": "Så förbereder du en snickeriförfrågan", "body": "Vad du bör skicka för att få ett konkret svar snabbare."},
            ],
        },
    },
    "da": {
        "production": {
            "related_eyebrow": "B2B-guides",
            "related_title": "Hurtigere fra idé til tilbud",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Hvornår kan en kort serie trækomponenter betale sig?", "body": "Hvornår prøve, første serie eller gentagelig proces er den rigtige vej."},
                {"page": "advertising_events", "eyebrow": "Reklame og events", "title": "Trækomponenter til reklame- og eventfirmaer", "body": "Sådan forbereder du en forespørgsel om displays, POS, prototyper og kampagneserier."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Minimumsgrundlaget der hjælper os med at vurdere projektet hurtigere."},
            ],
        },
        "guide": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Hvis projektet handler om komponenter til virksomheder",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Trækomponenter til virksomheder", "body": "Omfang for B2B-produktion, halvfabrikata og komponenter efter prøve."},
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Hvornår giver en kort serie mening?", "body": "Guide til prøve, første serie og løbende samarbejde."},
                {"page": "advertising_events", "eyebrow": "Reklame og events", "title": "Trækomponenter til reklame- og eventfirmaer", "body": "En separat vej for displays, POS og korte kampagneserier."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Forbered projektet til dialog",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Produktion af trækomponenter", "body": "Omfang for virksomheder, korte serier og halvfabrikata i træ."},
                {"page": "advertising_events", "eyebrow": "Reklame og events", "title": "Trækomponenter til reklame- og eventfirmaer", "body": "Sådan beskriver du en display, prototype eller eventserie."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Hvad du bør sende for at få et konkret svar hurtigere."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Næste skridt",
            "related_title": "Afklar serien eller send brief",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Produktion af trækomponenter", "body": "Omfang for virksomheder, korte serier og halvfabrikata i træ."},
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Hvornår giver en kort serie mening?", "body": "Guide til prøve, første serie og gentagelig proces."},
                {"page": "guide", "eyebrow": "Tilbud", "title": "Sådan forbereder du en snedkerforespørgsel", "body": "Hvad du bør sende for at få et konkret svar hurtigere."},
            ],
        },
    },
    "no": {
        "production": {
            "related_eyebrow": "B2B-guider",
            "related_title": "Raskere fra idé til vurdering",
            "related_links": [
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Når lønner en kort serie trekomponenter seg?", "body": "Når prøve, første serie eller repeterbar prosess er riktig vei."},
                {"page": "advertising_events", "eyebrow": "Reklame og event", "title": "Trekomponenter for reklame- og eventbedrifter", "body": "Slik forbereder du en forespørsel om displayer, POS, prototyper og kampanjeserier."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Minimumsgrunnlaget som hjelper oss å vurdere prosjektet raskere."},
            ],
        },
        "guide": {
            "related_eyebrow": "Neste steg",
            "related_title": "Hvis prosjektet gjelder komponenter for bedrifter",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Trekomponenter for bedrifter", "body": "Omfang for B2B-produksjon, halvfabrikata og komponenter etter prøve."},
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Når gir en kort serie mening?", "body": "Guide for prøve, første serie og fast samarbeid."},
                {"page": "advertising_events", "eyebrow": "Reklame og event", "title": "Trekomponenter for reklame- og eventbedrifter", "body": "En egen vei for displayer, POS og korte kampanjeserier."},
            ],
        },
        "short_series": {
            "related_eyebrow": "Neste steg",
            "related_title": "Forbered prosjektet for dialog",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Produksjon av trekomponenter", "body": "Omfang for bedrifter, korte serier og halvfabrikata i tre."},
                {"page": "advertising_events", "eyebrow": "Reklame og event", "title": "Trekomponenter for reklame- og eventbedrifter", "body": "Slik beskriver du en display, prototype eller eventserie."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Hva du bør sende for å få et konkret svar raskere."},
            ],
        },
        "advertising_events": {
            "related_eyebrow": "Neste steg",
            "related_title": "Avklar serien eller send brief",
            "related_links": [
                {"page": "production", "eyebrow": "Tilbud", "title": "Produksjon av trekomponenter", "body": "Omfang for bedrifter, korte serier og halvfabrikata i tre."},
                {"page": "short_series", "eyebrow": "Korte serier", "title": "Når gir en kort serie mening?", "body": "Guide til prøve, første parti og repeterbar prosess."},
                {"page": "guide", "eyebrow": "Forespørsel", "title": "Slik forbereder du en snekkerforespørsel", "body": "Hva du bør sende for å få et konkret svar raskere."},
            ],
        },
    },
}

for _code, _pages in ADVERTISING_RELATED_LINK_SECTIONS.items():
    for _page_key, _data in _pages.items():
        CONTENT[_code]["pages"][_page_key].update(_data)


def _with_runtime_fields(page_key, page, language_code=None):
    page = page.copy()
    page["key"] = page_key
    page["path"] = PATHS[page_key]
    page["template"] = TEMPLATES[page_key]
    if "hero_photo" in page:
        page["hero_photo"] = PHOTO_PLACEHOLDERS[page["hero_photo"]]
    if "b2b_photo" in page:
        page["b2b_photo"] = PHOTO_PLACEHOLDERS[page["b2b_photo"]]
    if "related_links" in page:
        links = []
        for link in page["related_links"]:
            link = link.copy()
            if "page" in link:
                link["url"] = get_localized_path(PATHS[link["page"]], language_code)
            links.append(link)
        page["related_links"] = links
    return page


def _with_case_photos(cases):
    resolved = []
    for case in cases:
        case = case.copy()
        case["photo"] = PHOTO_PLACEHOLDERS[case["photo"]]
        resolved.append(case)
    return resolved


def normalize_language(language_code):
    return (language_code or "pl").split("-")[0]


def get_localized_path(path, language_code):
    code = normalize_language(language_code)
    if code == DEFAULT_LANGUAGE:
        return path
    return f"/{code}{path}"


def get_content(language_code):
    code = normalize_language(language_code)
    return CONTENT.get(code, CONTENT["pl"])


def get_page_content(page_key, language_code):
    content = get_content(language_code)
    return _with_runtime_fields(page_key, content["pages"][page_key], language_code)


def get_nav_items(language_code):
    nav = get_content(language_code)["nav"]
    return [
        ("production", nav["production"], get_localized_path(PATHS["production"], language_code)),
        ("construction", nav["construction"], get_localized_path(PATHS["construction"], language_code)),
        ("architects", nav["architects"], get_localized_path(PATHS["architects"], language_code)),
        ("realizations", nav["realizations"], get_localized_path(PATHS["realizations"], language_code)),
        ("quote", nav["quote"], get_localized_path(PATHS["quote"], language_code)),
        ("contact", nav["contact"], get_localized_path(PATHS["contact"], language_code)),
    ]


def get_process_steps(language_code):
    return get_content(language_code)["process_steps"]


def get_audience_cards(language_code):
    cards = []
    for card in get_content(language_code)["audience_cards"]:
        card = card.copy()
        card["url"] = get_localized_path(card["url"], language_code)
        cards.append(card)
    return cards


def get_realization_cases(language_code):
    return _with_case_photos(get_content(language_code)["realization_cases"])


def iter_sitemap_pages(language_code):
    for key in PAGE_ORDER:
        yield get_page_content(key, language_code)
