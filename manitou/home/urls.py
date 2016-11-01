# -*- coding: utf-8 -*-
from django.conf.urls import url
from home.views import SliderListAPIView, LifterAPIView, MessageView

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '6/11/16 / 12:46 PM'
__git__ = 'https://github.com/mateuszdargacz'

urlpatterns = [
    url(r'^company_data/$', SliderListAPIView.as_view(), name='company_data'),
    url(r'^slides/$', SliderListAPIView.as_view(), name='slides'),
    url(r'^lifters/$', LifterAPIView.as_view(), name='lifters'),
    url(r'^message/$', MessageView.as_view(), name='message'),

]