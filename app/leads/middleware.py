from leads.attribution import update_attribution_from_request


SKIPPED_PATHS = {"/favicon.ico", "/robots.txt", "/sitemap.xml"}
SKIPPED_PREFIXES = ("/admin", "/static", "/media")


class AttributionCaptureMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "GET" and request.path not in SKIPPED_PATHS and not request.path.startswith(SKIPPED_PREFIXES):
            try:
                update_attribution_from_request(request)
            except Exception:
                pass
        return self.get_response(request)
