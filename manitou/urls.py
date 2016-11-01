#! /usr/bin/env python2.7
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomeView

admin.autodiscover()

urlpatterns = [
    # Homepage
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include('home.urls', namespace='api')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
]
