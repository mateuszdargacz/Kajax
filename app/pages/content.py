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
        "filename": "custom-wooden-stairs-pomorskie.jpg",
        "label": "Wooden stairs project",
        "description": "Finished stairs in a real interior, with clean geometry.",
    },
    "doors_detail": {
        "key": "doors_detail",
        "filename": "custom-wooden-doors-detail.jpg",
        "label": "Custom wooden doors detail",
        "description": "Doors, trims or construction joinery detail in context.",
    },
    "artistic_detail": {
        "key": "artistic_detail",
        "filename": "custom-artistic-woodwork-detail.jpg",
        "label": "Custom artistic woodwork",
        "description": "Unusual detail, premium custom element or architectural woodwork.",
    },
}

PATHS = {
    "home": "/",
    "production": "/produkcja-elementow-drewnianych/",
    "construction": "/stolarka-budowlana/",
    "architects": "/dla-architektow-i-firm/",
    "realizations": "/realizacje/",
    "quote": "/wycena/",
    "contact": "/kontakt/",
}

DEFAULT_LANGUAGE = "pl"

TEMPLATES = {
    "home": "pages/home.html",
    "production": "pages/service_page.html",
    "construction": "pages/service_page.html",
    "architects": "pages/service_page.html",
    "realizations": "pages/realizations.html",
    "quote": "pages/quote.html",
    "contact": "pages/contact.html",
}

