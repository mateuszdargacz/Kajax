$(document).ready(function () {

    (function ($) {
        "use strict";


        jQuery.validator.addMethod('answercheck', function (value, element) {
            return this.optional(element) || /^\bcat\b$/.test(value);
        }, "type the correct answer -_-");

        // validate contactForm form
        $(function () {
            $('form').each(function () {  // attach to all form elements on page

                $(this).validate({
                    rules: {
                        name: {
                            required: true,
                            minlength: 3
                        },
                        email: {
                            required: true,
                            email: true
                        },
                        subject: {
                            required: false,
                            minlength: 7
                        },
                        message: {
                            required: true,
                            minlength: 25
                        }
                    },
                    messages: {
                        name: {
                            required: "Musimy wiedzieć kto pisze...",
                            minlength: "nie słyszałem o tak krótkim imieniu..."
                        },
                        email: {
                            required: "Do kogo mamy odpisać???"
                        },
                        subject: {
                            required: "O czym chciałbyś napisać? ",
                            minlength: "Za krótki tytuł wiadomości"
                        },
                        message: {
                            required: "um... nie lubimy pustych wiadomości...",
                            minlength: "Tylko tyle? napisz coś więcej!"
                        }
                    },
                    submitHandler: function (form) {
                        var $form = $(form);
                        $form.ajaxSubmit({
                            type: "POST",
                            data: $form.serialize(),
                            url: "/api/message/",
                            success: function (res) {
                                $form.find(':input').attr('disabled', 'disabled');
                                $form.fadeTo("slow", 0.15, function () {
                                    $(this).find(':input').attr('disabled', 'disabled');
                                    $(this).find('label').css('cursor', 'default');
                                    $form.parent().find('#success').fadeIn();
                                });
                            },
                            error: function (res) {
                                $form.fadeTo("slow", 0.15, function () {
                                    $form.parent().find('#error').fadeIn();
                                });
                            }
                        })
                    }
                })
            });
        })

    })(jQuery)
})