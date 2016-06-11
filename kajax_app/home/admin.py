# -*- coding: utf-8 -*-
from functools import update_wrapper

from django.conf.urls import patterns
from django.template.defaulttags import url
from django.utils.encoding import force_text

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

from kajax_app.home.models import Slider, CompanyData, SliderImage, Project, ProjectImage, Message, Client

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '6/11/16 / 10:18 AM'
__git__ = 'https://github.com/mateuszdargacz'


class SingletonModelAdmin(admin.ModelAdmin):
    change_form_template = "admin/singleton_models/change_form.html"

    def has_add_permission(self, request):
        """ Singleton pattern: prevent addition of new objects """
        return False

    def get_urls(self):

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        urlpatterns = patterns('',
            url(r'^history/$',
                wrap(self.history_view),
                {'object_id': '1'},
                name='%s_%s_history' % info),
            url(r'^$',
                wrap(self.change_view),
                {'object_id': '1'},
                name='%s_%s_change' % info),
        )
        return urlpatterns

    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """
        opts = obj._meta

        msg = _('%(obj)s was changed successfully.') % {'obj': force_text(obj)}
        if request.POST.has_key("_continue"):
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


admin.register(CompanyData, SingletonModelAdmin)
admin.register(Slider, SingletonModelAdmin)
admin.register(SliderImage)


admin.register(Client)
admin.register(Project)
admin.register(ProjectImage)
admin.register(Message)
