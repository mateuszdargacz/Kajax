(function () {
    window.dataLayer = window.dataLayer || [];

    function pushEvent(name, params) {
        window.dataLayer.push(Object.assign({ event: name }, params || {}));
    }

    document.querySelectorAll("[data-track='phone_click']").forEach(function (link) {
        link.addEventListener("click", function () {
            pushEvent("phone_click", { link_url: link.href });
        });
    });

    document.querySelectorAll("[data-track='email_click']").forEach(function (link) {
        link.addEventListener("click", function () {
            pushEvent("email_click", { link_url: link.href });
        });
    });

    var quoteForm = document.querySelector("[data-quote-form]");
    if (quoteForm) {
        var started = false;
        var viewed = false;
        if ("IntersectionObserver" in window) {
            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (!viewed && entry.isIntersecting) {
                        viewed = true;
                        pushEvent("quote_form_view");
                    }
                });
            }, { threshold: 0.3 });
            observer.observe(quoteForm);
        }

        quoteForm.addEventListener("input", function (event) {
            if (!started) {
                started = true;
                pushEvent("quote_form_start", { field_name: event.target.name || "" });
            }
        });

        quoteForm.addEventListener("change", function (event) {
            if (event.target.type === "file" && event.target.files.length) {
                pushEvent("file_upload_complete", { file_count: event.target.files.length });
            }
            if (event.target.name === "inquiry_type") {
                pushEvent("project_type_select", { project_type: event.target.value });
            }
        });

        quoteForm.addEventListener("submit", function () {
            pushEvent("generate_lead", { lead_type: "quote_request" });
        });
    }

    if ("IntersectionObserver" in window) {
        var portfolioObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !entry.target.dataset.tracked) {
                    entry.target.dataset.tracked = "true";
                    pushEvent(entry.target.dataset.trackView || "portfolio_view");
                }
            });
        }, { threshold: 0.45 });

        document.querySelectorAll("[data-track-view]").forEach(function (element) {
            portfolioObserver.observe(element);
        });
    }
})();