PAGE_ORDER = ["home", "production", "construction", "architects", "realizations", "quote", "contact"]

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
                "title": "Kajax Stolarstwo | Elementy drewniane, stolarka budowlana i realizacje na wymiar",
                "description": "Stolarnia z Gościcina dla firm, architektów i inwestorów. Elementy drewniane, krótkie serie, schody, drzwi, listwy i customowe realizacje.",
                "hero_photo": "hero_workshop",
                "b2b_photo": "b2b_components_series",
                "hero_alt": "Warsztat stolarski przygotowany do produkcji elementów drewnianych i realizacji na wymiar",
                "eyebrow": "Stolarnia produkcyjno-budowlana z Pomorza",
                "h1": "Stolarnia dla firm, architektów i wymagających realizacji z drewna",
                "lead": "Wykonujemy elementy drewniane, stolarkę budowlaną i projekty na wymiar. Pracujemy na zdjęciach, rysunkach i specyfikacjach: od pojedynczego detalu po krótką serię.",
                "primary_cta": "Wyślij projekt do wyceny",
                "secondary_cta": "Zobacz zakres prac",
            },
            "production": {
                "title": "Elementy drewniane na zamówienie dla firm | Kajax",
                "description": "Krótkie serie, półprodukty i detale drewniane według wzoru, zdjęcia albo rysunku. Dla producentów, wykonawców, firm reklamowych i projektantów.",
                "hero_photo": "b2b_components_series",
                "hero_alt": "Powtarzalne elementy drewniane wykonane w krótkiej serii dla firmy",
                "eyebrow": "B2B / krótkie serie / półprodukty",
                "h1": "Elementy drewniane na zamówienie dla firm",
                "lead": "Przygotowujemy drewniane detale, półprodukty i krótkie serie według wzoru, zdjęcia, rysunku lub specyfikacji. To kierunek dla firm, które potrzebują sprawdzonej stolarni bez budowania własnego zaplecza.",
                "primary_cta": "Wyślij specyfikację do wyceny",
                "sections": [
                    {
                        "title": "Dla kogo pracujemy",
                        "body": "Dla producentów mebli, firm reklamowych i POS, wykonawców wnętrz, manufaktur oraz projektantów, którzy potrzebują drewnianych elementów w małych lub powtarzalnych partiach.",
                        "items": ["prototypy i próbki", "krótkie serie", "elementy według wzoru", "stała współpraca po dopasowaniu procesu"],
                    },
                    {
                        "title": "Jakie elementy mają sens",
                        "body": "Najlepiej sprawdzają się elementy, które da się jasno opisać wymiarem, materiałem, wykończeniem i powtarzalnością. Logistykę, pakowanie i wysyłkę ustalamy po poznaniu projektu.",
                        "items": ["listwy, profile i ramy", "drewniane półprodukty", "elementy ekspozycji i displayów", "detale do dalszego montażu lub wykończenia"],
                    },
                    {
                        "title": "Jak zacząć",
                        "body": "Wyślij zdjęcie, rysunek albo krótki opis. Dopytamy o materiał, ilość, tolerancję, wykończenie i termin. Przy większej serii można zacząć od próbki lub prototypu.",
                        "items": ["zdjęcie lub rysunek", "orientacyjna ilość", "materiał i wykończenie", "termin oraz sposób odbioru"],
                    },
                ],
                "faq": [
                    ("Czy realizujecie zamówienia B2B poza Pomorzem?", "Tak, jeśli projekt i logistyka mają sens. Dla elementów B2B zakładamy możliwość współpracy w Polsce i Europie, ale wysyłka i pakowanie są ustalane indywidualnie."),
                    ("Czy można zacząć od jednej próbki?", "Tak. Przy powtarzalnych elementach próbka często jest najlepszym sposobem ustalenia wymiaru, wykończenia i kosztu serii."),
                ],
            },
            "construction": {
                "title": "Stolarka budowlana Pomorskie | Schody, drzwi i listwy | Kajax",
                "description": "Schody drewniane, drzwi, listwy, zabudowy i elementy wykończeniowe na wymiar. Stolarnia z Gościcina obsługująca Pomorskie i okolice Wejherowa.",
                "hero_photo": "stairs_project",
                "hero_alt": "Schody drewniane wykonane na wymiar jako przykład stolarki budowlanej",
                "eyebrow": "Schody / drzwi / listwy / zabudowy",
                "h1": "Schody, drzwi, listwy i stolarka drewniana na wymiar",
                "lead": "Wykonujemy stolarkę budowlaną dla domów, lokali i inwestycji, gdzie liczy się solidne wykonanie, trwałość i dopasowanie do projektu.",
                "primary_cta": "Zapytaj o stolarkę budowlaną",
                "sections": [
                    {
                        "title": "Zakres prac",
                        "body": "Pomagamy przy elementach wykończeniowych i konstrukcyjnych z drewna, szczególnie tam, gdzie gotowe rozwiązania nie pasują do projektu albo oczekiwanego standardu.",
                        "items": ["schody drewniane", "drzwi wewnętrzne i zewnętrzne", "listwy, progi, opaski i parapety", "zabudowy i nietypowe elementy wykończeniowe"],
                    },
                    {
                        "title": "Kiedy zgłosić projekt",
                        "body": "Im wcześniej znamy wymiary, miejsce montażu i oczekiwany termin, tym łatwiej ocenić wykonalność i uniknąć kosztownych zmian na budowie.",
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
                "description": "Niestandardowe detale drewniane, customowe realizacje i stolarka według projektu dla architektów, projektantów, wykonawców i firm.",
                "hero_photo": "artistic_detail",
                "hero_alt": "Nietypowy detal drewniany wykonany według projektu dla architekta lub firmy",
                "eyebrow": "Custom / detale / projekty specjalne",
                "h1": "Stolarnia do trudniejszych projektów i detali drewnianych",
                "lead": "Pomagamy wykonać niestandardowe elementy drewniane do wnętrz, ekspozycji i realizacji projektowych. Pracujemy na koncepcjach, rysunkach, zdjęciach i ustaleniach z wykonawcą.",
                "primary_cta": "Omów projekt",
                "sections": [
                    {
                        "title": "Kiedy warto napisać",
                        "body": "Gdy projekt wymaga rozmowy o detalu, materiale, sposobie montażu albo sensownej technologii wykonania, a gotowe rozwiązanie nie wystarcza.",
                        "items": ["detale do wnętrz premium", "elementy ekspozycji i lokali", "customowe zabudowy", "odtworzenia lub nietypowe profile"],
                    },
                    {
                        "title": "Jak współpracujemy",
                        "body": "Najpierw ustalamy intencję projektu i ograniczenia techniczne. Potem doprecyzowujemy materiał, wymiary, wykończenie, montaż i termin.",
                        "items": ["analiza rysunku lub zdjęć", "doprecyzowanie technologii", "próbka, jeśli ma sens", "realizacja i odbiór"],
                    },
                ],
                "faq": [
                    ("Czy wykonujecie pojedyncze nietypowe elementy?", "Tak, jeśli projekt ma jasny zakres i da się go sensownie wykonać technologicznie."),
                    ("Czy pracujecie z architektami?", "Tak. Najlepiej, gdy zapytanie zawiera rysunek, inspirację, materiał i oczekiwany efekt końcowy."),
                ],
            },
            "realizations": {
                "title": "Realizacje stolarskie | Kajax",
                "description": "Wybrane realizacje stolarskie: schody, drzwi, listwy, detale drewniane i projekty na wymiar. Każda realizacja opisana kontekstem i zakresem prac.",
                "h1": "Realizacje z kontekstem, nie tylko galeria",
                "lead": "Docelowo każda realizacja powinna pokazywać materiał, zakres, problem do rozwiązania i efekt. Na start pokazujemy typy projektów, które warto sfotografować i opisać.",
            },
            "quote": {
                "title": "Wyślij projekt do wyceny | Kajax",
                "description": "Wyślij zdjęcie, rysunek, specyfikację albo opis projektu. Ocenimy, czy możemy wykonać element, krótką serię lub stolarkę na wymiar.",
                "h1": "Wyślij projekt do wyceny",
                "lead": "Nie musisz mieć pełnej dokumentacji. Napisz krótko, czego potrzebujesz, zostaw telefon albo email, a szczegóły doprecyzujemy w rozmowie.",
            },
            "contact": {
                "title": "Kontakt | Kajax Stolarstwo Gościcino",
                "description": "Kontakt z Kajax Stolarstwo: Gościcino, Pomorskie. Zapytania B2B, stolarka budowlana, realizacje custom i projekty na wymiar.",
                "h1": "Kontakt",
                "lead": "Najwygodniej zacząć od krótkiego formularza wyceny. Przy pilnych sprawach można zadzwonić.",
            },
        },
        "process_steps": [
            ("Wysyłasz materiał", "Zdjęcie, rysunek, specyfikację albo krótki opis elementu i oczekiwanego efektu."),
            ("Dopytujemy technicznie", "Materiał, ilość, wymiary, tolerancje, termin, wykończenie oraz sposób odbioru lub logistyki."),
            ("Oceniamy wykonalność", "Sprawdzamy, czy projekt pasuje do możliwości warsztatu i czy ma sens kosztowo."),
            ("Próbka lub wycena", "Przy serii można zacząć od próbki. Przy prostszych pracach przechodzimy do wyceny."),
        ],
        "audience_cards": [
            {"title": "Elementy drewniane dla firm", "body": "Krótkie serie, półprodukty, elementy według wzoru i projekty B2B, gdzie liczy się powtarzalność.", "url": PATHS["production"], "cta": "Zobacz produkcję B2B"},
            {"title": "Stolarka budowlana", "body": "Schody, drzwi, listwy, zabudowy i drewniane elementy wykończeniowe dla inwestycji lokalnych.", "url": PATHS["construction"], "cta": "Zobacz zakres stolarki"},
            {"title": "Custom i trudniejsze realizacje", "body": "Nietypowe detale, realizacje według projektu i współpraca z architektami oraz wykonawcami.", "url": PATHS["architects"], "cta": "Zobacz współpracę projektową"},
        ],
        "realization_cases": [
            {"title": "Schody drewniane z detalem metalowym", "category": "Stolarka budowlana", "photo": "stairs_project", "alt": "Schody drewniane z balustradą jako przykład realizacji stolarskiej", "meta": ["materiał: drewno", "zakres: wykonanie i dopasowanie", "typ: inwestor prywatny"], "body": "Przykład realizacji pokazującej, jak stolarka może stać się widocznym elementem wnętrza. W nowym portfolio każdy taki projekt powinien dostać opis materiału, wyzwań i efektu."},
            {"title": "Drewniany detal do wnętrza", "category": "Custom / wnętrza", "photo": "precision_detail", "alt": "Precyzyjny detal drewniany do wnętrza premium", "meta": ["zakres: detal i wykończenie", "typ: projekt indywidualny", "obszar: Pomorskie"], "body": "Tego typu kadry budują wiarygodność wśród architektów i inwestorów. Potrzebujemy zdjęć, które pokazują detal, skalę i sposób wykonania."},
            {"title": "Drzwi, listwy i elementy stolarki", "category": "Drzwi / listwy / elementy", "photo": "doors_detail", "alt": "Drzwi drewniane jako przykład stolarki budowlanej na wymiar", "meta": ["zakres: stolarka budowlana", "typ: drzwi i wykończenie", "wycena: po zdjęciach i wymiarach"], "body": "Stolarka budowlana pozostaje ważnym filarem lokalnym. Formularz filtruje takie zapytania przez lokalizację, termin i zakres prac."},
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
            "title": "Kajax Joinery | Wooden components, construction joinery and custom woodwork",
            "description": "A joinery workshop from Gościcino for companies, architects and investors. Wooden components, short runs, stairs, doors, trims and custom woodwork.",
            "hero_photo": "hero_workshop",
            "b2b_photo": "b2b_components_series",
            "hero_alt": "Joinery workshop prepared for wooden component production and custom projects",
            "eyebrow": "Production and construction joinery from Pomerania",
            "h1": "A joinery workshop for companies, architects and demanding woodwork projects",
            "lead": "We make wooden components, construction joinery and custom projects. We work from photos, drawings and specifications: from a single detail to a short production run.",
            "primary_cta": "Send project for a quote",
            "secondary_cta": "See what we do",
        },
        "production": {
            "title": "Custom wooden components for companies | Kajax",
            "description": "Short runs, semi-finished wooden parts and details made from a sample, photo or drawing. For manufacturers, contractors, advertising firms and designers.",
            "hero_photo": "b2b_components_series",
            "hero_alt": "Repeatable wooden components made in a short run for a company",
            "eyebrow": "B2B / short runs / semi-finished parts",
            "h1": "Custom wooden components for companies",
            "lead": "We prepare wooden details, semi-finished parts and short runs based on a sample, photo, drawing or specification. It is a practical option for companies that need a reliable workshop without building their own production setup.",
            "primary_cta": "Send a specification for pricing",
            "sections": [
                {"title": "Who we work with", "body": "Furniture producers, POS and advertising companies, interior contractors, small manufacturers and designers who need wooden parts in small or repeatable batches.", "items": ["prototypes and samples", "short production runs", "parts made from a sample", "recurring cooperation after the process is aligned"]},
                {"title": "Which components make sense", "body": "The best projects can be clearly described by dimensions, material, finish and repeatability. Logistics, packing and shipping are agreed after we understand the project.", "items": ["trims, profiles and frames", "wooden semi-finished parts", "display and POS components", "parts for further assembly or finishing"]},
                {"title": "How to start", "body": "Send a photo, drawing or short description. We will ask about material, quantity, tolerance, finish and timing. For larger runs, a sample or prototype can be the first step.", "items": ["photo or drawing", "approximate quantity", "material and finish", "deadline and pickup or logistics"]},
            ],
            "faq": [
                ("Do you handle B2B orders outside Pomerania?", "Yes, if the project and logistics make sense. For B2B components we can discuss cooperation in Poland and across Europe, with shipping and packing agreed individually."),
                ("Can we start with one sample?", "Yes. For repeatable components, a sample is often the best way to confirm dimensions, finish and the cost of a production run."),
            ],
        },
        "construction": {
            "title": "Construction joinery in Pomerania | Stairs, doors and trims | Kajax",
            "description": "Custom wooden stairs, doors, trims, built-ins and finishing elements. A Gościcino workshop serving Pomerania and the Wejherowo area.",
            "hero_photo": "stairs_project",
            "hero_alt": "Custom wooden stairs as an example of construction joinery",
            "eyebrow": "Stairs / doors / trims / built-ins",
            "h1": "Custom wooden stairs, doors, trims and construction joinery",
            "lead": "We make construction joinery for homes, venues and local investments where solid execution, durability and fit to the project matter.",
            "primary_cta": "Ask about construction joinery",
            "sections": [
                {"title": "Scope of work", "body": "We help with wooden finishing and structural details, especially where ready-made solutions do not fit the project or expected standard.", "items": ["wooden stairs", "internal and external doors", "trims, thresholds, casings and window boards", "built-ins and unusual finishing elements"]},
                {"title": "When to get in touch", "body": "The earlier we know the dimensions, installation place and expected timing, the easier it is to assess feasibility and avoid costly changes on site.", "items": ["plans or measurements", "photos of the installation area", "material information", "project timeline"]},
            ],
            "faq": [
                ("Do you work locally?", "For construction joinery, the priority is Pomerania, Gościcino, Wejherowo and the Tricity area."),
                ("Can I send photos instead of a drawing?", "Yes. Photos are enough for the first conversation, but pricing will require dimensions and technical details."),
            ],
        },
        "architects": {
            "title": "Joinery for architects, designers and companies | Kajax",
            "description": "Custom wooden details, project-based woodwork and made-to-measure joinery for architects, designers, contractors and companies.",
            "hero_photo": "artistic_detail",
            "hero_alt": "Unusual wooden detail made to a project for an architect or company",
            "eyebrow": "Custom / details / special projects",
            "h1": "A workshop for more demanding wooden details and custom projects",
            "lead": "We help execute non-standard wooden elements for interiors, displays and project-based work. We work from concepts, drawings, photos and technical agreements with contractors.",
            "primary_cta": "Discuss a project",
            "sections": [
                {"title": "When it is worth writing", "body": "When a project needs a conversation about detail, material, installation method or sensible production technology, and a ready-made solution is not enough.", "items": ["premium interior details", "display and commercial elements", "custom built-ins", "recreated or unusual profiles"]},
                {"title": "How we cooperate", "body": "First we clarify the design intent and technical constraints. Then we specify material, dimensions, finish, installation and timing.", "items": ["drawing or photo review", "technical refinement", "sample if it makes sense", "production and handover"]},
            ],
            "faq": [
                ("Do you make single unusual elements?", "Yes, if the project has a clear scope and can be made sensibly with the workshop's technology."),
                ("Do you work with architects?", "Yes. The best inquiry includes a drawing, reference, material and the intended final effect."),
            ],
        },
        "realizations": {
            "title": "Woodwork projects | Kajax",
            "description": "Selected joinery projects: stairs, doors, trims, wooden details and custom work. Each case should explain context and scope, not just show a gallery.",
            "h1": "Project cases with context, not just a gallery",
            "lead": "Each case should show material, scope, the problem solved and the final effect. For launch, we show the types of projects that should be photographed and described.",
        },
        "quote": {
            "title": "Send a project for a quote | Kajax",
            "description": "Send a photo, drawing, specification or short project description. We will assess whether we can make the component, short run or custom joinery.",
            "h1": "Send a project for a quote",
            "lead": "You do not need full documentation. Briefly describe what you need, leave a phone number or email, and we will clarify the details in conversation.",
        },
        "contact": {
            "title": "Contact | Kajax Joinery Gościcino",
            "description": "Contact Kajax Joinery in Gościcino, Pomerania. B2B inquiries, construction joinery, custom projects and made-to-measure woodwork.",
            "h1": "Contact",
            "lead": "The easiest way to start is the short quote form. For urgent matters, call us.",
        },
    },
    "process_steps": [
        ("You send materials", "A photo, drawing, specification or short description of the component and expected result."),
        ("We ask technical questions", "Material, quantity, dimensions, tolerances, timing, finish and pickup or logistics."),
        ("We assess feasibility", "We check whether the project fits the workshop and makes sense economically."),
        ("Sample or quote", "For a production run, a sample can be the first step. Simpler projects can move directly to pricing."),
    ],
    "audience_cards": [
        {"title": "Wooden components for companies", "body": "Short runs, semi-finished parts, sample-based components and B2B projects where repeatability matters.", "url": PATHS["production"], "cta": "See B2B production"},
        {"title": "Construction joinery", "body": "Stairs, doors, trims, built-ins and wooden finishing elements for local projects.", "url": PATHS["construction"], "cta": "See construction joinery"},
        {"title": "Custom and demanding projects", "body": "Unusual details, project-based work and cooperation with architects and contractors.", "url": PATHS["architects"], "cta": "See project cooperation"},
    ],
    "realization_cases": [
        {"title": "Wooden stairs with metal detail", "category": "Construction joinery", "photo": "stairs_project", "alt": "Wooden stairs with railing as an example of custom joinery", "meta": ["material: wood", "scope: production and fitting", "type: private investor"], "body": "An example of a project where joinery becomes a visible interior feature. In the new portfolio, each case should explain material, challenges and final effect."},
        {"title": "Wooden interior detail", "category": "Custom / interiors", "photo": "precision_detail", "alt": "Precise wooden detail for a premium interior", "meta": ["scope: detail and finish", "type: individual project", "region: Pomerania"], "body": "These shots build trust with architects and investors. We need photos that show the detail, scale and method of execution."},
        {"title": "Doors, trims and joinery elements", "category": "Doors / trims / elements", "photo": "doors_detail", "alt": "Wooden doors as an example of made-to-measure construction joinery", "meta": ["scope: construction joinery", "type: doors and finishing", "quote: based on photos and dimensions"], "body": "Construction joinery remains an important local pillar. The form qualifies these inquiries by location, timing and scope."},
    ],
}


