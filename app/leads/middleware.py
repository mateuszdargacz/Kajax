from leads.attribution import update_attribution_from_request


class AttributionCaptureMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "GET" and not request.path.startswith(("/admin", "/static", "/media")):
            try:
                update_attribution_from_request(request)
            except Exception:
                pass
        return self.get_response(request)
