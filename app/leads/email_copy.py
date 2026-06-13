NOTIFICATION_COPY = {
    "subject": "Nowe zapytanie Kajax: {inquiry_type}",
    "title": "Nowe zapytanie z formularza Kajax",
    "saved_note": "Zapytanie zapisane w panelu admina.",
    "fields": {
        "name": "Imię",
        "email": "Email",
        "phone": "Telefon",
        "company": "Firma",
        "inquiry_type": "Typ zapytania",
        "scale": "Skala",
        "location": "Lokalizacja",
        "expected_timing": "Termin",
        "message": "Opis",
    },
}

CONFIRMATION_COPY = {
    "pl": {
        "subject": "Potwierdzenie otrzymania zapytania - Kajax",
        "greeting": "Dzień dobry,",
        "intro": "dziękujemy za przesłanie zapytania do Kajax Stolarstwo.",
        "body": "Otrzymaliśmy wiadomość. Sprawdzimy opis, materiał, skalę i sposób wykonania, a potem wrócimy z odpowiedzią. Jeśli do rzetelnej wyceny zabraknie danych, odpiszemy albo zadzwonimy z konkretnymi pytaniami.",
        "summary": "Podsumowanie",
        "inquiry_type": "Typ zapytania",
        "scale": "Skala",
        "location": "Lokalizacja",
        "closing": "Pozdrawiamy,\nKajax Stolarstwo",
    },
    "en": {
        "subject": "We received your inquiry - Kajax",
        "greeting": "Hello,",
        "intro": "thank you for sending your inquiry to Kajax Joinery.",
        "body": "We have received your project description. We will review the scope, material, quantity, timing and logistics, then reply. If anything is missing for the next pricing step, we will ask by email or phone.",
        "summary": "Summary",
        "inquiry_type": "Inquiry type",
        "scale": "Scale",
        "location": "Location",
        "closing": "Best regards,\nKajax Joinery",
    },
    "de": {
        "subject": "Wir haben Ihre Anfrage erhalten - Kajax",
        "greeting": "Guten Tag,",
        "intro": "vielen Dank für Ihre Anfrage an Kajax Tischlerei.",
        "body": "Wir haben Ihre Projektbeschreibung erhalten. Wir prüfen Umfang, Material, Menge, Termin und Logistik und melden uns danach. Falls Informationen für den nächsten Schritt der Preisfindung fehlen, fragen wir per E-Mail oder telefonisch nach.",
        "summary": "Zusammenfassung",
        "inquiry_type": "Art der Anfrage",
        "scale": "Umfang",
        "location": "Standort",
        "closing": "Mit freundlichen Grüßen\nKajax Tischlerei",
    },
    "sv": {
        "subject": "Vi har tagit emot din förfrågan - Kajax",
        "greeting": "Hej,",
        "intro": "tack för att du skickade din förfrågan till Kajax Snickeri.",
        "body": "Vi har tagit emot projektbeskrivningen. Vi granskar omfattning, material, antal, tidplan och logistik och återkommer därefter. Om något saknas för nästa offertsteg frågar vi via e-post eller telefon.",
        "summary": "Sammanfattning",
        "inquiry_type": "Typ av förfrågan",
        "scale": "Omfattning",
        "location": "Plats",
        "closing": "Vänliga hälsningar\nKajax Snickeri",
    },
    "da": {
        "subject": "Vi har modtaget din forespørgsel - Kajax",
        "greeting": "Hej,",
        "intro": "tak fordi du sendte din forespørgsel til Kajax Snedkeri.",
        "body": "Vi har modtaget projektbeskrivelsen. Vi gennemgår omfang, materiale, antal, tidsplan og logistik og vender tilbage derefter. Hvis der mangler oplysninger til næste tilbudsskridt, spørger vi via e-mail eller telefon.",
        "summary": "Opsummering",
        "inquiry_type": "Type forespørgsel",
        "scale": "Omfang",
        "location": "Placering",
        "closing": "Med venlig hilsen\nKajax Snedkeri",
    },
    "no": {
        "subject": "Vi har mottatt forespørselen din - Kajax",
        "greeting": "Hei,",
        "intro": "takk for at du sendte forespørselen til Kajax Snekkerverksted.",
        "body": "Vi har mottatt prosjektbeskrivelsen. Vi vurderer omfang, materiale, antall, tidsplan og logistikk og kommer tilbake etterpå. Hvis noe mangler for neste prissteg, spør vi på e-post eller telefon.",
        "summary": "Oppsummering",
        "inquiry_type": "Type forespørsel",
        "scale": "Omfang",
        "location": "Sted",
        "closing": "Vennlig hilsen\nKajax Snekkerverksted",
    },
}


def normalize_language(language_code):
    return (language_code or "pl").split("-")[0]


def get_confirmation_copy(language_code):
    return CONFIRMATION_COPY.get(normalize_language(language_code), CONFIRMATION_COPY["pl"])