_SERVICE_TRANSLATIONS = {
    "de": {
        "nav": {"production": "Elementfertigung", "construction": "Bauschreinerei", "architects": "Für Architekten und Firmen", "realizations": "Referenzen", "quote": "Anfrage", "contact": "Kontakt"},
        "home": ("Kajax Tischlerei | Holzelemente, Bauschreinerei und Sonderanfertigungen", "Tischlerei aus Gościcino für Unternehmen, Architekten und Investoren. Holzelemente, Kleinserien, Treppen, Türen, Leisten und Sonderanfertigungen.", "Tischlerei für Unternehmen, Architekten und anspruchsvolle Holzprojekte", "Wir fertigen Holzelemente, Bauschreinerei und Sonderprojekte nach Maß. Wir arbeiten anhand von Fotos, Zeichnungen und Spezifikationen: vom einzelnen Detail bis zur Kleinserie.", "Projekt zur Anfrage senden", "Leistungsumfang ansehen"),
        "production_h1": "Holzelemente nach Maß für Unternehmen",
        "production_lead": "Wir fertigen Holzdetails, Halbzeuge und Kleinserien nach Muster, Foto, Zeichnung oder Spezifikation. Das ist sinnvoll für Unternehmen, die eine zuverlässige Werkstatt brauchen, ohne eigene Produktionskapazitäten aufzubauen.",
        "construction_h1": "Holztreppen, Türen, Leisten und Bauschreinerei nach Maß",
        "construction_lead": "Wir fertigen Bauschreinerei für Häuser, Objekte und lokale Investitionen, bei denen solide Ausführung, Haltbarkeit und genaue Anpassung zählen.",
        "architects_h1": "Eine Werkstatt für anspruchsvollere Holzdetails und Sonderprojekte",
        "architects_lead": "Wir helfen bei der Umsetzung nicht standardisierter Holzelemente für Innenräume, Ausstellungen und projektbezogene Arbeiten. Wir arbeiten mit Konzepten, Zeichnungen, Fotos und technischen Abstimmungen.",
        "quote_h1": "Projekt zur Anfrage senden",
        "quote_lead": "Sie brauchen keine vollständige Dokumentation. Beschreiben Sie kurz, was Sie benötigen, hinterlassen Sie Telefon oder E-Mail, und wir klären die Details im Gespräch.",
        "contact_h1": "Kontakt",
        "contact_lead": "Der einfachste Start ist das kurze Anfrageformular. In dringenden Fällen können Sie anrufen.",
    },
    "sv": {
        "nav": {"production": "Komponentproduktion", "construction": "Byggsnickeri", "architects": "För arkitekter och företag", "realizations": "Referenser", "quote": "Offert", "contact": "Kontakt"},
        "home": ("Kajax Snickeri | Träkomponenter, byggsnickeri och specialprojekt", "Snickeri från Gościcino för företag, arkitekter och investerare. Träkomponenter, korta serier, trappor, dörrar, lister och specialsnickeri.", "Snickeri för företag, arkitekter och krävande träprojekt", "Vi tillverkar träkomponenter, byggsnickeri och specialprojekt. Vi arbetar från foton, ritningar och specifikationer: från en enskild detalj till en kort serie.", "Skicka projekt för offert", "Se vad vi gör"),
        "production_h1": "Träkomponenter på beställning för företag",
        "production_lead": "Vi tar fram trädetaljer, halvfabrikat och korta serier efter prov, foto, ritning eller specifikation. Det passar företag som behöver en pålitlig verkstad utan att bygga egen produktion.",
        "construction_h1": "Trappor, dörrar, lister och byggsnickeri i trä",
        "construction_lead": "Vi utför byggsnickeri för hem, lokaler och lokala projekt där solidt utförande, hållbarhet och passform är viktigt.",
        "architects_h1": "En verkstad för mer krävande trädetaljer och specialprojekt",
        "architects_lead": "Vi hjälper till att genomföra specialanpassade träelement för interiörer, exponeringar och projekt. Vi arbetar från koncept, ritningar, foton och tekniska överenskommelser.",
        "quote_h1": "Skicka projekt för offert",
        "quote_lead": "Du behöver inte ha komplett dokumentation. Beskriv kort vad du behöver, lämna telefon eller e-post, så klargör vi detaljerna i dialog.",
        "contact_h1": "Kontakt",
        "contact_lead": "Det enklaste sättet att börja är det korta offertformuläret. Vid brådskande ärenden kan du ringa.",
    },
    "da": {
        "nav": {"production": "Komponentproduktion", "construction": "Byggesnedkeri", "architects": "For arkitekter og virksomheder", "realizations": "Referencer", "quote": "Tilbud", "contact": "Kontakt"},
        "home": ("Kajax Snedkeri | Trækomponenter, byggesnedkeri og specialprojekter", "Snedkeri fra Gościcino for virksomheder, arkitekter og investorer. Trækomponenter, korte serier, trapper, døre, lister og specialsnedkeri.", "Snedkeri for virksomheder, arkitekter og krævende træprojekter", "Vi fremstiller trækomponenter, byggesnedkeri og specialprojekter. Vi arbejder ud fra fotos, tegninger og specifikationer: fra en enkelt detalje til en kort serie.", "Send projekt til tilbud", "Se hvad vi laver"),
        "production_h1": "Trækomponenter på bestilling til virksomheder",
        "production_lead": "Vi fremstiller trædetaljer, halvfabrikata og korte serier efter prøve, foto, tegning eller specifikation. Det passer til virksomheder, der har brug for et pålideligt værksted uden at opbygge egen produktion.",
        "construction_h1": "Trapper, døre, lister og byggesnedkeri i træ",
        "construction_lead": "Vi udfører byggesnedkeri til boliger, lokaler og lokale projekter, hvor solid udførelse, holdbarhed og tilpasning er vigtig.",
        "architects_h1": "Et værksted til mere krævende trædetaljer og specialprojekter",
        "architects_lead": "Vi hjælper med at udføre specialtilpassede træelementer til interiører, displays og projektarbejde. Vi arbejder ud fra koncepter, tegninger, fotos og tekniske aftaler.",
        "quote_h1": "Send projekt til tilbud",
        "quote_lead": "Du behøver ikke fuld dokumentation. Beskriv kort, hvad du har brug for, angiv telefon eller e-mail, så afklarer vi resten i dialog.",
        "contact_h1": "Kontakt",
        "contact_lead": "Den nemmeste start er den korte tilbudsformular. Ved hastesager kan du ringe.",
    },
    "no": {
        "nav": {"production": "Komponentproduksjon", "construction": "Byggsnekkerarbeid", "architects": "For arkitekter og bedrifter", "realizations": "Referanser", "quote": "Forespørsel", "contact": "Kontakt"},
        "home": ("Kajax Snekkerverksted | Trekomponenter, byggsnekkerarbeid og spesialprosjekter", "Snekkerverksted fra Gościcino for bedrifter, arkitekter og investorer. Trekomponenter, korte serier, trapper, dører, lister og spesialarbeid.", "Snekkerverksted for bedrifter, arkitekter og krevende treprosjekter", "Vi lager trekomponenter, byggsnekkerarbeid og spesialprosjekter. Vi arbeider ut fra bilder, tegninger og spesifikasjoner: fra én detalj til en kort serie.", "Send prosjekt til vurdering", "Se hva vi gjør"),
        "production_h1": "Trekomponenter på bestilling for bedrifter",
        "production_lead": "Vi lager tredetaljer, halvfabrikata og korte serier etter prøve, bilde, tegning eller spesifikasjon. Det passer bedrifter som trenger et pålitelig verksted uten å bygge egen produksjon.",
        "construction_h1": "Trapper, dører, lister og byggsnekkerarbeid i tre",
        "construction_lead": "Vi utfører byggsnekkerarbeid for boliger, lokaler og lokale prosjekter der solid utførelse, holdbarhet og tilpasning er viktig.",
        "architects_h1": "Et verksted for mer krevende tredetaljer og spesialprosjekter",
        "architects_lead": "Vi hjelper med å utføre spesialtilpassede treelementer til interiør, utstillinger og prosjektarbeid. Vi jobber fra konsepter, tegninger, bilder og tekniske avklaringer.",
        "quote_h1": "Send prosjekt til vurdering",
        "quote_lead": "Du trenger ikke full dokumentasjon. Beskriv kort hva du trenger, legg igjen telefon eller e-post, så avklarer vi detaljene i dialog.",
        "contact_h1": "Kontakt",
        "contact_lead": "Den enkleste starten er det korte forespørselsskjemaet. Ved hastesaker kan du ringe.",
    },
}

