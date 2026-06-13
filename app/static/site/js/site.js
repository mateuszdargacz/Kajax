(function () {
    window.dataLayer = window.dataLayer || [];

    var body = document.body || {};
    var pageContext = {
        page_key: body.dataset ? body.dataset.pageKey || "" : "",
        page_type: body.dataset ? body.dataset.pageType || "" : "",
        business_line: body.dataset ? body.dataset.businessLine || "" : "",
        service_area: body.dataset ? body.dataset.serviceArea || "" : "",
        language: body.dataset ? body.dataset.language || document.documentElement.lang || "" : document.documentElement.lang || "",
    };

    var projectBusinessLines = {
        b2b_components: "b2b_wooden_components",
        construction_joinery: "construction_joinery",
        custom_artistic: "custom_architectural_details",
        other: "mixed",
    };

    function assign(target, source) {
        Object.keys(source || {}).forEach(function (key) {
            if (source[key] !== undefined && source[key] !== null && source[key] !== "") {
                target[key] = source[key];
            }
        });
        return target;
    }

    function pushEvent(name, params) {
        window.dataLayer.push(assign(assign({ event: name }, pageContext), params || {}));
    }

    function linkUrl(link) {
        return link.getAttribute("href") || link.href || "";
    }

    function eventBusinessLine(element, projectType) {
        if (projectType && projectBusinessLines[projectType]) {
            return projectBusinessLines[projectType];
        }
        if (element && element.dataset && element.dataset.businessLine) {
            return element.dataset.businessLine;
        }
        return pageContext.business_line;
    }

    function eventIntent(link) {
        var href = linkUrl(link);
        if (link.dataset && link.dataset.ctaIntent) {
            return link.dataset.ctaIntent;
        }
        if (href.indexOf("tel:") === 0) {
            return "phone";
        }
        if (href.indexOf("mailto:") === 0) {
            return "email";
        }
        if (href.indexOf("/wycena/") !== -1) {
            return "quote";
        }
        if (href.indexOf("jak-przygotowac-zapytanie") !== -1) {
            return "guide";
        }
        return "navigation";
    }

    function currentProjectType(form) {
        var field = form ? form.querySelector("[name='inquiry_type']") : null;
        return field ? field.value || "" : "";
    }

    function fieldStep(fieldName) {
        if (fieldName === "name" || fieldName === "phone" || fieldName === "email") {
            return "contact";
        }
        if (fieldName === "inquiry_type" || fieldName === "scale") {
            return "project_type";
        }
        if (fieldName === "message" || fieldName === "company" || fieldName === "location" || fieldName === "expected_timing") {
            return "scope";
        }
        if (fieldName === "attachments") {
            return "files";
        }
        if (fieldName === "consent") {
            return "consent";
        }
        return "other";
    }

    function hasCompletedValue(field) {
        if (!field || !field.name) {
            return false;
        }
        if (field.type === "checkbox") {
            return field.checked;
        }
        if (field.type === "file") {
            return field.files && field.files.length > 0;
        }
        return String(field.value || "").trim().length > 0;
    }

    function caseParams(element) {
        if (!element) {
            return {};
        }
        return {
            case_id: element.dataset.caseId || "",
            case_type: element.dataset.caseType || "",
            business_line: eventBusinessLine(element),
        };
    }

    pushEvent("kajax_page_view");

    var scrollThresholds = [25, 50, 75, 90];
    var sentScrollDepths = {};
    function trackScrollDepth() {
        var documentHeight = Math.max(
            document.body.scrollHeight,
            document.documentElement.scrollHeight,
            document.body.offsetHeight,
            document.documentElement.offsetHeight,
        );
        var viewportBottom = window.scrollY + window.innerHeight;
        var scrollable = Math.max(documentHeight - window.innerHeight, 1);
        var percent = Math.min(100, Math.round((viewportBottom - window.innerHeight) / scrollable * 100));
        scrollThresholds.forEach(function (threshold) {
            if (!sentScrollDepths[threshold] && percent >= threshold) {
                sentScrollDepths[threshold] = true;
                pushEvent("scroll_depth", { percent: threshold });
            }
        });
    }
    window.addEventListener("scroll", trackScrollDepth, { passive: true });
    window.addEventListener("load", trackScrollDepth);

    document.querySelectorAll("[data-track='phone_click']").forEach(function (link) {
        link.addEventListener("click", function () {
            pushEvent("phone_click", {
                link_url: linkUrl(link),
                cta_location: link.dataset.ctaLocation || "",
                business_line: eventBusinessLine(link),
            });
        });
    });

    document.querySelectorAll("[data-track='email_click']").forEach(function (link) {
        link.addEventListener("click", function () {
            pushEvent("email_click", {
                link_url: linkUrl(link),
                cta_location: link.dataset.ctaLocation || "",
                business_line: eventBusinessLine(link),
            });
        });
    });

    document.querySelectorAll("[data-track-cta]").forEach(function (link) {
        link.addEventListener("click", function () {
            var params = {
                cta_id: link.dataset.trackCta || "",
                cta_location: link.dataset.ctaLocation || "",
                cta_text: (link.textContent || "").trim(),
                link_url: linkUrl(link),
                business_line: eventBusinessLine(link),
                intent: eventIntent(link),
            };
            pushEvent("cta_click", params);
            if (pageContext.page_type === "guide") {
                pushEvent("guide_cta_click", params);
            }
            var caseElement = link.closest("[data-track-view]");
            if (caseElement) {
                pushEvent("portfolio_card_click", assign(caseParams(caseElement), { link_url: linkUrl(link) }));
            }
        });
    });

    var quoteForm = document.querySelector("[data-quote-form]");
    if (quoteForm) {
        var started = false;
        var viewed = false;
        var sentSteps = {};
        var completedFields = {};

        function quoteParams(extra) {
            var projectType = currentProjectType(quoteForm);
            return assign(
                {
                    project_type: projectType,
                    business_line: eventBusinessLine(quoteForm, projectType),
                },
                extra || {},
            );
        }

        function pushFormView() {
            if (!viewed) {
                viewed = true;
                pushEvent("quote_form_view", quoteParams());
            }
        }

        if ("IntersectionObserver" in window) {
            var quoteObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        pushFormView();
                    }
                });
            }, { threshold: 0.3 });
            quoteObserver.observe(quoteForm);
        } else {
            pushFormView();
        }

        if (quoteForm.dataset.hasErrors === "true") {
            pushEvent("quote_form_submit_error", quoteParams({ error_type: "validation" }));
        }

        quoteForm.addEventListener("input", function (event) {
            if (!started) {
                started = true;
                pushEvent("quote_form_start", quoteParams({ field_name: event.target.name || "" }));
            }
        });

        quoteForm.addEventListener("change", function (event) {
            var field = event.target;
            var fieldName = field.name || "";
            var stepName = fieldStep(fieldName);
            if (!sentSteps[stepName]) {
                sentSteps[stepName] = true;
                pushEvent("quote_form_step", quoteParams({ step_name: stepName }));
            }
            if (field.type === "file" && field.files && field.files.length) {
                pushEvent("file_upload_complete", quoteParams({ file_count: field.files.length }));
            }
            if (fieldName === "inquiry_type") {
                pushEvent("project_type_select", quoteParams());
            }
            if (hasCompletedValue(field) && !completedFields[fieldName]) {
                completedFields[fieldName] = true;
                pushEvent("quote_form_field_complete", quoteParams({ field_name: fieldName }));
            }
        });

        quoteForm.addEventListener("focusout", function (event) {
            var field = event.target;
            var fieldName = field.name || "";
            if (hasCompletedValue(field) && !completedFields[fieldName]) {
                completedFields[fieldName] = true;
                pushEvent("quote_form_field_complete", quoteParams({ field_name: fieldName }));
            }
        });

        quoteForm.addEventListener("submit", function () {
            pushEvent("quote_form_submit_attempt", quoteParams({ intent: "quote" }));
        });
    }

    var success = document.querySelector("[data-quote-success]");
    if (success) {
        var successParams = {
            lead_type: success.dataset.leadType || "quote_request",
            project_type: success.dataset.projectType || "",
            business_line: success.dataset.businessLine || eventBusinessLine(success, success.dataset.projectType || ""),
        };
        pushEvent("quote_thank_you_view", successParams);
        pushEvent("generate_lead", successParams);
    }

    if ("IntersectionObserver" in window) {
        var portfolioObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !entry.target.dataset.tracked) {
                    entry.target.dataset.tracked = "true";
                    pushEvent(entry.target.dataset.trackView || "portfolio_view", caseParams(entry.target));
                    if (pageContext.page_key === "realizations") {
                        pushEvent("case_study_view", caseParams(entry.target));
                    }
                }
            });
        }, { threshold: 0.45 });

        document.querySelectorAll("[data-track-view]").forEach(function (element) {
            portfolioObserver.observe(element);
        });

        var guideObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !entry.target.dataset.guideTracked) {
                    entry.target.dataset.guideTracked = "true";
                    pushEvent("guide_section_view", {
                        section_id: entry.target.dataset.guideSection || "",
                    });
                }
            });
        }, { threshold: 0.45 });

        document.querySelectorAll("[data-guide-section]").forEach(function (element) {
            guideObserver.observe(element);
        });

        var contactObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !entry.target.dataset.contactTracked) {
                    entry.target.dataset.contactTracked = "true";
                    pushEvent("contact_panel_view", {
                        panel_id: entry.target.dataset.contactPanel || "",
                    });
                }
            });
        }, { threshold: 0.45 });

        document.querySelectorAll("[data-contact-panel]").forEach(function (element) {
            contactObserver.observe(element);
        });
    }

    document.querySelectorAll(".faq-list details").forEach(function (details, index) {
        details.addEventListener("toggle", function () {
            if (details.open && !details.dataset.faqTracked) {
                details.dataset.faqTracked = "true";
                pushEvent("faq_open", {
                    faq_id: pageContext.page_key + "_faq_" + (index + 1),
                });
            }
        });
    });
})();
