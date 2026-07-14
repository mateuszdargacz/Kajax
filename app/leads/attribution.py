from urllib.parse import urlparse


TRACKING_FIELDS = [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_content",
    "utm_term",
    "utm_id",
    "gclid",
    "gbraid",
    "wbraid",
    "fbclid",
    "msclkid",
    "ttclid",
    "li_fat_id",
    "visitor_id",
    "session_id",
    "piecode_visitor_id",
    "piecode_session_id",
]

VISITOR_ID_FIELDS = ["visitor_id", "piecode_visitor_id"]
SESSION_ID_FIELDS = ["session_id", "piecode_session_id"]

SESSION_KEY = "marketing_attribution"


def clean_value(value, max_length=500):
    return str(value or "").strip()[:max_length]


def request_path(request):
    try:
        return request.get_full_path()[:500]
    except Exception:
        return clean_value(getattr(request, "path", ""), 500)


def referrer_from_request(request):
    return clean_value(request.META.get("HTTP_REFERER", ""), 500)


def traffic_source(source="", medium=""):
    source = clean_value(source, 80).lower()
    medium = clean_value(medium, 80).lower()
    if source and medium:
        return f"{source} / {medium}"
    if source:
        return source
    return "direct"


def extract_tracking_params(mapping):
    return {
        field: clean_value(mapping.get(field), 500)
        for field in TRACKING_FIELDS
        if clean_value(mapping.get(field), 500)
    }


def tracking_from_post(request):
    return extract_tracking_params(request.POST)


def tracking_from_cookies(request):
    return extract_tracking_params(request.COOKIES)


def update_attribution_from_request(request):
    current = dict(request.session.get(SESSION_KEY, {}) or {})
    query_tracking = extract_tracking_params(request.GET)
    referrer = referrer_from_request(request)
    path = request_path(request)

    if not current:
        current.update({
            "first_landing_path": path,
            "first_referrer": referrer,
            "first_traffic_source": traffic_source(
                query_tracking.get("utm_source", ""),
                query_tracking.get("utm_medium", ""),
            ),
        })

    if query_tracking:
        for key, value in query_tracking.items():
            current[f"last_{key}"] = value
            current.setdefault(f"first_{key}", value)
        current["last_landing_path"] = path
        current["last_referrer"] = referrer
        current["last_traffic_source"] = traffic_source(
            query_tracking.get("utm_source", current.get("last_utm_source", "")),
            query_tracking.get("utm_medium", current.get("last_utm_medium", "")),
        )
        if "utm_source" in query_tracking:
            current.setdefault("first_traffic_source", traffic_source(
                query_tracking.get("utm_source", ""),
                query_tracking.get("utm_medium", ""),
            ))
    else:
        current.setdefault("last_landing_path", path)
        if referrer:
            current.setdefault("last_referrer", referrer)

    request.session[SESSION_KEY] = current
    return current


def attribution_for_lead(request):
    session_attribution = dict(request.session.get(SESSION_KEY, {}) or {})
    posted_tracking = {
        **tracking_from_cookies(request),
        **extract_tracking_params(request.GET),
        **tracking_from_post(request),
    }
    path = request_path(request)
    referrer = referrer_from_request(request)

    for key, value in posted_tracking.items():
        session_attribution[f"last_{key}"] = value
        session_attribution.setdefault(f"first_{key}", value)

    source = session_attribution.get("last_utm_source") or posted_tracking.get("utm_source", "")
    medium = session_attribution.get("last_utm_medium") or posted_tracking.get("utm_medium", "")
    campaign = session_attribution.get("last_utm_campaign") or posted_tracking.get("utm_campaign", "")
    content = session_attribution.get("last_utm_content") or posted_tracking.get("utm_content", "")
    term = session_attribution.get("last_utm_term") or posted_tracking.get("utm_term", "")
    utm_id = session_attribution.get("last_utm_id") or posted_tracking.get("utm_id", "")

    payload = {
        **session_attribution,
        "landing_path": session_attribution.get("first_landing_path") or path,
        "last_landing_path": path,
        "last_referrer": referrer or session_attribution.get("last_referrer", ""),
        "traffic_source": traffic_source(source, medium),
        "last_traffic_source": traffic_source(source, medium),
        "last_utm_source": source,
        "last_utm_medium": medium,
        "last_utm_campaign": campaign,
        "last_utm_content": content,
        "last_utm_term": term,
        "last_utm_id": utm_id,
    }

    for click_id in ["gclid", "gbraid", "wbraid", "fbclid", "msclkid", "ttclid", "li_fat_id"]:
        value = session_attribution.get(f"last_{click_id}") or posted_tracking.get(click_id, "")
        if value:
            payload[click_id] = value

    for output_key, fields in {"visitor_id": VISITOR_ID_FIELDS, "session_id": SESSION_ID_FIELDS}.items():
        value = next(
            (
                session_attribution.get(f"last_{field}") or posted_tracking.get(field, "")
                for field in fields
                if session_attribution.get(f"last_{field}") or posted_tracking.get(field, "")
            ),
            "",
        )
        if value:
            payload[output_key] = value

    return {key: value for key, value in payload.items() if value}


def host_from_site_url(site_url):
    parsed = urlparse(site_url or "")
    return parsed.netloc or parsed.path