_LOCALIZED_DETAILS = {
    "de": {
        "production_sections": [
            {"title": "Für wen wir arbeiten", "body": "Für Möbelhersteller, POS- und Werbefirmen, Innenausbauer, kleine Manufakturen und Designer, die Holzteile in kleinen oder wiederholbaren Serien benötigen.", "items": ["Prototypen und Muster", "Kleinserien", "Elemente nach Muster", "regelmäßige Zusammenarbeit nach Prozessabstimmung"]},
            {"title": "Welche Elemente sinnvoll sind", "body": "Am besten eignen sich Projekte, die sich klar über Maße, Material, Oberfläche und Wiederholbarkeit beschreiben lassen. Logistik, Verpackung und Versand klären wir nach Sichtung des Projekts.", "items": ["Leisten, Profile und Rahmen", "Holz-Halbzeuge", "Display- und POS-Elemente", "Teile zur weiteren Montage oder Veredelung"]},
            {"title": "So starten wir", "body": "Senden Sie ein Foto, eine Zeichnung oder eine kurze Beschreibung. Wir fragen nach Material, Menge, Toleranzen, Oberfläche und Termin. Bei größeren Serien kann ein Muster oder Prototyp der erste Schritt sein.", "items": ["Foto oder Zeichnung", "ungefähre Menge", "Material und Oberfläche", "Termin sowie Abholung oder Logistik"]},
        ],
        "production_faq": [
            ("Bearbeiten Sie B2B-Aufträge außerhalb Pommerns?", "Ja, wenn Projekt und Logistik sinnvoll sind. Für B2B-Holzelemente können wir über Zusammenarbeit in Polen und Europa sprechen; Versand und Verpackung werden individuell abgestimmt."),
            ("Können wir mit einem Muster beginnen?", "Ja. Bei wiederholbaren Elementen ist ein Muster oft der beste Weg, um Maße, Oberfläche und Kosten einer Serie zu bestätigen."),
        ],
        "construction_sections": [
            {"title": "Leistungsumfang", "body": "Wir unterstützen bei Holzdetails für Ausbau und Konstruktion, besonders dort, wo Standardlösungen nicht zum Projekt oder zum gewünschten Niveau passen.", "items": ["Holztreppen", "Innen- und Außentüren", "Leisten, Schwellen, Verkleidungen und Fensterbänke", "Einbauten und ungewöhnliche Ausbauelemente"]},
            {"title": "Wann Sie sich melden sollten", "body": "Je früher wir Maße, Einbauort und gewünschten Termin kennen, desto leichter können wir Machbarkeit bewerten und teure Änderungen auf der Baustelle vermeiden.", "items": ["Pläne oder Maße", "Fotos des Einbauorts", "Information zum Material", "Zeitplan des Projekts"]},
        ],
        "construction_faq": [
            ("Arbeiten Sie lokal?", "Bei Bauschreinerei liegt der Schwerpunkt auf Pommern, Gościcino, Wejherowo und der Dreistadt."),
            ("Kann ich Fotos statt einer Zeichnung senden?", "Ja. Fotos reichen für das erste Gespräch, für eine belastbare Anfrage brauchen wir später Maße und technische Details."),
        ],
        "architects_sections": [
            {"title": "Wann sich eine Anfrage lohnt", "body": "Wenn ein Projekt eine Abstimmung zu Detail, Material, Montage oder sinnvoller Fertigungstechnologie braucht und Standardlösungen nicht reichen.", "items": ["Details für hochwertige Innenräume", "Display- und Gewerbeelemente", "maßgefertigte Einbauten", "Nachbildungen oder ungewöhnliche Profile"]},
            {"title": "Wie wir zusammenarbeiten", "body": "Zuerst klären wir Entwurfsabsicht und technische Grenzen. Danach präzisieren wir Material, Maße, Oberfläche, Montage und Termin.", "items": ["Prüfung von Zeichnungen oder Fotos", "technische Präzisierung", "Muster, wenn sinnvoll", "Fertigung und Übergabe"]},
        ],
        "architects_faq": [
            ("Fertigen Sie einzelne ungewöhnliche Elemente?", "Ja, wenn der Umfang klar ist und das Element mit der Werkstatttechnologie sinnvoll gefertigt werden kann."),
            ("Arbeiten Sie mit Architekten?", "Ja. Am hilfreichsten sind Zeichnung, Referenzbild, Materialangabe und die Beschreibung des gewünschten Endeffekts."),
        ],
        "process_steps": [
            ("Sie senden Unterlagen", "Ein Foto, eine Zeichnung, eine Spezifikation oder eine kurze Beschreibung des Elements und des gewünschten Ergebnisses."),
            ("Wir stellen technische Fragen", "Material, Menge, Maße, Toleranzen, Termin, Oberfläche sowie Abholung oder Logistik."),
            ("Wir prüfen die Machbarkeit", "Wir bewerten, ob das Projekt zur Werkstatt passt und wirtschaftlich sinnvoll ist."),
            ("Muster oder Angebot", "Bei Serien kann ein Muster der erste Schritt sein. Einfachere Projekte gehen direkt in die Preisfindung."),
        ],
        "audience_cards": [
            {"title": "Holzelemente für Unternehmen", "body": "Kleinserien, Halbzeuge, Elemente nach Muster und B2B-Projekte, bei denen Wiederholbarkeit zählt.", "url": PATHS["production"], "cta": "B2B-Fertigung ansehen"},
            {"title": "Bauschreinerei", "body": "Treppen, Türen, Leisten, Einbauten und Holzdetails für lokale Bau- und Ausbauprojekte.", "url": PATHS["construction"], "cta": "Bauschreinerei ansehen"},
            {"title": "Sonderanfertigungen und anspruchsvolle Projekte", "body": "Ungewöhnliche Details, projektbezogene Arbeiten und Zusammenarbeit mit Architekten und Ausführenden.", "url": PATHS["architects"], "cta": "Projektzusammenarbeit ansehen"},
        ],
        "realization_cases": [
            {"title": "Holztreppe mit Metalldetail", "category": "Bauschreinerei", "photo": "stairs_project", "alt": "Holztreppe mit Geländer als Beispiel für maßgefertigte Schreinerarbeit", "meta": ["Material: Holz", "Umfang: Fertigung und Anpassung", "Typ: privater Investor"], "body": "Ein Beispiel dafür, wie Schreinerarbeit zu einem sichtbaren Element des Innenraums wird. Im neuen Portfolio sollte jedes Projekt Material, Herausforderungen und Ergebnis erklären."},
            {"title": "Holzdetail für Innenräume", "category": "Sonderanfertigung / Innenraum", "photo": "precision_detail", "alt": "Präzises Holzdetail für einen hochwertigen Innenraum", "meta": ["Umfang: Detail und Oberfläche", "Typ: individuelles Projekt", "Region: Pommern"], "body": "Solche Aufnahmen schaffen Vertrauen bei Architekten und Investoren. Wir brauchen Fotos, die Detail, Maßstab und Ausführung zeigen."},
            {"title": "Türen, Leisten und Schreinerteile", "category": "Türen / Leisten / Elemente", "photo": "doors_detail", "alt": "Holztüren als Beispiel für maßgefertigte Bauschreinerei", "meta": ["Umfang: Bauschreinerei", "Typ: Türen und Ausbau", "Anfrage: nach Fotos und Maßen"], "body": "Bauschreinerei bleibt ein wichtiger lokaler Bereich. Das Formular qualifiziert solche Anfragen über Standort, Termin und Umfang."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Werkstatt für Holzelemente, Bauschreinerei und Sonderprojekte", "eyebrow": "Produktions- und Bauschreinerei aus Pommern"},
            "production": {"title": "Holzelemente nach Maß für Unternehmen | Kajax", "description": "Kleinserien, Halbzeuge und Holzdetails nach Muster, Foto oder Zeichnung. Für Hersteller, Handwerker, Werbefirmen und Designer.", "hero_alt": "Wiederholbare Holzelemente in Kleinserie für ein Unternehmen", "eyebrow": "B2B / Kleinserien / Halbzeuge", "primary_cta": "Spezifikation zur Anfrage senden"},
            "construction": {"title": "Bauschreinerei in Pommern | Treppen, Türen und Leisten | Kajax", "description": "Holztreppen, Türen, Leisten, Einbauten und Ausbauelemente nach Maß. Tischlerei aus Gościcino für Pommern und Umgebung Wejherowo.", "hero_alt": "Holztreppe nach Maß als Beispiel für Bauschreinerei", "eyebrow": "Treppen / Türen / Leisten / Einbauten", "primary_cta": "Bauschreinerei anfragen"},
            "architects": {"title": "Tischlerei für Architekten, Designer und Firmen | Kajax", "description": "Sonderdetails aus Holz, projektbezogene Schreinerarbeit und maßgefertigte Elemente für Architekten, Designer, Ausführende und Unternehmen.", "hero_alt": "Ungewöhnliches Holzdetail nach Projekt für Architekt oder Unternehmen", "eyebrow": "Sonderanfertigung / Details / Spezialprojekte", "primary_cta": "Projekt besprechen"},
            "realizations": {"title": "Schreinerprojekte | Kajax", "description": "Ausgewählte Schreinerarbeiten: Treppen, Türen, Leisten, Holzdetails und Sonderanfertigungen. Jede Referenz soll Kontext und Umfang erklären.", "h1": "Referenzen mit Kontext, nicht nur eine Galerie", "lead": "Jede Referenz sollte Material, Umfang, gelöste Aufgabe und Ergebnis zeigen. Zum Start zeigen wir Projekttypen, die fotografiert und beschrieben werden sollten."},
            "quote": {"title": "Projekt zur Anfrage senden | Kajax", "description": "Senden Sie Foto, Zeichnung, Spezifikation oder kurze Projektbeschreibung. Wir prüfen, ob wir Element, Kleinserie oder Sonderanfertigung umsetzen können."},
            "contact": {"title": "Kontakt | Kajax Tischlerei Gościcino", "description": "Kontakt zu Kajax Tischlerei in Gościcino, Pommern. B2B-Anfragen, Bauschreinerei, Sonderprojekte und maßgefertigte Holzelemente."},
        },
    },
    "sv": {
        "production_sections": [
            {"title": "Vem vi arbetar med", "body": "Möbelproducenter, POS- och reklamföretag, inredningsentreprenörer, små tillverkare och designers som behöver trädelar i små eller återkommande serier.", "items": ["prototyper och prover", "korta serier", "delar efter prov", "återkommande samarbete efter processanpassning"]},
            {"title": "Vilka komponenter passar", "body": "De bästa projekten kan beskrivas tydligt med mått, material, ytbehandling och repeterbarhet. Logistik, packning och frakt bestäms när vi förstår projektet.", "items": ["lister, profiler och ramar", "halvfabrikat i trä", "display- och POS-komponenter", "delar för vidare montering eller ytbehandling"]},
            {"title": "Så kommer vi igång", "body": "Skicka ett foto, en ritning eller en kort beskrivning. Vi frågar om material, antal, toleranser, ytbehandling och tidplan. Vid större serier kan ett prov eller en prototyp vara första steget.", "items": ["foto eller ritning", "ungefärligt antal", "material och ytbehandling", "deadline samt upphämtning eller logistik"]},
        ],
        "production_faq": [
            ("Tar ni B2B-uppdrag utanför Pommern?", "Ja, om projektet och logistiken är rimliga. För B2B-komponenter kan vi diskutera samarbete i Polen och Europa, men frakt och packning avtalas individuellt."),
            ("Kan vi börja med ett prov?", "Ja. För återkommande komponenter är ett prov ofta det bästa sättet att bekräfta mått, ytbehandling och kostnad för en serie."),
        ],
        "construction_sections": [
            {"title": "Omfattning", "body": "Vi hjälper till med trädetaljer för bygg och inredning, särskilt där färdiga lösningar inte passar projektet eller den förväntade nivån.", "items": ["trätrappor", "inner- och ytterdörrar", "lister, trösklar, foder och fönsterbänkar", "inbyggnader och ovanliga avslutningsdetaljer"]},
            {"title": "När du bör kontakta oss", "body": "Ju tidigare vi känner till mått, plats för montage och önskad tidplan, desto lättare är det att bedöma genomförbarhet och undvika dyra ändringar på plats.", "items": ["ritningar eller mått", "foton av montageplatsen", "information om material", "projektets tidplan"]},
        ],
        "construction_faq": [
            ("Arbetar ni lokalt?", "För byggsnickeri prioriterar vi Pommern, Gościcino, Wejherowo och Tricity-området."),
            ("Kan jag skicka foton istället för ritning?", "Ja. Foton räcker för första samtalet, men för offert behövs mått och tekniska detaljer."),
        ],
        "architects_sections": [
            {"title": "När det är värt att skriva", "body": "När projektet kräver samtal om detalj, material, montage eller vettig tillverkningsteknik och färdiga lösningar inte räcker.", "items": ["detaljer till premiuminteriörer", "display- och kommersiella element", "specialanpassade inbyggnader", "återskapade eller ovanliga profiler"]},
            {"title": "Så samarbetar vi", "body": "Först klargör vi designintention och tekniska begränsningar. Därefter specificerar vi material, mått, ytbehandling, montage och tidplan.", "items": ["granskning av ritning eller foto", "teknisk precisering", "prov om det är relevant", "tillverkning och överlämning"]},
        ],
        "architects_faq": [
            ("Gör ni enstaka ovanliga element?", "Ja, om projektet har tydlig omfattning och kan tillverkas på ett tekniskt rimligt sätt."),
            ("Arbetar ni med arkitekter?", "Ja. Den bästa förfrågan innehåller ritning, referens, material och önskat slutresultat."),
        ],
        "process_steps": [
            ("Du skickar underlag", "Foto, ritning, specifikation eller en kort beskrivning av komponenten och önskat resultat."),
            ("Vi ställer tekniska frågor", "Material, antal, mått, toleranser, tidplan, ytbehandling samt upphämtning eller logistik."),
            ("Vi bedömer genomförbarhet", "Vi kontrollerar om projektet passar verkstaden och är ekonomiskt rimligt."),
            ("Prov eller offert", "Vid serier kan ett prov vara första steget. Enklare projekt kan gå direkt till offert."),
        ],
        "audience_cards": [
            {"title": "Träkomponenter för företag", "body": "Korta serier, halvfabrikat, komponenter efter prov och B2B-projekt där repeterbarhet är viktig.", "url": PATHS["production"], "cta": "Se B2B-produktion"},
            {"title": "Byggsnickeri", "body": "Trappor, dörrar, lister, inbyggnader och trädetaljer för lokala projekt.", "url": PATHS["construction"], "cta": "Se byggsnickeri"},
            {"title": "Special och krävande projekt", "body": "Ovanliga detaljer, projektbaserat arbete och samarbete med arkitekter och entreprenörer.", "url": PATHS["architects"], "cta": "Se projektsamarbete"},
        ],
        "realization_cases": [
            {"title": "Trätrappa med metalldetalj", "category": "Byggsnickeri", "photo": "stairs_project", "alt": "Trätrappa med räcke som exempel på specialsnickeri", "meta": ["material: trä", "omfattning: tillverkning och anpassning", "typ: privat investerare"], "body": "Ett exempel på hur snickeri kan bli en synlig del av interiören. I den nya portföljen bör varje projekt förklara material, utmaningar och resultat."},
            {"title": "Trädetalj för interiör", "category": "Special / interiör", "photo": "precision_detail", "alt": "Precis trädetalj för en premiuminteriör", "meta": ["omfattning: detalj och finish", "typ: individuellt projekt", "region: Pommern"], "body": "Sådana bilder bygger förtroende hos arkitekter och investerare. Vi behöver foton som visar detalj, skala och utförande."},
            {"title": "Dörrar, lister och snickeridelar", "category": "Dörrar / lister / delar", "photo": "doors_detail", "alt": "Trädörrar som exempel på måttanpassat byggsnickeri", "meta": ["omfattning: byggsnickeri", "typ: dörrar och finish", "offert: efter foton och mått"], "body": "Byggsnickeri är fortsatt ett viktigt lokalt område. Formuläret kvalificerar sådana förfrågningar genom plats, tidplan och omfattning."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snickeriverkstad för träkomponenter, byggsnickeri och specialprojekt", "eyebrow": "Produktions- och byggsnickeri från Pommern"},
            "production": {"title": "Träkomponenter på beställning för företag | Kajax", "description": "Korta serier, halvfabrikat och trädetaljer efter prov, foto eller ritning. För tillverkare, entreprenörer, reklamföretag och designers.", "hero_alt": "Återkommande träkomponenter tillverkade i kort serie för ett företag", "eyebrow": "B2B / korta serier / halvfabrikat", "primary_cta": "Skicka specifikation för offert"},
            "construction": {"title": "Byggsnickeri i Pommern | Trappor, dörrar och lister | Kajax", "description": "Trätrappor, dörrar, lister, inbyggnader och avslutningsdetaljer på mått. Snickeri från Gościcino för Pommern och området kring Wejherowo.", "hero_alt": "Måttanpassad trätrappa som exempel på byggsnickeri", "eyebrow": "Trappor / dörrar / lister / inbyggnader", "primary_cta": "Fråga om byggsnickeri"},
            "architects": {"title": "Snickeri för arkitekter, designers och företag | Kajax", "description": "Specialdetaljer i trä, projektbaserat snickeri och måttanpassade element för arkitekter, designers, entreprenörer och företag.", "hero_alt": "Ovanlig trädetalj tillverkad enligt projekt för arkitekt eller företag", "eyebrow": "Special / detaljer / särskilda projekt", "primary_cta": "Diskutera projekt"},
            "realizations": {"title": "Snickeriprojekt | Kajax", "description": "Utvalda snickeriprojekt: trappor, dörrar, lister, trädetaljer och specialarbete. Varje referens bör förklara kontext och omfattning.", "h1": "Referenser med kontext, inte bara ett galleri", "lead": "Varje referens bör visa material, omfattning, löst problem och resultat. I starten visar vi projekttyper som bör fotograferas och beskrivas."},
            "quote": {"title": "Skicka projekt för offert | Kajax", "description": "Skicka foto, ritning, specifikation eller kort projektbeskrivning. Vi bedömer om vi kan tillverka komponenten, serien eller specialsnickeriet."},
            "contact": {"title": "Kontakt | Kajax Snickeri Gościcino", "description": "Kontakt med Kajax Snickeri i Gościcino, Pommern. B2B-förfrågningar, byggsnickeri, specialprojekt och måttanpassat träarbete."},
        },
    },
    "da": {
        "production_sections": [
            {"title": "Hvem vi arbejder for", "body": "Møbelproducenter, POS- og reklamefirmaer, indretningsentreprenører, små producenter og designere, der har brug for trædele i små eller gentagelige serier.", "items": ["prototyper og prøver", "korte serier", "dele efter prøve", "løbende samarbejde efter procesafstemning"]},
            {"title": "Hvilke komponenter giver mening", "body": "De bedste projekter kan beskrives klart med mål, materiale, finish og gentagelighed. Logistik, pakning og forsendelse aftales, når vi kender projektet.", "items": ["lister, profiler og rammer", "halvfabrikata i træ", "display- og POS-komponenter", "dele til videre montage eller finish"]},
            {"title": "Sådan starter vi", "body": "Send et foto, en tegning eller en kort beskrivelse. Vi spørger ind til materiale, antal, tolerancer, finish og tidsplan. Ved større serier kan en prøve eller prototype være første skridt.", "items": ["foto eller tegning", "omtrentligt antal", "materiale og finish", "deadline samt afhentning eller logistik"]},
        ],
        "production_faq": [
            ("Tager I B2B-opgaver uden for Pommern?", "Ja, hvis projekt og logistik giver mening. For B2B-komponenter kan vi drøfte samarbejde i Polen og Europa; forsendelse og pakning aftales individuelt."),
            ("Kan vi starte med én prøve?", "Ja. For gentagelige komponenter er en prøve ofte den bedste måde at bekræfte mål, finish og pris for en serie."),
        ],
        "construction_sections": [
            {"title": "Omfang", "body": "Vi hjælper med trædetaljer til byggeri og indretning, især hvor standardløsninger ikke passer til projektet eller det ønskede niveau.", "items": ["trætrapper", "indvendige og udvendige døre", "lister, tærskler, gerigter og vinduesplader", "indbygninger og usædvanlige afslutningsdetaljer"]},
            {"title": "Hvornår du bør kontakte os", "body": "Jo tidligere vi kender mål, montagested og ønsket tidsplan, desto lettere er det at vurdere gennemførlighed og undgå dyre ændringer på stedet.", "items": ["tegninger eller mål", "fotos af montagestedet", "information om materiale", "projektets tidsplan"]},
        ],
        "construction_faq": [
            ("Arbejder I lokalt?", "For byggesnedkeri prioriterer vi Pommern, Gościcino, Wejherowo og Tricity-området."),
            ("Kan jeg sende fotos i stedet for tegning?", "Ja. Fotos er nok til den første samtale, men et tilbud kræver mål og tekniske detaljer."),
        ],
        "architects_sections": [
            {"title": "Hvornår det er værd at skrive", "body": "Når projektet kræver dialog om detalje, materiale, montage eller fornuftig produktionsteknik, og færdige løsninger ikke er nok.", "items": ["detaljer til premiuminteriør", "display- og erhvervselementer", "specialtilpassede indbygninger", "genskabte eller usædvanlige profiler"]},
            {"title": "Sådan samarbejder vi", "body": "Først afklarer vi designintention og tekniske begrænsninger. Derefter præciserer vi materiale, mål, finish, montage og tidsplan.", "items": ["gennemgang af tegning eller foto", "teknisk præcisering", "prøve hvis det giver mening", "produktion og aflevering"]},
        ],
        "architects_faq": [
            ("Laver I enkelte usædvanlige elementer?", "Ja, hvis projektet har et klart omfang og kan fremstilles teknisk fornuftigt."),
            ("Arbejder I med arkitekter?", "Ja. Den bedste forespørgsel indeholder tegning, reference, materiale og ønsket slutresultat."),
        ],
        "process_steps": [
            ("Du sender materiale", "Foto, tegning, specifikation eller en kort beskrivelse af komponenten og det ønskede resultat."),
            ("Vi stiller tekniske spørgsmål", "Materiale, antal, mål, tolerancer, tidsplan, finish samt afhentning eller logistik."),
            ("Vi vurderer gennemførlighed", "Vi kontrollerer, om projektet passer til værkstedet og giver økonomisk mening."),
            ("Prøve eller tilbud", "Ved serier kan en prøve være første skridt. Enklere projekter kan gå direkte til pris."),
        ],
        "audience_cards": [
            {"title": "Trækomponenter til virksomheder", "body": "Korte serier, halvfabrikata, komponenter efter prøve og B2B-projekter, hvor gentagelighed er vigtig.", "url": PATHS["production"], "cta": "Se B2B-produktion"},
            {"title": "Byggesnedkeri", "body": "Trapper, døre, lister, indbygninger og trædetaljer til lokale projekter.", "url": PATHS["construction"], "cta": "Se byggesnedkeri"},
            {"title": "Special og krævende projekter", "body": "Usædvanlige detaljer, projektbaseret arbejde og samarbejde med arkitekter og entreprenører.", "url": PATHS["architects"], "cta": "Se projektsamarbejde"},
        ],
        "realization_cases": [
            {"title": "Trætrappe med metaldetalje", "category": "Byggesnedkeri", "photo": "stairs_project", "alt": "Trætrappe med rækværk som eksempel på specialsnedkeri", "meta": ["materiale: træ", "omfang: produktion og tilpasning", "type: privat investor"], "body": "Et eksempel på, hvordan snedkerarbejde kan blive et synligt element i interiøret. I den nye portefølje bør hvert projekt forklare materiale, udfordringer og resultat."},
            {"title": "Trædetalje til interiør", "category": "Special / interiør", "photo": "precision_detail", "alt": "Præcis trædetalje til et premiuminteriør", "meta": ["omfang: detalje og finish", "type: individuelt projekt", "region: Pommern"], "body": "Sådanne billeder skaber tillid hos arkitekter og investorer. Vi har brug for fotos, der viser detalje, skala og udførelse."},
            {"title": "Døre, lister og snedkerdele", "category": "Døre / lister / dele", "photo": "doors_detail", "alt": "Trædøre som eksempel på måltilpasset byggesnedkeri", "meta": ["omfang: byggesnedkeri", "type: døre og finish", "tilbud: efter fotos og mål"], "body": "Byggesnedkeri er fortsat et vigtigt lokalt område. Formularen kvalificerer sådanne forespørgsler via placering, tidsplan og omfang."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snedkerværksted til trækomponenter, byggesnedkeri og specialprojekter", "eyebrow": "Produktions- og byggesnedkeri fra Pommern"},
            "production": {"title": "Trækomponenter på bestilling til virksomheder | Kajax", "description": "Korte serier, halvfabrikata og trædetaljer efter prøve, foto eller tegning. For producenter, entreprenører, reklamefirmaer og designere.", "hero_alt": "Gentagelige trækomponenter fremstillet i kort serie til en virksomhed", "eyebrow": "B2B / korte serier / halvfabrikata", "primary_cta": "Send specifikation til tilbud"},
            "construction": {"title": "Byggesnedkeri i Pommern | Trapper, døre og lister | Kajax", "description": "Trætrapper, døre, lister, indbygninger og afslutningsdetaljer på mål. Snedkeri fra Gościcino for Pommern og området omkring Wejherowo.", "hero_alt": "Måltilpasset trætrappe som eksempel på byggesnedkeri", "eyebrow": "Trapper / døre / lister / indbygninger", "primary_cta": "Spørg om byggesnedkeri"},
            "architects": {"title": "Snedkeri for arkitekter, designere og virksomheder | Kajax", "description": "Specialdetaljer i træ, projektbaseret snedkeri og måltilpassede elementer til arkitekter, designere, entreprenører og virksomheder.", "hero_alt": "Usædvanlig trædetalje fremstillet efter projekt til arkitekt eller virksomhed", "eyebrow": "Special / detaljer / særlige projekter", "primary_cta": "Drøft projekt"},
            "realizations": {"title": "Snedkeriprojekter | Kajax", "description": "Udvalgte snedkeriprojekter: trapper, døre, lister, trædetaljer og specialarbejde. Hver reference bør forklare kontekst og omfang.", "h1": "Referencer med kontekst, ikke kun et galleri", "lead": "Hver reference bør vise materiale, omfang, løst problem og resultat. Til start viser vi projekttyper, der bør fotograferes og beskrives."},
            "quote": {"title": "Send projekt til tilbud | Kajax", "description": "Send foto, tegning, specifikation eller kort projektbeskrivelse. Vi vurderer, om vi kan fremstille komponenten, serien eller specialsnedkeriet."},
            "contact": {"title": "Kontakt | Kajax Snedkeri Gościcino", "description": "Kontakt Kajax Snedkeri i Gościcino, Pommern. B2B-forespørgsler, byggesnedkeri, specialprojekter og måltilpasset træarbejde."},
        },
    },
    "no": {
        "production_sections": [
            {"title": "Hvem vi jobber for", "body": "Møbelprodusenter, POS- og reklamefirmaer, interiørentreprenører, små produsenter og designere som trenger tredeler i små eller repeterbare serier.", "items": ["prototyper og prøver", "korte serier", "deler etter prøve", "fast samarbeid etter prosessavklaring"]},
            {"title": "Hvilke komponenter passer", "body": "De beste prosjektene kan beskrives tydelig med mål, materiale, overflate og repeterbarhet. Logistikk, pakking og frakt avklares når vi kjenner prosjektet.", "items": ["lister, profiler og rammer", "halvfabrikata i tre", "display- og POS-komponenter", "deler for videre montering eller finish"]},
            {"title": "Slik starter vi", "body": "Send et bilde, en tegning eller en kort beskrivelse. Vi spør om materiale, antall, toleranser, overflate og tidsplan. Ved større serier kan en prøve eller prototype være første steg.", "items": ["bilde eller tegning", "omtrentlig antall", "materiale og overflate", "frist samt henting eller logistikk"]},
        ],
        "production_faq": [
            ("Tar dere B2B-oppdrag utenfor Pommern?", "Ja, hvis prosjekt og logistikk gir mening. For B2B-komponenter kan vi diskutere samarbeid i Polen og Europa; frakt og pakking avtales individuelt."),
            ("Kan vi starte med én prøve?", "Ja. For repeterbare komponenter er en prøve ofte den beste måten å bekrefte mål, overflate og kostnad for en serie."),
        ],
        "construction_sections": [
            {"title": "Omfang", "body": "Vi hjelper med tredetaljer til bygg og interiør, særlig der standardløsninger ikke passer prosjektet eller ønsket nivå.", "items": ["tretrapper", "innvendige og utvendige dører", "lister, terskler, gerikter og vindusbrett", "innbygginger og uvanlige avslutningsdetaljer"]},
            {"title": "Når du bør ta kontakt", "body": "Jo tidligere vi kjenner mål, monteringssted og ønsket tidsplan, desto lettere er det å vurdere gjennomførbarhet og unngå dyre endringer på stedet.", "items": ["tegninger eller mål", "bilder av monteringsstedet", "informasjon om materiale", "prosjektets tidsplan"]},
        ],
        "construction_faq": [
            ("Jobber dere lokalt?", "For byggsnekkerarbeid prioriterer vi Pommern, Gościcino, Wejherowo og Tricity-området."),
            ("Kan jeg sende bilder i stedet for tegning?", "Ja. Bilder holder for første samtale, men et tilbud krever mål og tekniske detaljer."),
        ],
        "architects_sections": [
            {"title": "Når det er verdt å skrive", "body": "Når prosjektet krever dialog om detalj, materiale, montering eller fornuftig produksjonsteknikk, og ferdige løsninger ikke er nok.", "items": ["detaljer til premiuminteriør", "display- og næringselementer", "spesialtilpassede innbygginger", "gjenskapte eller uvanlige profiler"]},
            {"title": "Slik samarbeider vi", "body": "Først avklarer vi designintensjon og tekniske begrensninger. Deretter presiserer vi materiale, mål, overflate, montering og tidsplan.", "items": ["gjennomgang av tegning eller bilde", "teknisk presisering", "prøve hvis det gir mening", "produksjon og overlevering"]},
        ],
        "architects_faq": [
            ("Lager dere enkelte uvanlige elementer?", "Ja, hvis prosjektet har tydelig omfang og kan lages på en teknisk fornuftig måte."),
            ("Jobber dere med arkitekter?", "Ja. Den beste forespørselen inneholder tegning, referanse, materiale og ønsket sluttresultat."),
        ],
        "process_steps": [
            ("Du sender materiale", "Bilde, tegning, spesifikasjon eller en kort beskrivelse av komponenten og ønsket resultat."),
            ("Vi stiller tekniske spørsmål", "Materiale, antall, mål, toleranser, tidsplan, overflate samt henting eller logistikk."),
            ("Vi vurderer gjennomførbarhet", "Vi sjekker om prosjektet passer verkstedet og gir økonomisk mening."),
            ("Prøve eller tilbud", "Ved serier kan en prøve være første steg. Enklere prosjekter kan gå direkte til pris."),
        ],
        "audience_cards": [
            {"title": "Trekomponenter for bedrifter", "body": "Korte serier, halvfabrikata, komponenter etter prøve og B2B-prosjekter der repeterbarhet er viktig.", "url": PATHS["production"], "cta": "Se B2B-produksjon"},
            {"title": "Byggsnekkerarbeid", "body": "Trapper, dører, lister, innbygginger og tredetaljer for lokale prosjekter.", "url": PATHS["construction"], "cta": "Se byggsnekkerarbeid"},
            {"title": "Spesial og krevende prosjekter", "body": "Uvanlige detaljer, prosjektbasert arbeid og samarbeid med arkitekter og entreprenører.", "url": PATHS["architects"], "cta": "Se prosjektsamarbeid"},
        ],
        "realization_cases": [
            {"title": "Tretrapp med metalldetalj", "category": "Byggsnekkerarbeid", "photo": "stairs_project", "alt": "Tretrapp med rekkverk som eksempel på spesialtilpasset snekkerarbeid", "meta": ["materiale: tre", "omfang: produksjon og tilpasning", "type: privat investor"], "body": "Et eksempel på hvordan snekkerarbeid kan bli et synlig element i interiøret. I den nye porteføljen bør hvert prosjekt forklare materiale, utfordringer og resultat."},
            {"title": "Tredetalj til interiør", "category": "Spesial / interiør", "photo": "precision_detail", "alt": "Presis tredetalj til et premiuminteriør", "meta": ["omfang: detalj og finish", "type: individuelt prosjekt", "region: Pommern"], "body": "Slike bilder bygger tillit hos arkitekter og investorer. Vi trenger foto som viser detalj, skala og utførelse."},
            {"title": "Dører, lister og snekkerdeler", "category": "Dører / lister / deler", "photo": "doors_detail", "alt": "Tredører som eksempel på måltilpasset byggsnekkerarbeid", "meta": ["omfang: byggsnekkerarbeid", "type: dører og finish", "tilbud: etter bilder og mål"], "body": "Byggsnekkerarbeid er fortsatt et viktig lokalt område. Skjemaet kvalifiserer slike forespørsler via sted, tidsplan og omfang."},
        ],
        "page_updates": {
            "home": {"hero_alt": "Snekkerverksted for trekomponenter, byggsnekkerarbeid og spesialprosjekter", "eyebrow": "Produksjons- og byggsnekkerverksted fra Pommern"},
            "production": {"title": "Trekomponenter på bestilling for bedrifter | Kajax", "description": "Korte serier, halvfabrikata og tredetaljer etter prøve, bilde eller tegning. For produsenter, entreprenører, reklamefirmaer og designere.", "hero_alt": "Repeterbare trekomponenter produsert i kort serie for en bedrift", "eyebrow": "B2B / korte serier / halvfabrikata", "primary_cta": "Send spesifikasjon for vurdering"},
            "construction": {"title": "Byggsnekkerarbeid i Pommern | Trapper, dører og lister | Kajax", "description": "Tretrapper, dører, lister, innbygginger og avslutningsdetaljer på mål. Snekkerverksted fra Gościcino for Pommern og området rundt Wejherowo.", "hero_alt": "Måltilpasset tretrapp som eksempel på byggsnekkerarbeid", "eyebrow": "Trapper / dører / lister / innbygginger", "primary_cta": "Spør om byggsnekkerarbeid"},
            "architects": {"title": "Snekkerverksted for arkitekter, designere og bedrifter | Kajax", "description": "Spesialdetaljer i tre, prosjektbasert snekkerarbeid og måltilpassede elementer for arkitekter, designere, entreprenører og bedrifter.", "hero_alt": "Uvanlig tredetalj laget etter prosjekt for arkitekt eller bedrift", "eyebrow": "Spesial / detaljer / særlige prosjekter", "primary_cta": "Diskuter prosjekt"},
            "realizations": {"title": "Snekkerprosjekter | Kajax", "description": "Utvalgte snekkerprosjekter: trapper, dører, lister, tredetaljer og spesialarbeid. Hver referanse bør forklare kontekst og omfang.", "h1": "Referanser med kontekst, ikke bare et galleri", "lead": "Hver referanse bør vise materiale, omfang, løst problem og resultat. Til start viser vi prosjekttyper som bør fotograferes og beskrives."},
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


def _with_runtime_fields(page_key, page):
    page = page.copy()
    page["key"] = page_key
    page["path"] = PATHS[page_key]
    page["template"] = TEMPLATES[page_key]
    if "hero_photo" in page:
        page["hero_photo"] = PHOTO_PLACEHOLDERS[page["hero_photo"]]
    if "b2b_photo" in page:
        page["b2b_photo"] = PHOTO_PLACEHOLDERS[page["b2b_photo"]]
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
    return _with_runtime_fields(page_key, content["pages"][page_key])


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
