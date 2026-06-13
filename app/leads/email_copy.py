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
        "body": "Otrzymaliśmy opis projektu i wrócimy z odpowiedzią po analizie zakresu, materiału, ilości oraz terminu. Jeśli do wyceny zabraknie informacji, dopytamy mailowo lub telefonicznie.",
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
        "body": "We have received your project description and will reply after reviewing the scope, material, quantity and timing. If anything is missing, we will ask by email or phone.",
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
        "body": "Wir haben Ihre Projektbeschreibung erhalten und melden uns nach Prüfung von Umfang, Material, Menge und Termin. Falls Informationen fehlen, fragen wir per E-Mail oder telefonisch nach.",
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
        "body": "Vi har tagit emot projektbeskrivningen och återkommer efter att vi granskat omfattning, material, antal och tidplan. Om något saknas frågar vi via e-post eller telefon.",
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
        "body": "Vi har modtaget projektbeskrivelsen og vender tilbage efter gennemgang af omfang, materiale, antal og tidsplan. Hvis der mangler oplysninger, spørger vi via e-mail eller telefon.",
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
        "body": "Vi har mottatt prosjektbeskrivelsen og kommer tilbake etter å ha vurdert omfang, materiale, antall og tidsplan. Hvis noe mangler, spør vi på e-post eller telefon.",
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
