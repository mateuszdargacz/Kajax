# -*- coding: utf-8 -*-
from functools import update_wrapper

from django.utils.encoding import force_text

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

from home.models import Slider, CompanyData, SliderImage, Message, Lifter, LifterImage, LifterFeature, AddEquip

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '6/11/16 / 10:18 AM'
__git__ = 'https://github.com/mateuszdargacz'

admin.autodiscover()


class SingletonModelAdmin(admin.ModelAdmin):
    change_form_template = "admin/singleton_models/change_form.html"

    def has_add_permission(self, request):
        """ Singleton pattern: prevent addition of new objects """
        return False

    def get_urls(self):
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        urlpatterns = [
            url(r'^history/$', wrap(self.history_view), {'object_id': '1'}, name='%s_%s_history' % info),
            url(r'^$', wrap(self.change_view), {'object_id': '1'}, name='%s_%s_change' % info),
            url(r'^change/$', wrap(self.change_view), {'object_id': '1'}, name='%s_%s_changelist' % info),

        ]
        return urlpatterns

    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """
        msg = _('%(obj)s was changed successfully.') % {'obj': force_text(obj)}
        if request.POST.get("_continue"):
            self.message_user(request, msg + ' ' + _("You may edit it again below."))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)
            return HttpResponseRedirect("../../")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if object_id == '1':
            self.model.objects.get_or_create(pk=1)
        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context,
        )


class SliderImageAdmin(admin.ModelAdmin):
    exclude = ('slider',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_created']


class LifterImageAdminInline(admin.TabularInline):
    model = LifterImage
    extra = 0


class LifterFeatureAdminInline(admin.TabularInline):
    extra = 0
    model = LifterFeature


class LifterAdmin(admin.ModelAdmin):
    inlines = [LifterImageAdminInline, LifterFeatureAdminInline]


admin.site.register(CompanyData, SingletonModelAdmin)
admin.site.register(Slider, SingletonModelAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Lifter, LifterAdmin)
